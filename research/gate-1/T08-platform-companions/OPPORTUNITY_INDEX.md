---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Opportunity Index

Exactly seven unranked Qualified Gate 1 Candidates are recorded. Nine API-only concepts were withdrawn in External Governance Correction Cycle 2; Cycle 3 moved four assumption-led concepts to the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). No Opportunity Score, rank, or commercial disposition is assigned.

Each qualified candidate problem/workflow statement has exactly one type. Inferences cite direct or observable-friction evidence plus explicit limits. Watchlist assumptions OPP-2026-703, 704, 706, and 708 remain owned by the Strategy Agent with their full claim treatment and platform contracts preserved in EXCLUSIONS. No validation or integration work is authorized in Gate 1.

| ID | Host; user workflow; problem claim type | Authorized integration path | Dependency and policy risk | Distribution route | Fallback strategy | Evidence / confidence |
|---|---|---|---|---|---|---|
| OPP-2026-712 | GitHub Issues; author checks acceptance evidence to reduce issue-handoff miscommunication; problem type: inference | GitHub App on selected repositories with Issues read/write and webhook | Org owner installation restrictions, permission expansion approval, rate limits | GitHub Marketplace or direct selected-repo install | Repository Action validates issue form/linked Markdown without external data | Problem W08-31; feasibility P08-18 through P08-21; medium-high |
| OPP-2026-713 | GitHub PRs; reviewer receives a linked evidence bundle to reduce repeated context/revision work; problem type: inference | GitHub App webhooks with read-only pull/check metadata; write only for explicit status/comment | Sensitive repo metadata, installation scope, API limits, permission changes | GitHub Marketplace/direct install | CI job generates Markdown artifact inside repository | Problem W08-32; feasibility P08-18 through P08-21; medium-high |
| OPP-2026-715 | Dropbox; external file collection shows missing required files and sync status; problem type: inference | OAuth App Folder where possible or Dropbox Chooser/Saver components | Full Dropbox access must be avoided unless necessary; review/consent; unpublished exact limits | Dropbox app distribution plus service/agency channel | Secure upload portal or user-selected files; no account-wide access | Problem W08-33; feasibility P08-22, P08-23; medium-low |
| OPP-2026-716 | Dropbox; owner reviews selected-folder sync conflicts and version/organization exceptions; problem type: inference | OAuth with narrowly required sharing/file metadata scope; team link only if necessary | Full Dropbox/team access, customer trust, 429 handling, exact limits unknown | Dropbox app distribution or managed customer install | User exports a selected-folder/version report for comparison | Problem W08-33; feasibility P08-22, P08-23; medium-low |
| OPP-2026-717 | Shopify; merchant identifies partially fulfilled/out-of-stock orders and prepares customer action digest; problem type: inference | Admin GraphQL API and webhooks with minimum order/fulfillment scopes | Protected customer data review, PII, API version/query cost, App Store review | Shopify App Store or merchant custom app | Merchant CSV export/manual exception upload | Problem W08-34; feasibility P08-24 through P08-27; medium-low |
| OPP-2026-718 | Shopify; merchant reconciles return/refund evidence and reporting state for human review; problem type: inference | Admin API/webhooks for selected orders/refunds; request protected fields only if required | Customer/order PII, protected-data requirements, no automated denial, throttling | Shopify App Store/custom app | Order-specific manual upload/export packet | Problem W08-35; feasibility P08-24 through P08-27; medium-low |
| OPP-2026-719 | Shopify; merchant records approval/provenance for catalog changes where native audit detail is insufficient; problem type: inference | Product webhooks/Admin API; avoid customer data and use scoped product access | API versioning, query cost, review, actor attribution limits, merchant write confirmation | Shopify App Store/custom app | Product CSV diff and signed approval report | Problem W08-36; feasibility P08-25 through P08-27; medium |

## Integrity check

- The seven qualified IDs and four watchlist IDs are unique and confined to OPP-2026-700 through OPP-2026-719; together they equal the 11-candidate Cycle-2 auditable universe. Earlier withdrawn IDs 700, 701, 702, 705, 707, 709, 710, 711, and 714 remain separately preserved in [EXCLUSIONS.md](EXCLUSIONS.md).
- Every qualified and watchlist record preserves host, workflow, official path, dependency/policy risk, distribution, fallback, evidence, and confidence.
- Fallbacks avoid undocumented/private APIs and credential collection.
- API feasibility is not treated as demand or product selection.
