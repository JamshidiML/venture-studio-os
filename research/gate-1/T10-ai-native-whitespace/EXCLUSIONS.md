---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T10 Exclusions and Rejected Spaces

| Excluded space | Reason | Rule/evidence |
|---|---|---|
| Generic chatbot, universal assistant, or prompt library | No concrete job, evaluation contract, or defensible workflow; explicit Issue #13 exclusion. | Issue #13 |
| Thin wrapper around a single model call | Vendor capability alone is not durable user value; no workflow or fallback. | Issue #13; T10-S08–S09 |
| Autonomous medical, legal, financial, employment, benefits, or rights decisions | High-stakes authority, error, bias, and regulatory risk; expressly excluded. | Issue #13; T10-S06–S07, S10 |
| Surveillance, emotion inference, impersonation, deepfakes, or credential collection | Disproportionate privacy/safety harm and explicit prohibition. | Issue #13; T10-S06–S07 |
| Spam, bulk persuasion, deceptive engagement, or copyright circumvention | Harmful or unlawful behavior; no authorization. | Issue #13; T10-S10 |
| Fully autonomous web/computer agent for open-ended work | Reliability remains task-duration dependent and failures are material. | T10-S05, S11 |
| Consumer routines/habits, aging/accessibility service, household finance, learning, wellbeing, creator, SMB-admin, platform companion, or family coordination as primary value | Reserved for T01–T09; cross-thread collision prohibited. | Parent #3 and Issues #4–#12 |
| Training or benchmarking a new foundation model | Issue prohibits building/benchmarking models and Gate 1 does not authorize implementation. | Issue #13 |
| Rights-free ingestion assumption for books, archives, standards, or private corpora | Copyright, license, privacy, and data-path evidence must be explicit. | T10-S07, S10 |
| “Human in the loop” without named authority or surfaced evidence | Cosmetic oversight does not control errors. | T10-S06–S07, S12 |
| Candidate justified only by model novelty or benchmark score | Novelty/performance is not demand or defensibility evidence. | Issue #13; T10-S04–S06 |
| Robot or physical autonomy | Household/real-world task reliability and safety exceed this thread's authorized evidence. | T10-S05 |

## Edge-case rule

A workflow can remain in T10 only when the newly viable core is high-context AI transformation with explicit evaluation and provenance. If its primary user value is ordinary administration or a domain workflow assigned elsewhere, it is excluded regardless of AI use.

## Cycle 3 disposition boundary

The [AI Hypothesis Watchlist](EVIDENCE_GAPS.md#ai-hypothesis-watchlist) is not a deletion or permanent exclusion. Its 10 IDs remain T10-owned, preserve their full evaluation and safety contracts, and cannot be reused. They may return to the qualified set only after direct or clearly adjacent observed old-workflow evidence supports the bounded problem.

External Governance Cycle 3 re-review requested
