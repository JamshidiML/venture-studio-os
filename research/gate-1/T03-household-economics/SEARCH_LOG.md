---
status: in-review
version: 0.1.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Search Log

## Reproducible Method

- Search/access date and cutoff: `2026-07-22`.
- Inclusion: official U.S. household-finance surveys, consumer-protection sources, metrology/unit-pricing standards, current price indexes, environmental cost research, residential-energy information, telecommunications labels, warranty/return guidance.
- Exclusion: affiliate blogs, coupon sites, SEO market-size estimates, bank/vendor marketing, scraping-dependent comparisons, investment/tax/credit/insurance/lending advice, and any source without verifiable provenance.
- Current-law rule: search for the latest regulator page before relying on a rule announcement; record vacatur or pending rulemaking.

| Run | Exact query | Result used | Decision |
|---:|---|---|---|
| 1 | `site:federalreserve.gov consumers communities SHED 2024 report unexpected expense May 2025` | T03-S01 | included: official national survey |
| 2 | `site:consumerfinance.gov/data-research/research-reports making ends meet survey 2024 2025 bills expenses` | T03-S02 | included: official bill/expense evidence |
| 3 | `site:ftc.gov subscriptions negative option consumer reports recurring charges 2024 2025` | T03-S04 | included as consumer guidance, not current-law authority |
| 4 | `site:ftc.gov 2026 negative option subscriptions current rule consumer FTC` | T03-S03 | included: latest status and complaint context |
| 5 | `site:ftc.gov 2025 court vacated click-to-cancel rule official FTC negative option rule vacated` | T03-S03 | current page confirms vacated 2024 rule; older rule announcement not relied upon |
| 6 | `site:nist.gov/pml/owm unit pricing guide consumer official grocery` | T03-S05/T03-S06 | included: official comparison method and jurisdiction variation |
| 7 | `site:epa.gov/land-research estimating cost food waste American consumers April 2025` | T03-S07 | included with national-model limitation |
| 8 | `site:eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php 2024 household electricity uses` | T03-S08 | included with underlying-data age warning |
| 9 | `site:fcc.gov broadband labels consumer price fees 2024 2025` | T03-S09 | included: official label evidence |
| 10 | `site:bls.gov/cpi latest annual 2025 consumer prices food energy household official` | T03-S10 | included only for dated-baseline requirement |
| 11 | `site:consumer.ftc.gov warranties receipts returns cooling off rule 2025 consumer` | T03-S11/T03-S12 | included with policy/jurisdiction limitations |
| 12 | `site:energy.gov/energysaver estimating appliance energy use operating cost official` | no additional source | not used: current result did not provide a sufficiently clear dated consumer page; EIA retained |

## Searches Not Performed

- No bank aggregation/API search was used to qualify a candidate because Issue #6 requires feasibility, consent, jurisdiction, and API evidence before reliance; all candidates have manual input.
- No competitor pricing, download, revenue, user-count, app-store, or review data was used.
- No tax, credit, debt, investment, insurance, or lending research was performed beyond confirming those boundaries.
