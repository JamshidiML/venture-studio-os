---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T09 Exclusions and Rejected Spaces

| Excluded space | Reason and authority boundary | Evidence or rule |
|---|---|---|
| Child location surveillance or covert device monitoring | Violates Issue #12 boundary and creates disproportionate safety/privacy exposure. | Issue #12; T09-S06–S08, S11 |
| Custody schedules that interpret legal orders or recommend custody outcomes | Legal advice and authority determination are outside Gate 1 and thread scope. | Issue #12 |
| Medical diagnosis, symptom interpretation, treatment, or medication coordination | Clinical workflow belongs outside this non-clinical coordination thread. | Issue #12 |
| School administration, gradebooks, attendance enforcement, or teacher-facing SIS | Explicitly assigned outside T09; high integration and child-data burden. | Issue #12 |
| Family lending, allowance banking, investment, or financial advice | Household finance belongs to T03 and may be regulated. | Issues #6 and #12 |
| Child engagement streaks, public leaderboards, or manipulative reward loops | Engagement is not a proxy for healthy value; child manipulation is prohibited. | Issue #12; T09-S11 |
| Private-message interception or sentiment scoring of children | Covert monitoring and high-risk inference conflict with consent and minimization. | Issue #12; T09-S06–S08 |
| Emergency dispatch or guaranteed safety alerts | Reliability claims and emergency-response duties exceed evidence and authorization. | Issue #12 |
| Dating, family social networks, or public child-content feeds | Network dependence, privacy, and unsafe-contact risks; explicitly excluded social spaces. | Parent #3 / Issue #12 |
| General single-user chores, reminders, lists, or calendars | Belongs to T01 unless the core job requires multi-person household coordination. | Issues #4 and #12 |
| Elder-care monitoring or accessibility support as the primary job | Belongs to T02; T09 can include household coordination only when aging is incidental. | Issues #5 and #12 |
| Automated decisions about parental fitness, child risk, or household conflict | High-stakes inference, bias, and due-process risk; prohibited. | Issue #12; T09-S11 |
| Retired Cycle-2 candidates: new-household onboarding (812), guest-access pack (814), quiet-hours router (815), shared-item ledger (819), and generic low-stakes decision record (820) | Candidate-specific direct problem evidence was not located; contextual population, regulation, and platform sources were insufficient. IDs remain retired and are not reused. | External Governance PR #22; SEARCH_LOG negative findings |

## Boundary rule used

A candidate remained in T09 only if shared household state, permissions, or handoffs were intrinsic. Being marketed to parents was not sufficient.

## Hypothesis Watchlist

These four records were part of the 15-candidate Cycle-2 auditable universe but are not Qualified Gate 1 Candidates in Cycle 3. They remain owned by T09 and retain their complete Issue #12 contracts. They are not retired, ranked, selected, or authorized for family recruitment or Gate 2.

Conflict and harm controls remain attached wherever relevant to both qualified and watchlist concepts: partial adoption, coercion, shame, false neutrality, parental conflict, child exposure, consent, revocation, privacy, notification failure, and setup burden. Moving a concept to the watchlist does not weaken these controls.

### Preserved Issue #12 candidate contracts

| ID | Original concept | Household composition | Primary user | Shared-user dynamics | Trust, consent, and harm constraints | Frequency | Current workaround | WTP evidence | Retention risk | Claim basis and current confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| OPP-2026-803 | Family transport handoff board showing driver, passenger, pickup point, and exception acknowledgment. | Multi-driver household | Coordinating adult or authorized driver | Each driver confirms only assigned legs; passengers can view approved details. | Explicit membership, revocable access, no continuous location, visible acknowledgement limitations; partial adoption, parental conflict, false neutrality, child exposure, privacy, and notification-failure risks remain explicit. | Recurring activity/childcare transport is evidenced generally; exact cadence unknown. | Group chat and shared calendar | none; no payment claim | Missed notifications, setup burden, conflict, or partial adoption can undermine trust quickly. | inference: recurring care/activity work (T09-S01, S04) makes explicit handoffs plausible; low confidence because no transport-failure study exists. |
| OPP-2026-810 | Temporary caregiver briefing pack with purpose-limited routines, contacts, and automatic expiry. | Household engaging a babysitter or temporary caregiver | Parent or guardian | Owner selects fields; caregiver receives time-limited read access and confirms receipt. | Explicit recipient consent, expiry, revocation, data minimization, privacy, no credentials, no emergency-response claim; false reassurance, notification failure, child exposure, and setup burden remain explicit. | Care episodes recur for some households; segment cadence unmeasured. | Paper notes and messaging | none; no payment claim | Infrequent care, setup effort, notification failure, or distrust of data sharing may limit retention. | inference: recurring care plus retention safeguards (T09-S01, S06–S08) support a bounded briefing workflow; medium-low confidence, but no briefing-failure evidence exists. |
| OPP-2026-813 | Permission-aware family-event album request gathering adult consent before identifiable child media is shared. | Family hosting or attending an event | Adult media organizer | Contributors upload only after the relevant adult permission state is visible. | Consent scope, revocation, biometric sensitivity, child exposure, parental conflict, false neutrality, coercion, privacy, export, deletion, and platform limits are explicit. | Event-driven; recurrence is household-specific and unmeasured. | Ad hoc messages and cloud albums | none; no payment claim | Consent friction, setup burden, revocation failure, conflict, or platform duplication may prevent repeated use. | inference: child-data safeguards and platform alternatives (T09-S06–S08, S11) support constraints, not pain; low confidence. |
| OPP-2026-818 | Rotating pet-care coordination for feeding, walking, supplies, and exception notes. | Shared household with pets | Adult pet owner | Members acknowledge routine handoffs; owner resolves exceptions. | No health advice, medication, automated monitoring, coercive reminders, shame, or false-neutrality claim; participation is revocable and notification limits are visible. | Pet-care cadence is recurring by definition but not quantified by the sources used. | Whiteboard and chat | none; no payment claim | Low switching value, setup burden, notification failure, or incomplete participation may reduce retention. | inference: recurring household activity (T09-S01) makes a shared handoff record plausible; low confidence because no pet-care handoff failure is observed. |

### Qualification gap and reconsideration record

| ID | Why not currently qualified | Evidence searched | Missing evidence | Conditions required for reconsideration | Original Thread ownership |
|---|---|---|---|---|---|
| OPP-2026-803 | General transport/activity recurrence does not establish transport-handoff failure. | T09-S01, T09-S04, T09-S13; calendar and group-chat alternatives | Direct observation of missed/ambiguous transport handoffs, frequency/severity, current workaround friction, adoption across adults, and WTP. | Independent or direct-user evidence must observe the bounded handoff failure; no location surveillance or safety guarantee may be added. | T09 — family and household |
| OPP-2026-810 | Care recurrence and privacy guidance do not establish temporary-briefing failure or a repeatable product job. | T09-S01–S02, T09-S06–S08; paper-note and messaging alternatives | Observed briefing omissions/failures, recurrence, setup burden relative to workaround, recipient acceptance, notification reliability, and WTP. | Direct workflow evidence must support the briefing job while preserving consent, expiry, revocation, minimization, and no-emergency-reliance boundaries. | T09 — family and household |
| OPP-2026-813 | Child-data rules and album alternatives establish constraints, not pain-specific consent-request workflow evidence. | T09-S05–S08, T09-S11; cloud-album and messaging alternatives | Observed family-event consent failure, recurrence, contributor/guardian behavior, revocation feasibility, platform overlap, and WTP. | Direct workflow evidence must show a repeated consent coordination failure; child exposure, conflict, coercion, privacy, revocation, and platform risks remain mandatory. | T09 — family and household |
| OPP-2026-818 | General household recurrence does not establish shared pet-care handoff failure. | T09-S01; whiteboard and chat alternatives | Observed missed/duplicated pet-care handoffs, consequence/frequency, shared-user participation, current workaround friction, and WTP. | Direct workflow evidence must establish the bounded handoff problem; no health advice, monitoring, shame, coercion, or false reliability claim may be added. | T09 — family and household |

External Governance Cycle 3 re-review requested
