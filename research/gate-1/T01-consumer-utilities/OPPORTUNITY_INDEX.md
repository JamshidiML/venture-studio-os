---
status: in-review
version: 0.1.2
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
| OPP-2026-011 | Infrequently used possessions are hard to relocate. | Individuals; memory/photos. | unsupported hypothesis; T01-S01 is context only | very low: no direct problem evidence | moving/storage communities | precise home locations are sensitive; local storage default |
| OPP-2026-012 | Borrowed household items lack a neutral return record. | Individuals lending/borrowing; chat/memory. | unsupported hypothesis; T01-S01 is context only | very low: no direct problem evidence | neighborhood reuse communities | no contact graph or coercive reminders |
| OPP-2026-013 | Small errands are inefficient when scattered across lists. | Adults doing local errands; notes/calendar. | T01-S01; inference | medium: household-management frequency direct | local-living and organization search | no continuous location collection |
| OPP-2026-014 | Repeated trips require reconstructing similar packing lists. | Travelers/participants; static checklist. | unsupported hypothesis; no direct source | very low: ATUS does not measure packing friction | packing-checklist search | no destination booking/platform dependency |
| OPP-2026-015 | Household plants have differing care cadences. | Plant owners; tags/calendar. | unsupported hypothesis; no direct source | very low: category not isolated in ATUS | plant-care content search | no guarantee; climate/species variability visible |
| OPP-2026-016 | Routine pet care handoffs can be ambiguous. | Pet owners; note/message. | unsupported hypothesis; T01-S08 is animal-keeping context only | very low: no handoff-failure evidence | pet-owner communities | exclude diagnosis, medication, veterinary or emergency advice |
| OPP-2026-017 | Seasonal household tasks disappear between infrequent cycles. | Renters/homeowners; annual calendar. | T01-S05; inference | medium: annual cadence direct; missed-task data absent | seasonal maintenance search | local climate and tenancy responsibility vary |
| OPP-2026-018 | General task lists do not surface actions suited to a short waiting period. | Adults with fragmented idle time; task list. | unsupported hypothesis; no direct source | very low: idle-time problem unmeasured | productivity search, excluding work/SMB positioning | no productivity or wellbeing outcome claim |
| OPP-2026-019 | Repeated chores are hard to recall after completion, causing duplicate work or uncertainty. | Adults managing chores; notes/habit tracker. | unsupported hypothesis; T01-S01 is recurrence context only | very low: duplicate-work claim unmeasured | home-organization search | minimal data; avoid surveillance and streak pressure |
| OPP-2026-020 | Travel or disruption breaks routines and forces people to reconstruct the restart order. | Adults resuming household routines; memory/list. | unsupported hypothesis; T01-S01/S02 are context only | very low: restart pain unmeasured | routine-restart search | no clinical habit-treatment framing |

## Candidate-to-Source Coverage Matrix

`Direct` means the source observes user pain or behavior tied to the candidate problem. `Context` includes population, category, cadence, and official guidance. Safety guidance is never classified as direct pain. A dash means no qualifying source was found and must not be read as positive evidence.

| ID | Direct problem evidence | Contextual / population evidence | Current-alternative evidence | Technical feasibility | Legal / privacy / safety / platform evidence | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|
| 001 | — | S01/S05 | — | manual calendar assumed | S05 guidance boundary | consolidated cadence will reduce omissions |
| 002 | — | S06 recurring-test guidance only | — | manual record assumed | S06 safety guidance | users need a separate record |
| 003 | — | S05 maintenance-cadence guidance only | — | manual tracker assumed | manufacturer schedule prevails | cadence consolidation creates value |
| 004 | S02/S03 food-management drivers | S07 national cost model | — | manual queue assumed | S04 food guidance | queue changes behavior |
| 005 | S02/S03 leftover-use context | S07 national cost model | S04 is guidance, not behavior evidence | manual ledger assumed | S04 food guidance | ledger changes behavior |
| 006 | S02 displaced-meal driver | — | — | manual list assumed | — | reset list prevents waste |
| 007 | — | S01 household activity | — | manual list assumed | — | replenishment pain is frequent |
| 008 | — | S01 household activity | — | photo/note assumed | user-owned content only | care-memory failure is frequent |
| 009 | — | S01 household activity | — | task list assumed | — | rotation reduces omissions |
| 010 | — | S01 household activity | — | notes/timer assumed | no clinical framing | setup overhead is material |
| 011 | — | S01 household activity | — | local photo/note assumed | sensitive location data | possessions are repeatedly lost |
| 012 | — | S01 household activity | — | manual record assumed | no social graph/coercion | neutral record improves returns |
| 013 | — | S01 household activity | — | manual batching assumed | no continuous location | batching friction is material |
| 014 | — | — | — | static checklist assumed | no booking dependency | packing reconstruction is recurrent |
| 015 | — | — | — | calendar assumed | climate/species variation | plant-care misses are recurrent |
| 016 | — | S08 animal-keeping only | — | message/note assumed | veterinary/emergency boundary | pet handoff ambiguity is recurrent |
| 017 | — | S05 seasonal-maintenance guidance only | — | calendar assumed | climate/tenancy variation | missed cycles create sufficient pain |
| 018 | — | S01 general time-use only | — | task tagging assumed | no outcome claim | idle-time queue creates value |
| 019 | — | S01 chore recurrence only | — | note capture assumed | privacy/no streak pressure | duplicate-work uncertainty is recurrent |
| 020 | — | S01/S02 general routine context | — | restart list assumed | no clinical framing | disruption creates restart-order pain |

## Portfolio Notes Without Ranking

- Coverage includes safety, food visibility, upkeep, personal organization, errands, repeatable lists, care routines, and interruption recovery.
- Candidates `004`–`006` have more specific behavioral evidence than the remaining concepts; this statement describes evidence specificity, not attractiveness or rank.
- Candidate `016` stays strictly non-clinical and household-facing. Candidate `018` is personal-only, not an employee or SMB workflow.
- Candidates `011`, `012`, `014`–`016`, and `018`–`020` are explicitly downgraded to `very low` confidence; all unsupported assumptions are visible in the matrix.
- None assumes network effects, proprietary data, paid APIs, or a dominant-platform integration.
