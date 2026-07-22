---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T05 Exclusions

| Excluded space | Reason | Evidence or rule |
|---|---|---|
| Symptom checker, diagnosis or triage | Clinical decision risk and explicit issue boundary | Issue #8; W07 |
| Treatment, medication or supplement recommender | Could cause direct harm; outside general wellness | Issue #8; W02, W07 |
| Crisis intervention or suicide-risk detection | Requires specialized clinical/safety operations | Issue #8 |
| Eating-disorder optimization, calorie punishment or extreme weight loss | High harm and retention-ethics risk | Issue #8; W07 |
| Medical-device measurement or disease prediction | Regulatory and accuracy risk | Issue #8; W07 |
| Blood-pressure, glucose or oxygen estimation without authorized hardware | Clinical measurement and dangerous reliance | FDA boundary in W07 |
| Personalized rehabilitation or pain-treatment plan | Clinical workflow | Issue #8 |
| Automated interpretation of symptom journals | Converts neutral organization into medical advice | Issue #8; W07 |
| Sale or advertising use of health data | Disproportionate privacy risk | W08–W11 |
| Background collection of unnecessary sensor/location data | Violates minimization and platform-policy expectations | W09–W11 |
| Punitive streaks, public shame or compulsive engagement | Retention-ethics violation | Issue #8 user-safety requirement |
| General productivity, finance, education or caregiver tool | Reserved to other threads | Parent #3 isolation contract |

No excluded concept was included under a softer label.

## Hypothesis Watchlist

These concepts are not Qualified Gate 1 Candidates. Their original IDs remain owned by T05 and cannot be reused. Every future reconsideration remains subject to the absolute prohibition on diagnosis, interpretation, risk scoring, triage, treatment, medical advice and crisis-intervention claims.

| Opportunity ID | Original concept | Why not qualified / consolidation status | Current confidence | Evidence searched | Missing evidence | Risk and safety constraints | Conditions for reconsideration | Original ownership |
|---|---|---|---|---|---|---|---|---|
| OPP-2026-401 | User-defined wind-down sequence builder | No observed sequence-building problem; consolidated into qualified sleep family 400 | medium | W01, W06; checklists, timers, meditation apps | Evidence of a distinct repeated sequence job beyond 400 | No sleep-effect/treatment claim; professional help for persistent impairment | Direct workflow evidence shows a distinct event, input and output | T05 — Issue #8 |
| OPP-2026-402 | Sleep-environment self-check journal | No observed environment-journal pain; consolidated into 400 | low | W01; notes and sleep trackers | Direct self-observation workflow and current failure | No causal interpretation; sensitive export/delete | Evidence distinguishes neutral journaling from 400 without causal claims | T05 — Issue #8 |
| OPP-2026-403 | Travel or shift routine reset checklist | No direct travel/shift workflow evidence; consolidated into 400 | low | W01; calendars and generic advice | Direct traveler/shift-worker routine-reset evidence | No circadian-disorder, fatigue-safety or treatment advice | Direct bounded workflow evidence plus qualified safety review | T05 — Issue #8 |
| OPP-2026-404 | Morning routine and daylight reminder log | No observed morning/daylight workflow; consolidated into 400 | low | W01, W06; habit apps and alarms | Direct routine evidence distinct from 400 | No biological-effect, diagnosis or treatment claim | Evidence establishes a separate workflow without biological advice | T05 — Issue #8 |
| OPP-2026-405 | Desk movement-break timer | Population prevalence/guidance do not qualify a tool; canonical concept for 405–409 movement family | low | W03–W04; OS timers and wearables | Direct sedentary-worker cue workflow and failure evidence | User-controlled intensity, accessibility, no exercise prescription | Direct observation establishes a bounded movement-cue job | T05 — Issue #8 |
| OPP-2026-406 | Walking-habit planner | No direct walking-planning pain; consolidated into 405 | medium | W03–W04; pedometers, apps, paper | Direct walking-planning workflow distinct from 405 | No calorie, disease, weight or medical claim | Evidence demonstrates distinct event/input/output and safe user control | T05 — Issue #8 |
| OPP-2026-407 | Strength-session consistency log | Guidance does not establish logging pain; consolidated into 405 | medium | W04; workout logs and spreadsheets | Direct self-chosen strength-log workflow | No exercise/load prescription or rehabilitation | Evidence establishes a distinct log job among already-safe user choices | T05 — Issue #8 |
| OPP-2026-408 | Personal mobility-routine card organizer | No direct card-organization workflow; consolidated into 405 | low | W03–W04; notes and video bookmarks | Direct evidence of recurring card organization | No injury/pain/rehabilitation guidance; content rights | Evidence establishes distinct workflow and qualified safety boundary | T05 — Issue #8 |
| OPP-2026-409 | Time-and-equipment movement prompt deck | No direct prompt-selection workflow; consolidated into 405 | medium | W03–W04; search, videos and cards | Direct contextual-prompt workflow distinct from 405 | User chooses safe activity; accessibility/contraindication notice; no prescription | Direct observation plus safety review demonstrates separate job | T05 — Issue #8 |
| OPP-2026-410 | Meal-prep cadence planner | Dietary guidance is context, not meal-planning pain | medium | W05; calendars and meal planners | Direct routine-meal organization workflow and switching friction | General organization only; no medical diet or outcome claim | Direct observation of planning failures unmet by alternatives | T05 — Issue #8 |
| OPP-2026-411 | Pantry-to-balanced-meal organizer | Guidance does not establish pantry-decision pain | low | W05; recipe sites and notes | Direct pantry-update/decision workflow evidence | No nutrient optimization, allergy guarantee or medical advice | Direct evidence establishes bounded non-clinical organization | T05 — Issue #8 |
| OPP-2026-412 | Produce rotation and use-first reminder | No observed rotation/reminder pain or waste effect | low | W05; fridge notes and grocery apps | Direct household workflow and measured failure, without fabricated waste claim | Never guess food-safety dates; no health/waste outcome claim | Direct observation establishes use-first workflow and safe date source | T05 — Issue #8 |
| OPP-2026-415 | Paced breathing and grounding timer | Public guidance does not establish demand for a separate timer | medium | W06; timers and meditation apps | Direct chosen-relaxation workflow and current failure | No anxiety treatment, interpretation or crisis claim; clear exit/help route | Direct evidence plus clinical-safety review supports bounded timer use | T05 — Issue #8 |
| OPP-2026-416 | Work-recovery boundary planner | Broad stress context does not observe an end-of-work ritual problem | low | W06, W15; calendars and focus apps | Direct worker boundary workflow and non-use evidence | No burnout diagnosis, employer surveillance, scoring or coercion | Direct worker evidence establishes a voluntary bounded workflow | T05 — Issue #8 |
| OPP-2026-418 | Mood-and-energy context journal | Broad stress/mood context does not establish journal pain | low | W12, W15; paper journals and mood trackers | Direct consumer recording behavior, failure modes and non-use | No interpretation, screening, diagnosis, risk score, triage, treatment, crisis claim or medical advice; local/delete/export | Direct evidence and qualified privacy/safety review support facts-only recording | T05 — Issue #8 |
| OPP-2026-419 | Neutral symptom-observation log and user-controlled export | W17 is an adjacent clinical pilot; consumer pain and preference are unobserved | low | W16–W17; notes, portals and symptom apps | Direct consumer pre-visit facts-recording workflow and non-use evidence | Preserve full jurisdiction matrix; facts only; no interpretation, risk score, triage, diagnosis, treatment, medical advice or crisis intervention | Direct consumer evidence plus named-jurisdiction legal, privacy and clinical-safety review | T05 — Issue #8 |
