---
status: in-review
version: 0.1.4
owner_role: Strategy Agent
last_reviewed: 2026-07-23
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Market Discovery — Household Economics and Savings

## Executive Summary

- **The auditable universe contains 20 low-regulatory, manual-first concepts: 4 Qualified Gate 1 Candidates and 16 Hypothesis Watchlist Candidates.** Neither tier is ranked. The qualified set is limited to recurring subscription/cancellation complaints and adjacent observed bill difficulty; comparison, calculator, consumer-guidance, record, and Cooling-Off Rule concepts remain preserved as hypotheses without qualifying workflow evidence.
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
| Candidate count | 4 qualified + 16 watchlist = 20 auditable IDs |
| Reserved IDs | `OPP-2026-200` through `OPP-2026-299`; this artifact uses `200` through `219` only |
| Explicit exclusions | Lending, investing, securities, crypto, insurance underwriting, tax filing, debt collection, regulated advice, credit scoring, gambling, custody of funds, general utilities, health, education, aging/accessibility, creator, SMB, and platform companion workflows |

## Methodology

The search prioritized current U.S. regulator, official survey, standards, energy, telecommunications, and environmental sources. The first complete draft defined 20 candidate workflows and broad evidence. The correction pass added source dates/access dates/geographies/limitations, current negative-option rule status, candidate-level claim types and constraints, jurisdiction flags, manual fallback, exact query logs, evidence ceilings, and a boundary between information organization and regulated advice.

External Governance Correction Cycle 2 resolved the Cooling-Off Rule blocker with the FTC's dedicated September 2025 article and audited every candidate's source classification. External re-review verified both `EXT-GOV-01` and `T03-EXT-B02` as resolved. Cycle 3 moved candidates `205`, `211`, `215`, and `218` to the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). External Governance Cycle 3 then scored the package `94/100`, losing one source-quality point, four qualified/watchlist-integrity points, and one analytical-rigor point because 12 remaining qualified rows were still supported only by regulation, guidance, standards, context, feasibility, or asserted alternatives.

Issue #25 applies the contract consistently. No source was added merely to preserve count. IDs `203`, `206`–`210`, `212`–`214`, `216`–`217`, and `219` moved to the existing watchlist. T03-S13, the dedicated September 2025 FTC authority, remains fully preserved for `219` as legal context and a safety boundary; it does not independently qualify user pain.

Qualification requires direct observed problem evidence or clearly adjacent observed workflow evidence for a household-economic workflow authorized by Issue #6; no handling or movement of funds; no credit/insurance/tax/investment decision; no assumed bank or inbox access; user-verifiable inputs; an explicit jurisdiction or source-date warning where relevant; and no guaranteed savings claim. Regulation and consumer guidance establish constraints or current alternatives, not direct pain.

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

## Qualified Gate 1 Candidate Universe

The four qualified candidates are below and in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md). Sixteen other IDs remain auditable in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist); they are not qualified candidates. No disputed ID was strengthened because no qualifying workflow source was added.

| Opportunity ID | Bounded workflow | Evidence status | Confidence | Primary constraint |
|---|---|---|---|---|
| OPP-2026-200 | Manual subscription inventory | inference from T03-S03/S04 | medium | no bank/inbox access assumed |
| OPP-2026-201 | Renewal and price-change log | inference from T03-S03/S04 | medium | terms user-verified; law varies |
| OPP-2026-202 | Cancellation evidence pack | inference from T03-S03/S04 | medium | records only; no legal conclusion |
| OPP-2026-204 | Household bill calendar | inference from T03-S01/S02 | medium | no payment execution or bank access |

## Legal, Privacy, Security, and Trust Controls

- **Information, not advice:** calculations show user-entered scenarios, assumptions, units, dates, and arithmetic. They do not recommend borrowing, investing, insurance, tax positions, debt actions, or providers.
- **No financial access assumption:** no bank credential, open-banking API, card feed, inbox, retailer account, or transaction scraping is required. Optional integrations would need separate feasibility, consent, security, jurisdiction, and API evidence.
- **No custody or execution:** candidates never hold funds, initiate payments, cancel services, file disputes, submit legal notices, or switch providers.
- **Jurisdiction and freshness:** consumer rights, cooling-off, gift-card, broadband, utility, warranty, and return terms must show jurisdiction, source, observation date, and user verification. The vacated 2024 FTC rule is not treated as current law.
- **Security:** receipts and bills may expose addresses, account numbers, barcodes, and purchase history; minimize fields, redact by default, encrypt appropriately, and define deletion/retention before any later build.
- **Trust:** never guarantee savings, use invented “typical” prices, hide affiliate compensation, sell transaction data, or present uncertain OCR/extraction as verified.

## Exclusions, Risks, and Unknowns

Detailed decisions and the 16-entry Hypothesis Watchlist are in [EXCLUSIONS.md](EXCLUSIONS.md); evidence limits are in [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md). No direct willingness-to-pay, retention, switching-success, channel-cost, or realized-savings evidence was found. Candidate values therefore remain hypotheses.

## Confidence Assessment

Overall confidence is `medium` that recurring-charge/cancellation and bill-difficulty workflows exist for retained `200`–`202` and `204`. Confidence is `very low` for the 16 watchlist concepts and `low` to `medium` that any retained workflow produces enough incremental value for adoption or payment. No regulation, standard, estimate, or guidance is transformed into user pain, market size, or revenue.

## Recommended Next Action

Review the four-qualified/16-watchlist split, unchanged 13-source register, dedicated T03-S13 Cooling-Off Rule source, candidate 219's preserved narrow locations/exclusions/deadline/no-advice treatment inside the watchlist, exact External Cycle-3 point loss, source classification, jurisdiction labels, manual fallback, security, and absence of regulated advice. Do not select a winner or begin Gate 2.

Final External Governance re-review requested
