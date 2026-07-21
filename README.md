# Venture Studio OS

A founder-operated, AI-assisted operating system for discovering, validating, selecting, building, governing, and learning from digital product opportunities.

## Purpose

This repository is the single source of truth for:

- market discovery and opportunity screening
- due diligence and investment decisions
- validation experiments
- product requirements and architecture
- Codex engineering execution
- independent ChatGPT governance reviews
- reusable knowledge and lessons learned

## Operating model

- **ChatGPT Strategy Agent:** research, opportunity analysis, validation design, business blueprint, PRD.
- **ChatGPT Governance Agent:** independent review, scoring, evidence checks, Go/No-Go decisions.
- **Codex Engineering Agent:** repository work, implementation, tests, CI/CD, and technical documentation.
- **Founder:** final authority for strategic, financial, legal, and release decisions.

## Current status

**Foundation initialization** — no product has been selected and no application development is authorized yet.

## Repository map

- [`docs/`](docs/VENTURE_STUDIO_OVERVIEW.md) — operating model, workflow, roles, and stage gates
- [`prompts/`](prompts/README.md) — active prompts for ChatGPT and Codex
- [`templates/`](templates/OPPORTUNITY_SCORECARD.md) — reusable decision and delivery artifacts
- [`research/`](research/README.md) — market discovery evidence
- [`products/`](products/README.md) — approved product workspaces
- [`decisions/`](decisions/README.md) — authoritative decision records
- [`knowledge/`](knowledge/README.md) — reusable organizational learning
- [`governance/`](governance/README.md) — independent reviews and release gates

## First execution sequence

1. Approve the operating model and evidence rules.
2. Run global market discovery.
3. Screen and rank opportunities.
4. Perform deep due diligence on the leading candidates.
5. Make an explicit Go / Hold / Pivot / No-Go decision.
6. Validate the chosen opportunity before product development.
7. Create the PRD and architecture.
8. Authorize Codex implementation through reviewed GitHub issues.

See [`docs/WORKFLOW.md`](docs/WORKFLOW.md) for the detailed process.

## Foundation validation

The foundation uses dependency-free checks for required files, Markdown front matter, internal links, stable opportunity IDs, and empty placeholder artifacts.

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the issue, branch, artifact, and pull-request rules.

## Next authorized step

**Exact next step after Foundation v0.1 approval:** create and approve a GitHub issue authorizing Gate 1 global market discovery with [`prompts/chatgpt/03_MARKET_DISCOVERY.md`](prompts/chatgpt/03_MARKET_DISCOVERY.md). Do not begin product selection or implementation as part of foundation approval.
