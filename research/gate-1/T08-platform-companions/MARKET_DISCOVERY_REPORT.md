---
status: in-review
version: 0.2.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Gate 1 Market Discovery — Companion Tools for Dominant Platforms

## Executive summary

This report documents 20 unranked companion-tool candidates across Google Workspace, Slack, Microsoft 365/Teams, GitHub, Dropbox, and Shopify. Every candidate has an official, documented integration route and an explicit fallback that does not rely on scraping, credentials, private APIs, spam, surveillance, or circumvention.

Feasibility is conditional. Google may require OAuth verification and, for server-side restricted-scope data, an annual independent security assessment. Slack ties events to OAuth scopes, applies method-specific limits, and manually reviews Marketplace submissions. Microsoft Graph requires least-privilege consent and can throttle requests; tenant administrators may control installation. GitHub Apps expose granular permissions and Marketplace rules. Dropbox uses OAuth scopes, does not publish exact general rate limits, and recommends least access. Shopify reviews apps, rate-limits APIs, and separately reviews protected customer data.

Official API availability proves an authorized path, not customer demand, popularity, or commercial attractiveness. No platform usage, install, revenue, download, or WTP figures are claimed. No winner is selected and Gate 2 has not begun.

## Objective and scope

- Authorization: Parent [Issue #3](https://github.com/JamshidiML/venture-studio-os/issues/3) and child [Issue #11](https://github.com/JamshidiML/venture-studio-os/issues/11).
- Gate: 1 — market discovery only.
- Scope: companion tools that extend messaging, email, calendar, cloud-storage, commerce, and collaboration workflows without replacing the host.
- Geography: platform documentation is generally global; tenant, plan, app type, account type, national cloud, and local-law limitations are recorded.
- Source cutoff and access date: 2026-07-22.
- Candidate count: exactly 20, OPP-2026-700 through OPP-2026-719.
- Exclusions: see [EXCLUSIONS.md](EXCLUSIONS.md).

## Methodology

Only official developer documentation and platform policies were used for API, permission, review, distribution, rate-limit, and shutdown-risk claims. Dynamic pages record access date; missing page dates are marked “date unavailable.” Each candidate qualified only when it had:

1. a host-specific user workflow and value wedge;
2. a current official API, component, webhook, action, or app route;
3. least-privilege and review/consent implications stated;
4. dependency and policy risk stated;
5. an official or independent distribution route stated;
6. a non-private-API fallback;
7. no prohibited scraping, spam, credential handling, surveillance, or platform replacement.

Full source records are in [SOURCE_REGISTER.md](SOURCE_REGISTER.md), queries in [SEARCH_LOG.md](SEARCH_LOG.md), and candidate-level integration records in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

Every candidate problem/workflow statement below is an assumption owned by the Strategy Agent. Impact if wrong: that candidate cannot advance because its problem remains unvalidated, regardless of API feasibility. Planned review/test: revisit only through separately authorized future research or validation; no such work is authorized in Gate 1.

## Material claims

| Claim ID | Claim | Type | Support | Scope | Confidence | Limitation |
|---|---|---|---|---|---|---|
| C08-01 | Public Google Workspace apps using sensitive or restricted scopes must complete verification; server-side restricted-scope data can require an annual independent security assessment. | evidence | P08-01, P08-02 | Google user data / public apps | high | Exact scope classification and exceptions must be checked for a final design. |
| C08-02 | Google Workspace Marketplace policies can lead to denial, disabling, unpublishing, or account action, and require OAuth2 and substantive integration. | evidence | P08-03, P08-04 | Workspace Marketplace | high | Policies can change; re-check before submission. |
| C08-03 | Gmail, Calendar, and Drive expose official change-notification or change-log paths, each with delivery or state limitations. | evidence | P08-05, P08-06, P08-07 | Google Workspace | high | Gmail watches expire; Calendar notifications can drop; Drive changes are latest state, not field deltas. |
| C08-04 | Slack Events are scope-bound, require timely acknowledgement, and can be rate-limited or disabled; non-Marketplace apps face changed history/replies limits. | evidence | P08-08, P08-09 | Slack apps | high | Method limits and Marketplace status can change. |
| C08-05 | Slack shortcuts and Marketplace review offer authorized interaction and distribution paths with confirmation and review requirements. | evidence | P08-10, P08-11, P08-12 | Slack apps | high | Marketplace review is discretionary and not demand evidence. |
| C08-06 | Microsoft Graph and Teams use declared permissions and consent; admins may control installation, and least privilege is recommended. | evidence | P08-13, P08-14 | Microsoft 365 / Teams | high | Delegated vs application permission materially changes risk. |
| C08-07 | Microsoft Graph throttles with 429 responses and Retry-After; Outlook and drive resources support change notifications or delta with resource-specific constraints. | evidence | P08-15, P08-16, P08-17 | Microsoft Graph | high | Limits vary by service, app, tenant, and request type. |
| C08-08 | GitHub Apps have granular repository/organization/account permissions, installation control, rate limits, webhooks, and Marketplace requirements. | evidence | P08-18 through P08-21 | GitHub | high | Organization owners can restrict installations; enterprise and preview features differ. |
| C08-09 | Dropbox uses OAuth scopes and App Folder/Full Dropbox access; exact general API limits are not published and 429/Retry-After must be handled. | evidence | P08-22, P08-23 | Dropbox | high | Documentation is older but current and official; exact limits remain unknown. |
| C08-10 | Shopify public apps are reviewed, APIs are rate-limited, and protected customer data requires minimized access and possible review. | evidence | P08-24 through P08-27 | Shopify | high | API versions, protected-data rules, and review requirements can change. |
| C08-11 | User-invoked, event-driven, least-privilege companions with manual fallbacks should have lower policy exposure than broad history ingestion or autonomous actions. | inference | C08-01 through C08-10 | All six hosts | high | Lower is relative, not a guarantee of approval. |
| C08-12 | Host-platform distribution will materially reduce acquisition friction for at least some candidates. | assumption | Owner: Strategy Agent | Candidate distribution | low | Impact if wrong: host-platform distribution cannot support candidate advancement. Planned review/test: revisit only in a separately authorized future channel test. Marketplace availability does not prove discoverability, conversion, or WTP. |
| C08-13 | If later authorized, at least 6 of 10 target users for a candidate will complete its host-native workflow twice in 14 days without requesting broader permissions. | hypothesis | Measure: repeated completion and permission refusal; success: at least 6/10 complete twice with no broadened scopes; kill: fewer than 3/10; 14-day time box | Future bounded test | low | No user testing or outreach is authorized or performed here. |

## Opportunity universe

| ID | Host platform and recurring problem | Authorized path | Problem claim type; feasibility support | Confidence | Principal policy/dependency risk |
|---|---|---|---|---|---|
| OPP-2026-700 | Gmail: commitments disappear in inboxes. | Gmail API OAuth and push/history | assumption; C08-01, C08-03 | medium | Mail scope may be sensitive/restricted; watch renewal and dropped events. |
| OPP-2026-701 | Gmail: selected attachments are filed inconsistently. | Gmail API OAuth; user-selected/manual fallback | assumption; C08-01, C08-03 | medium | Message/file data sensitivity and verification. |
| OPP-2026-702 | Google Calendar: agenda, decision, and follow-up context fragments. | Calendar API events/watch | assumption; C08-03 | medium | Expiring channels and non-guaranteed notifications. |
| OPP-2026-703 | Google Drive: selected-folder permission/change drift is hard to review. | Drive Changes API and authorized permissions read | assumption; C08-01 through C08-03 | medium | Scope breadth, shared-drive coverage, state reconstruction. |
| OPP-2026-704 | Slack: decisions in messages are not captured with context. | User-invoked message shortcut and modal | assumption; C08-04, C08-05 | medium-high | Scope review, 3-second acknowledgement, Marketplace approval. |
| OPP-2026-705 | Slack: structured requests arrive as incomplete free text. | Global/message shortcut, modal, workflow step | assumption; C08-05 | medium-high | User confirmation and installation approval. |
| OPP-2026-706 | Slack: handoffs age without explicit owner/action. | Events API for opted-in channels plus reminders | assumption; C08-04 | medium | History/replies limits, channel visibility, spam risk. |
| OPP-2026-707 | Teams: approval requests lack a consistent evidence packet. | Teams app with RSC or least-privilege Graph | assumption; C08-06, C08-07 | medium | Tenant/admin consent and permission classification. |
| OPP-2026-708 | Teams: channel decisions lack a durable register. | Bot/action or scoped events, human capture | assumption; C08-06, C08-07 | medium | Broad chat permissions can block adoption. |
| OPP-2026-709 | Outlook shared mailbox: service exceptions are discovered late. | Graph mail change notifications | assumption; C08-06, C08-07 | medium | Shared mailbox/application permission and admin consent. |
| OPP-2026-710 | Outlook Calendar: material changes lack a concise owner brief. | Graph event change notifications | assumption; C08-07 | medium | Subscription expiry and mailbox limits. |
| OPP-2026-711 | OneDrive/SharePoint: selected evidence folders change without approval context. | DriveItem delta/change notifications | assumption; C08-06, C08-07 | medium | Files/Sites scopes and delta semantics. |
| OPP-2026-712 | GitHub Issues: acceptance criteria are incomplete at handoff. | GitHub App, Issues metadata/write on selected repos | assumption; C08-08 | medium-high | Installation approval and write permission. |
| OPP-2026-713 | GitHub PRs: review evidence is scattered across checks and comments. | GitHub App webhooks and read permissions | assumption; C08-08 | medium-high | Rate limits, repository selection, sensitive code metadata. |
| OPP-2026-714 | GitHub Releases: readiness evidence is not packaged consistently. | GitHub App release/check metadata | assumption; C08-08 | medium | Marketplace requirements and feature overlap. |
| OPP-2026-715 | Dropbox: client file requests arrive incomplete. | OAuth App Folder or Chooser/Saver components | assumption; C08-09 | medium | Full Dropbox scope must be avoided unless necessary. |
| OPP-2026-716 | Dropbox: shared-folder permission changes lack a review digest. | OAuth scoped sharing/file metadata APIs | assumption; C08-09 | medium-low | Full-account/team access and unpublished exact limits. |
| OPP-2026-717 | Shopify: fulfillment exceptions are spread across orders and messages. | GraphQL Admin API/webhooks with approved scopes | assumption; C08-10 | medium | Protected customer data, review, version and query-cost limits. |
| OPP-2026-718 | Shopify: return/refund evidence packets are assembled manually. | Admin API/webhooks with protected-data review | assumption; C08-10 | medium | Personal/order data and no automated entitlement denial. |
| OPP-2026-719 | Shopify: catalog changes lack a lightweight approval trail. | Product webhooks/Admin API without customer fields where possible | assumption; C08-10 | medium-high | App review, API versions, rate limits; merchant remains decision maker. |

The field-complete, unranked index is [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

## Platform feasibility matrix

| Host | Official path verified | Permission/review path | Rate/change risk | Distribution path | Required fallback principle |
|---|---|---|---|---|---|
| Google Workspace | Gmail/Calendar notifications; Drive changes | OAuth verification; Marketplace app review; restricted-scope assessment where applicable | Watches/channels expire; notifications can drop; changes are not full deltas | Workspace Marketplace or domain/internal deployment | User-selected/manual import, ICS, or exported report |
| Slack | Events, shortcuts, modals, workflow extensions | OAuth scopes; Marketplace manual/security review | Method/event limits, 3-second ACK, potential disablement | Slack Marketplace or approved unlisted install | Signed web form or manual queue; never scrape history |
| Microsoft 365/Teams | Graph mail/calendar/drive, Teams app/RSC | Delegated/application consent; tenant admin policies | 429/Retry-After, subscription expiry, service limits | Teams Store/AppSource or tenant catalog | Email/link/ICS/export workflow |
| GitHub | GitHub App permissions, webhooks, REST/GraphQL | Installation/authorization; owner restrictions; Marketplace rules | API limits and permission updates | GitHub Marketplace or direct selected-repo install | Repository-native Action or generated Markdown |
| Dropbox | OAuth, App Folder/Full Dropbox, components | Scopes and app review/production status | Unpublished exact limits; 429/Retry-After | Dropbox app distribution plus independent channel | Chooser/Saver, selected-folder upload, or export |
| Shopify | Admin GraphQL, webhooks, app review | App Store review; protected customer-data request/review | Versioning, query-cost limits, possible temporary reduction | Shopify App Store or custom app | Merchant CSV/export and manual packet |

## Legal, privacy, safety, and shutdown boundaries

- Request the smallest scope and the smallest resource set; selected folder, selected repository, user-invoked message, or delegated account is preferred over tenant-wide history.
- Use event/webhook paths instead of polling when official docs recommend them; implement idempotency, expiry renewal, retries, backoff, and missed-event reconciliation.
- Encrypt tokens and user data; segregate tenants; maintain revocation, deletion, audit, and incident-response controls.
- Do not send messages or make writes without clear user initiation or confirmation.
- Do not use customer, employee, message, order, or file data for unrelated model training, advertising, surveillance, or resale.
- Every candidate must retain a manual/export fallback and a host-dependency disclosure. Host shutdown can still end automated functionality.

## Confidence assessment

Confidence in API/policy feasibility is high for the bounded paths recorded. Confidence in product opportunity attractiveness is low to medium because no demand, paid conversion, usage, or competitive-gap research was authorized. T08 therefore presents feasible candidates, not recommendations.

## Quality and lifecycle

The complete first draft scored 86/100. Corrections added official path-level verification, source dates/limits, per-candidate dependency/risk/distribution/fallback fields, claim IDs, reproducible queries, and explicit shutdown/fallback controls. The corrected creator self-score is 100/100; Governance is pending. See [QUALITY_SCORE_HISTORY.md](QUALITY_SCORE_HISTORY.md) and [CORRECTION_LOG.md](CORRECTION_LOG.md).

## Recommended next action

Request independent Governance review. Keep every candidate unranked and stop before Gate 2, due diligence, validation, product selection, PRD, or implementation.
