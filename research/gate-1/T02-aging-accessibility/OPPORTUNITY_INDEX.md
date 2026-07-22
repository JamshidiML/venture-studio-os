---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Opportunity Index

This index contains the eight Qualified Gate 1 Candidates. They are unranked. Twelve context-only concepts remain preserved under their original IDs in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). Evidence references resolve in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). Each proposed utility remains an `inference`; demographic prevalence is never presented as demand.

| ID | Problem and bounded utility | User / current alternative | Evidence basis | Confidence rationale | Reachability hypothesis | Consent, safety, accessibility, or platform constraint |
|---|---|---|---|---|---|---|
| OPP-2026-100 | People repeatedly explain access needs; a user-owned preference passport could standardize chosen instructions. | Person with access needs; verbal repetition or notes. | T02-S02/S03/S08/S12 | medium: T02-S12 directly reports communication-preference failures; passport demand unmeasured | disability organizations and accessibility-resource search | selective sharing, revocation, no medical details required |
| OPP-2026-101 | Dense letters or PDFs can block comprehension; a plain-language restatement could preserve source-linked meaning. | Older adult/person with cognitive or reading access need; helper rereads document. | T02-S07/S12 | medium: inaccessible/digestible-information barrier direct; restatement workflow and accuracy untested | libraries, aging/disability service organizations | no legal/medical interpretation; original always visible |
| OPP-2026-102 | Printed instructions may be too small or visually dense; a large-print card maker could reformat user-provided content. | Person with low vision; photocopy/handwritten card. | T02-S03/S08 | medium: visual need and standard direct | low-vision organizations and print-access search | user confirms meaning; contrast/reflow tested; no conformance claim |
| OPP-2026-110 | Transport accessibility can require advance questions about boarding, seating, sensory, and mobility conditions. | Person with access needs; calls and ad hoc checklist. | T02-S01/S03/S12 | medium: T02-S12 directly reports extensive preparation for physical access; transport-specific checklist demand is unmeasured | transit accessibility offices and disability groups | information may change; verify with operator; no booking/API dependency |
| OPP-2026-111 | Venue visits require repeated call-ahead questions. | Person with mobility/sensory access need; phone note. | T02-S12 | medium: physical barriers and advance preparation are direct; card demand remains inference | community access organizations | never certify venue accessibility; timestamp user reports |
| OPP-2026-114 | Tech-support sessions fail when goals, permissions, and handback are unclear. | Older adult/helper; informal remote or in-person support. | T02-S05/S12 | medium: need for meaningful support and workarounds direct; session-handback failure unmeasured | libraries, senior centers, community digital inclusion | no credential capture, hidden remote access, or permanent helper permissions |
| OPP-2026-115 | People with hearing access needs repeatedly explain communication preferences. | Person with hearing need; verbal/written request. | T02-S02/S03 | medium: domain and AT context direct | hearing-access organizations | no diagnosis/device recommendation; text alternative required |
| OPP-2026-116 | Users need personal control over contrast, spacing, and text size for supplied content. | Person with visual/cognitive access need; browser zoom/manual reformat. | T02-S07/S08 | medium: common barriers and criteria direct | accessibility-resource search | preserve original; do not claim transformed content is fully conformant |

## Source-to-Domain Matrix

Legend: `D` = direct problem/lived-experience evidence; `C` = contextual/population evidence; `T` = technical standard or automated test; `L` = legal/regulatory context; dash = no qualifying support.

| Source | Visual | Hearing | Cognitive | Mobility | Caregiver | Transport / venue | Public service | Social connection |
|---|---|---|---|---|---|---|---|---|
| S01 | C | C | C | C | — | C | — | C |
| S02 | C | C | C | C | C | — | — | — |
| S03 | C | C | — | C | — | — | — | — |
| S04 | C | C | C | C | C | — | — | — |
| S05 | — | — | — | — | C | — | C | C |
| S06 | — | — | — | — | D | — | — | — |
| S07 | T | T | T | T | — | — | T | — |
| S08 | T | T | T | T | — | — | T | — |
| S09 | L | L | L | L | — | L | L | — |
| S10 | — | — | — | — | — | — | — | C |
| S11 | — | — | — | — | C | — | — | C |
| S12 | D | D | D | D | C | D | D | D |

## Candidate-to-Source Coverage Matrix

The matrix distinguishes an evidenced access barrier from the proposed workflow. Standards, demographics, and regulations are never classified as direct pain.

| ID | Final status | Direct problem evidence | Contextual / population evidence | Current-alternative evidence | Technical feasibility | Legal / privacy / safety / platform evidence | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|---|
| 100 | qualified | S12 communication-preference failures | S02/S03 | S12 repeated explanation/workarounds | S08 design baseline only | consent/revocation is an unsourced safety rule | preference passport adoption |
| 101 | qualified | S12 inaccessible/digestible information | S04/S07 | S12 family/help and workarounds | S08 baseline; accurate restatement untested | no legal/medical interpretation | restatement preserves meaning |
| 102 | qualified | S12 format/screen-reader barriers | S03 | — | S08 baseline | preserve original | card workflow demand |
| 103 | watchlist | — | S02/S04 | helper/paper is stated, not sourced | untested | non-clinical/undoable | task cards improve sequencing |
| 104 | watchlist | — | S02/S03 | voice memo/paper not sourced | speech recognition category S02 | no always-on listening | voice notebook adoption |
| 105 | watchlist | — | S06 caregiver context | message/paper not sourced | untested | consent/revocation required | handoff omissions and utility value |
| 106 | watchlist | — | S06 caregiver workload context, not board pain | chat/spreadsheet not sourced | untested | anti-coercion boundary | board changes workload |
| 107 | watchlist | — | S06 support context, not request-pack pain | calls/messages not sourced | untested | no vetted-helper claim | request pack improves respite access |
| 108 | watchlist | — | S02/S04 | paper/helper not sourced | untested | hard clinical boundary | questions are forgotten often |
| 109 | watchlist | — | S02/S06 | handwritten note not sourced | untested | user-authored only | recap need is frequent |
| 110 | qualified | S12 preparation/physical barriers | S01/S03 | S12 calls/workarounds generally | untested | operator verification | transport checklist is wanted |
| 111 | qualified | S12 venue barriers/preparation | S01/S03 | S12 workarounds | untested | never certify accessibility | card reduces access burden |
| 112 | watchlist | S12 digital/process barriers only | S07/S09 | S12 reliance on help generally | checklist untested | eligibility/legal boundary | document-assembly pain |
| 113 | watchlist | — | S05 trust/privacy only | ad hoc call/search not sourced | untested | never authenticate messages | scam worksheet demand |
| 114 | qualified | S12 support/process barrier only | S05 | S12 reliance on family/friends | session checklist untested | no credentials/remote control | handback failure is material |
| 115 | qualified | S12 communication-preference failures | S02/S03 | repeated explanation S12 | static card assumed | no diagnosis/device claim | card reduces repetition |
| 116 | qualified | S12 format barriers | S07 | browser zoom not sourced | S08 baseline | no conformance claim | converter preserves semantics |
| 117 | watchlist | — | S02/S03 | wallet card not sourced | static output assumed | no emergency reliance | chosen contacts need this format |
| 118 | watchlist | — | S01/S02 | photos/paper not sourced | inventory untested | no assessment claim | home-inventory pain is recurrent |
| 119 | watchlist | — | S10/S11/S12 isolation context | calendar/call list not sourced | cadence untested | no treatment/coercion | cadence planner improves connection |

## Coverage Notes

- The qualified set spans visual, hearing, cognitive-access, mobility/venue preparation, and technology-support workflows; caregiver, task-card, appointment, public-service, static-information, home-inventory, and connection concepts remain on the watchlist.
- Watchlist candidates 108–109 retain hard non-clinical boundaries; any diagnostic or clinical integration would disqualify them even from reconsideration.
- Watchlist candidates 105–107 retain care-recipient agency, consent, and unpaid-family-care boundaries; they are not professional care-workforce operations.
- No candidate requires a dominant-platform API, covert sensors, health records, prescription data, or a proprietary network.
- Candidates `101`, `112`–`114`, `118`, and `119` continue to separate evidenced digital/access context from proposed workflow pain. Only `101` and `114` have sufficiently adjacent observed barriers/workarounds for qualified investigation; the others remain watchlist concepts.
