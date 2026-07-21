---
status: in-review
version: 0.1.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Opportunity Index

Exactly 20 candidates are included and unranked. Evidence references resolve in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). Each proposition is an `inference`; demographic prevalence is never presented as demand.

| ID | Problem and bounded utility | User / current alternative | Evidence basis | Confidence rationale | Reachability hypothesis | Consent, safety, accessibility, or platform constraint |
|---|---|---|---|---|---|---|
| OPP-2026-100 | People repeatedly explain access needs; a user-owned preference passport could standardize chosen instructions. | Person with access needs; verbal repetition or notes. | T02-S02/S03/S08 | medium: access domains and standards direct; workflow demand unmeasured | disability organizations and accessibility-resource search | selective sharing, revocation, no medical details required |
| OPP-2026-101 | Dense letters or PDFs can block comprehension; a plain-language restatement could preserve source-linked meaning. | Older adult/person with cognitive or reading access need; helper rereads document. | T02-S04/S07 | medium: access barrier plausible; translation accuracy untested | libraries, aging/disability service organizations | no legal/medical interpretation; original always visible |
| OPP-2026-102 | Printed instructions may be too small or visually dense; a large-print card maker could reformat user-provided content. | Person with low vision; photocopy/handwritten card. | T02-S03/S08 | medium: visual need and standard direct | low-vision organizations and print-access search | user confirms meaning; contrast/reflow tested; no conformance claim |
| OPP-2026-103 | Multi-step everyday tasks may need consistent, accessible sequencing. | Person with cognitive/motor access needs; paper cue cards/helper prompts. | T02-S02/S04 | medium: relevant domains direct; task-card efficacy unknown | occupational-access and independent-living organizations | non-clinical, user-configured, printable and undoable |
| OPP-2026-104 | Touch-heavy interfaces can exclude visual/motor users; a voice-first notebook could capture personal routines. | Person with visual/motor access need; voice memo or paper. | T02-S02/S03 | medium: speech recognition is recognized AT; adoption unknown | assistive-tech resource channels | no always-on listening; keyboard/touch/manual alternative |
| OPP-2026-105 | Family-caregiver handoffs can omit context; a consent-based summary could capture selected tasks and preferences. | Care recipient plus unpaid caregiver; message/paper. | T02-S06 | medium: caregiving intensity direct, handoff failures unmeasured | caregiver organizations | care recipient owns data, sees recipients, revokes sharing |
| OPP-2026-106 | Unpaid caregivers need to make workload and boundaries visible. | Family caregiver; chat/spreadsheet. | T02-S06 | medium: burden context direct; tool effect unknown | caregiver support groups | no employment scheduling; avoid guilt and coercion |
| OPP-2026-107 | Asking for respite help requires repeatedly specifying safe, bounded tasks. | Family caregiver; calls/messages. | T02-S06 | medium: support need direct, request-pack demand unmeasured | caregiver organizations | no guarantee of vetted helper or service availability |
| OPP-2026-108 | People forget questions in appointments; a preparation sheet could organize user-authored questions. | Older/disabled adult; paper note/helper. | T02-S02/S04 | low: adjacent to health access but no workflow study | patient-access organizations only after boundary review | no symptom analysis, triage, diagnosis, treatment, or prioritization |
| OPP-2026-109 | Users need a record of what they understood after a visit. | Older/disabled adult and chosen helper; handwritten note. | T02-S02/S06 | low: adjacent need inferred | caregiver/access organizations | user-authored record only; no clinical summarization claim |
| OPP-2026-110 | Transport accessibility can require advance questions about boarding, seating, sensory, and mobility conditions. | Person with access needs; calls and ad hoc checklist. | T02-S01/S03 | medium: environmental barriers direct | transit accessibility offices and disability groups | information may change; verify with operator; no booking/API dependency |
| OPP-2026-111 | Venue visits require repeated call-ahead questions. | Person with mobility/sensory access need; phone note. | T02-S01/S03 | medium: environmental relevance direct | community access organizations | never certify venue accessibility; timestamp user reports |
| OPP-2026-112 | Public-service applications require assembling documents in an accessible order. | Older/disabled adult; agency checklist/helper. | T02-S07/S09 | low: digital barriers direct, workflow demand indirect | libraries and public-service navigators | no eligibility determination or legal advice; jurisdiction visible |
| OPP-2026-113 | Suspicious messages create pressure; a pause-and-verify worksheet could route users to independently sourced contact details. | Older adult/chosen helper; ad hoc search/call. | T02-S05 | low: trust/privacy barriers direct, scam workflow unmeasured | consumer-protection and aging organizations | never declare a message safe; no link-clicking or credential request |
| OPP-2026-114 | Tech-support sessions fail when goals, permissions, and handback are unclear. | Older adult/helper; informal remote or in-person support. | T02-S05 | medium: support demand/barriers direct | libraries, senior centers, community digital inclusion | no credential capture, hidden remote access, or permanent helper permissions |
| OPP-2026-115 | People with hearing access needs repeatedly explain communication preferences. | Person with hearing need; verbal/written request. | T02-S02/S03 | medium: domain and AT context direct | hearing-access organizations | no diagnosis/device recommendation; text alternative required |
| OPP-2026-116 | Users need personal control over contrast, spacing, and text size for supplied content. | Person with visual/cognitive access need; browser zoom/manual reformat. | T02-S07/S08 | medium: common barriers and criteria direct | accessibility-resource search | preserve original; do not claim transformed content is fully conformant |
| OPP-2026-117 | Important personal information may need an accessible static format for chosen contacts. | Older/disabled adult; wallet card/paper. | T02-S02/S03 | low: relevant access need; specific use unmeasured | independent-living organizations | no monitoring, dispatch, or emergency-response guarantee; data minimization |
| OPP-2026-118 | Home barriers are hard to inventory before asking a professional or landlord. | Older/disabled adult and chosen helper; photos/paper list. | T02-S01/S02 | medium: supportive environment direct | aging-in-place and disability groups | observation only; no building, fall-risk, or clinical assessment |
| OPP-2026-119 | Social-connection intentions are easy to lose without a user-directed cadence. | Older adult; calendar/call list. | T02-S10/S11 | medium: isolation context direct; app effect unknown | community and aging organizations | no mental-health treatment, surveillance, or coercive caregiver alerts |

## Coverage Notes

- The universe spans visual, hearing, mobility, cognitive-access, independent-living, caregiver, transport, public-service, technology-support, and connection workflows.
- Candidates 108–109 are included only as non-clinical organization aids; any diagnostic or clinical integration would disqualify them.
- Candidates 105–107 are for unpaid family caregiving, not professional care-workforce operations.
- No candidate requires a dominant-platform API, covert sensors, health records, prescription data, or a proprietary network.
