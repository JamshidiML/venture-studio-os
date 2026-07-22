---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Exclusions

| Space considered | Decision | Reason / rule |
|---|---|---|
| Loan or credit-product comparison, refinancing, or qualification | excluded | Lending/credit advice and regulatory boundary. |
| Investment, securities, crypto, retirement allocation, or trading | excluded | Explicit Issue #6 prohibition and suitability/custody risk. |
| Insurance recommendation, pricing prediction, or underwriting | excluded | Explicit prohibition; regulated and discriminatory-risk domain. |
| Tax filing, deduction advice, benefit optimization, or audit support | excluded | Tax/legal advice boundary. |
| Debt collection, settlement, prioritization, or negotiation | excluded | Explicit prohibition and high consumer-harm risk. |
| Credit score monitoring or improvement | excluded | Credit-scoring boundary and data sensitivity. |
| Gambling, betting budget, or speculative reward tool | excluded | Explicit prohibition and behavioral harm. |
| Wallet, escrow, payment initiation, automated switching, or value custody | excluded | Funds custody/execution and authorization risk. |
| Mandatory bank/open-banking/card feed | excluded | No documented API availability, consent, security, or jurisdiction feasibility; manual fallback required. |
| Inbox or retailer-account scraping as core dependency | excluded | Platform/API, credential, privacy, and T08 overlap. |
| Affiliate-led “best provider” ranking | excluded | Conflict of interest, incomplete comparisons, and recommendation risk. |
| Generic shopping list or household task app | excluded | General utility belongs to T01 unless economic comparison is the primary value. |
| Finance organizer aimed specifically at older adults | excluded from T02 but retained only as general T03 | User demographics do not change the functional finance boundary. |
| Automated legal-rights, refund-eligibility, or dispute determination | excluded | Jurisdiction and legal-advice risk. |
| Guaranteed savings or invented “average household” outcomes | excluded | No evidence supports realized product impact. |

The 2024 FTC expanded click-to-cancel rule is also excluded as a current legal premise because the FTC's March 2026 material identifies it as vacated.

## Hypothesis Watchlist

These concepts remain owned by T03 under their original IDs but are not Qualified Gate 1 Candidates. Household cost pressure, energy context, regulation, and arithmetic feasibility cannot independently establish the proposed workflow pain.

| Opportunity ID | Original concept | Reason not currently qualified | Current confidence | Evidence searched | Missing evidence | Risk and safety constraints | Conditions for future reconsideration | Original Thread ownership |
|---|---|---|---|---|---|---|---|---|
| OPP-2026-205 | Manual bill-variance explainer comparing a changed bill with prior usage or terms | T03-S02 and T03-S10 provide household-cost and dated-price context, not observed variance-reconciliation pain. | very low | T03-S02/S10; CFPB, BLS, bill-help, utility, and household-cost queries in SEARCH_LOG.md | Direct household observation, complaints, diaries, or interviews showing recurrent reconciliation failure and current spreadsheet/call workarounds. | Arithmetic and user annotations only; no causal, billing-error, legal-rights, tariff, payment, or personalized financial-advice conclusion; local/minimum data. | Reconsider only after direct workflow evidence shows recurrence/severity and users can verify every input, date, and calculation. | T03 — household economics and savings |
| OPP-2026-211 | Repair-versus-replace worksheet combining upfront cost, expected life, energy, and uncertainty | T03-S01 and T03-S08 establish resilience and energy context, not a measured repair/replace decision workflow. | very low | T03-S01/S08; household resilience, appliance energy, and maintenance query coverage | Direct household decision observations/interviews, current-alternative mapping, and evidence that comparison dimensions recur. | Transparent scenarios only; no safety assessment, financing, provider recommendation, guaranteed life, repair instruction, or professional-equivalence claim. | Reconsider only with direct workflow evidence plus bounded assumptions, explicit uncertainty, and a safe referral boundary. | T03 — household economics and savings |
| OPP-2026-215 | Home-service quote normalizer for inconsistent scopes and units | T03-S01/S02 are broad financial context and do not observe quote-comparison friction. | very low | T03-S01/S02; home-service planning and household-cost queries | User-supplied quote samples and direct interviews/observations showing inconsistent scope/units and consequential comparison failure. | No provider ranking, licensing, quality, legal, safety, availability, or price-fairness judgment; no vendor scraping or affiliate steering. | Reconsider only after direct evidence documents the bounded quote event and a neutral user-entered normalization schema. | T03 — household economics and savings |
| OPP-2026-218 | Gift-card/store-credit expiry and issuer-term record | No registered source directly supports issuer-term tracking pain; even legal context would not alone establish user pain. | very low | Consumer-protection, returns/refunds, and current-law queries; no qualifying gift-card/credit source found | Current issuer/jurisdiction authority plus direct consumer workflow evidence of recurrent value/term tracking failure and current alternatives. | No value custody, balance claim, expiry/rights determination, issuer integration, credential access, or legal advice; jurisdiction and source date visible. | Reconsider only after both current legal/issuer context and direct consumer workflow evidence are documented. | T03 — household economics and savings |

The auditable T03 universe remains 20 IDs: 16 qualified and four watchlist. No ID was deleted, reused, or renumbered. Candidate 219 is not in the watchlist: its dedicated September 2025 FTC authority and narrow locations, exclusions, third-business-day deadline, jurisdiction, and no-advice boundaries remain intact.
