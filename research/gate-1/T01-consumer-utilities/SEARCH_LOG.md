---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T01
issue_number: 4
gate: 1
---

# T01 Search Log

## Reproducible Method

- Search date and source cutoff: `2026-07-22`.
- Discovery surface: web search plus direct opening of authoritative result pages.
- Inclusion: official statistics/guidance or primary research with date, scope, and methodology; relevant to repeated non-clinical consumer or household friction.
- Exclusion: SEO market-size pages, anonymous claims, app-store popularity, unsourced competitor pages, product-copying material, personal finance, clinical, education, accessibility, creator, SMB, or platform-companion research.
- Freshness rule: use current pages for changing facts; retain older guidance only when the date and staleness limitation are explicit.

| Run | Exact query | Result used | Decision |
|---:|---|---|---|
| 1 | `site:bls.gov/news.release/atus.nr0.htm American Time Use Survey 2024 June 2025 household activities` | T01-S01 | included: official national time-use evidence |
| 2 | `site:epa.gov/land-research/food-waste-research US household food waste 2024 2025` | T01-S07 | included: official modeled cost and waste context |
| 3 | `site:foodsafety.gov keep food safe FoodKeeper app storage chart official` | T01-S04 | included with stale-date warning |
| 4 | `site:wrap.ngo/resources/report household food waste 2024 UK report` | T01-S02, T01-S03 | included: current disclosed UK household survey and behavior analysis |
| 5 | `site:census.gov time use household activities 2025 American Time Use official household management errands` | no additional source | not used: BLS is the direct ATUS owner |
| 6 | `site:energy.gov home maintenance checklist consumer official recurring maintenance` | T01-S05 | included: cadence evidence, not demand evidence |
| 7 | `site:usfa.fema.gov smoke alarm monthly test official 2025` | T01-S06 | included: direct safety cadence |
| 8 | `site:aphis.usda.gov pet ownership survey 2024 official routines` | T01-S08 | included narrowly; scope mismatch lowers confidence |
| 9 | `site:consumer.ftc.gov warranties receipts returns cooling off rule 2025 consumer` | T01-S09 | boundary source; purchase-deadline concepts assigned to T03 |
| 10 | `site:census.gov older adults living alone 2024 report 65` | no T01 source | excluded: aging/accessibility belongs to T02 |

## External Governance Evidence Audit

The Cycle-2 correction did not pad the register with adjacent sources. A candidate-by-candidate audit found no direct problem evidence in the existing register for possession location, borrowed-item return, reusable packing, plant care, pet handoff, idle-time queues, completion capture, or routine restart. Those candidates were downgraded to unsupported `very low` confidence hypotheses; T01-S08 remains contextual animal-keeping evidence and is not represented as pet-handoff pain.

Cycle 3 added no search and no source. It accepted the Cycle-2 external finding that those eight concepts lack qualifying evidence, moved them to the Hypothesis Watchlist, and retained the existing evidence classifications and full 20-ID coverage matrix.

## Search Coverage Check

The search covered frequency, food management, household maintenance, safety cadence, and non-clinical animal care. Direct demand, willingness-to-pay, retention, and acquisition evidence were intentionally not inferred from these sources and remain in [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md).
