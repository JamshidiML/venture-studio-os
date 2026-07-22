---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Exclusions

| Excluded space | Reason | Authority / evidence |
|---|---|---|
| Direct clone or replacement of Gmail, Slack, Teams, GitHub, Dropbox, Shopify, or another core platform | Violates companion-only scope and creates unrealistic platform competition. | Issue #11 |
| Unauthorized scraping, browser-session replay, private endpoints, or reverse-engineered mobile APIs | Explicitly prohibited and creates shutdown/security risk. | Issue #11 |
| Credential collection, password vaulting for host accounts, or shared login automation | Explicitly prohibited; use OAuth/component routes only. | Issue #11; P08-01, P08-22 |
| Spam, unsolicited bulk messaging, deceptive engagement, fake reviews, or install manipulation | Explicitly prohibited and violates platform policies. | Issue #11; P08-03, P08-09 |
| Surveillance or continuous employee/customer monitoring | Disproportionate privacy risk; not required for any qualified candidate. | Issue #11 and evidence rules |
| Broad mailbox/chat/history ingestion when a user-invoked or selected-resource path exists | Violates least privilege and raises verification/admin friction. | P08-02, P08-04, P08-14, P08-18 |
| Dependency on undocumented rate limits or assumed unlimited API access | Exact limits may be unpublished or dynamic. | P08-09, P08-15, P08-23, P08-25 |
| Autonomous messages, approvals, refunds, entitlement denials, repository writes, or purchases without confirmation | High consequence and often policy-sensitive; companions keep a human in control. | P08-03, P08-10, P08-14, P08-24 |
| General creator tool not dependent on a host platform | Reserved for T06. | Issue #11 |
| General SMB workflow tool where platform dependency is incidental | Reserved for T07. | Issue #11 |
| Platform popularity, install counts, or Marketplace rank used as opportunity evidence | Popularity is not problem, demand, or WTP evidence. | Issue #11 |
| Product ranking, deep competitor diligence, customer validation, MVP, PRD, or implementation | Outside Gate 1. | Parent #3 and Issue #11 |

## Correction Cycle 2 candidate withdrawals

These rows are preserved for audit history and are no longer counted as retained candidates.

| Opportunity ID | Withdrawn concept | Reason |
|---|---|---|
| OPP-2026-700 | Gmail commitment follow-up | Gmail API feasibility did not establish lost-commitment pain in Gmail users. |
| OPP-2026-701 | Gmail attachment filing | OAuth/file paths did not establish inconsistent attachment filing as a user problem. |
| OPP-2026-702 | Google Calendar context linker | Calendar notifications did not establish fragmented agenda/decision/follow-up pain. |
| OPP-2026-705 | Slack structured request intake | Shortcut/modal availability did not establish incomplete free-text requests. |
| OPP-2026-707 | Teams approval evidence packet | Teams/Graph permissions did not establish approval-packet inconsistency, and native Approvals creates major overlap. |
| OPP-2026-709 | Outlook shared-mailbox exception queue | Change-notification feasibility did not establish late service-exception discovery. |
| OPP-2026-710 | Outlook Calendar change brief | Subscription feasibility did not establish owner-brief pain. |
| OPP-2026-711 | OneDrive/SharePoint approval-context review | Delta/API feasibility and broad Teams-review context did not establish evidence-folder approval pain. |
| OPP-2026-714 | GitHub release readiness packet | GitHub App feasibility did not establish inconsistent release-evidence packaging. |

## Hypothesis Watchlist

These four records were part of the 11-candidate Cycle-2 auditable universe but are not Qualified Gate 1 Candidates in Cycle 3. They remain owned by T08 and retain their full Issue #11 platform-companion contracts. They are not withdrawn, ranked, selected, or authorized for integration work.

### Preserved Issue #11 candidate contracts

| ID | Original host, concept, user workflow, and claim type | Authorized integration path | Evidence searched and current alternative | Dependency, permissions, policy, distribution, and shutdown risk | Fallback strategy | Current confidence |
|---|---|---|---|---|---|---|
| OPP-2026-703 | Google Drive; owner reviews selected-folder permission/change drift; problem type: assumption | Drive API changes plus minimum metadata/permission scope for selected resources | W08-28 documents broad admin permissions/settings friction; native Admin/Drive controls; P08-01–P08-04 and P08-07 establish feasibility only | Shared-drive/user logs, state reconstruction, broad scopes, OAuth verification/security assessment, Marketplace/domain deployment, API/policy change or loss of access | User selects/exports folder report; no full-drive crawl | medium-low |
| OPP-2026-704 | Slack; user captures an important message as a decision with owner and rationale; problem type: assumption | Message shortcut, modal, scoped write to app store; event context only | W08-29 documents important messages buried broadly; native search/saved messages; P08-08–P08-12 establish feasibility only | OAuth scopes, 3-second acknowledgement, message privacy, Marketplace review, method-limit/change risk, event disablement or app removal | Signed web form with user-chosen permalink/text | medium |
| OPP-2026-706 | Slack; opted-in handoff messages receive owner/age reminders to reduce loss in message flow; problem type: assumption | Events API for explicit channels and message posting with minimal scopes | W08-29 documents overload/missed messages broadly; native notifications/search; P08-08, P08-09, P08-11 establish feasibility only | History/replies limits, channel visibility, notification spam, Marketplace/customer approval, event disablement, host policy or API shutdown | Manual queue or scheduled digest from user-submitted handoffs | medium-low |
| OPP-2026-708 | Teams; user captures a channel decision without indexing all chat history; problem type: assumption | User-invoked bot/action; resource-specific consent or narrow Graph permission | W08-30 documents channel/notification overload broadly; native channels/search; P08-13–P08-15 establish feasibility only | Broad chat read is high-friction; tenant consent, throttling, Teams Store/catalog distribution, permission/policy change or host shutdown | User submits message link/text to external register | low-medium |

### Qualification gap and reconsideration record

| ID | Why not currently qualified | Missing evidence | Risk and safety constraints retained | Conditions required for reconsideration | Original Thread ownership |
|---|---|---|---|---|---|
| OPP-2026-703 | Broad permissions/settings complaints do not directly establish selected-folder drift review as the user job. | Exact-workflow observation, frequency/severity, current workaround friction, buyer authority, and WTP. | Least privilege, selected resources only, no full-drive crawl, verification/security-assessment and shutdown fallback. | Independent or direct-user evidence must observe the bounded Drive drift workflow; API feasibility alone cannot qualify it. | T08 — platform companions |
| OPP-2026-704 | Buried-message evidence does not directly establish decision capture with owner/rationale as a repeated job. | Decision-specific incidence, user-invoked capture behavior, adoption, privacy acceptance, and WTP. | User invocation, minimum message context, scope review, acknowledgement and Marketplace limits, no history scraping. | Exact Slack decision-capture workflow evidence must be added while preserving privacy and non-scraping boundaries. | T08 — platform companions |
| OPP-2026-706 | Notification overload does not directly establish aged handoff reminders as the bounded problem. | Observed handoff loss/aging, recurrence, reminder benefit/harm, current alternative friction, and WTP. | Opted-in channels only, anti-spam limits, visibility controls, no broad history ingestion, shutdown fallback. | Exact Slack handoff workflow evidence must demonstrate investigability without relying on API availability or notification volume alone. | T08 — platform companions |
| OPP-2026-708 | Teams overload complaints do not directly establish a channel-decision registry/capture job. | Observed decision-retrieval failure, frequency, admin acceptance, current workaround friction, and WTP. | User-invoked capture, no tenant-wide indexing, least privilege, admin consent, throttling and shutdown fallback. | Exact Teams decision-capture workflow evidence must be added; Graph feasibility and broad overload cannot qualify it. | T08 — platform companions |

External Governance Cycle 3 re-review requested
