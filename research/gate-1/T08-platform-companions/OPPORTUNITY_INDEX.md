---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Opportunity Index

Exactly 11 retained unranked Gate 1 candidates are recorded. Nine API-only concepts were withdrawn in External Governance Correction Cycle 2 and remain preserved in [EXCLUSIONS.md](EXCLUSIONS.md). No Opportunity Score or commercial disposition is assigned.

Each candidate problem/workflow statement has exactly one type. Inferences cite direct or observable-friction evidence plus explicit limits. Assumptions (OPP-2026-703, 704, 706, and 708) are owned by the Strategy Agent; impact if wrong: the affected candidate cannot advance regardless of API feasibility; planned review/test: revisit only through separately authorized future research or validation. No such work is authorized in Gate 1.

| ID | Host; user workflow; problem claim type | Authorized integration path | Dependency and policy risk | Distribution route | Fallback strategy | Evidence / confidence |
|---|---|---|---|---|---|---|
| OPP-2026-703 | Google Drive; owner reviews selected-folder permission/change drift; problem type: assumption | Drive API changes plus minimum metadata/permission scope for selected resources | Shared-drive/user logs, state reconstruction, broad Drive scopes, verification | Workspace Marketplace or domain deployment | User selects/exports folder report; no full-drive crawl | Problem W08-28; feasibility P08-01 through P08-04, P08-07; medium-low |
| OPP-2026-704 | Slack; user captures an important message as a decision with owner and rationale; problem type: assumption | Message shortcut, modal, scoped write to app store; event context only | OAuth scopes, 3-second ACK, message context privacy, Marketplace review | Slack Marketplace or workspace-approved unlisted app | Signed web form with pasted permalink/text chosen by user | Problem W08-29; feasibility P08-08 through P08-12; medium |
| OPP-2026-706 | Slack; opted-in handoff messages receive owner/age reminders to reduce loss in message flow; problem type: assumption | Events API for explicit channels and message posting with minimal scopes | conversations.history/replies limits, visibility, event disablement, notification spam | Slack Marketplace or customer-approved install | Manual queue or scheduled digest from user-submitted handoffs | Problem W08-29; feasibility P08-08, P08-09, P08-11; medium-low |
| OPP-2026-708 | Teams; user captures a channel decision without indexing all chat history; problem type: assumption | User-invoked bot/action; RSC or narrow Graph permission | Broad chat read is high-friction; admin controls and throttling | Teams Store or tenant app catalog | User submits message link/text to external register | Problem W08-30; feasibility P08-13 through P08-15; low-medium |
| OPP-2026-712 | GitHub Issues; author checks acceptance evidence to reduce issue-handoff miscommunication; problem type: inference | GitHub App on selected repositories with Issues read/write and webhook | Org owner installation restrictions, permission expansion approval, rate limits | GitHub Marketplace or direct selected-repo install | Repository Action validates issue form/linked Markdown without external data | Problem W08-31; feasibility P08-18 through P08-21; medium-high |
| OPP-2026-713 | GitHub PRs; reviewer receives a linked evidence bundle to reduce repeated context/revision work; problem type: inference | GitHub App webhooks with read-only pull/check metadata; write only for explicit status/comment | Sensitive repo metadata, installation scope, API limits, permission changes | GitHub Marketplace/direct install | CI job generates Markdown artifact inside repository | Problem W08-32; feasibility P08-18 through P08-21; medium-high |
| OPP-2026-715 | Dropbox; external file collection shows missing required files and sync status; problem type: inference | OAuth App Folder where possible or Dropbox Chooser/Saver components | Full Dropbox access must be avoided unless necessary; review/consent; unpublished exact limits | Dropbox app distribution plus service/agency channel | Secure upload portal or user-selected files; no account-wide access | Problem W08-33; feasibility P08-22, P08-23; medium-low |
| OPP-2026-716 | Dropbox; owner reviews selected-folder sync conflicts and version/organization exceptions; problem type: inference | OAuth with narrowly required sharing/file metadata scope; team link only if necessary | Full Dropbox/team access, customer trust, 429 handling, exact limits unknown | Dropbox app distribution or managed customer install | User exports a selected-folder/version report for comparison | Problem W08-33; feasibility P08-22, P08-23; medium-low |
| OPP-2026-717 | Shopify; merchant identifies partially fulfilled/out-of-stock orders and prepares customer action digest; problem type: inference | Admin GraphQL API and webhooks with minimum order/fulfillment scopes | Protected customer data review, PII, API version/query cost, App Store review | Shopify App Store or merchant custom app | Merchant CSV export/manual exception upload | Problem W08-34; feasibility P08-24 through P08-27; medium-low |
| OPP-2026-718 | Shopify; merchant reconciles return/refund evidence and reporting state for human review; problem type: inference | Admin API/webhooks for selected orders/refunds; request protected fields only if required | Customer/order PII, protected-data requirements, no automated denial, throttling | Shopify App Store/custom app | Order-specific manual upload/export packet | Problem W08-35; feasibility P08-24 through P08-27; medium-low |
| OPP-2026-719 | Shopify; merchant records approval/provenance for catalog changes where native audit detail is insufficient; problem type: inference | Product webhooks/Admin API; avoid customer data and use scoped product access | API versioning, query cost, review, actor attribution limits, merchant write confirmation | Shopify App Store/custom app | Product CSV diff and signed approval report | Problem W08-36; feasibility P08-25 through P08-27; medium |

## Integrity check

- The 11 retained IDs are unique and confined to OPP-2026-700 through OPP-2026-719. Withdrawn IDs 700, 701, 702, 705, 707, 709, 710, 711, and 714 remain in [EXCLUSIONS.md](EXCLUSIONS.md).
- Every row names host, workflow, official path, dependency/policy risk, distribution, fallback, evidence, and confidence.
- Fallbacks avoid undocumented/private APIs and credential collection.
- API feasibility is not treated as demand or product selection.
