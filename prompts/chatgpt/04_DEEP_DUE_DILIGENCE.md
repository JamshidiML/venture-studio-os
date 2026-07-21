---
status: active
version: 0.1.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# Gate 3 Deep Due Diligence

## Authorization

Use only for opportunity IDs named in a Founder-approved Gate 3 issue after screening. Do not widen the candidate set, make the final investment decision, or authorize implementation.

## Inputs

- approved issue and Gate 2 decision
- selected `OPP-YYYY-NNN` scorecards and source evidence
- [`docs/EVIDENCE_AND_CONFIDENCE_RULES.md`](../../docs/EVIDENCE_AND_CONFIDENCE_RULES.md)
- [`templates/DUE_DILIGENCE_REPORT.md`](../../templates/DUE_DILIGENCE_REPORT.md)

## Task

Stress-test customer pain, frequency, current alternatives, willingness-to-pay evidence, accessible demand, differentiation, distribution, economics, technical feasibility, AI value, legal/privacy/security exposure, dependencies, and failure modes.

## Required method

1. State the candidate and bounded questions before gathering evidence.
2. Build a claim-to-source register with dates, confidence, and limitations.
3. Seek disconfirming evidence and credible substitutes, including manual workarounds.
4. Separate build feasibility from demand and business viability.
5. Use ranges and scenarios where evidence cannot support point estimates.
6. Define unresolved assumptions, cheap falsification steps, automatic blockers, and kill criteria.

## Output

Create one `draft` due-diligence report per authorized opportunity under `research/`, using the template. Provide a bounded recommendation of `GO`, `HOLD`, `PIVOT`, or `NO-GO` for Governance and Founder consideration. Stop before validation execution, PRD creation, or engineering work.
