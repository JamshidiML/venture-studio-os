---
status: active
version: 0.1.0
owner_role: Founder
last_reviewed: 2026-07-22
---

# Artifact Lifecycle

## Governed front matter

Governed Markdown artifacts contain:

```yaml
---
status: draft
version: 0.1.0
owner_role: Strategy Agent
last_reviewed: YYYY-MM-DD
---
```

Opportunity-specific artifacts also include `opportunity_id: OPP-YYYY-NNN`. Actual artifacts replace placeholders with an ISO date and assigned ID; reusable templates retain the placeholders.

## Lifecycle states

| Status | Authority and permitted use |
|---|---|
| `draft` | Incomplete working artifact; may inform discussion but cannot pass a gate |
| `in-review` | Frozen review candidate awaiting independent assessment; not yet authoritative |
| `approved` | Current source of truth for its stated scope and version |
| `superseded` | Replaced by a named newer artifact or version; retained for traceability |
| `deprecated` | Retained for history but unsuitable for new work and not replaced one-to-one |

`active` is reserved for operating instructions, prompts, collection guides, and policies. It is not a substitute for `approved` on research, decisions, validation results, PRDs, or governance reviews.

## Allowed transitions

- `draft` → `in-review` when the owner declares the artifact complete for its gate.
- `in-review` → `draft` when rework is required.
- `in-review` → `approved` only after required review and Founder decision.
- `approved` → `superseded` when a replacement is approved and linked.
- any non-historical state → `deprecated` only with a recorded rationale.

No transition is implied by a merge. The artifact front matter and corresponding decision record must agree.

## Versioning and change control

Use semantic versions. Patch versions clarify without changing a gate decision, minor versions add compatible analysis or scope, and major versions change the decision basis or contract. When approved content changes materially, create a new review and preserve the prior version through Git history and an explicit supersession link.

## Naming and storage

Use descriptive uppercase template names, ISO dates in dated records, and stable opportunity IDs. Store raw and synthesized evidence under [`research/`](../research/README.md), authoritative gate decisions under [`decisions/`](../decisions/README.md), independent reviews under [`governance/`](../governance/README.md), and reusable lessons under [`knowledge/`](../knowledge/README.md).

## Ownership and review

The `owner_role` maintains content accuracy. Governance assesses gate readiness independently. The Founder approves lifecycle transitions that carry authority. Engineering may automate validation but may not change an artifact's strategic meaning or status without authorization.
