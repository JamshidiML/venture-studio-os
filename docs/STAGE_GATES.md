---
status: active
version: 0.1.0
owner_role: Founder
last_reviewed: 2026-07-22
---

# Stage Gates

This file turns the lifecycle in [`WORKFLOW.md`](WORKFLOW.md) into review contracts. Passing a gate authorizes only the next action shown below.

| Gate | Required input | Exit evidence | Decision owner | Authorized next action |
|---|---|---|---|---|
| 0 — System readiness | Operating docs, prompts, templates, validation | Internal links and checks pass; roles, evidence rules, lifecycle, and decision authority are approved | Founder | Open an issue for Gate 1 market discovery |
| 1 — Market discovery | Approved scope and discovery method | Sourced opportunity universe with claim types, confidence, exclusions, and unknowns | Founder after Governance review | Screen documented opportunities |
| 2 — Opportunity screening | Gate 1 evidence and scorecards | Comparable scores, automatic blockers, rationale, and shortlist uncertainty | Founder after Governance review | Authorize due diligence for named candidates |
| 3 — Deep due diligence | Authorized candidate IDs | Evidence on pain, alternatives, differentiation, economics, feasibility, distribution, and risk | Founder after Governance review | Prepare an investment decision |
| 4 — Investment decision | Due-diligence report and governance review | Recorded `GO`, `HOLD`, `PIVOT`, or `NO-GO`, including kill criteria and open risks | Founder | Authorize validation only for a `GO` or bounded `PIVOT` |
| 5 — Validation | Approved validation experiment | Results tied to thresholds, deviations, learning, and falsified or surviving assumptions | Founder after Governance review | Define a product only if validation passes |
| 6 — Product definition | Validation result and draft PRD | Approved PRD, MVP boundaries, acceptance criteria, architecture inputs, data/privacy needs | Founder after Governance review | Open engineering issues |
| 7 — Engineering execution | Approved issues and Gate 6 artifacts | Tested implementation, technical docs, traceable PRs, and operational evidence | Founder | Request release governance review |
| 8 — Governance and release | Release candidate and evidence | Independent business, security, privacy, test, operability, and rollback assessment | Founder | Release, conditionally release, or return to rework |
| 9 — Learning loop | Decision and execution outcomes | Reusable lessons, updated assumptions, and linked source artifacts | Founder | Feed learning into a separately authorized cycle |

## Gate decision record

Every gate decision must name:

- gate and decision date
- artifact paths and versions reviewed
- decision and rationale
- blockers and accepted risks
- conditions, owners, and review dates
- exact next authorized action

A gate is not passed by implication. Missing evidence, an `in-review` artifact, or an unresolved critical blocker keeps the gate closed.

## Rework and regression

Governance may return an artifact for rework without changing its source content. New evidence that invalidates a passed gate triggers a new decision record and may return work to an earlier gate. Historical decisions remain preserved and linked through the lifecycle rules in [`ARTIFACT_LIFECYCLE.md`](ARTIFACT_LIFECYCLE.md).
