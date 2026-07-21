---
status: in-review
version: 0.1.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T01
issue_number: 4
gate: 1
---

# T01 Opportunity Index

All 20 entries are qualified for inclusion in the Gate 1 universe only. They are deliberately unranked. `Evidence basis` references [SOURCE_REGISTER.md](SOURCE_REGISTER.md); candidate propositions are inferences unless explicitly labeled otherwise.

| ID | Problem and bounded utility | Segment and current alternative | Evidence basis / claim type | Confidence rationale | Reachability hypothesis | Principal constraint |
|---|---|---|---|---|---|---|
| OPP-2026-001 | Routine home checks are distributed across different cadences; a manual maintenance cadence could consolidate them. | Renters/homeowners; calendar or paper list. | T01-S01/S05; inference | medium: recurring work and cadence are direct, tool demand is not | homeowner/renter communities and maintenance-content search | must not represent professional inspection |
| OPP-2026-002 | People need to remember and record smoke-alarm tests. | Residents responsible for alarms; calendar/date label. | T01-S06; inference | medium: required action is direct; missed-test prevalence unknown | public fire-safety content and housing groups | safety disclaimer; no claim that a test proves safety |
| OPP-2026-003 | Filters and other household consumables have heterogeneous replacement intervals. | Households; packaging notes/calendar. | T01-S05; inference | medium: cadence is direct; user pain unmeasured | home-maintenance search | manufacturer schedule prevails; no device control |
| OPP-2026-004 | Foods needing earlier use can become invisible in a pantry or refrigerator. | Adults responsible for food; memory/sticky note. | T01-S02/S03/S04; inference | medium: behavior evidence is relevant across two sources | food-waste education channels | storage guidance and allergens must not be improvised |
| OPP-2026-005 | Leftovers lack a simple visible “use first” record. | Adults storing prepared food; labels/memory. | T01-S02/S04; inference | medium: leftover use is supported; adoption unknown | food-waste and meal-planning search | no safety guarantee; date labels are user-entered |
| OPP-2026-006 | A displaced meal can invalidate a plan and increase waste. | Adults with changing schedules; ad hoc list. | T01-S02; inference | medium: driver observed in a current UK survey | meal-planning communities without recipe/content copying | geography and self-report limit transfer |
| OPP-2026-007 | Non-financial household supplies run out at uneven rates. | Adults replenishing supplies; memory/list. | T01-S01; inference | low: only category-level recurrence is evidenced | general household-organization search | avoid retailer, inbox, or price integration |
| OPP-2026-008 | Garment-care details are forgotten after labels fade or items leave the closet. | People managing clothing; label photo/note. | T01-S01; inference | low: plausible repeated task, no direct failure data | clothing-care search | no fabric-result guarantee; user-owned photos only |
| OPP-2026-009 | Cleaning tasks recur at different intervals and are easy to bunch or omit. | Adults doing housework; generic task list. | T01-S01; inference | medium: housework frequency direct, cadence pain indirect | cleaning and home-organization content | avoid shame and punitive streak mechanics |
| OPP-2026-010 | Large decluttering goals create setup overhead; a micro-session queue could preserve the next action. | Adults organizing homes; notes/timer. | T01-S01; inference | low: no direct decluttering evidence | home-organization search | no clinical or hoarding-treatment framing |
| OPP-2026-011 | Infrequently used possessions are hard to relocate. | Individuals; memory/photos. | T01-S01; inference | low: broad organization evidence only | moving/storage communities | precise home locations are sensitive; local storage default |
| OPP-2026-012 | Borrowed household items lack a neutral return record. | Individuals lending/borrowing; chat/memory. | T01-S01; inference | low: recurrence and demand unmeasured | neighborhood reuse communities | no contact graph or coercive reminders |
| OPP-2026-013 | Small errands are inefficient when scattered across lists. | Adults doing local errands; notes/calendar. | T01-S01; inference | medium: household-management frequency direct | local-living and organization search | no continuous location collection |
| OPP-2026-014 | Repeated trips require reconstructing similar packing lists. | Travelers/participants; static checklist. | T01-S01; inference | low: relevant but indirect time-use support | packing-checklist search | no destination booking/platform dependency |
| OPP-2026-015 | Household plants have differing care cadences. | Plant owners; tags/calendar. | T01-S01; inference | low: category not isolated in ATUS | plant-care content search | no guarantee; climate/species variability visible |
| OPP-2026-016 | Routine pet care handoffs can be ambiguous. | Pet owners; note/message. | T01-S01/T01-S08; inference | low: APHIS scope is narrow and does not measure handoff failures | pet-owner communities | exclude diagnosis, medication, veterinary or emergency advice |
| OPP-2026-017 | Seasonal household tasks disappear between infrequent cycles. | Renters/homeowners; annual calendar. | T01-S05; inference | medium: annual cadence direct; missed-task data absent | seasonal maintenance search | local climate and tenancy responsibility vary |
| OPP-2026-018 | General task lists do not surface actions suited to a short waiting period. | Adults with fragmented idle time; task list. | T01-S01; inference | low: no direct idle-time problem evidence | productivity search, excluding work/SMB positioning | no productivity or wellbeing outcome claim |
| OPP-2026-019 | Repeated chores are hard to recall after completion, causing duplicate work or uncertainty. | Adults managing chores; notes/habit tracker. | T01-S01; inference | low: task recurrence direct, duplicate-work claim unmeasured | home-organization search | minimal data; avoid surveillance and streak pressure |
| OPP-2026-020 | Travel or disruption breaks routines and forces people to reconstruct the restart order. | Adults resuming household routines; memory/list. | T01-S01/S02; inference | low: disruption link is indirect | routine-restart search | no clinical habit-treatment framing |

## Portfolio Notes Without Ranking

- Coverage includes safety, food visibility, upkeep, personal organization, errands, repeatable lists, care routines, and interruption recovery.
- Candidates `004`–`006` have more specific behavioral evidence than the remaining concepts; this statement describes evidence specificity, not attractiveness or rank.
- Candidate `016` stays strictly non-clinical and household-facing. Candidate `018` is personal-only, not an employee or SMB workflow.
- None assumes network effects, proprietary data, paid APIs, or a dominant-platform integration.
