---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T05 Opportunity Index

Exactly 20 unranked Gate 1 candidates are listed. All are general-wellness workflow candidates; none diagnoses, treats, prevents disease, advises medication or claims a health outcome. Each stated repeat-use mechanism is an **assumption** owned by the Strategy Agent. Impact if wrong: it cannot support candidate advancement, retention, or a health/behavior claim. Planned review/test: only after a separately authorized Gate 5 issue, define a consented workflow study for the relevant cadence; no measure or threshold is authorized at Gate 1.

| ID | Recurring problem / candidate workflow | Segment and frequency | Current alternatives | Evidence basis; claim type; confidence | WTP status | Repeat-use mechanism assumption | Safety, privacy or platform constraint |
|---|---|---|---|---|---|---|---|
| OPP-2026-400 | Bedtime and wake-time consistency planner | Adults seeking routine consistency; daily | Alarms, calendars, sleep apps | W01; inference from sleep difficulties; medium | Unknown | Daily plan and morning reflection | No insomnia diagnosis or treatment claim; local-first data |
| OPP-2026-401 | User-defined wind-down sequence builder | Adults with inconsistent evenings; daily | Checklists, timers, meditation apps | W01, W06; inference; medium | Unknown | Reusable evening sequence | Do not claim improved sleep; escalate persistent impairment to professional help |
| OPP-2026-402 | Sleep-environment self-check journal | Adults tracking bedroom/routine context; occasional then weekly | Notes, sleep trackers | W01; assumption; low | Unknown | Compare self-observed context over time | No causal interpretation; sensitive journal export/delete |
| OPP-2026-403 | Travel or shift routine reset checklist | Travelers and shift workers; episodic | Calendars, generic sleep advice | W01; assumption; low | Unknown | Event-triggered use | No circadian-disorder or fatigue-safety advice |
| OPP-2026-404 | Morning routine and daylight reminder log | Adults building a morning routine; daily | Habit apps, alarms | W01, W06; assumption; low | Unknown | Daily cue and completion log | No treatment or biological-effect claim |
| OPP-2026-405 | Desk movement-break timer | Sedentary knowledge workers; multiple times daily | OS timers, wearables | W03–W04; inference; high for context, low for product demand | Unknown | Frequent workday cue | Accessibility and user-controlled intensity; not exercise prescription |
| OPP-2026-406 | Walking-habit planner | Insufficiently active adults; daily/weekly | Pedometers, fitness apps, paper plans | W03–W04; inference; medium | Unknown | Route-free goal and weekly reflection | No calorie, disease or weight-loss promise |
| OPP-2026-407 | Strength-session consistency log | Adults already choosing safe exercises; twice weekly | Workout logs, spreadsheets | W04; inference; medium | Unknown | Recurring weekly sessions | Does not prescribe exercise, load or rehabilitation |
| OPP-2026-408 | Personal mobility-routine card organizer | Adults with self-chosen low-risk routines; several times weekly | Notes, video bookmarks | W03–W04; assumption; low | Unknown | Saved routine cards | No injury, pain or rehabilitation guidance; content rights |
| OPP-2026-409 | Time-and-equipment movement prompt deck | Adults seeking short activity options; daily | Search, fitness videos, cards | W03–W04; inference; medium | Unknown | Contextual prompt rotation | User chooses safe activity; accessibility and contraindication disclaimer |
| OPP-2026-410 | Meal-prep cadence planner | Adults organizing routine meals; weekly | Calendars, meal planners | W05; inference; medium | Unknown | Weekly plan/shop/prep cycle | General food organization only; no medical diets |
| OPP-2026-411 | Pantry-to-balanced-meal organizer | Adults reducing meal decision friction; several times weekly | Recipe sites, notes | W05; assumption; low | Unknown | Repeated pantry updates and meal choices | No nutrient optimization or allergy safety guarantees |
| OPP-2026-412 | Produce rotation and use-first reminder | Household food planners; weekly | Fridge notes, grocery apps | W05; assumption; low | Unknown | Grocery-cycle reset | Food-safety dates must not be guessed; avoid waste claims without measurement |
| OPP-2026-413 | User-set hydration habit log | Adults tracking a self-set routine; daily | Bottles, alarms, fitness apps | W13; direct behavior context, product inference; medium | Unknown | Daily cue and log | No universal intake target; overconsumption and medical-condition warning |
| OPP-2026-414 | Stress-event and coping-context journal | Adults reflecting on everyday stress; event-triggered | Journals, notes, mood apps | W06, W15; direct stress context, journal inference; medium | Unknown | Event entries and weekly review | Non-diagnostic; crisis handling out of scope; sensitive data minimization |
| OPP-2026-415 | Paced breathing and grounding timer | Adults choosing a relaxation routine; episodic/daily | Timer, meditation apps | W06; inference; medium | Unknown | Short repeat sessions | No anxiety treatment claim; clear exit and help-seeking notice |
| OPP-2026-416 | Work-recovery boundary planner | Knowledge workers; workdays | Calendar blocks, focus apps | W06; assumption; low | Unknown | End-of-work ritual | No burnout diagnosis; avoid employer surveillance |
| OPP-2026-417 | User-controlled digital-break cadence coach | Adult internet users already setting boundaries; daily | OS screen-time tools, do-not-disturb, timers | W14; direct existing behavior/alternative, coach inference; medium | Unknown | Workday and evening cues | No addiction claim; no punitive lockouts or manipulative streaks |
| OPP-2026-418 | Mood-and-energy context journal | Adults tracking subjective wellbeing; daily | Paper journals, mood trackers | W12, W15; broad context only, unsupported workflow assumption; low | Unknown | Daily check-in and pattern review | No screening/diagnosis or generated interpretation; local storage, deletion and clear crisis boundary |
| OPP-2026-419 | Neutral symptom-observation log and user-controlled export | Adults preparing factual notes for themselves or a clinician; event-triggered | Notes, patient portals, symptom apps | W16–W17; adjacent workflow/current alternative, consumer-need assumption; low | Unknown | Entries around recurring observations | Plain user-entered facts only; no interpretation, risk scoring, triage, diagnosis or treatment; explicit consent and user-controlled export |

## Coverage and integrity check

- Domains: sleep routine, movement habits, meal organization, stress self-management, digital boundaries and neutral journaling.
- Frequencies: multiple-times-daily, daily, several-times-weekly, weekly and event-triggered.
- Clinical boundary: every candidate is organizational or reflective; none claims diagnosis, prevention, cure, mitigation or treatment.
- WTP: unknown for every candidate. Public-health prevalence and existing paid categories are not treated as payment evidence.
- Repeat use: all mechanisms are assumptions under the owner/impact/planned-review treatment above and must avoid punitive, shame-based or compulsive engagement.

## Adjacent-candidate boundary check

| Cluster | Distinction retained after external review | Consolidation trigger |
|---|---|---|
| 400–404 sleep | 400 schedules time; 401 stores a user-defined sequence; 402 records environment; 403 is travel/shift event-triggered; 404 records a morning cue | Consolidate 400/401/404 if direct observation does not distinguish schedule, sequence and cue; remove 402/403 absent direct demand |
| 405–409 movement | 405 is a sedentary-work timer; 406 is a walking plan; 407 logs self-chosen strength sessions; 408 organizes user-owned routine cards; 409 filters prompts by time/equipment | Consolidate 408/409 if users do not maintain cards separately from prompts; no exercise prescription is allowed |

## Candidate-to-source coverage matrix

`None` identifies an evidence gap. Guidance, regulation and platform policy are never counted as direct problem evidence.

| Candidate | Direct problem evidence | Contextual / population evidence | Current-alternative evidence | Technical feasibility | Legal / privacy / safety / platform | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|
| 400 | None | W01 | Alarms, calendars, sleep apps | Not researched | W07–W11; no treatment | Planner need, cadence, effect |
| 401 | None | W01, W06 | Checklists, timers, meditation apps | Not researched | W07–W11; help-seeking boundary | Sequence-builder need/effect |
| 402 | None | W01 | Notes, sleep trackers | Not researched | W08–W11; no causal interpretation | Environment-journal need |
| 403 | None | W01 | Calendars, generic advice | Not researched | Fatigue-safety boundary | Reset-checklist need |
| 404 | None | W01, W06 | Habit apps, alarms | Not researched | W07–W11; no biological claim | Morning-cue need/effect |
| 405 | None | W03–W04 | OS timers, wearables | Timer feasibility untested | Accessibility; no prescription | Movement-timer demand/effect |
| 406 | None | W03–W04 | Pedometers, fitness apps, paper | Not researched | No calorie/disease claim | Walking-planner demand/effect |
| 407 | None | W04 | Workout logs, sheets | Not researched | No load/rehabilitation advice | Strength-log need |
| 408 | None | W03–W04 | Notes, video bookmarks | Not researched | Content rights; no rehab | Card-organizer need |
| 409 | None | W03–W04 | Search, videos, cards | Not researched | Accessibility/contraindication boundary | Prompt-deck need |
| 410 | None | W05 | Calendars, meal planners | Not researched | No medical diet | Cadence-planner demand |
| 411 | None | W05 | Recipe sites, notes | Not researched | No nutrient/allergy guarantee | Pantry-decision pain |
| 412 | None | W05 | Fridge notes, grocery apps | Not researched | No guessed safety dates | Produce-rotation pain/waste effect |
| 413 | W13 situation-dependent behavior | None | Bottles, alarms, fitness apps | Not researched | W07–W11; no target; overconsumption warning | Logging/reminder preference and effect |
| 414 | W15 stress/planning difficulty | W06, W12 | Journals, notes, mood apps | Not researched | W07–W11; crisis/diagnosis boundary | Journal preference/effect |
| 415 | None | W06 | Timers, meditation apps | Timer feasibility untested | No anxiety treatment; safe exit | Grounding-timer demand/effect |
| 416 | None | W06, W15 | Calendars, focus apps | Not researched | No employer surveillance/burnout claim | Work-recovery ritual pain |
| 417 | W14 boundary strategies | None | W14 do-not-disturb/offline time; timers | OS behavior unverified | W09–W11; no addiction/punitive lockout | Need for separate coach/effect |
| 418 | None | W12, W15 | Journals, mood trackers | Not researched | W07–W11; sensitive data/no screening | Mood-energy journal pain and pattern value |
| 419 | None | W16 | W16 patient portals; notes, symptom apps | W17 adjacent patient-entered clinical workflow only; consumer export/interop unverified | W07–W11; jurisdiction matrix below | Consumer pain, frequency and preference |

## Candidate 419 jurisdiction and data-classification matrix

This matrix is a Gate 1 risk screen, not legal advice. Any interpretation, risk score, recommendation or urgency classification is outside candidate 419.

| Geography / channel | Data classification trigger | Potential regime / policy | Allowed Gate 1 concept behavior | Required later review |
|---|---|---|---|---|
| United States; consumer app outside HIPAA entity | Individually identifiable symptom/health observations | FTC Health Breach Notification Rule (W08); state health/privacy laws not mapped | User-entered factual record, local-first storage, explicit export/delete; no sale/ads | Named-state counsel review and data-flow inventory |
| United States; provider/plan integration | Data handled for a covered entity/business associate | HIPAA applicability may attach; W16 portals are current alternatives | No integration assumed; user-controlled file export only | Contract, role and HIPAA/security analysis |
| EU/EEA | Health-related personal data may be special-category data | GDPR and national rules; not yet researched in this thread | No EU launch claim; explicit consent does not by itself resolve all legal bases | Named-country DPO/counsel review and DPIA |
| Apple App Store | Health/medical data and app behavior | Apple review guideline W11 | Data minimization, deletion/export and no medical claim | Recheck current policy before distribution |
| Google Play | Health-app declaration, permissions and sensitive data | Google Play W09–W10 | No sensor/health permission assumed; privacy disclosure mandatory | Candidate-specific declaration/permission review |
| Any geography | Interpretation, triage, diagnosis, prevention/treatment or urgency advice | FDA/device and local medical-device rules (W07) | **Prohibited:** store/display/export user-entered facts only | Founder/Governance must reject any scope drift |
