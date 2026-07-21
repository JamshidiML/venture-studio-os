---
status: in-review
version: 0.1.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Market Discovery — Aging, Accessibility, and Caregivers

## Executive Summary

- **Twenty bounded candidates were documented without selecting or ranking a product.** They address accessible information, independent everyday tasks, consent-based family-caregiver coordination, trusted technology support, public-service navigation, transport preparation, and social connection.
- **Need is broad but heterogeneous.** Current global and U.S. evidence shows substantial populations with age-related or disability-related access needs, while both WHO and AARP stress that people, families, usability, affordability, privacy, and support must be considered together ([T02-S01](SOURCE_REGISTER.md), [T02-S02](SOURCE_REGISTER.md), [T02-S05](SOURCE_REGISTER.md)).
- **Digital barriers remain observable.** WebAIM's February 2025 automated scan found detectable WCAG failures on most of the sampled top one million home pages, while WCAG 2.2 and the EU Accessibility Act provide relevant standards and regulatory context ([T02-S07](SOURCE_REGISTER.md), [T02-S08](SOURCE_REGISTER.md), [T02-S09](SOURCE_REGISTER.md)).
- **No clinical claim or vulnerable-user exploitation is present.** All candidates are non-diagnostic, manual-first, revocable-consent oriented, and explicitly bounded away from emergency response, prescription management, surveillance, eligibility decisions, and credential handling.

## Objective and Scope

| Field | Bound |
|---|---|
| Authorization | [Parent Issue #3](https://github.com/JamshidiML/venture-studio-os/issues/3) and [Issue #5](https://github.com/JamshidiML/venture-studio-os/issues/5) |
| Geography | Global demographic/assistive-technology context; U.S. disability, caregiving, living-arrangement, technology, and social-connection evidence; EU accessibility context |
| Segments | Older adults, people with visual/hearing/mobility/cognitive-access needs, and unpaid family caregivers |
| Source cutoff | 2026-07-22 |
| Candidate count | Exactly 20 |
| Reserved IDs | `OPP-2026-100` through `OPP-2026-199`; this artifact uses `100` through `119` only |
| Explicit exclusions | Diagnosis/treatment, emergency-response claims, clinical prescription integration, insurance underwriting, covert surveillance, exploitative/dark-pattern products, general consumer utilities, finance, education, creator tools, SMB workflows, and platform companions |

## Methodology

The search prioritized primary or authoritative demographic, disability, accessibility, caregiver, technology-adoption, and social-connection sources. The first draft created the candidate universe and basic source map. The correction pass added claim types, full metadata, source limitations, candidate-specific consent/privacy/accessibility constraints, cross-geography cautions, exact queries, evidence gaps, and hard clinical/emergency/credential boundaries.

Qualification required: direct fit with Issue #5; a traceable problem-category source; a defined user or caregiver; preservation of the older adult's or disabled person's agency; non-clinical wording; no emergency guarantee; no hidden monitoring; an accessible manual fallback; and explicit uncertainty. A candidate's inclusion is not evidence of commercial demand.

## Evidence-Backed Problem Landscape

| Material claim | Type | Source | Confidence | Interpretation and limitation |
|---|---|---|---|---|
| Population ageing is global and highly heterogeneous; there is no single “typical older person.” | evidence | T02-S01 | high | WHO demographic and environment framing is global; projections do not establish demand for any product. |
| Assistive technology includes digital tools such as speech recognition, time-management software, and captioning; cost, awareness, access, fragmentation, and workforce capacity are barriers. | evidence | T02-S02 | high | WHO global synthesis supports design space but does not identify which lightweight utility will be adopted. |
| U.S. disability prevalence differs by measure; current CDC sources show substantial vision, hearing, mobility, cognition, self-care, and independent-living needs. | evidence | T02-S03/T02-S04 | high | Different surveys and questions produce different estimates, so figures are not combined into one market size. |
| U.S. adults age 50+ use technology widely, but privacy, value, usability, and age-inappropriate design remain barriers. | evidence | T02-S05 | medium | AARP's 2025 fieldwork is an online survey; people without internet access may be underrepresented. |
| Family caregiving is widespread and varies in intensity and support needs. | evidence | T02-S06 | medium | AARP/NAC national research is relevant but does not prove demand for a specific coordination tool. |
| Automated testing found detectable WCAG failures on 94.8% of the top one million home pages tested in February 2025. | evidence | T02-S07 | high | Automated tools detect only a subset of barriers; absence of errors is not conformance, and home pages are not whole services. |
| Revocable, user-controlled sharing will be trusted more than continuous monitoring. | assumption | No direct comparative source; owner: Strategy Agent | low | Must be tested with users and caregivers; it is a safety-preserving design assumption, not demand evidence. |
| A candidate should be killed if consent cannot be understood and revoked independently by target users in moderated accessibility testing. | hypothesis | Not tested | low | Falsifiable later-gate safety threshold; no validation is claimed here. |

## Opportunity Universe

The full traceable index is in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

| Opportunity ID | Bounded workflow | Primary user | Evidence status | Confidence | Critical boundary |
|---|---|---|---|---|---|
| OPP-2026-100 | Personal accessibility-preference passport | Person with access needs | inference from T02-S02/S03/S08 | medium | user-owned and selectively shared |
| OPP-2026-101 | Plain-language document restatement | Older adult/person with cognitive or reading access need | inference from T02-S04/S07 | medium | no legal/medical interpretation |
| OPP-2026-102 | Large-print instruction-card maker | Person with low vision | inference from T02-S03/S08 | medium | preserve meaning; source visible |
| OPP-2026-103 | Accessible step-by-step everyday task cards | Person needing cognitive/motor access support | inference from T02-S02/S04 | medium | non-clinical and user-configured |
| OPP-2026-104 | Voice-first personal routine notebook | Person with visual/motor access need | inference from T02-S02/S03 | medium | local/manual fallback; no always-on audio |
| OPP-2026-105 | Consent-based caregiver handoff summary | Care recipient and unpaid family caregiver | inference from T02-S06 | medium | care recipient controls fields and revocation |
| OPP-2026-106 | Caregiver task-load boundary board | Unpaid family caregiver | inference from T02-S06 | medium | not a professional workforce tool |
| OPP-2026-107 | Respite-help request pack | Unpaid family caregiver | inference from T02-S06 | medium | no service availability guarantee |
| OPP-2026-108 | Appointment question-preparation sheet | Older/disabled adult | inference from T02-S02/S04 | low | no diagnosis, triage, or medical advice |
| OPP-2026-109 | User-authored visit recap organizer | Older/disabled adult and chosen helper | inference from T02-S02/S06 | low | record only; no clinical interpretation |
| OPP-2026-110 | Transport accessibility call-ahead checklist | Person with mobility/sensory access needs | inference from T02-S01/S03 | medium | verify with operator; no availability claim |
| OPP-2026-111 | Accessible venue-preparation card | Person with mobility/sensory access needs | inference from T02-S01/S03 | medium | venue information can change |
| OPP-2026-112 | Public-service document checklist | Older/disabled adult | inference from T02-S07/S09 | low | no eligibility or legal advice |
| OPP-2026-113 | Scam-message pause-and-verify worksheet | Older adult and chosen helper | inference from T02-S05 | low | education only; never guarantee authenticity |
| OPP-2026-114 | Trusted technology-support session checklist | Older adult and helper | inference from T02-S05 | medium | no credential collection or remote control |
| OPP-2026-115 | Hearing-friendly conversation preparation card | Person with hearing access needs | inference from T02-S02/S03 | medium | no hearing diagnosis or device claim |
| OPP-2026-116 | Personal format converter for contrast, spacing, and text size | Person with visual/cognitive access needs | inference from T02-S07/S08 | medium | conversion must preserve source and not claim conformance |
| OPP-2026-117 | Accessible personal emergency-information card | Older/disabled adult | inference from T02-S02/S03 | low | static information only; no emergency response |
| OPP-2026-118 | Home accessibility observation inventory | Older/disabled adult and chosen helper | inference from T02-S01/S02 | medium | not a clinical or building-safety assessment |
| OPP-2026-119 | User-directed social-connection cadence planner | Older adult at isolation risk | inference from T02-S10/S11 | medium | no mental-health treatment or coercion |

## Consent, Privacy, Safety, and Accessibility Controls

- **Agency before caregiver convenience:** the person receiving support owns the record, chooses fields and recipients, can see access, and can revoke sharing. Incapacity or legal-authority questions require professional/legal handling outside the product.
- **Data minimization:** no continuous audio, camera, location, biometrics, health-record integration, credential storage, or covert presence detection. Sensitive notes default to local/manual storage.
- **No clinical or emergency reliance:** appointment and visit tools organize user-authored questions/notes only. Emergency cards are static references and never promise routing, monitoring, or response.
- **Accessibility baseline:** use WCAG 2.2 as a minimum web standard, provide keyboard, screen-reader, zoom/reflow, contrast, target-size, plain-language, caption/transcript, and non-voice alternatives; automated checks never substitute for disabled-user testing.
- **Affordability and support:** evaluate low-bandwidth, printable, phone-assisted, and caregiver-assisted paths. Do not assume every target user owns a current smartphone or can pay a subscription.
- **Vulnerability:** forbid dark patterns, fear-based upsells, default caregiver visibility, hidden data sale, discriminatory eligibility decisions, and claims that equate age with incapacity.

## Exclusions, Risks, and Unknowns

See [EXCLUSIONS.md](EXCLUSIONS.md) and [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md). Critical unknowns include user-controlled consent comprehension, accessibility across diverse impairments, affordability, reachability beyond online panels, caregiver/care-recipient conflicts, and candidate-level willingness to pay.

## Confidence Assessment

Overall confidence is `high` that accessibility and caregiving frictions exist at material scale, `medium` that the bounded workflow families are relevant, and `low` to `medium` for candidate-level adoption or payment. This distinction prevents demographic prevalence from being treated as product demand.

## Recommended Next Action

Request independent Governance review against `templates/THREAD_QUALITY_SCORECARD.md`, with particular attention to consent, clinical boundaries, emergency reliance, affordability, and disabled-user representation. Do not begin Gate 2 or select a product.
