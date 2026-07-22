---
status: in-review
version: 0.1.2
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T01
issue_number: 4
gate: 1
---

# T01 Correction Log

| Correction ID | Cycle-1 point loss | Targeted change | Files changed | Verification | Status |
|---|---|---|---|---|---|
| T01-C01 | Exclusion destinations incomplete (-1) | Added explicit boundary reason and destination for cross-thread concepts. | EXCLUSIONS.md | 15 reviewed spaces have decisions; no ID reassignment. | resolved |
| T01-C02 | Dates/staleness incomplete (-4) | Added publication/observation dates, common access date, geography, limitations, and confidence; marked FoodKeeper and undated guidance. | SOURCE_REGISTER.md | All nine sources have all required metadata fields. | resolved |
| T01-C03 | Claim type inconsistent (-4) | Added evidence/inference/assumption/hypothesis labels in the problem landscape and candidate-level inference labels. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | 20/20 candidates carry source IDs and type. | resolved |
| T01-C04 | Overlap notes incomplete (-1) | Clarified T02/T03/T05/T08/T09 boundaries and preserved manual fallbacks. | EXCLUSIONS.md, OPPORTUNITY_INDEX.md | Scope scan shows no cross-thread product claim. | resolved |
| T01-C05 | Uncertainty treatment incomplete (-3) | Added demand, WTP, retention, distribution, safety, privacy, and geography gaps with evidence needed and risk. | EVIDENCE_GAPS.md | Every gap has affected IDs and a current ceiling. | resolved |
| T01-C06 | Safety/privacy/platform detail incomplete (-3) | Added candidate constraints and cross-cutting minimum-data, safety, IP, and ethics rules. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | Food/fire/pet/location candidates each have explicit limits. | resolved |
| T01-C07 | Search reproducibility incomplete (-3) | Recorded exact queries, selection order, unused-result decisions, and coverage check. | SEARCH_LOG.md | Ten queries are reproducible and mapped to source IDs or exclusions. | resolved |

No content was corrected by inflating an Opportunity Score. No Opportunity Score was calculated.

## Internal Pre-review (not independent)

| Review ID | Finding | Required correction | Verification | Status |
|---|---|---|---|---|
| T01-G01 | A prior Codex self-review simulated a 100/100 Governance result. | Preserve as non-authoritative history and relabel it as internal. | This section and the score history now identify it as an Internal Pre-review; no independent score is claimed. | superseded by external review |

## External Governance Review — Cycle 1

Authoritative external score: `92/100`. Common blocker: `EXT-GOV-01` — prior Codex review was not independent.

### External Point-Loss Register

| Dimension | Maximum | External award | Lost | Finding |
|---|---:|---:|---:|---|
| Scope compliance and exclusions | 10 | 10 | 0 | no loss |
| Source quality and freshness | 20 | 17 | 3 | sources did not independently support every named weak workflow |
| Claim-level evidence and traceability | 15 | 15 | 0 | no loss |
| Opportunity coverage and diversity | 15 | 12 | 3 | weak candidates were retained without a visible source-coverage audit |
| Analytical rigor and uncertainty | 15 | 14 | 1 | unsupported workflow assumptions needed explicit downgrade treatment |
| Legal, safety, privacy, and platform constraints | 10 | 10 | 0 | no loss |
| Reproducibility of search method | 10 | 10 | 0 | no loss |
| Clarity and repository hygiene | 5 | 4 | 1 | embedded self-review was mislabeled independent |
| **Total** | **100** | **92** | **8** | **external score is authoritative** |

| Review ID | External finding / required correction | Applied correction | Verification | Status |
|---|---|---|---|---|
| EXT-GOV-01 | Codex-authored “Independent Governance Review” is not independent. | Relabeled every surviving reference as Internal Pre-review and retained its historical simulated score without treating it as external. | QUALITY_SCORE_HISTORY.md, CORRECTION_LOG.md, THREAD_SUMMARY.md | correction applied; external verification pending |
| T01-EXT-C01 | Add a candidate-to-source matrix separating direct problem, context, current alternative, feasibility, constraints, and unsupported assumptions. | Added 20/20 coverage rows with a strict direct-evidence definition and explicit dashes. | OPPORTUNITY_INDEX.md | resolved internally |
| T01-EXT-C02 | Strengthen, downgrade, or remove possession location, borrowed items, packing, plant care, pet handoff, idle-time, completion capture, and routine restart. | Downgraded all eight to `very low`; clarified that T01-S01/S08 are context only and added a named evidence gap. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EVIDENCE_GAPS.md | resolved internally |
| T01-EXT-C03 | Log the exact eight-point loss. | Added the dimension-level external point-loss register above. | CORRECTION_LOG.md, QUALITY_SCORE_HISTORY.md | resolved internally |

External Governance re-review requested.
