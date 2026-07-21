---
status: in-review
version: 0.1.1
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
