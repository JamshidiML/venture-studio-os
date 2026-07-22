---
status: in-review
version: 0.2.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T10 Correction Log

| ID | Trigger / lost points | Targeted correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-01 | Scope/exclusion lost 2. | Added edge-case rule, explicit cross-thread boundaries, and rejection of autonomous/high-stakes/generic agents. | EXCLUSIONS, OPPORTUNITY_INDEX | All candidates are bounded review workflows. | resolved |
| C-02 | Source quality lost 3. | Added ILO, Stanford, NIST, METR, EU, and multiple current provider sources with limitations. | SOURCE_REGISTER, REPORT | Twelve-source balance; provider claims triangulated. | resolved |
| C-03 | Traceability lost 4. | Added material claim register and candidate evidence basis/confidence. | REPORT, OPPORTUNITY_INDEX | No capability evidence is presented as demand. | resolved |
| C-04 | Coverage lost 1. | Added public consultation, datasets, schemas, standards, collection stewardship, and records queues. | OPPORTUNITY_INDEX | Exactly 20 IDs across four clusters. | resolved |
| C-05 | Rigor lost 4. | Added per-candidate measurable quality hypothesis, human authority, risk, fallback, plus 12 evidence gaps. | OPPORTUNITY_INDEX, EVIDENCE_GAPS | Evaluation contract visible for every candidate. | resolved |
| C-06 | Legal/safety lost 2. | Added data rights, copyright, privacy, AI Act, records, provenance, and vendor fallback controls. | REPORT, EXCLUSIONS, EVIDENCE_GAPS | No compliance or autonomy claim. | resolved |
| C-07 | Reproducibility lost 2. | Added exact queries, source hierarchy, rejected classes, negative findings, and cutoff. | SEARCH_LOG | Research path and ceiling are reproducible. | resolved |

## Governance corrections

Independent review completed 2026-07-22. Governance did not rewrite source research.

| ID | Governance finding / point loss | Required correction | Files to change by creator | Verification | Status |
|---|---|---|---|---|---|
| G10-01 | Critical B10-001; coverage lost 6 and traceability lost 1. Issue #13's candidate contract and hard-boundary fields are incomplete. | Add reachable user, old workflow, enabling capability, model/data dependency and viable data path, human oversight, unit-cost risk, privacy/security risk, defensibility hypothesis, and fallback to every candidate. | OPPORTUNITY_INDEX.md; update report/summary if needed | Creator completed 20 of 20 records across keyed tables; Governance re-verification required. | creator-resolved; Governance pending |
| G10-02 | Rigor lost 6 and traceability lost 1. Quality hypotheses often name a metric without success threshold, kill threshold, or time box. | Add a full measurable/falsifiable evaluation contract per candidate and type every material inference, assumption, and hypothesis correctly. | OPPORTUNITY_INDEX.md, MARKET_DISCOVERY_REPORT.md, EVIDENCE_GAPS.md | Creator added full per-candidate quality contracts and candidate-specific defensibility hypotheses under a complete D-contract; Governance audit required. | creator-resolved; Governance pending |
| G10-03 | Legal/privacy/platform lost 2. Candidate-level lawful data path and privacy/security analysis is uneven. | Record source rights/consent, data sensitivity, retention/residency, confidentiality, access controls, and provider exposure as applicable per candidate. | OPPORTUNITY_INDEX.md | Creator added candidate-specific data path and risk treatment; Governance re-verification required. | creator-resolved; Governance pending |
| G10-04 | Critical B10-002; hygiene lost 1. Draft status conflicts with creator-complete/review-ready language. | After correction, increment version consistently and transition all nine artifacts to in-review. | All nine artifacts | All nine now use `in-review`, version `0.2.0`; Governance re-verification required. | creator-resolved; Governance pending |
| G10-05 | Governance score is 83/100 with two open critical blockers. | Apply only documented corrections, rerun repository validation/tests/diff checks, and request Governance re-review. | QUALITY_SCORE_HISTORY.md, THREAD_SUMMARY.md after correction | New creator cycle preserves first Governance review; local checks rerun before re-review. | creator-resolved; Governance pending |

## Governance Cycle 2 disposition

Independent Governance re-read all nine corrected artifacts and did not rewrite source research.

| Finding | Re-review verification | Status |
|---|---|---|
| B10-001 / G10-01 through G10-03 | Twenty of 20 candidates now satisfy the Issue #13 field and hard-boundary contract across two keyed tables; R-contract assumption and candidate-specific quality/D-contract hypotheses have the required treatments. | resolved |
| B10-002 / G10-04 | Nine of nine artifacts are consistently in-review at version 0.2.0 after substantive correction. | resolved |
| G10-05 | Repository validator, three unit tests, `git diff --check`, lifecycle counts, artifact count, ID range, and both 20-row table counts pass. Governance rescored the package at 100/100. | resolved; Governance complete |

Latest Governance score: **100/100**. Critical blockers: **0**. Historical score and findings remain in QUALITY_SCORE_HISTORY.md as the audit trail.
