---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T01
issue_number: 4
gate: 1
---

# T01 Exclusions

| Space or candidate considered | Decision | Reason and rule applied | Destination if applicable |
|---|---|---|---|
| Subscription cancellation and price-change tracker | excluded from T01 | Core value is household cost reduction and recurring-charge management. | T03 scope |
| Senior medication reminders | excluded | Clinical/senior overlap; medication safety and integration risk. | T02 only if non-clinical issue permits; otherwise out of Gate 1 |
| Accessibility overlay for third-party sites | excluded | Accessibility and platform-companion overlap; technical/legal risk. | T02/T08 boundary review |
| Study planner | excluded | Education workflow is explicitly out of scope. | T04 scope |
| Creator publishing checklist | excluded | Creator/prosumer workflow. | T06 scope |
| Employee chore/work-order system | excluded | SMB workflow and multi-user operations. | T07 scope |
| Email or browser companion that extracts tasks | excluded | Critical platform/inbox dependency and T08 overlap. | T08 scope |
| Family command center | excluded | Multi-person family coordination is T09. | T09 scope |
| Symptom, medication, mood, sleep, or treatment tracker | excluded | Health diagnosis/treatment or non-clinical wellbeing boundary. | T05 or prohibited clinical scope |
| Gambling, dating, social network, game, or adult utility | excluded | Explicit Issue #4 prohibition. | none |
| Continuous household-member location or activity surveillance | excluded | Disproportionate privacy risk and lack of informed consent. | none |
| Dark-pattern streak enforcer or shame notifications | excluded | Manipulative engagement conflicts with governance rules. | none |
| Community marketplace requiring network liquidity | excluded | Large proprietary network dependency. | none |
| Copied competitor interface/content library | excluded | Intellectual-property and differentiation violation. | none |
| Automated food-safety decision maker | excluded | Would overstate stale/general guidance and create safety risk. | none |

## Hypothesis Watchlist

These concepts remain owned by T01 and retain their original IDs, but they are not Qualified Gate 1 Candidates. Context, guidance, and feasibility do not substitute for direct or clearly adjacent observed workflow evidence.

| Opportunity ID | Original concept | Reason not currently qualified | Current confidence | Evidence searched | Missing evidence | Risk and safety constraints | Conditions for future reconsideration | Original Thread ownership |
|---|---|---|---|---|---|---|---|---|
| OPP-2026-011 | Personal possession-location register for infrequently used household items | T01-S01 shows general household activity, not repeated possession-location failures. | very low | T01-S01; household time-use and organization queries in SEARCH_LOG.md | Direct diary, interview, observation, or complaint evidence of recurrent relocation pain. | Exact home locations are sensitive; local-only/minimum-data default and no surveillance. | Reconsider only if direct evidence establishes recurrence and severity in a bounded segment and a safe manual path. | T01 — consumer utilities |
| OPP-2026-012 | Borrowed-item return log | General household activity does not observe borrowing, return failures, or demand for a neutral record. | very low | T01-S01; household-management and neighborhood-reuse query coverage | Direct lender/borrower workflow evidence, including frequency and social failure modes. | No contact graph, coercive reminders, public shaming, or inferred relationships. | Reconsider only after observed recurring return friction and consent-safe reminder requirements are documented. | T01 — consumer utilities |
| OPP-2026-014 | Reusable packing checklist | No registered source observes recurrent packing-list reconstruction pain. | very low | Time-use and consumer-utility query set; no qualifying source found | Direct traveler/participant diary, interview, complaint, or representative survey evidence. | No booking dependency, destination inference, or sensitive itinerary collection. | Reconsider only if bounded users directly report repeated reconstruction with material cost or error. | T01 — consumer utilities |
| OPP-2026-015 | Plant-care rotation | No registered source isolates household plant-care misses or cadence pain. | very low | Household-activity, maintenance, and care queries; no qualifying plant-workflow source | Direct plant-owner workflow evidence of recurring missed/duplicated care. | No horticultural guarantee; species, climate, toxicity, and local conditions stay visible. | Reconsider only with observed workflow evidence and an authoritative, versioned safety-content boundary. | T01 — consumer utilities |
| OPP-2026-016 | Non-clinical pet-care handoff | T01-S08 is animal-keeping context and does not measure companion-animal handoff ambiguity. | very low | T01-S08 and animal-care query recorded in SEARCH_LOG.md | Direct multi-carer pet routine evidence showing missed or duplicated handoffs. | No diagnosis, medication, veterinary, treatment, or emergency reliance; consent and minimum data required. | Reconsider only after a direct handoff study and a strict non-clinical/manual fallback are documented. | T01 — consumer utilities |
| OPP-2026-018 | Waiting-time micro-task queue | No source observes idle-time task-selection pain or utility demand. | very low | General time-use and productivity-adjacent query coverage; no qualifying source | Direct observation or diary evidence of recurrent fragmented-time task-selection friction. | No productivity or wellbeing outcome claim; no employee monitoring. | Reconsider only if a bounded personal-use segment demonstrates the recurring user event and desired output. | T01 — consumer utilities |
| OPP-2026-019 | “Done today” completion capture | T01-S01 establishes chore recurrence, not duplicate-work or completion-recall failures. | very low | T01-S01; household-work and organization query coverage | Direct evidence of frequent uncertainty or duplication after household task completion. | Minimum data; no household-member surveillance, shame, or punitive streaks. | Reconsider only with observed completion-recall pain and explicit multi-person consent requirements. | T01 — consumer utilities |
| OPP-2026-020 | Routine restart after interruption | T01-S01/S02 provide general routine context, not restart-order pain after disruption. | very low | T01-S01/S02; time-use and disrupted-meal query coverage | Direct diary/interview evidence of recurrent restart failures in a bounded non-clinical segment. | No clinical habit-treatment framing, outcome claim, or invasive behavior tracking. | Reconsider only if interruption and restart are directly observed and a manual non-clinical workflow is sufficient. | T01 — consumer utilities |

No excluded or watchlist candidate was silently deleted or reassigned an ID. The auditable universe remains 20 IDs: 12 qualified and eight watchlist. Reserved IDs outside `OPP-2026-001`–`020` remain unallocated.
