---
status: active
version: 0.1.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# Gate 5 Validation Design

## Authorization

Use only after a recorded Gate 4 `GO` or bounded `PIVOT` and a Founder-approved issue naming the opportunity and assumptions to test. Design does not itself authorize contacting participants, spending money, collecting personal data, or building a product.

## Inputs

- investment decision and governance review
- approved opportunity ID and due-diligence report
- [`templates/VALIDATION_EXPERIMENT.md`](../../templates/VALIDATION_EXPERIMENT.md)
- legal, privacy, budget, channel, and time constraints

## Task

Design the smallest ethical experiments capable of falsifying the core problem, audience, value proposition, reachability, and willingness-to-pay assumptions before full MVP development.

## Required method

1. Rank assumptions by impact and uncertainty.
2. Convert each prioritized assumption into a measurable hypothesis.
3. Define participant criteria, channel, sample rationale, procedure, instrument, success threshold, kill threshold, time box, and owner.
4. Identify consent, privacy, incentive, bias, and data-retention controls.
5. Prefer reversible, low-cost tests and behavioral evidence over stated enthusiasm.
6. Predefine how contradictory or inconclusive results affect `GO`, `HOLD`, `PIVOT`, or `NO-GO`.

## Output

Create a `draft` experiment artifact under `research/` using the template. Mark all unobserved outcomes as hypotheses or assumptions; never invent results. End with the approvals required to execute the experiment. Stop before execution, product definition, or engineering implementation.
