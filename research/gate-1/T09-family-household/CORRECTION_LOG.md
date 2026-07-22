---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T09 Correction Log

| ID | Trigger / point loss | Targeted correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-01 | Scope edge cases cost 1 point. | Added boundary rule and explicit rejection of single-user utilities, finance, aging-primary, school-admin, medical, legal, and surveillance spaces. | EXCLUSIONS, OPPORTUNITY_INDEX | All 20 candidates require multi-person household state or handoff. | resolved |
| C-02 | Source freshness/coverage cost 3 points. | Added current 2025 ATUS, Census 2025/2026, platform documentation, and regulator sources with dates and limits. | SOURCE_REGISTER, REPORT | Twelve sources; primary authority prioritized. | resolved |
| C-03 | Claim typing/traceability cost 3 points. | Added material evidence table and per-candidate claim type, source basis, confidence, and gap. | REPORT, OPPORTUNITY_INDEX | No candidate is presented as validated demand. | resolved |
| C-04 | Coverage cost 1 point. | Added temporary caregiver, household onboarding, consent-aware sharing, guest access, and family decision workflows. | OPPORTUNITY_INDEX | Four clusters contain exactly 20 candidates. | resolved |
| C-05 | Uncertainty analysis cost 3 points. | Added ten named evidence gaps, affected candidates, risk, ceiling, and later test. | EVIDENCE_GAPS, REPORT | Every material unknown has owner/test boundary. | resolved |
| C-06 | Safety/privacy cost 2 points. | Added consent, retention, child-readable notice, conflict/coercion, data-minimization, and no-surveillance requirements. | REPORT, EXCLUSIONS, EVIDENCE_GAPS | Legal sources used as triggers, not compliance claims. | resolved |
| C-07 | Reproducibility cost 2 points. | Added exact search strings, date, source classes, negative findings, and rejected evidence types. | SEARCH_LOG | Search path can be repeated with acknowledged indexing variance. | resolved |

## Internal pre-review corrections (historical; not independent)

Codex internal pre-review completed 2026-07-22. It was a simulation by the artifact creator, not independent Governance. The findings and claimed scores below are retained only as history.

| ID | Governance finding / point loss | Required correction | Files to change by creator | Verification | Status |
|---|---|---|---|---|---|
| G09-01 | Critical B09-001; coverage lost 5 and traceability lost 1. Issue #12's eight per-candidate fields are not uniformly recorded. | Add household composition, primary user, shared-user dynamics, trust/consent, frequency, current workaround, candidate-specific WTP evidence or none, and retention risk to all 20 candidates. | OPPORTUNITY_INDEX.md; update report/summary if needed | Creator completed 20 of 20 records; Governance re-verification required. | creator-resolved; Governance pending |
| G09-02 | Rigor lost 3 and traceability lost 1. Hypothesis labels do not meet the evidence-rule contract. | For each material or candidate hypothesis, add measure, success threshold, kill threshold, and time box; otherwise relabel and fully document inference or assumption. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EVIDENCE_GAPS.md | Creator relabeled propositions as evidence-linked inferences and removed unsupported WTP hypothesis; Governance audit required. | creator-resolved; Governance pending |
| G09-03 | Critical B09-002; hygiene lost 1. Draft status conflicts with creator-complete/review-ready language. | After correcting content, increment version consistently and transition all nine artifacts to in-review. | All nine artifacts | All nine now use `in-review`, version `0.2.0`; Governance re-verification required. | creator-resolved; Governance pending |
| G09-04 | Governance score is 89/100 with two open critical blockers. | Apply only the listed corrections, rerun repository validation/tests/diff checks, and request Governance re-review. | QUALITY_SCORE_HISTORY.md, THREAD_SUMMARY.md after correction | New creator cycle preserves first Governance review; local checks rerun before re-review. | creator-resolved; Governance pending |

## Internal Governance Simulation Cycle 2 disposition (historical; not independent)

Codex internally re-read all nine corrected artifacts. This was not an external or independent review.

| Finding | Re-review verification | Status |
|---|---|---|
| B09-001 / G09-01 and G09-02 | Twenty of 20 rows now contain all eight Issue #12 candidate fields plus a valid evidence-linked inference basis and confidence; WTP evidence is explicitly none and no incomplete material hypothesis remains. | resolved |
| B09-002 / G09-03 | Nine of nine artifacts are consistently in-review at version 0.2.0 after substantive correction. | resolved |
| G09-04 | Repository validator, three unit tests, `git diff --check`, lifecycle counts, artifact count, ID range, and 20-row count pass. Governance rescored the package at 100/100. | resolved; Governance complete |

Historical internal simulation result: **100/100**. It has no external Governance authority and is preserved only as an audit record.

## External Governance Correction Cycle 2

Authoritative external review: PR #22, submitted 2026-07-22. Previous external score: **88/100**. Common blocker `EXT-GOV-01` remains pending external closure after creator correction.

| ID | External finding / point loss | Targeted correction | Files changed | Creator verification | Status |
|---|---|---|---|---|---|
| EXT09-01 | Source quality lost 4: insufficient direct family, co-parent, and shared-household coordination evidence. | Added direct parent surveys, cognitive-household-labor research, a cohabiting-couple probe study, and separated-family lived-experience research with dates, geography, limitations, and confidence. | SOURCE_REGISTER, SEARCH_LOG, REPORT | Five new independent sources registered; none treated as product demand. | creator-corrected; external re-review pending |
| EXT09-02 | Traceability lost 2 and coverage lost 3: context, direct problem, alternatives, legal constraints, and assumptions were blended. | Added a 15-row candidate-to-source matrix with six required evidence classes and explicit `none` values. | OPPORTUNITY_INDEX | Matrix covers every retained candidate and distinguishes direct from contextual evidence. | creator-corrected; external re-review pending |
| EXT09-03 | Guest access, quiet hours, shared item, low-stakes decision, and household onboarding lacked direct support. | Removed IDs 812, 814, 815, 819, and 820; preserved their retirement and did not reuse IDs. | OPPORTUNITY_INDEX, REPORT, SEARCH_LOG, SUMMARY | Candidate count changed 20 → 15; weak concepts were not padded with irrelevant sources. | creator-corrected; external re-review pending |
| EXT09-04 | Rigor lost 2: conflict-harm and non-participation needed clearer treatment for co-parent, role rotation, missed tasks, and shared decisions. | Added separated-family conflict evidence; made non-participation/conflict explicit for 801, 806, and 807; retired unsupported shared-decision candidate 820. | SOURCE_REGISTER, OPPORTUNITY_INDEX, EVIDENCE_GAPS | Matrix and candidate risks expose adoption and harm ceilings. | creator-corrected; external re-review pending |
| EXT09-05 | Hygiene lost 1 and `EXT-GOV-01`: Codex reviews were mislabeled independent; external findings/score and lifecycle update were missing. | Relabeled every prior Codex review as internal simulation, preserved history, recorded external score/findings, and moved all nine artifacts consistently to version 0.3.0 with `in-review` status. | all nine artifacts | Lifecycle, labels, history, and review request checked locally. | creator-corrected; external re-review pending |

External Governance re-review requested.
