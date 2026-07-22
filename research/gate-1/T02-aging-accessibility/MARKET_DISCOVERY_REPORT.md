---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Market Discovery — Aging, Accessibility, and Caregivers

## Executive Summary

- **The auditable universe contains 20 bounded concepts: 8 Qualified Gate 1 Candidates and 12 Hypothesis Watchlist Candidates.** Neither tier is ranked. The qualified set is limited to communication, information-format, transport/venue-preparation, and technology-support workflows with direct or clearly adjacent lived-experience evidence.
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
| Candidate count | 8 qualified + 12 watchlist = 20 auditable IDs |
| Reserved IDs | `OPP-2026-100` through `OPP-2026-199`; this artifact uses `100` through `119` only |
| Explicit exclusions | Diagnosis/treatment, emergency-response claims, clinical prescription integration, insurance underwriting, covert surveillance, exploitative/dark-pattern products, general consumer utilities, finance, education, creator tools, SMB workflows, and platform companions |

## Methodology

The search prioritized primary or authoritative demographic, disability, accessibility, caregiver, technology-adoption, and social-connection sources. The first draft created the candidate universe and basic source map. The correction pass added claim types, full metadata, source limitations, candidate-specific consent/privacy/accessibility constraints, cross-geography cautions, exact queries, evidence gaps, and hard clinical/emergency/credential boundaries.

Qualification requires direct observed problem evidence or clearly adjacent observed workflow evidence, direct fit with Issue #5, a defined user, preservation of agency, non-clinical wording, no emergency guarantee, no hidden monitoring, an accessible manual fallback, and explicit uncertainty. Population statistics, broad caregiver burden, technical standards, regulation, and general access context cannot independently qualify a workflow. A candidate's inclusion is not evidence of commercial demand.

External Governance Correction Cycle 2 added a source-classification audit and direct lived-experience evidence. ONS interviewed 56 disabled adults with varied impairments; participants described inaccessible online services, poor information, inflexible processes, extensive preparation and workarounds, reliance on family/friends, and inaccessible communication/format choices. This is direct barrier evidence, but it does not prove demand for the proposed workflow utilities.

Cycle 3 applied the external two-tier finding without adding source count. Eight concepts remain qualified because the ONS interviews directly observe their communication, format, physical-access preparation, or support-process problem family. Twelve context-only concepts (`103`–`109`, `112`–`113`, and `117`–`119`) moved to the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist) with their IDs, constraints, and future evidence requirements intact.

## Evidence-Backed Problem Landscape

| Material claim | Type | Source | Confidence | Interpretation and limitation |
|---|---|---|---|---|
| Population ageing is global and highly heterogeneous; there is no single “typical older person.” | evidence | T02-S01 | high | WHO demographic and environment framing is global; projections do not establish demand for any product. |
| Assistive technology includes digital tools such as speech recognition, time-management software, and captioning; cost, awareness, access, fragmentation, and workforce capacity are barriers. | evidence | T02-S02 | high | WHO global synthesis supports design space but does not identify which lightweight utility will be adopted. |
| U.S. disability prevalence differs by measure; current CDC sources show substantial vision, hearing, mobility, cognition, self-care, and independent-living needs. | evidence | T02-S03/T02-S04 | high | Different surveys and questions produce different estimates, so figures are not combined into one market size. |
| U.S. adults age 50+ use technology widely, but privacy, value, usability, and age-inappropriate design remain barriers. | evidence | T02-S05 | medium | AARP's 2025 fieldwork is an online survey; people without internet access may be underrepresented. |
| Family caregiving is widespread and varies in intensity and support needs. | evidence | T02-S06 | medium | AARP/NAC national research is relevant but does not prove demand for a specific coordination tool. |
| Automated testing found detectable WCAG failures on 94.8% of the top one million home pages tested in February 2025. | evidence | T02-S07 | high | Automated tools detect only a subset of barriers; absence of errors is not conformance, and home pages are not whole services. |
| Disabled participants reported physical, digital, information, communication, and process barriers, plus preparation/workarounds and reliance on family or friends. | evidence | T02-S12 | medium | Direct qualitative lived-experience evidence from 56 UK interviews; not representative prevalence and not candidate demand. |
| Revocable, user-controlled sharing will be trusted more than continuous monitoring. | assumption | No direct comparative source; owner: Strategy Agent | low | Must be tested with users and caregivers; it is a safety-preserving design assumption, not demand evidence. |
| A candidate should be killed if consent cannot be understood and revoked independently by target users in moderated accessibility testing. | hypothesis | Not tested | low | Falsifiable later-gate safety threshold; no validation is claimed here. |

## Qualified Gate 1 Candidate Universe

The eight qualified candidates are below and in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md). Twelve other IDs remain auditable in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist); they are not qualified candidates.

| Opportunity ID | Bounded workflow | Primary user | Evidence status | Confidence | Critical boundary |
|---|---|---|---|---|---|
| OPP-2026-100 | Personal accessibility-preference passport | Person with access needs | inference from T02-S02/S03/S08/S12 | medium | user-owned and selectively shared |
| OPP-2026-101 | Plain-language document restatement | Older adult/person with cognitive or reading access need | access barrier evidenced by T02-S12; workflow remains inference | medium | no legal/medical interpretation |
| OPP-2026-102 | Large-print instruction-card maker | Person with low vision | inference from T02-S03/S08 | medium | preserve meaning; source visible |
| OPP-2026-110 | Transport accessibility call-ahead checklist | Person with mobility/sensory access needs | environmental preparation evidenced by T02-S12; checklist remains inference | medium | verify with operator; no availability claim |
| OPP-2026-111 | Accessible venue-preparation card | Person with mobility/sensory access needs | physical barrier/planning evidenced by T02-S12; card remains inference | medium | venue information can change |
| OPP-2026-114 | Trusted technology-support session checklist | Older adult and helper | support barrier evidenced by T02-S05/S12; session checklist remains inference | medium | no credential collection or remote control |
| OPP-2026-115 | Hearing-friendly conversation preparation card | Person with hearing access needs | inference from T02-S02/S03 | medium | no hearing diagnosis or device claim |
| OPP-2026-116 | Personal format converter for contrast, spacing, and text size | Person with visual/cognitive access needs | inference from T02-S07/S08 | medium | conversion must preserve source and not claim conformance |

## Consent, Privacy, Safety, and Accessibility Controls

- **Agency before caregiver convenience:** the person receiving support owns the record, chooses fields and recipients, can see access, and can revoke sharing. Incapacity or legal-authority questions require professional/legal handling outside the product.
- **Data minimization:** no continuous audio, camera, location, biometrics, health-record integration, credential storage, or covert presence detection. Sensitive notes default to local/manual storage.
- **No clinical or emergency reliance:** appointment and visit tools organize user-authored questions/notes only. Emergency cards are static references and never promise routing, monitoring, or response.
- **Accessibility baseline:** use WCAG 2.2 as a minimum web standard, provide keyboard, screen-reader, zoom/reflow, contrast, target-size, plain-language, caption/transcript, and non-voice alternatives; automated checks never substitute for disabled-user testing.
- **Affordability and support:** evaluate low-bandwidth, printable, phone-assisted, and caregiver-assisted paths. Do not assume every target user owns a current smartphone or can pay a subscription.
- **Vulnerability:** forbid dark patterns, fear-based upsells, default caregiver visibility, hidden data sale, discriminatory eligibility decisions, and claims that equate age with incapacity.

## Exclusions, Risks, and Unknowns

See [EXCLUSIONS.md](EXCLUSIONS.md) for both boundary exclusions and the 12-entry watchlist, and [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md) for unresolved evidence. Critical unknowns include user-controlled consent comprehension, accessibility across diverse impairments, affordability, reachability beyond online panels, caregiver/care-recipient conflicts, and candidate-level willingness to pay.

## Confidence Assessment

Overall confidence is `high` that accessibility and caregiving frictions exist, `medium` that the eight qualified workflow families are investigable, and `low` to `medium` for candidate-level adoption or payment. The 12 watchlist concepts remain `low` or `very low` at the specific-workflow level. This distinction prevents demographic prevalence from being treated as product demand.

## Recommended Next Action

Review the 8-qualified/12-watchlist split, coverage matrices, direct-lived-experience classification, consent, clinical boundaries, emergency reliance, offline accessibility, affordability, and disabled-user representation. Do not begin Gate 2 or select a product.

External Governance Cycle 3 re-review requested
