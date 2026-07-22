---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T09 Gate 1 Market Discovery — Family and Household Coordination

## Executive summary

This Gate 1 thread documents 15 retained, non-ranked opportunity inferences for families, co-parents, and shared households. Five candidates were removed during External Governance Correction Cycle 2 when direct-problem searches did not support them. Current public evidence establishes that household management and childcare consume recurring time; direct surveys and small qualitative studies additionally document unequal schedule/household responsibility, cognitive household labor, negotiation, and separated-family communication risks. The evidence does **not** establish willingness to pay, product-market fit, or a winning product.

Direct evidence is strongest for schedule management, division of household labor, household negotiation, and separated-family communication. It remains segment-limited and does not prove demand for any particular solution. Existing family calendars and supervision products demonstrate alternatives and permission complexity only; regulation and population statistics are not classified as direct pain.

## Objective and scope

- Authorization: Parent Issue [#3](https://github.com/JamshidiML/venture-studio-os/issues/3), child Issue [#12](https://github.com/JamshidiML/venture-studio-os/issues/12)
- Gate: 1 — market discovery only
- Geography: United States and European/United Kingdom regulatory and usage evidence; candidate inferences require country-specific validation
- Source cutoff and access date: 2026-07-22
- Assigned ID range: `OPP-2026-801` through `OPP-2026-820`; retained IDs: 15, with 812, 814, 815, 819, and 820 retired and not reused
- Explicit exclusions: surveillance, covert monitoring, custody/legal advice, medical diagnosis, school administration, general finance, manipulative child engagement, and single-user utilities without a shared-household core

## Methodology

The thread searched current government statistics, direct independent parent surveys, peer-reviewed household-work research, participatory/lived-experience studies, regulator guidance, and official platform documentation. The candidate coverage matrix separately classifies direct problem evidence, context, alternatives, feasibility, legal/safety constraints, and unsupported assumptions. Each material claim is typed as `evidence`, `inference`, `assumption`, or `hypothesis`; category-level evidence is never silently promoted to candidate demand.

Searches, dates, and negative findings are reproducible in [SEARCH_LOG.md](SEARCH_LOG.md). Source metadata and limitations are in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). No interviews, surveys, price tests, or platform API tests were performed.

## Material evidence register

| Claim | Type | Source | Geography / date | Confidence | Limitation |
|---|---|---|---|---|---|
| Household management and childcare are recurring activities with measurable time burden. | evidence | T09-S01, T09-S02 | US; 2025 activity data released 2026 | high | Time use does not prove software demand or willingness to pay. |
| Family structure and living arrangements are diverse enough that one fixed household model would exclude meaningful segments. | evidence | T09-S03, T09-S04 | US; 2025 estimates / 2023 survey | high | US definitions and samples do not generalize globally. |
| Parents manage children's digital use and report material online-safety concerns. | evidence | T09-S05 | UK; report published 2025 | medium | Some underlying experience data predates publication; attitudes are not purchase behavior. |
| Products processing children's data can require parental consent, data minimization, retention limits, and child-readable communication. | evidence | T09-S06, T09-S07, T09-S08 | US/EU; rules current in 2025–2026 | high | Applicability depends on age, data, service design, and jurisdiction; legal advice is still required. |
| Family calendars and supervision suites already cover broad scheduling and device-control jobs. | evidence | T09-S09, T09-S10 | Platform documentation current at access | high | Feature availability varies by account, device, country, and future platform changes. |
| Working parents directly report unequal division and differing perceptions of household/parenting responsibilities, plus explicit decision factors during childcare disruption. | evidence | T09-S13 | US survey; 2026 | high | Self-report and subgroup limits; no product or payment evidence. |
| Parents directly report uneven responsibility for managing children’s schedules and activities. | evidence | T09-S14 | US survey; 2023 | medium-high | Older and limited couple subgroup; no solution demand. |
| Cognitive household work includes anticipating, planning, delegating, and monitoring; surveyed mothers reported unequal responsibility and associated wellbeing/relationship burden. | evidence | T09-S15 | US convenience sample; 2024 | medium | Cross-sectional, mother-only, high-income/educated sample; no causal or market conclusion. |
| Cohabiting couples and young people in separated families describe negotiation, recognition, ongoing communication, flexibility, and conflict harms in lived household coordination. | evidence | T09-S16, T09-S17 | South Korea 2025 / Australia 2018 | medium-low | Small, culturally specific studies; one is older and family-law-context-specific. |
| Narrow coordination tools may be more viable when they minimize child data and interoperate with existing calendars. | inference | T09-S06–S10 | Cross-source inference | medium | No direct demand or retention evidence. |

## Opportunity universe

The 15 retained candidates are fully defined in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md). They span schedule handoffs, shared responsibilities, household knowledge, school/activity logistics, consent-aware sharing, and temporary-care coordination. No candidate is ranked.

| ID range | Cluster | Candidate count | Evidence posture |
|---|---|---:|---|
| OPP-2026-801..805 | schedule and handoff integrity | 5 | recurring-work evidence plus bounded inferences |
| OPP-2026-806..810 | shared responsibilities and readiness | 5 | direct cognitive-labor/collaboration evidence plus bounded inferences |
| OPP-2026-811, 813 | household knowledge and permissions | 2 | household-work context plus legal/platform constraints |
| OPP-2026-816..818 | events and preparation | 3 | schedule/cognitive-labor evidence plus bounded inferences |

## Analytical observations

1. **Some coordination pain is directly supported; solution demand is not.** Parent surveys and small household/separated-family studies support schedule, division-of-labor, negotiation, and communication friction, but do not identify the highest-value workflow or a product response.
2. **Multi-user permissions are part of the product problem.** Official family-calendar documentation shows that ownership, editing, sharing, departure, and child-account events create state changes that must be designed explicitly.
3. **Minors change the acceptable data model.** The safest early candidates avoid collecting child behavioral data, location history, or private communications and work through adult-controlled, purpose-limited records.
4. **Household diversity defeats a single assumed family structure.** Candidate validation must include co-parent, blended, multigenerational, roommate, and guardian contexts where relevant without implying legal authority.
5. **Platform dependence is a risk, not evidence.** Calendar export/import may be a practical path, but current API scopes, review requirements, and fallback behavior require later verification.

## Legal, safety, privacy, and platform constraints

- Collect the minimum household and child data needed for a declared purpose; define retention and deletion.
- Require informed adult authority for child-related records and use child-readable notices where children interact directly.
- Avoid covert monitoring, behavioral scoring, manipulative engagement, and location surveillance.
- Model household roles as configurable permissions, not assumptions about custody or legal guardianship.
- Treat school messages and health/allergy notes as potentially sensitive; prefer local or user-controlled storage where feasible.
- Do not claim that COPPA, GDPR, DSA, or platform-policy compliance is automatic; obtain jurisdiction-specific review before execution.

## Exclusions

Rejected spaces and the rule applied are recorded in [EXCLUSIONS.md](EXCLUSIONS.md), including custody decision tools, child surveillance, medical guidance, school administration, family lending, and engagement-maximizing child products.

## Risks, assumptions, and unknowns

- G-01: no direct evidence yet identifies which segment experiences the most severe coordination failure.
- G-02: willingness to pay and buyer identity are unknown for all candidates.
- G-03: notification fatigue, household conflict, and uneven participation may defeat retention.
- G-04: calendar and messaging integrations have not been technically verified.
- G-05: child-data applicability and consent flows vary by jurisdiction and candidate design.

See [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md) for owners and proposed later tests.

## Confidence assessment

Confidence is **high** that family and household coordination is recurring and that child-data safeguards are material. Confidence is **medium** that narrow, permission-aware workflows can improve on generic calendars. Confidence is **low** for candidate-level demand, willingness to pay, retention, and acquisition. These limits are compatible with Gate 1 because they are explicit and no winner is selected.

## Recommended next action

External Governance re-review requested for corrected version 0.3.0. Do not advance any candidate to Gate 2, contact families, define an MVP, or implement software without separate Founder authorization.
