---
status: in-review
version: 0.1.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Opportunity Index

Exactly 20 candidates are qualified for the unranked Gate 1 universe. Evidence IDs resolve in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). Every candidate proposition is an `inference`; no opportunity score or disposition is assigned.

| ID | Problem and bounded utility | Segment / current alternative | Evidence basis | Confidence rationale | Reachability hypothesis | Jurisdiction, privacy, security, or advice constraint |
|---|---|---|---|---|---|---|
| OPP-2026-200 | Recurring services are scattered; a manual inventory could make terms visible. | Subscription users; memory/card statement. | T03-S03/S04 | medium: complaint/problem context direct, adoption unknown | consumer-protection and subscription-help search | no bank/inbox access; current terms user-entered |
| OPP-2026-201 | Renewal price and promo-end changes are hard to compare over time. | Subscription users; calendar/receipts. | T03-S03/S04 | medium | same as 200 | show observation date; no guarantee of renewal notice or price |
| OPP-2026-202 | Consumers need a record of cancellation attempts and confirmations. | Subscription users; email folder/screenshots. | T03-S03/S04 | medium | consumer-protection content | records only; no cancellation execution, dispute filing, or legal conclusion |
| OPP-2026-203 | Free-trial deadlines are easy to miss. | Trial users; calendar. | T03-S04 | medium: regulator guidance explicitly recommends calendar tracking | free-trial help search | user verifies terms; no “safe offer” determination |
| OPP-2026-204 | Bills have heterogeneous due dates and frequencies. | Households; calendar/bank reminder. | T03-S01/S02 | medium: bill difficulty direct, organization effect unknown | budgeting and bill-organization search | manual schedule only; no payment or cash-flow advice |
| OPP-2026-205 | A changed bill is hard to reconcile with prior usage/terms. | Utility/service customers; spreadsheet/calls. | T03-S02/S10 | low: broad cost pressure only | bill-help search | arithmetic and annotations only; no causal or legal determination |
| OPP-2026-206 | Package sizes make shelf prices hard to compare; a unit calculator normalizes units. | Grocery/household-goods shoppers; mental math. | T03-S05/S06 | high: NIST directly supports unit-pricing comparison | unit-price search and consumer educators | compatible units only; store label/user input verified |
| OPP-2026-207 | Consumers lack a dated personal price history for repeat purchases. | Repeat shoppers; receipts/spreadsheet. | T03-S05/S06/S10 | medium: comparison method direct, demand unknown | grocery savings communities | local observations, no market-wide “fair price” claim |
| OPP-2026-208 | Package downsizing obscures effective price changes. | Repeat shoppers; memory/old packages. | T03-S06 | medium: NIST explicitly identifies shrinkflation context | unit-price education channels | product matching and units must be verified |
| OPP-2026-209 | Basket alternatives have different quantities and availability. | Household shopper; spreadsheet/calculator. | T03-S05/S06 | medium | grocery planning search | scenario only; taxes, availability, quality, travel cost shown separately |
| OPP-2026-210 | Households cannot see the cost of personally discarded food. | Adults managing groceries; waste log. | T03-S07 | medium: cost category direct, diary adoption unknown | food-waste education channels | use personal entries; never assign EPA average as promised savings |
| OPP-2026-211 | Repair/replace comparisons mix upfront cost, expected life, energy, and uncertainty. | Appliance-owning households; mental estimate. | T03-S01/S08 | low: components relevant, failure workflow unmeasured | appliance-maintenance search | transparent scenario, no safety, financing, or provider recommendation |
| OPP-2026-212 | Appliance operating cost is opaque without usage and tariff math. | Households; energy label/calculator. | T03-S08 | medium: end-use variation direct | energy-information search | user tariff/usage; timestamp; no guaranteed saving |
| OPP-2026-213 | Energy bills lack a household annotation history for weather, occupancy, or appliance changes. | Utility customers; spreadsheet/notes. | T03-S08/S10 | medium | energy-bill help search | correlations only; no causal diagnosis or tariff-switch advice |
| OPP-2026-214 | Broadband offers present comparable facts in labels but users still need a side-by-side record. | Home internet shoppers; tabs/spreadsheet. | T03-S09 | high: label purpose direct | broadband-label search | use current user-supplied labels; no eligibility/API/speed guarantee |
| OPP-2026-215 | Home-service quotes use inconsistent scopes and units. | Households seeking routine services; spreadsheet. | T03-S01/S02 | low: cost pressure only, quote friction not directly measured | home-service planning search | normalize user-entered scope; no provider ranking, licensing, or safety judgment |
| OPP-2026-216 | Receipts and warranties become separated when a claim is needed. | Owners of household goods; paper/email folders. | T03-S11 | medium: FTC directly advises keeping both | warranty/repair help search | redact sensitive fields; retention/deletion; no credential or inbox requirement |
| OPP-2026-217 | Return windows and required records vary by seller. | Shoppers; receipt/calendar. | T03-S12 | medium: FTC explicitly notes varying deadlines/documents | return/refund help search | seller/jurisdiction controls; tracker is not a rights determination |
| OPP-2026-218 | Store credits and gift cards have hard-to-track issuer terms. | Consumers holding credits; wallet/email. | T03-S02 | low: household difficulty broad, specific problem unevidenced | consumer-protection search | issuer/jurisdiction research missing; no value custody |
| OPP-2026-219 | Cooling-off rights apply only to bounded transactions and deadlines. | Consumers in covered in-person/temporary-location sales; paper forms. | T03-S12 | medium: FTC guidance direct, coverage narrow | consumer-protection organizations | show source/jurisdiction and exclusions; no legal advice or submission |

## Coverage Notes

- Candidate families: recurring charges (200–203), bills (204–205), retail comparison (206–209), food/energy economics (210–213), plan/quote comparison (214–215), and consumer records/deadlines (216–219).
- `OPP-2026-218` is intentionally low confidence pending issuer/jurisdiction evidence.
- No candidate touches funds, creditworthiness, investments, loans, insurance decisions, debt collection, tax filing, or regulated advice.
