---
status: active
version: 0.1.0
owner_role: Founder
last_reviewed: 2026-07-22
---

# Contributing

Contributions are issue-driven and must preserve the separation between Strategy, Governance, Engineering, and Founder authority described in [`docs/AGENT_RESPONSIBILITIES.md`](docs/AGENT_RESPONSIBILITIES.md).

## Before starting

1. Confirm that an approved GitHub issue states the scope and acceptance criteria.
2. Read the governing artifacts linked from the issue.
3. Identify the current stage gate and the action it authorizes.
4. Record ambiguity as a blocker instead of inventing strategy, evidence, or scope.

## Branches and commits

- Branch from the default branch using `agent/<short-description>` for agent-authored work.
- Keep the branch limited to one approved issue.
- Use small, reviewable commits with terse descriptions.
- Do not mix market research, product selection, or implementation into repository-maintenance work.

## Artifact rules

- Governed Markdown files require `status`, `version`, `owner_role`, and `last_reviewed` front matter.
- Use lifecycle states and transitions from [`docs/ARTIFACT_LIFECYCLE.md`](docs/ARTIFACT_LIFECYCLE.md).
- Use ISO dates (`YYYY-MM-DD`) and stable opportunity IDs (`OPP-YYYY-NNN`).
- Separate evidence, inference, assumption, and hypothesis according to [`docs/EVIDENCE_AND_CONFIDENCE_RULES.md`](docs/EVIDENCE_AND_CONFIDENCE_RULES.md).
- Preserve prior decisions by superseding them; do not silently rewrite history.
- Directory guides must explain allowed content and may not be empty placeholders.

## Validation

Run both checks before requesting review:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

The same checks run in GitHub Actions. A contribution is not review-ready while required files are absent, internal links are broken, governed front matter is invalid, or empty placeholder artifacts exist.

## Pull requests

Open a draft pull request unless an issue explicitly requests another state. Include:

- the linked issue
- summary and complete file list
- decisions and assumptions
- validation commands and results
- risks, limitations, and unresolved blockers
- rollback notes
- the recommended governance gate

The author must not merge without the approval and authority required by the current gate.
