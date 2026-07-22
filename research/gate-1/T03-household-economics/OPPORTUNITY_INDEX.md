---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Opportunity Index

This index contains the 16 Qualified Gate 1 Candidates. They are unranked. Four unsupported concepts remain preserved under their original IDs in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). Evidence IDs resolve in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). Every proposed utility remains an `inference`; no Opportunity Score or product disposition is assigned.

| ID | Problem and bounded utility | Segment / current alternative | Evidence basis | Confidence rationale | Reachability hypothesis | Jurisdiction, privacy, security, or advice constraint |
|---|---|---|---|---|---|---|
| OPP-2026-200 | Recurring services are scattered; a manual inventory could make terms visible. | Subscription users; memory/card statement. | T03-S03/S04 | medium: complaint/problem context direct, adoption unknown | consumer-protection and subscription-help search | no bank/inbox access; current terms user-entered |
| OPP-2026-201 | Renewal price and promo-end changes are hard to compare over time. | Subscription users; calendar/receipts. | T03-S03/S04 | medium | same as 200 | show observation date; no guarantee of renewal notice or price |
| OPP-2026-202 | Consumers need a record of cancellation attempts and confirmations. | Subscription users; email folder/screenshots. | T03-S03/S04 | medium | consumer-protection content | records only; no cancellation execution, dispute filing, or legal conclusion |
| OPP-2026-203 | Free-trial deadlines are easy to miss. | Trial users; calendar. | T03-S04 | medium: regulator guidance explicitly recommends calendar tracking | free-trial help search | user verifies terms; no “safe offer” determination |
| OPP-2026-204 | Bills have heterogeneous due dates and frequencies. | Households; calendar/bank reminder. | T03-S01/S02 | medium: bill difficulty direct, organization effect unknown | budgeting and bill-organization search | manual schedule only; no payment or cash-flow advice |
| OPP-2026-206 | Package sizes make shelf prices hard to compare; a unit calculator normalizes units. | Grocery/household-goods shoppers; mental math. | T03-S05/S06 | high: NIST directly supports unit-pricing comparison | unit-price search and consumer educators | compatible units only; store label/user input verified |
| OPP-2026-207 | Consumers lack a dated personal price history for repeat purchases. | Repeat shoppers; receipts/spreadsheet. | T03-S05/S06/S10 | medium: comparison method direct, demand unknown | grocery savings communities | local observations, no market-wide “fair price” claim |
| OPP-2026-208 | Package downsizing obscures effective price changes. | Repeat shoppers; memory/old packages. | T03-S06 | medium: NIST explicitly identifies shrinkflation context | unit-price education channels | product matching and units must be verified |
| OPP-2026-209 | Basket alternatives have different quantities and availability. | Household shopper; spreadsheet/calculator. | T03-S05/S06 | medium | grocery planning search | scenario only; taxes, availability, quality, travel cost shown separately |
| OPP-2026-210 | Households cannot see the cost of personally discarded food. | Adults managing groceries; waste log. | T03-S07 | medium: cost category direct, diary adoption unknown | food-waste education channels | use personal entries; never assign EPA average as promised savings |
| OPP-2026-212 | Appliance operating cost is opaque without usage and tariff math. | Households; energy label/calculator. | T03-S08 | medium: end-use variation direct | energy-information search | user tariff/usage; timestamp; no guaranteed saving |
| OPP-2026-213 | Energy bills lack a household annotation history for weather, occupancy, or appliance changes. | Utility customers; spreadsheet/notes. | T03-S08/S10 | medium | energy-bill help search | correlations only; no causal diagnosis or tariff-switch advice |
| OPP-2026-214 | Broadband offers present comparable facts in labels but users still need a side-by-side record. | Home internet shoppers; tabs/spreadsheet. | T03-S09 | high: label purpose direct | broadband-label search | use current user-supplied labels; no eligibility/API/speed guarantee |
| OPP-2026-216 | Receipts and warranties become separated when a claim is needed. | Owners of household goods; paper/email folders. | T03-S11 | medium: FTC directly advises keeping both | warranty/repair help search | redact sensitive fields; retention/deletion; no credential or inbox requirement |
| OPP-2026-217 | Return windows and required records vary by seller. | Shoppers; receipt/calendar. | T03-S12 | medium: FTC explicitly notes varying deadlines/documents | return/refund help search | seller/jurisdiction controls; tracker is not a rights determination |
| OPP-2026-219 | Cooling-off rights apply only to bounded transactions and deadlines. | Consumers in covered home/workplace/dormitory or seller temporary-location sales; paper forms. | T03-S13 | medium: dedicated FTC guidance directly states locations, exclusions, and midnight of the third business day; checklist adoption unknown | consumer-protection organizations | show source/jurisdiction/exclusions; not online/general retail; no coverage decision, advice, or submission |

## Candidate-to-Source Coverage Matrix

`Direct` means a source observes user pain or behavior tied to the candidate problem. Population statistics, price indexes, regulations, and guidance are never classified as direct pain; they appear as context, alternatives, feasibility, or constraints.

| ID | Final status | Direct problem evidence | Contextual / population evidence | Current-alternative evidence | Technical feasibility | Legal / privacy / safety / platform evidence | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|---|
| 200 | qualified | S03 complaints/difficult cancellation | — | S04 terms/records guidance | manual inventory assumed | S03 current rule status | inventory demand |
| 201 | qualified | — | S03 complaint context | S04 calendar/records guidance | manual log assumed | jurisdiction/terms vary | longitudinal comparison value |
| 202 | qualified | S03 cancellation complaints | — | S04 confirmation/records guidance | manual evidence pack | no execution/legal conclusion | pack improves outcomes |
| 203 | qualified | — | — | S04 calendar recommendation | calendar feasible in principle | user-entered terms | adoption/frequency |
| 204 | qualified | S02 difficulty paying bills, not calendar pain | S01 financial resilience | calendar stated, not sourced | manual calendar assumed | no payment/bank access | heterogeneous dates create sufficient pain |
| 205 | watchlist | — | S02 cost pressure; S10 dated prices | spreadsheet/calls stated, not sourced | arithmetic feasible in principle | no causal/advice claim | variance reconciliation pain |
| 206 | qualified | — | S05/S06 comparison guidance | mental math stated, not sourced | unit arithmetic specified by S05/S06 | jurisdiction/store-label variation | separate calculator demand |
| 207 | qualified | — | S05/S06 unit-pricing context; S10 dated prices | receipts/spreadsheet stated, not sourced | manual history assumed | local/time-specific only | personal history demand |
| 208 | qualified | — | S06 package-size comparison context | old package/memory stated, not sourced | unit arithmetic specified | product matching accuracy | history changes decisions |
| 209 | qualified | — | S05/S06 unit-comparison guidance | spreadsheet stated, not sourced | scenario arithmetic assumed | taxes/availability shown | basket comparer demand |
| 210 | qualified | — | S07 modeled food-waste cost, not diary pain | log stated, not sourced | manual diary assumed | no inherited average/savings | diary completion/value |
| 211 | watchlist | — | S01 resilience; S08 energy context | mental estimate stated, not sourced | scenario math assumed | no safety/finance/provider advice | repair/replace pain |
| 212 | qualified | — | S08 energy-use components, not user pain | label/calculator stated, not sourced | tariff/usage arithmetic assumed | timestamp/no saving guarantee | standalone calculator demand |
| 213 | qualified | — | S08 energy; S10 prices | spreadsheet/notes stated, not sourced | annotation assumed | correlation only | annotation history demand |
| 214 | qualified | — | S09 regulatory comparison-label context | tabs/spreadsheet stated, not sourced | user-supplied label comparison | no API/eligibility/speed guarantee | extra comparer demand |
| 215 | watchlist | — | S01/S02 household cost context | spreadsheet stated, not sourced | normalization assumed | no ranking/licensing/safety judgment | inconsistent-scope pain |
| 216 | qualified | — | S11 record-retention guidance | paper/email folders stated, not sourced | manual vault assumed | sensitive-data minimization | separation/loss frequency |
| 217 | qualified | — | S12 seller-policy/deadline context | S12 receipt/calendar guidance | manual tracker assumed | seller/jurisdiction controls | tracker adoption |
| 218 | watchlist | — | — | wallet/email stated, not sourced | record assumed | issuer/jurisdiction research missing | expiry/term pain |
| 219 | qualified | — | — | paper forms/certified mail S13 | checklist arithmetic/manual record assumed | S13 narrow federal rule, locations, exclusions, three-business-day deadline, state variation, no advice | covered-user pain, checklist adoption and comprehension |

## Coverage Notes

- Qualified candidate families: recurring charges (200–203), bill organization (204), retail comparison (206–209), food/energy economics (210, 212–213), plan comparison (214), and consumer records/deadlines (216–217, 219). The four other concepts remain in the watchlist.
- `OPP-2026-205`, `211`, `215`, and `218` are watchlist-only at `very low` confidence pending direct workflow evidence; `219` remains qualified with dedicated T03-S13 and its narrow legal boundary.
- No candidate touches funds, creditworthiness, investments, loans, insurance decisions, debt collection, tax filing, or regulated advice.
