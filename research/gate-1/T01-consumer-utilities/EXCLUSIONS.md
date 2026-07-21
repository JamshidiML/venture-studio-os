---
status: in-review
version: 0.1.1
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

No excluded candidate was silently deleted or reassigned an ID. Reserved IDs not used in this 20-candidate universe remain unallocated.
