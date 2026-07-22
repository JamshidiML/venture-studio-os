---
status: in-review
version: 0.1.2
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Correction Log

| Correction ID | Cycle-1 loss / blocker | Targeted correction | Verification | Status |
|---|---|---|---|---|
| T02-C01 | Scope boundaries (-2) | Added explicit clinical, emergency, professional-care, family, finance, platform, credential, and exploitation exclusions. | 15 exclusion rows; no out-of-scope ID. | resolved |
| T02-C02 | Source method/geography (-3) | Added survey/sample definitions, source dates, geography, limitations, and conflict notes. | 11/11 source rows complete. | resolved |
| T02-C03 | Claim traceability (-4) | Added source IDs and claim-type handling to material claims and all candidates. | 20/20 index rows trace to source IDs and are labeled as inference. | resolved |
| T02-C04 | Coverage summary (-1) | Added domain coverage and boundary notes. | Visual, hearing, mobility, cognitive, independence, caregiver, transport, service, support, and connection coverage visible. | resolved |
| T02-C05 | Demographics versus demand (-4) | Added explicit non-equivalence, measurement conflicts, and candidate demand gaps. | No prevalence value is used as market size or WTP evidence. | resolved |
| T02-C06 | Consent/emergency blocker and controls (-4 plus T02-B01) | Added user ownership, revocation, access visibility, data minimization, no monitoring, no emergency reliance, no credentials, and clinical hard stops. | Relevant candidate rows contain specific control; blocker closed. | resolved |
| T02-C07 | Search reproducibility (-3) | Added exact queries, population-definition rule, unused searches, and selection criteria. | Ten searches map to included sources or explicit non-use. | resolved |

No opportunity score, winner, or attractiveness ranking was changed or created during correction.

## Internal Pre-review (not independent)

| Review ID | Finding | Required correction | Verification | Status |
|---|---|---|---|---|
| T02-G01 | A prior Codex self-review simulated 100/100 and checked the creator blocker. | Preserve as internal history; do not present it as an independent score. | Relabeled here, in score history, and in summary. | superseded by external review |

## External Governance Review — Cycle 1

Authoritative external score: `94/100`. Common blocker: `EXT-GOV-01`.

### External Point-Loss Register

| Dimension | Maximum | External award | Lost | Finding |
|---|---:|---:|---:|---|
| Scope compliance and exclusions | 10 | 10 | 0 | no loss |
| Source quality and freshness | 20 | 18 | 2 | no lived-experience or participatory source from older/disabled people/caregivers |
| Claim-level evidence and traceability | 15 | 15 | 0 | no loss |
| Opportunity coverage and diversity | 15 | 13 | 2 | no source-domain matrix across required domains |
| Analytical rigor and uncertainty | 15 | 14 | 1 | digital-access evidence was not consistently separated from workflow pain |
| Legal, safety, privacy, and platform constraints | 10 | 10 | 0 | no loss |
| Reproducibility of search method | 10 | 10 | 0 | no loss |
| Clarity and repository hygiene | 5 | 4 | 1 | same-process Codex review mislabeled independent |
| **Total** | **100** | **94** | **6** | **external score is authoritative** |

| Review ID | External finding / required correction | Applied correction | Verification | Status |
|---|---|---|---|---|
| EXT-GOV-01 | Prior Codex review was not independent. | Relabeled all surviving references as Internal Pre-review/Simulation and preserved the historical 100 as non-authoritative. | QUALITY_SCORE_HISTORY.md, CORRECTION_LOG.md, THREAD_SUMMARY.md | correction applied; external verification pending |
| T02-EXT-C01 | Add at least one lived-experience/participatory source from older adults, disabled people, or unpaid caregivers. | Added T02-S12: 56 ONS qualitative interviews with disabled adults, with method, date, geography, limitations, and confidence. | SOURCE_REGISTER.md, SEARCH_LOG.md, MARKET_DISCOVERY_REPORT.md | resolved internally |
| T02-EXT-C02 | Add source-domain coverage for visual, hearing, cognitive, mobility, caregiver, transport, public-service, and social domains. | Added an eight-domain source matrix using direct/context/technical/legal codes. | OPPORTUNITY_INDEX.md | resolved internally |
| T02-EXT-C03 | Distinguish digital-access evidence from workflow-pain evidence for 101, 112–114, 118, and 119. | Rewrote rationales, downgraded 118/119, and added 20-row source coverage separating barrier from workflow. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EVIDENCE_GAPS.md | resolved internally |
| T02-EXT-C04 | Log the exact six-point loss. | Added the dimension-level point-loss register above. | CORRECTION_LOG.md, QUALITY_SCORE_HISTORY.md | resolved internally |

External Governance re-review requested.
