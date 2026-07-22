---
status: in-review
version: 0.1.2
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Search Log

## Reproducible Method

- Search/access date and cutoff: `2026-07-22`.
- Inclusion: current official or primary evidence about ageing, disability domains, assistive technology, caregiver burden, technology adoption/barriers, accessibility standards, digital accessibility prevalence, living arrangements, or social connection.
- Exclusion: clinical treatment/diagnosis, emergency monitoring, vendor claims, unverified market sizes, inaccessible paywalled evidence, surveillance products, and sources that stereotype age or disability.
- Population rule: preserve each source's definition; never combine age 50+, age 60+, age 65+, BRFSS disability, ACS disability, or functioning difficulty as if identical.

| Run | Exact query | Result used | Decision |
|---:|---|---|---|
| 1 | `site:who.int/news-room/fact-sheets/detail age ageing and health 2025 older people` | T02-S01 | included: current global authoritative context |
| 2 | `site:who.int/news-room/fact-sheets/detail assistive-technology 2024 2025` | T02-S02 | included: global assistive-technology barriers |
| 3 | `site:cdc.gov disability data adults United States 2024 2025` | T02-S03/T02-S04 | included separately because measures differ |
| 4 | `site:aarp.org research caregiving in the US 2025 report` | T02-S06 | included: disclosed national caregiving research |
| 5 | `site:aarp.org/research/topics/technology 2025 older adults technology trends survey` | T02-S05 | included: current survey and method |
| 6 | `site:w3.org/WAI/standards-guidelines/wcag WCAG 2.2 Recommendation 2023` | T02-S08 | included: normative standard |
| 7 | `site:webaim.org/projects/million/ 2025 report accessibility errors` | T02-S07 | included with automated-test limitations |
| 8 | `site:nia.nih.gov health loneliness social isolation older people 2024 2025` | T02-S11 | included: authoritative outreach synthesis |
| 9 | `site:census.gov older adults living alone 2024 report 65` | T02-S10 | included with living-alone/loneliness distinction |
| 10 | `site:europa.eu European Accessibility Act 28 June 2025 official` | T02-S09 | included as EU regulatory context, not legal advice |
| 11 | `site:ons.gov.uk disabled people's experiences activities goods services qualitative interviews accessibility` | T02-S12 | included: 56 lived-experience interviews; supports reported access/workaround barriers, not prevalence or product demand |

## Searches Not Converted Into Claims

- Product/vendor searches were intentionally avoided because popularity, marketing, and feature lists do not establish unmet need.
- No source was found that directly compares willingness to pay for the 20 candidates; no such claim is made.
- Clinical-condition searches were stopped at the hard boundary because this issue authorizes non-clinical independence support only.
