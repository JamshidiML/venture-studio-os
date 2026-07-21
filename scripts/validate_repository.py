#!/usr/bin/env python3
"""Dependency-free validation for the Venture Studio OS repository."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote


REQUIRED_PATHS = (
    "README.md",
    "CONTRIBUTING.md",
    "docs/WORKFLOW.md",
    "docs/VENTURE_STUDIO_OVERVIEW.md",
    "docs/AGENT_RESPONSIBILITIES.md",
    "docs/STAGE_GATES.md",
    "docs/EVIDENCE_AND_CONFIDENCE_RULES.md",
    "docs/ARTIFACT_LIFECYCLE.md",
    "prompts/README.md",
    "prompts/chatgpt/01_STRATEGY_AGENT.md",
    "prompts/chatgpt/02_GOVERNANCE_AGENT.md",
    "prompts/chatgpt/03_MARKET_DISCOVERY.md",
    "prompts/chatgpt/04_DEEP_DUE_DILIGENCE.md",
    "prompts/chatgpt/05_VALIDATION_DESIGN.md",
    "prompts/codex/01_ENGINEERING_AGENT.md",
    "prompts/codex/02_REPOSITORY_MAINTENANCE.md",
    "templates/OPPORTUNITY_SCORECARD.md",
    "templates/MARKET_SCREENING_REPORT.md",
    "templates/DUE_DILIGENCE_REPORT.md",
    "templates/INVESTMENT_DECISION.md",
    "templates/VALIDATION_EXPERIMENT.md",
    "templates/PRD.md",
    "templates/RISK_REGISTER.md",
    "templates/GOVERNANCE_REVIEW.md",
    "research/README.md",
    "products/README.md",
    "decisions/README.md",
    "knowledge/README.md",
    "governance/README.md",
    ".github/workflows/repository-validation.yml",
    "scripts/validate_repository.py",
    "tests/test_validate_repository.py",
)

COLLECTION_GUIDES = (
    "research/README.md",
    "products/README.md",
    "decisions/README.md",
    "knowledge/README.md",
    "governance/README.md",
)

FRONT_MATTER_KEYS = ("status", "version", "owner_role", "last_reviewed")
ALLOWED_STATUSES = {
    "active",
    "draft",
    "in-review",
    "approved",
    "superseded",
    "deprecated",
}
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
OPPORTUNITY_ID = re.compile(r"^(?:OPP-\d{4}-\d{3}|OPP-YYYY-NNN)$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def parse_front_matter(path: Path) -> tuple[dict[str, str], str | None]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}, "missing opening front-matter delimiter"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, "missing closing front-matter delimiter"

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return {}, f"invalid front-matter line: {line!r}"
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    return fields, None


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and "__pycache__" not in path.parts
    )


def validate_required_paths(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
        elif len(path.read_text(encoding="utf-8").strip()) < 200:
            errors.append(f"required file is not substantive: {relative}")
    return errors


def validate_front_matter(root: Path) -> list[str]:
    errors: list[str] = []
    for path in markdown_files(root):
        relative = path.relative_to(root).as_posix()
        if relative == "README.md":
            continue
        fields, parse_error = parse_front_matter(path)
        if parse_error:
            errors.append(f"{relative}: {parse_error}")
            continue
        for key in FRONT_MATTER_KEYS:
            if not fields.get(key):
                errors.append(f"{relative}: missing front-matter key {key!r}")
        status = fields.get("status", "")
        if status and status not in ALLOWED_STATUSES:
            errors.append(f"{relative}: unsupported status {status!r}")
        version = fields.get("version", "")
        if version and not SEMVER.fullmatch(version):
            errors.append(f"{relative}: version must use semantic versioning")
        reviewed = fields.get("last_reviewed", "")
        placeholder_date_allowed = relative.startswith("templates/")
        if reviewed and not (placeholder_date_allowed and reviewed == "YYYY-MM-DD"):
            try:
                if not ISO_DATE.fullmatch(reviewed):
                    raise ValueError
                date.fromisoformat(reviewed)
            except ValueError:
                errors.append(f"{relative}: last_reviewed must be a valid ISO date")
        opportunity_id = fields.get("opportunity_id")
        if opportunity_id and not OPPORTUNITY_ID.fullmatch(opportunity_id):
            errors.append(f"{relative}: invalid opportunity_id {opportunity_id!r}")
    return errors


def validate_internal_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in markdown_files(root):
        relative = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(content):
            target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            file_target = unquote(target.split("#", 1)[0])
            if not file_target:
                continue
            resolved = (path.parent / file_target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{relative}: link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"{relative}: broken internal link: {raw_target}")
    return errors


def validate_no_empty_placeholders(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        if path.name in {".gitkeep", ".keep"}:
            errors.append(f"empty-folder sentinel is prohibited: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"empty file is prohibited: {relative}")
    for relative in COLLECTION_GUIDES:
        path = root / relative
        if path.is_file() and len(path.read_text(encoding="utf-8").strip()) < 400:
            errors.append(f"collection guide is not substantive: {relative}")
    return errors


def validate_readme_next_step(root: Path) -> list[str]:
    readme = root / "README.md"
    if not readme.is_file():
        return []
    required = "Exact next step after Foundation v0.1 approval:"
    if required not in readme.read_text(encoding="utf-8"):
        return ["README.md: missing exact next step after foundation approval"]
    return []


def validate_repository(root: Path) -> list[str]:
    checks = (
        validate_required_paths,
        validate_front_matter,
        validate_internal_links,
        validate_no_empty_placeholders,
        validate_readme_next_step,
    )
    return [error for check in checks for error in check(root)]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed: {len(REQUIRED_PATHS)} required files")
    print(f"Front matter checked: {len(markdown_files(root)) - 1} governed Markdown files")
    print("Internal links resolved and no empty placeholder artifacts found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
