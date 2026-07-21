---
status: active
version: 0.1.0
owner_role: Founder
last_reviewed: 2026-07-22
---

# Venture Studio OS Overview

## Purpose

Venture Studio OS is a repository-based operating system for one founder working with specialized AI agents. It makes research, investment, validation, product, engineering, and governance work reviewable without turning the operating model into a software platform.

The repository is the source of truth. Chat sessions are working contexts; only reviewed repository artifacts and decision records carry durable authority.

## Foundation scope

Foundation v0.1 provides:

- explicit role and decision boundaries
- stage gates with entry and exit criteria
- evidence and confidence rules
- artifact status, versioning, and supersession rules
- reusable prompts and artifact templates
- lightweight repository validation

It does not contain market findings, select a product, authorize validation, or authorize application development.

## Operating principles

1. Evidence unlocks gates; document production alone does not.
2. The Founder grants scope through approved issues and makes final strategic, financial, legal, and release decisions.
3. Strategy authors research and product-definition artifacts; Governance reviews them independently.
4. Engineering acts only on approved issues and authoritative inputs.
5. Each artifact has an owner, lifecycle state, version, review date, and repository destination.
6. Uncertainty is visible through claim types, confidence levels, assumptions, and kill criteria.
7. The smallest falsifying experiment precedes expensive implementation.

## Repository as an operating system

| Layer | Location | Purpose |
|---|---|---|
| Operating rules | [`docs/`](../docs/WORKFLOW.md) | Defines roles, gates, evidence, and artifact governance |
| Agent instructions | [`prompts/`](../prompts/README.md) | Supplies bounded, role-specific execution contracts |
| Artifact contracts | [`templates/`](../templates/OPPORTUNITY_SCORECARD.md) | Makes outputs consistent and reviewable |
| Evidence | [`research/`](../research/README.md) | Stores sourced market and validation evidence |
| Product work | [`products/`](../products/README.md) | Contains only explicitly approved product workspaces |
| Decisions | [`decisions/`](../decisions/README.md) | Records authoritative Founder decisions |
| Learning | [`knowledge/`](../knowledge/README.md) | Preserves reusable lessons without changing decisions |
| Independent review | [`governance/`](../governance/README.md) | Stores gate assessments and release reviews |

## Founder-scale cadence

For each authorized unit of work, the Founder opens or approves an issue, the responsible role produces a versioned artifact, Governance reviews when a gate requires independence, and the Founder records the resulting decision. Work stops at the next gate until a new action is authorized.

See [`WORKFLOW.md`](WORKFLOW.md) for the lifecycle and [`STAGE_GATES.md`](STAGE_GATES.md) for gate contracts.
