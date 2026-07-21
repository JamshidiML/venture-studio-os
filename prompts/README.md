---
status: active
version: 0.1.0
owner_role: Founder
last_reviewed: 2026-07-22
---

# Prompt Catalog

Prompts are role contracts, not standing authorization. Before use, provide an approved issue, current gate, authoritative input paths and versions, expected destination, and explicit stop condition.

## ChatGPT prompts

| Prompt | Use |
|---|---|
| [`01_STRATEGY_AGENT.md`](chatgpt/01_STRATEGY_AGENT.md) | Governing Strategy role and output contract |
| [`02_GOVERNANCE_AGENT.md`](chatgpt/02_GOVERNANCE_AGENT.md) | Independent gate and risk review |
| [`03_MARKET_DISCOVERY.md`](chatgpt/03_MARKET_DISCOVERY.md) | Gate 1 opportunity-universe research |
| [`04_DEEP_DUE_DILIGENCE.md`](chatgpt/04_DEEP_DUE_DILIGENCE.md) | Gate 3 review of explicitly authorized opportunity IDs |
| [`05_VALIDATION_DESIGN.md`](chatgpt/05_VALIDATION_DESIGN.md) | Gate 5 falsification experiment design |

## Codex prompts

| Prompt | Use |
|---|---|
| [`01_ENGINEERING_AGENT.md`](codex/01_ENGINEERING_AGENT.md) | Governing Engineering role and PR contract |
| [`02_REPOSITORY_MAINTENANCE.md`](codex/02_REPOSITORY_MAINTENANCE.md) | Documentation, templates, automation, and repository health |

## Use rules

1. Start from the governing role prompt, then add only the task prompt authorized by the issue.
2. Do not combine Strategy authorship and Governance approval in one role or pass.
3. Do not use a later-gate prompt before the preceding gate decision exists.
4. Save substantive outputs with the matching template and lifecycle front matter.
5. Stop at the requested gate and name the next action requiring Founder authorization.
