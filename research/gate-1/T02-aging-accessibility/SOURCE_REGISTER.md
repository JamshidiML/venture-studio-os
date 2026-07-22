---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Source Register

Access date for every source: `2026-07-22`.

| ID | Source, owner, and URL | Publication / observation date | Geography / segment | Claim supported | Limitations | Confidence |
|---|---|---|---|---|---|---|
| T02-S01 | [Ageing and health](https://www.who.int/en/news-room/fact-sheets/detail/ageing-and-health), World Health Organization | 2025-10-01 | Global older population | Population ageing, heterogeneity, environmental barriers, and independence context. | Projections and synthesis; no product-demand or country-specific adoption evidence. | high |
| T02-S02 | [Assistive technology](https://www.who.int/news-room/fact-sheets/detail/assistive-technology), WHO | 2024-01-02 | Global people needing assistive products | Digital assistive tools, integrated needs, and barriers including awareness, cost, access, fragmentation, and workforce. | Broad global synthesis; country access varies; not candidate-specific demand. | high |
| T02-S03 | [Disability and Functioning FastStats](https://www.cdc.gov/nchs/fastats/disability.htm), CDC/NCHS | page current at access; reported data year 2024 | U.S. adults 18+ | Current hearing, vision, and mobility difficulty measures. | Measures differ from BRFSS/ACS; self-report and definition differences prevent simple aggregation. | high |
| T02-S04 | [CDC disability data release](https://www.cdc.gov/media/releases/2024/s0716-adult-disability.html), CDC | 2024-07-16; underlying BRFSS 2022 | U.S. adults | More than one in four adults reported a disability under BRFSS definitions; cognition, mobility, independent living, hearing, vision, and self-care are relevant domains. | 2022 data; self-report; prevalence varies by instrument. | high |
| T02-S05 | [2026 Tech Trends and Adults 50-Plus](https://www.aarp.org/pri/topics/technology/internet-media-devices/2026-technology-trends-older-adults/), AARP Research | 2025-12-08; fieldwork 2025-09-09 to 2025-10-06 | 3,838 U.S. adults; age 50+ focus | High device adoption alongside privacy, value, usability, support, and age-fit concerns. | Online survey may underrepresent people offline or with severe access barriers; association, not demand experiment. | medium |
| T02-S06 | [Caregiving in the US 2025: Caring Across States](https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-2025-caring-across-states/), AARP and National Alliance for Caregiving | 2025-10-28 | U.S. unpaid family caregivers | Caregiving is widespread; intensity, financial strain, and available support vary by state. | Organization-sponsored survey; does not evaluate a specific coordination product. | medium |
| T02-S07 | [The WebAIM Million — 2025](https://webaim.org/projects/million/2025), WebAIM | tests in 2025-02; updated 2025-03-31 | Top one million home pages from Tranco list | 94.8% had detectable WCAG failures; common automated errors include contrast, alt text, labels, links, buttons, and language. | Automated subset only; home page only; absence of detected errors is not accessibility/conformance. | high |
| T02-S08 | [What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), W3C WAI | Recommendation published 2023-10-05 | Web content, global standard | Current accessibility success criteria include focus, target size, consistent help, redundant entry, and accessible authentication. | Technical standard, not user demand or legal advice; conformance requires broader testing. | high |
| T02-S09 | [The EU becomes more accessible for all](https://digital-strategy.ec.europa.eu/en/news/eu-becomes-more-accessible-all), European Commission | 2025-06-27; EAA application 2025-06-28 | European Union | EAA applies accessibility requirements to specified products/services. | High-level summary; obligations depend on product, service, member-state implementation, and legal analysis. | high |
| T02-S10 | [How Many Young and Older Adults Lived Alone?](https://www.census.gov/library/stories/2024/05/living-arrangements.html), U.S. Census Bureau | 2024-05-30; data year 2022 | U.S. adults | Nearly three in ten adults 65+ lived alone, relevant to independence and connection context. | Living alone is not the same as loneliness or support need; 2022 data. | high |
| T02-S11 | [Social Isolation and Loneliness Outreach Toolkit](https://www.nia.nih.gov/toolkits/social-isolation), National Institute on Aging | updated 2026-06-02 | Older adults and caregivers, primarily U.S. | Older adults face social-isolation risk; toolkit cites one in four community-dwelling adults 65+ as socially isolated. | Outreach synthesis; source statistic is older peer-reviewed research; does not prove app efficacy. | medium |
| T02-S12 | [Disabled people's experiences with activities, goods and services, UK](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/disability/bulletins/disabledpeoplesexperienceswithactivitiesgoodsandservicesuk/februarytomarch2022), UK Office for National Statistics | 2022-07-18; 56 interviews conducted 2022-02 to 2022-03 | Disabled adults 18+ across the UK with varied impairments | Participants described inaccessible online services, poor information, inflexible systems, preparation/workarounds, reliance on family/friends, cognitive demands, screen-reader/format barriers, communication-preference failures, and the need to involve disabled people in service decisions. | Purposive qualitative sample; not representative prevalence; private-sector focus and 2022 fieldwork; it supports lived experience, not demand for any candidate. | medium |

## Conflict and Transfer Notes

- CDC sources use different disability measures and therefore produce different estimates. They are displayed as separate evidence, not merged into a market-size figure.
- WHO global projections, U.S. surveys, and EU regulatory context answer different questions; no one geography is silently generalized to another.
- AARP online samples may exclude some of the people most affected by digital barriers, so adoption estimates do not erase offline support needs.
- WebAIM automated results indicate detectable technical barriers, not complete conformance or lived-experience quality.
- T02-S12 supplies direct lived-experience evidence through qualitative interviews. It is deliberately not converted into prevalence, market size, or proof that any proposed workflow is wanted.
