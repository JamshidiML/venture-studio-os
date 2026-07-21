---
status: active
version: 0.1.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# Gate 1 Market Discovery

## Authorization

Use only when a Founder-approved issue explicitly opens Gate 1 and defines scope, exclusions, time horizon, and repository destination. This prompt does not authorize product selection, due diligence, validation, or implementation.

## Inputs

- approved issue and Gate 0 decision
- [`docs/EVIDENCE_AND_CONFIDENCE_RULES.md`](../../docs/EVIDENCE_AND_CONFIDENCE_RULES.md)
- [`templates/MARKET_SCREENING_REPORT.md`](../../templates/MARKET_SCREENING_REPORT.md)
- research scope, geographies, segments, constraints, and source cutoff date

## Task

Create a broad, evidence-backed opportunity universe. Identify recurring problems and underserved workflows without copying protected products or treating competitor popularity as sufficient evidence. Assign stable `OPP-YYYY-NNN` IDs and distinguish evidence, inference, assumption, and hypothesis.

## Required method

1. Record search scope, queries, dates, source selection, and exclusions.
2. Prefer current primary sources for changing facts and corroborate consequential claims.
3. Capture problem, affected segment, current alternatives, observable friction, reachability, and legal or platform constraints.
4. Flag sparse, conflicting, stale, or geographically mismatched evidence.
5. Exclude obviously unsafe, deceptive, infringing, inaccessible, or structurally infeasible spaces with rationale.
6. Produce a screening-ready universe, not a winning product recommendation.

## Output

Populate `templates/MARKET_SCREENING_REPORT.md` as a `draft` under `research/`. Include methodology, evidence register, opportunity table, exclusions, assumptions, confidence, and unresolved questions. End with the next requested action: independent review of Gate 1 evidence. Stop before scoring a final winner or selecting a product.
