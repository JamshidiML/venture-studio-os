---
status: in-review
version: 0.1.4
owner_role: Strategy Agent
last_reviewed: 2026-07-23
thread_id: T01
issue_number: 4
gate: 1
---

# T01 Opportunity Index

This index contains the three Qualified Gate 1 Candidates. They are deliberately unranked. Seventeen unsupported concepts remain preserved, under their original IDs, in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). Issue #25 added no source merely to preserve qualification: the nine disputed rows had empty direct-evidence cells and moved to the watchlist. `Evidence basis` references [SOURCE_REGISTER.md](SOURCE_REGISTER.md); candidate propositions are inferences unless explicitly labeled otherwise.

| ID | Problem and bounded utility | Segment and current alternative | Evidence basis / claim type | Confidence rationale | Reachability hypothesis | Principal constraint |
|---|---|---|---|---|---|---|
| OPP-2026-004 | Foods needing earlier use can become invisible in a pantry or refrigerator. | Adults responsible for food; memory/sticky note. | T01-S02/S03/S04; inference | medium: behavior evidence is relevant across two sources | food-waste education channels | storage guidance and allergens must not be improvised |
| OPP-2026-005 | Leftovers lack a simple visible “use first” record. | Adults storing prepared food; labels/memory. | T01-S02/S04; inference | medium: leftover use is supported; adoption unknown | food-waste and meal-planning search | no safety guarantee; date labels are user-entered |
| OPP-2026-006 | A displaced meal can invalidate a plan and increase waste. | Adults with changing schedules; ad hoc list. | T01-S02; inference | medium: driver observed in a current UK survey | meal-planning communities without recipe/content copying | geography and self-report limit transfer |

## Candidate-to-Source Coverage Matrix

`Direct` means the source observes user pain or behavior tied to the candidate problem. `Context` includes population, category, cadence, and official guidance. Safety guidance is never classified as direct pain. A dash means no qualifying source was found and must not be read as positive evidence.

| ID | Final status | Direct problem evidence | Contextual / population evidence | Current-alternative evidence | Technical feasibility | Legal / privacy / safety / platform evidence | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|---|
| 001 | watchlist | — | S01/S05 | — | manual calendar assumed | S05 guidance boundary | consolidated cadence will reduce omissions |
| 002 | watchlist | — | S06 recurring-test guidance only | — | manual record assumed | S06 safety guidance | users need a separate record |
| 003 | watchlist | — | S05 maintenance-cadence guidance only | — | manual tracker assumed | manufacturer schedule prevails | cadence consolidation creates value |
| 004 | qualified | S02/S03 food-management drivers | S07 national cost model | — | manual queue assumed | S04 food guidance | queue changes behavior |
| 005 | qualified | S02/S03 leftover-use context | S07 national cost model | S04 is guidance, not behavior evidence | manual ledger assumed | S04 food guidance | ledger changes behavior |
| 006 | qualified | S02 displaced-meal driver | — | — | manual list assumed | — | reset list prevents waste |
| 007 | watchlist | — | S01 household activity | — | manual list assumed | — | replenishment pain is frequent |
| 008 | watchlist | — | S01 household activity | — | photo/note assumed | user-owned content only | care-memory failure is frequent |
| 009 | watchlist | — | S01 household activity | — | task list assumed | — | rotation reduces omissions |
| 010 | watchlist | — | S01 household activity | — | notes/timer assumed | no clinical framing | setup overhead is material |
| 011 | watchlist | — | S01 household activity | — | local photo/note assumed | sensitive location data | possessions are repeatedly lost |
| 012 | watchlist | — | S01 household activity | — | manual record assumed | no social graph/coercion | neutral record improves returns |
| 013 | watchlist | — | S01 household activity | — | manual batching assumed | no continuous location | batching friction is material |
| 014 | watchlist | — | — | — | static checklist assumed | no booking dependency | packing reconstruction is recurrent |
| 015 | watchlist | — | — | — | calendar assumed | climate/species variation | plant-care misses are recurrent |
| 016 | watchlist | — | S08 animal-keeping only | — | message/note assumed | veterinary/emergency boundary | pet handoff ambiguity is recurrent |
| 017 | watchlist | — | S05 seasonal-maintenance guidance only | — | calendar assumed | climate/tenancy variation | missed cycles create sufficient pain |
| 018 | watchlist | — | S01 general time-use only | — | task tagging assumed | no outcome claim | idle-time queue creates value |
| 019 | watchlist | — | S01 chore recurrence only | — | note capture assumed | privacy/no streak pressure | duplicate-work uncertainty is recurrent |
| 020 | watchlist | — | S01/S02 general routine context | — | restart list assumed | no clinical framing | disruption creates restart-order pain |

## Portfolio Notes Without Ranking

- Qualified coverage is limited to food visibility and disrupted-meal reset workflows (`004`–`006`) supported by T01-S02/S03 observed food-management behavior. Safety, upkeep, organization, errands, repeatable lists, care routines, and interruption recovery remain visible in the watchlist rather than being qualified from context or guidance.
- Candidates `004`–`006` are retained because their direct behavioral basis survives the Issue #25 audit; this statement describes evidence specificity, not attractiveness or rank.
- Candidate `016` stays strictly non-clinical and household-facing. Candidate `018` is personal-only, not an employee or SMB workflow.
- Candidates `001`–`003`, `007`–`020` are on the Hypothesis Watchlist at `very low` confidence; all unsupported assumptions remain visible in the matrix and complete watchlist contracts.
- None assumes network effects, proprietary data, paid APIs, or a dominant-platform integration.

Final External Governance re-review requested
