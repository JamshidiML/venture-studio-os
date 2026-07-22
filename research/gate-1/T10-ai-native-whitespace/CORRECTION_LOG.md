---
status: in-review
version: 0.4.0
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

## Internal pre-review corrections (historical; not independent)

Codex internal pre-review completed 2026-07-22. It was a simulation by the artifact creator, not independent Governance. The findings and claimed scores below are retained only as history.

| ID | Governance finding / point loss | Required correction | Files to change by creator | Verification | Status |
|---|---|---|---|---|---|
| G10-01 | Critical B10-001; coverage lost 6 and traceability lost 1. Issue #13's candidate contract and hard-boundary fields are incomplete. | Add reachable user, old workflow, enabling capability, model/data dependency and viable data path, human oversight, unit-cost risk, privacy/security risk, defensibility hypothesis, and fallback to every candidate. | OPPORTUNITY_INDEX.md; update report/summary if needed | Creator completed 20 of 20 records across keyed tables; Governance re-verification required. | creator-resolved; Governance pending |
| G10-02 | Rigor lost 6 and traceability lost 1. Quality hypotheses often name a metric without success threshold, kill threshold, or time box. | Add a full measurable/falsifiable evaluation contract per candidate and type every material inference, assumption, and hypothesis correctly. | OPPORTUNITY_INDEX.md, MARKET_DISCOVERY_REPORT.md, EVIDENCE_GAPS.md | Creator added full per-candidate quality contracts and candidate-specific defensibility hypotheses under a complete D-contract; Governance audit required. | creator-resolved; Governance pending |
| G10-03 | Legal/privacy/platform lost 2. Candidate-level lawful data path and privacy/security analysis is uneven. | Record source rights/consent, data sensitivity, retention/residency, confidentiality, access controls, and provider exposure as applicable per candidate. | OPPORTUNITY_INDEX.md | Creator added candidate-specific data path and risk treatment; Governance re-verification required. | creator-resolved; Governance pending |
| G10-04 | Critical B10-002; hygiene lost 1. Draft status conflicts with creator-complete/review-ready language. | After correction, increment version consistently and transition all nine artifacts to in-review. | All nine artifacts | All nine now use `in-review`, version `0.2.0`; Governance re-verification required. | creator-resolved; Governance pending |
| G10-05 | Governance score is 83/100 with two open critical blockers. | Apply only documented corrections, rerun repository validation/tests/diff checks, and request Governance re-review. | QUALITY_SCORE_HISTORY.md, THREAD_SUMMARY.md after correction | New creator cycle preserves first Governance review; local checks rerun before re-review. | creator-resolved; Governance pending |

## Internal Governance Simulation Cycle 2 disposition (historical; not independent)

Codex internally re-read all nine corrected artifacts. This was not an external or independent review.

| Finding | Re-review verification | Status |
|---|---|---|
| B10-001 / G10-01 through G10-03 | Twenty of 20 candidates now satisfy the Issue #13 field and hard-boundary contract across two keyed tables; R-contract assumption and candidate-specific quality/D-contract hypotheses have the required treatments. | resolved |
| B10-002 / G10-04 | Nine of nine artifacts are consistently in-review at version 0.2.0 after substantive correction. | resolved |
| G10-05 | Repository validator, three unit tests, `git diff --check`, lifecycle counts, artifact count, ID range, and both 20-row table counts passed. Codex internally simulated a 100/100 rescore. | resolved in historical internal simulation |

Historical internal simulation result: **100/100**. It has no external Governance authority and is preserved only as an audit record.

## External Governance Correction Cycle 2

Authoritative external review: PR #24, submitted 2026-07-22. Previous external score: **94/100**. Common blocker `EXT-GOV-01` remains pending external closure after creator correction.

| ID | External finding / point loss | Targeted correction | Files changed | Creator verification | Status |
|---|---|---|---|---|---|
| EXT10-01 | Source quality lost 2: non-provider old-workflow evidence was thin for archives, evidence synthesis, public records, technical documentation, museums, and data stewardship. | Added eight practitioner, government, commissioned-independent, case-study, and academic sources; kept DOJ volume contextual rather than direct. | SOURCE_REGISTER, SEARCH_LOG, REPORT | T10-S13–S20 record date, geography/scope, limitation, and confidence. | creator-corrected; external re-review pending |
| EXT10-02 | Coverage lost 1: workflow problem, AI capability, risk/evaluation, reachability, and unsupported propositions were not mapped per candidate. | Added a 20-row coverage matrix separating all required evidence axes, with explicit `none` values. | OPPORTUNITY_INDEX | Every candidate has a complete classification row. | creator-corrected; external re-review pending |
| EXT10-03 | Overlaps among 900/904, 901/917, 903/914/916, and 907/908/918 needed resolution. | Added boundary decisions based on user, input corpus, output, decision authority, evaluation unit, and failure cost. | OPPORTUNITY_INDEX, REPORT | All named overlap groups are addressed without merging unlike workflows. | creator-corrected; external re-review pending |
| EXT10-04 | Hygiene lost 3 and `EXT-GOV-01`: Codex reviews were mislabeled independent; external score/findings and lifecycle state were not current. | Relabeled every prior Codex review as internal simulation, preserved audit history, recorded the external result, and moved all nine artifacts consistently to version 0.3.0 with `in-review` status. | all nine artifacts | Lifecycle, labels, history, and external review request checked locally. | creator-corrected; external re-review pending |

External Governance re-review requested.

## Authoritative External Governance Re-review — Cycle 2

PR #24 external review of version 0.3.0 assigned **96/100** with dimension scores **10, 19, 15, 12, 15, 10, 10, 5**. The review externally resolved `EXT-GOV-01`, verified the non-provider evidence/evidence-axis/overlap corrections, and opened completion finding `EXT2-T10-01`.

| ID | Cycle 2 finding | Cycle 3 required correction | Resolution evidence | Status |
|---|---|---|---|---|
| EXT-GOV-01 | Codex-authored review history was not independent. | None further; preserve the corrected labels and authoritative history. | External reviewer verified internal-simulation labels, lifecycle, authoritative score, and CI on the exact SHA. | **externally resolved** |
| EXT2-T10-01 | 900, 902, 905–907, 909, 912, 915–916, and 919 had no candidate-specific problem evidence but remained qualified. | Move all ten to an AI Hypothesis Watchlist; preserve IDs and every evaluation/risk contract; retain adjacent-workflow candidates only at low confidence. | OPPORTUNITY_INDEX contains 10 qualified IDs and a 20-row status matrix; EVIDENCE_GAPS contains 10 complete watchlist records and preserved contracts. | creator-resolved; external re-review required |

## External Governance Correction Cycle 3

| ID | Cycle 3 completion finding | Targeted resolution | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C3-T10-01 | Qualified Gate 1 Candidates and AI Hypothesis Watchlist Candidates were not yet separated. | Qualified 901, 903, 904, 908, 910, 911, 913, 914, 917, and 918; moved 900, 902, 905–907, 909, 912, 915–916, and 919 to the watchlist without deletion or renumbering. | REPORT, OPPORTUNITY_INDEX, EVIDENCE_GAPS, EXCLUSIONS, SCORE HISTORY, SUMMARY | 10 qualified + 10 watchlist = prior 20-ID universe; matrix disposition and full contracts preserved. | creator-resolved; external re-review required |
| C3-T10-02 | Broad workflow-family evidence could be mistaken for direct proof of the proposed subtask. | Marked eight retained adjacent-workflow candidates as subtask-unisolated and kept confidence low/medium-low. | REPORT, OPPORTUNITY_INDEX, EVIDENCE_GAPS | No capability, regulation, or context source is counted as candidate-specific pain. | resolved |
| C3-T10-03 | Cycle 2 score, blocker disposition, counts, and lifecycle needed current audit state. | Recorded external 96/100, marked EXT-GOV-01 externally resolved, bumped all nine artifacts to in-review 0.4.0, and requested Cycle 3 re-review. | all nine artifacts | Repository validator, three unit tests, diff check, lifecycle, ID, matrix, link, and contract checks passed locally; PR/CI re-check follows push. | creator-resolved; local validation passed |

No source was added, removed, or replaced in Cycle 3. No model benchmark, prototype, outreach, ranking, or Gate 2 work occurred.

External Governance Cycle 3 re-review requested
