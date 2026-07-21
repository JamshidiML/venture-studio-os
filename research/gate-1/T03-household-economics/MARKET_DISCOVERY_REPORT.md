---
status: in-review
version: 0.1.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Market Discovery — Household Economics and Savings

## Executive Summary

- **Twenty low-regulatory, manual-first candidates were documented and left unranked.** The universe covers recurring subscriptions and bills, price/unit comparison, grocery and food-waste organization, appliance/energy information, broadband-label comparison, quotes, receipts, warranties, returns, store credit, and cooling-off records.
- **Current official evidence supports recurring household financial friction without proving product demand.** Federal Reserve and CFPB surveys show constrained financial resilience and bill difficulty; FTC sources document continuing negative-option complaints; NIST identifies inconsistent unit-pricing regulation; EPA models material food-waste cost ([T03-S01](SOURCE_REGISTER.md), [T03-S02](SOURCE_REGISTER.md), [T03-S03](SOURCE_REGISTER.md), [T03-S05](SOURCE_REGISTER.md), [T03-S07](SOURCE_REGISTER.md)).
- **The design boundary avoids regulated finance.** No lending, investing, securities, crypto, insurance underwriting, tax, debt collection, credit scoring, custody, or personalized financial advice is proposed. No bank-data, email, retailer, or paid API access is assumed.
- **Jurisdiction and data handling remain decisive constraints.** Consumer rights, cooling-off periods, gift-card rules, utility/broadband terms, and privacy obligations vary. Candidates organize user-provided facts and source links; they do not decide legal rights or guarantee savings.

## Objective and Scope

| Field | Bound |
|---|---|
| Authorization | [Parent Issue #3](https://github.com/JamshidiML/venture-studio-os/issues/3) and [Issue #6](https://github.com/JamshidiML/venture-studio-os/issues/6) |
| Geography | Initial evidence scan: United States; jurisdiction is explicit and no global generalization is made |
| Segment | Consumers organizing household spending, bills, prices, receipts, and recurring costs |
| Source cutoff | 2026-07-22 |
| Candidate count | Exactly 20 |
| Reserved IDs | `OPP-2026-200` through `OPP-2026-299`; this artifact uses `200` through `219` only |
| Explicit exclusions | Lending, investing, securities, crypto, insurance underwriting, tax filing, debt collection, regulated advice, credit scoring, gambling, custody of funds, general utilities, health, education, aging/accessibility, creator, SMB, and platform companion workflows |

## Methodology

The search prioritized current U.S. regulator, official survey, standards, energy, telecommunications, and environmental sources. The first complete draft defined 20 candidate workflows and broad evidence. The correction pass added source dates/access dates/geographies/limitations, current negative-option rule status, candidate-level claim types and constraints, jurisdiction flags, manual fallback, exact query logs, evidence ceilings, and a boundary between information organization and regulated advice.

Qualification required: a recurring household-economic workflow authorized by Issue #6; at least one traceable official source; no handling or movement of funds; no credit/insurance/tax/investment decision; no assumed bank or inbox access; user-verifiable inputs; an explicit jurisdiction or source-date warning where relevant; and no guaranteed savings claim.

## Evidence-Backed Problem Landscape

| Material claim | Type | Source | Confidence | Interpretation and limitation |
|---|---|---|---|---|
| In the 2024 SHED, 63% of U.S. adults said they could cover a hypothetical $400 emergency expense using cash or equivalent, unchanged from 2022–2023. | evidence | T03-S01 | high | National survey evidence of resilience constraints; not candidate-specific demand and not a market size. |
| CFPB's 2024 survey reported deterioration in financial well-being and more households having difficulty paying bills or expenses. | evidence | T03-S02 | high | Direct official survey synthesis; does not identify which organization tool changes outcomes. |
| FTC reported in March 2026 that it continued to receive thousands of negative-option complaints annually and more than 100,000 over five years; the 2024 expanded rule had been vacated. | evidence | T03-S03 | high | Supports persistent subscription/cancellation friction and warns against treating the vacated 2024 rule as current law. |
| NIST reports that U.S. unit-pricing requirements vary by jurisdiction and positions unit pricing as a value-comparison method. | evidence | T03-S05/T03-S06 | high | Direct standards/regulatory overview; store data quality and package comparability remain user-verification issues. |
| EPA's April 2025 model estimated U.S. consumer food waste cost at $728 per person annually. | evidence | T03-S07 | high | National model, not personally realized savings; candidate impact cannot inherit this value. |
| FCC broadband labels are intended to disclose price, fees, data allowances, and performance information for comparison. | evidence | T03-S09 | high | Label availability/content can change; the tool must not scrape or guarantee plan eligibility. |
| Manual-first input will be acceptable enough to avoid bank, inbox, or retailer integration. | assumption | No direct source; owner: Strategy Agent | low | Privacy-preserving feasibility assumption; later testing must compare completion and accuracy without requiring regulated data access. |
| Kill a candidate if users cannot verify all monetary inputs and source dates before seeing any calculation. | hypothesis | Not tested | low | Future safety threshold; prevents opaque “AI savings” claims. |

## Opportunity Universe

The detailed index is in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

| Opportunity ID | Bounded workflow | Evidence status | Confidence | Primary constraint |
|---|---|---|---|---|
| OPP-2026-200 | Manual subscription inventory | inference from T03-S03/S04 | medium | no bank/inbox access assumed |
| OPP-2026-201 | Renewal and price-change log | inference from T03-S03/S04 | medium | terms user-verified; law varies |
| OPP-2026-202 | Cancellation evidence pack | inference from T03-S03/S04 | medium | records only; no legal conclusion |
| OPP-2026-203 | Free-trial deadline calendar | inference from T03-S04 | medium | user-entered terms; no guarantee |
| OPP-2026-204 | Household bill calendar | inference from T03-S01/S02 | medium | no payment execution or bank access |
| OPP-2026-205 | Manual bill-variance explainer | inference from T03-S02/T03-S10 | low | arithmetic only; no advice or cause claim |
| OPP-2026-206 | Grocery unit-price calculator | inference from T03-S05/S06 | high | consistent units and user verification |
| OPP-2026-207 | Personal price book | inference from T03-S05/S06 | medium | local/time-specific observations only |
| OPP-2026-208 | Package-size history | inference from T03-S06 | medium | barcode/product matching accuracy |
| OPP-2026-209 | Grocery basket scenario comparer | inference from T03-S05/S06 | medium | no price guarantee; taxes/availability vary |
| OPP-2026-210 | Food-waste cost diary | inference from T03-S07 | medium | personal measurements, no inherited national savings |
| OPP-2026-211 | Repair-versus-replace worksheet | inference from T03-S01/S08 | low | scenario tool, not financial/safety advice |
| OPP-2026-212 | Appliance operating-cost calculator | inference from T03-S08 | medium | user tariff and usage inputs; dated assumptions |
| OPP-2026-213 | Energy-bill usage annotation | inference from T03-S08/T03-S10 | medium | no causal or tariff-switch advice |
| OPP-2026-214 | Broadband-label plan comparer | inference from T03-S09 | high | labels/current offers user-verified |
| OPP-2026-215 | Home-service quote normalizer | inference from T03-S01/S02 | low | does not recommend provider or assess safety |
| OPP-2026-216 | Receipt and warranty record vault | inference from T03-S11 | medium | sensitive data minimization and retention |
| OPP-2026-217 | Return/refund deadline tracker | inference from T03-S12 | medium | retailer/jurisdiction terms control |
| OPP-2026-218 | Gift-card/store-credit expiry record | inference from T03-S02 | low | jurisdiction/issuer rules not researched |
| OPP-2026-219 | Purchase cooling-off checklist | inference from T03-S12 | medium | narrow FTC rule coverage; legal disclaimer |

## Legal, Privacy, Security, and Trust Controls

- **Information, not advice:** calculations show user-entered scenarios, assumptions, units, dates, and arithmetic. They do not recommend borrowing, investing, insurance, tax positions, debt actions, or providers.
- **No financial access assumption:** no bank credential, open-banking API, card feed, inbox, retailer account, or transaction scraping is required. Optional integrations would need separate feasibility, consent, security, jurisdiction, and API evidence.
- **No custody or execution:** candidates never hold funds, initiate payments, cancel services, file disputes, submit legal notices, or switch providers.
- **Jurisdiction and freshness:** consumer rights, cooling-off, gift-card, broadband, utility, warranty, and return terms must show jurisdiction, source, observation date, and user verification. The vacated 2024 FTC rule is not treated as current law.
- **Security:** receipts and bills may expose addresses, account numbers, barcodes, and purchase history; minimize fields, redact by default, encrypt appropriately, and define deletion/retention before any later build.
- **Trust:** never guarantee savings, use invented “typical” prices, hide affiliate compensation, sell transaction data, or present uncertain OCR/extraction as verified.

## Exclusions, Risks, and Unknowns

Detailed decisions are in [EXCLUSIONS.md](EXCLUSIONS.md) and evidence limits in [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md). No direct willingness-to-pay, retention, switching-success, channel-cost, or realized-savings evidence was found. Candidate values therefore remain hypotheses.

## Confidence Assessment

Overall confidence is `high` that household cost organization, recurring-charge, comparison, food-waste, and consumer-record frictions exist. Confidence is `low` to `medium` that any individual workflow produces enough incremental value for adoption or payment. No estimate is transformed into a market-size or revenue claim.

## Recommended Next Action

Request independent Governance review of the nine artifacts, including current-law treatment, jurisdiction labels, manual fallback, security, calculation transparency, and the absence of regulated advice. Do not select a winner or begin Gate 2.
