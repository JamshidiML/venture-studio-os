---
status: in-review
version: 0.1.4
owner_role: Strategy Agent
last_reviewed: 2026-07-23
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Opportunity Index

This index contains the four Qualified Gate 1 Candidates. They are unranked. Sixteen unsupported concepts remain preserved under their original IDs in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). Issue #25 added no source merely to preserve qualification: all 12 disputed rows lacked direct or clearly adjacent observed workflow evidence and moved to the watchlist. Evidence IDs resolve in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). Every proposed utility remains an `inference`; no Opportunity Score or product disposition is assigned.

| ID | Problem and bounded utility | Segment / current alternative | Evidence basis | Confidence rationale | Reachability hypothesis | Jurisdiction, privacy, security, or advice constraint |
|---|---|---|---|---|---|---|
| OPP-2026-200 | Recurring services are scattered; a manual inventory could make terms visible. | Subscription users; memory/card statement. | T03-S03/S04 | medium: complaint/problem context direct, adoption unknown | consumer-protection and subscription-help search | no bank/inbox access; current terms user-entered |
| OPP-2026-201 | Renewal price and promo-end changes are hard to compare over time. | Subscription users; calendar/receipts. | T03-S03/S04 | medium | same as 200 | show observation date; no guarantee of renewal notice or price |
| OPP-2026-202 | Consumers need a record of cancellation attempts and confirmations. | Subscription users; email folder/screenshots. | T03-S03/S04 | medium | consumer-protection content | records only; no cancellation execution, dispute filing, or legal conclusion |
| OPP-2026-204 | Bills have heterogeneous due dates and frequencies. | Households; calendar/bank reminder. | T03-S01/S02 | medium: bill difficulty direct, organization effect unknown | budgeting and bill-organization search | manual schedule only; no payment or cash-flow advice |

## Candidate-to-Source Coverage Matrix

`Direct` means a source observes user pain or behavior tied to the candidate problem. Population statistics, price indexes, regulations, and guidance are never classified as direct pain; they appear as context, alternatives, feasibility, or constraints.

| ID | Final status | Direct problem evidence | Contextual / population evidence | Current-alternative evidence | Technical feasibility | Legal / privacy / safety / platform evidence | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|---|
| 200 | qualified | S03 complaints/difficult cancellation | — | S04 terms/records guidance | manual inventory assumed | S03 current rule status | inventory demand |
| 201 | qualified | — | S03 complaint context | S04 calendar/records guidance | manual log assumed | jurisdiction/terms vary | longitudinal comparison value |
| 202 | qualified | S03 cancellation complaints | — | S04 confirmation/records guidance | manual evidence pack | no execution/legal conclusion | pack improves outcomes |
| 203 | watchlist | — | — | S04 calendar recommendation | calendar feasible in principle | user-entered terms | adoption/frequency |
| 204 | qualified | S02 difficulty paying bills, not calendar pain | S01 financial resilience | calendar stated, not sourced | manual calendar assumed | no payment/bank access | heterogeneous dates create sufficient pain |
| 205 | watchlist | — | S02 cost pressure; S10 dated prices | spreadsheet/calls stated, not sourced | arithmetic feasible in principle | no causal/advice claim | variance reconciliation pain |
| 206 | watchlist | — | S05/S06 comparison guidance | mental math stated, not sourced | unit arithmetic specified by S05/S06 | jurisdiction/store-label variation | separate calculator demand |
| 207 | watchlist | — | S05/S06 unit-pricing context; S10 dated prices | receipts/spreadsheet stated, not sourced | manual history assumed | local/time-specific only | personal history demand |
| 208 | watchlist | — | S06 package-size comparison context | old package/memory stated, not sourced | unit arithmetic specified | product matching accuracy | history changes decisions |
| 209 | watchlist | — | S05/S06 unit-comparison guidance | spreadsheet stated, not sourced | scenario arithmetic assumed | taxes/availability shown | basket comparer demand |
| 210 | watchlist | — | S07 modeled food-waste cost, not diary pain | log stated, not sourced | manual diary assumed | no inherited average/savings | diary completion/value |
| 211 | watchlist | — | S01 resilience; S08 energy context | mental estimate stated, not sourced | scenario math assumed | no safety/finance/provider advice | repair/replace pain |
| 212 | watchlist | — | S08 energy-use components, not user pain | label/calculator stated, not sourced | tariff/usage arithmetic assumed | timestamp/no saving guarantee | standalone calculator demand |
| 213 | watchlist | — | S08 energy; S10 prices | spreadsheet/notes stated, not sourced | annotation assumed | correlation only | annotation history demand |
| 214 | watchlist | — | S09 regulatory comparison-label context | tabs/spreadsheet stated, not sourced | user-supplied label comparison | no API/eligibility/speed guarantee | extra comparer demand |
| 215 | watchlist | — | S01/S02 household cost context | spreadsheet stated, not sourced | normalization assumed | no ranking/licensing/safety judgment | inconsistent-scope pain |
| 216 | watchlist | — | S11 record-retention guidance | paper/email folders stated, not sourced | manual vault assumed | sensitive-data minimization | separation/loss frequency |
| 217 | watchlist | — | S12 seller-policy/deadline context | S12 receipt/calendar guidance | manual tracker assumed | seller/jurisdiction controls | tracker adoption |
| 218 | watchlist | — | — | wallet/email stated, not sourced | record assumed | issuer/jurisdiction research missing | expiry/term pain |
| 219 | watchlist | — | — | paper forms/certified mail S13 | checklist arithmetic/manual record assumed | S13 narrow federal rule, locations, exclusions, three-business-day deadline, state variation, no advice | covered-user pain, checklist adoption and comprehension |

## Coverage Notes

- Qualified candidate families are limited to recurring subscription/cancellation complaints (`200`–`202`) and adjacent observed bill difficulty (`204`). The other 16 concepts remain preserved in the watchlist.
- `OPP-2026-203` and `205`–`219` are watchlist-only at `very low` confidence pending direct workflow evidence. Candidate `219` preserves dedicated T03-S13 and its complete narrow legal boundary despite becoming watchlist-only.
- No candidate touches funds, creditworthiness, investments, loans, insurance decisions, debt collection, tax filing, or regulated advice.

Final External Governance re-review requested
