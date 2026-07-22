---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Gate 1 Market Discovery — Companion Tools for Dominant Platforms

## Executive summary

This report documents 11 unranked companion-tool candidates across Google Workspace, Slack, Microsoft 365/Teams, GitHub, Dropbox, and Shopify. External Governance Correction Cycle 2 removed nine concepts whose only support was API or policy documentation. Every retained candidate has an official, documented integration route, a bounded problem-evidence record, and an explicit fallback that does not rely on scraping, credentials, private APIs, spam, surveillance, or circumvention.

Feasibility is conditional. Google may require OAuth verification and, for server-side restricted-scope data, an annual independent security assessment. Slack ties events to OAuth scopes, applies method-specific limits, and manually reviews Marketplace submissions. Microsoft Graph requires least-privilege consent and can throttle requests; tenant administrators may control installation. GitHub Apps expose granular permissions and Marketplace rules. Dropbox uses OAuth scopes, does not publish exact general rate limits, and recommends least access. Shopify reviews apps, rate-limits APIs, and separately reviews protected customer data.

Official API availability proves an authorized path, not customer demand, popularity, or commercial attractiveness. No platform usage, install, revenue, download, or WTP figures are claimed. No winner is selected and Gate 2 has not begun.

## Objective and scope

- Authorization: Parent [Issue #3](https://github.com/JamshidiML/venture-studio-os/issues/3) and child [Issue #11](https://github.com/JamshidiML/venture-studio-os/issues/11).
- Gate: 1 — market discovery only.
- Scope: companion tools that extend messaging, email, calendar, cloud-storage, commerce, and collaboration workflows without replacing the host.
- Geography: platform documentation is generally global; tenant, plan, app type, account type, national cloud, and local-law limitations are recorded.
- Source cutoff and access date: 2026-07-22.
- Candidate count: 11 retained candidates within OPP-2026-700 through OPP-2026-719; nine withdrawn concepts are preserved in [EXCLUSIONS.md](EXCLUSIONS.md).
- Exclusions: see [EXCLUSIONS.md](EXCLUSIONS.md).

## Methodology

Official developer documentation and platform policies are used only for API, permission, review, distribution, rate-limit, and shutdown-risk claims. Independent research, moderated user reviews, and platform-hosted first-person workflow reports are separately used for problem evidence. Dynamic pages record access date; missing page dates are marked “date unavailable.” Each retained candidate qualified only when it had:

1. a host-specific user workflow and at least bounded direct or observable-friction evidence;
2. a current official API, component, webhook, action, or app route;
3. least-privilege and review/consent implications stated;
4. dependency and policy risk stated;
5. an official or independent distribution route stated;
6. a non-private-API fallback;
7. no prohibited scraping, spam, credential handling, surveillance, or platform replacement.

Full source records are in [SOURCE_REGISTER.md](SOURCE_REGISTER.md), queries in [SEARCH_LOG.md](SEARCH_LOG.md), and candidate-level integration records in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

Each candidate problem/workflow statement below has exactly one type. Inferences cite direct or observable-friction evidence plus explicit limits. Assumptions (OPP-2026-703, 704, 706, and 708) are owned by the Strategy Agent; impact if wrong: the affected candidate cannot advance regardless of API feasibility; planned review/test: revisit only through separately authorized future research or validation. No such work is authorized in Gate 1.

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
| C08-14 | Current Google Workspace user reviews include direct reports that settings and permissions can be confusing, especially across teams or external users. | evidence | W08-28 | Self-selected Workspace reviewers | medium | Supports permission-management friction only; not Gmail commitment, attachment-filing, or Calendar-context problems. |
| C08-15 | Current Slack user reviews directly report notification overload, buried important messages, and difficulty finding prior conversations. | evidence | W08-29 | Self-selected Slack reviewers | medium | Does not isolate decision capture or handoff aging, and cannot establish prevalence. |
| C08-16 | Current Teams user reviews directly report channel/notification overload and interface clutter. | evidence | W08-30 | Self-selected Teams reviewers | medium | Does not establish approval-packet, mailbox-exception, calendar-change, or folder-approval pain. |
| C08-17 | An independent 2024 study identified self-admitted miscommunications in GitHub issue discussions. | evidence | W08-31 | Public open-source GitHub issues | high | Public-project evidence may not generalize to private teams; no WTP claim. |
| C08-18 | An empirical study of five GitHub projects found review/revision practices and avoidable repeated PR revisions. | evidence | W08-32 | Public GitHub pull requests | high | Older/public-project sample; does not prove evidence-bundle demand. |
| C08-19 | Current Dropbox user reviews directly report external-sharing difficulty, slow sync, conflicting copies, and organization/version-history limits. | evidence | W08-33 | Self-selected Dropbox reviewers | medium | Supports observable friction, not prevalence or a specific companion's WTP. |
| C08-20 | A Shopify merchant described needing to identify partially fulfilled orders and repeatedly communicate out-of-stock timing. | evidence | W08-34 | One merchant report | low-medium | Single platform-hosted account; no prevalence claim. |
| C08-21 | Shopify merchant discussion and a platform response document returns/reporting timing friction and a workflow change. | evidence | W08-35 | Shopify returns workflow | low-medium | Qualitative and platform-hosted; not direct WTP evidence. |
| C08-22 | A Shopify Plus user requested an audit-ready report for product, price, SKU, subscription, and reporting-logic changes that native logs did not provide. | evidence | W08-36 | One Shopify Plus organization | low-medium | Enterprise/Plus compliance case; may not apply to SMB merchants. |

## Opportunity universe

| ID | Host platform and recurring problem | Authorized path | Problem claim type; feasibility support | Confidence | Principal policy/dependency risk |
|---|---|---|---|---|---|
| OPP-2026-703 | Google Drive: selected-folder permission/change drift is hard to review. | Drive Changes API and authorized permissions read | assumption; problem C08-14; feasibility C08-01 through C08-03 | medium-low | Scope breadth, shared-drive coverage, state reconstruction. |
| OPP-2026-704 | Slack: important decisions can be buried in message flow and need user-invoked capture. | User-invoked message shortcut and modal | assumption; problem C08-15; feasibility C08-04, C08-05 | medium | Scope review, 3-second acknowledgement, Marketplace approval. |
| OPP-2026-706 | Slack: important handoff messages can be buried or missed amid notification overload. | Events API for opted-in channels plus reminders | assumption; problem C08-15; feasibility C08-04 | medium-low | History/replies limits, channel visibility, spam risk. |
| OPP-2026-708 | Teams: channel decisions can be difficult to retrieve amid channel/notification overload. | Bot/action or scoped events, human capture | assumption; problem C08-16; feasibility C08-06, C08-07 | low-medium | Broad chat permissions can block adoption. |
| OPP-2026-712 | GitHub Issues: miscommunication can make acceptance criteria incomplete at handoff. | GitHub App, Issues metadata/write on selected repos | inference; problem C08-17; feasibility C08-08 | medium-high | Installation approval and write permission. |
| OPP-2026-713 | GitHub PRs: repeated revisions and review context need a linked evidence bundle. | GitHub App webhooks and read permissions | inference; problem C08-18; feasibility C08-08 | medium-high | Rate limits, repository selection, sensitive code metadata. |
| OPP-2026-715 | Dropbox: client/external file collection can be slowed by sharing and synchronization friction. | OAuth App Folder or Chooser/Saver components | inference; problem C08-19; feasibility C08-09 | medium-low | Full Dropbox scope must be avoided unless necessary. |
| OPP-2026-716 | Dropbox: conflicting copies and version/organization limits need a selected-folder review digest. | OAuth scoped sharing/file metadata APIs | inference; problem C08-19; feasibility C08-09 | medium-low | Full-account/team access and unpublished exact limits. |
| OPP-2026-717 | Shopify: partially fulfilled/out-of-stock orders require repeated exception identification and customer communication. | GraphQL Admin API/webhooks with approved scopes | inference; problem C08-20; feasibility C08-10 | medium-low | Protected customer data, review, version and query-cost limits. |
| OPP-2026-718 | Shopify: returns/reporting state changes require human evidence and reconciliation. | Admin API/webhooks with protected-data review | inference; problem C08-21; feasibility C08-10 | medium-low | Personal/order data and no automated entitlement denial. |
| OPP-2026-719 | Shopify: product/catalog changes lack a sufficiently detailed audit trail for some regulated workflows. | Product webhooks/Admin API without customer fields where possible | inference; problem C08-22; feasibility C08-10 | medium | App review, API versions, rate limits; actor attribution may remain unavailable. |

The field-complete, unranked index is [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

## Candidate-to-source coverage matrix

`—` means no qualifying evidence was found. Problem evidence and technical feasibility are separate axes; API documentation never counts as user pain.

| Candidate | User segment / observable friction | Direct problem evidence | Context / population evidence | Current alternative evidence | Technical feasibility evidence | Legal / privacy / safety / platform evidence | Unsupported assumption / hypothesis |
|---|---|---|---|---|---|---|---|
| OPP-2026-703 | Workspace admins; confusing permissions/settings | W08-28 | — | Native Admin/Drive controls in W08-28 | P08-01 to P08-03, P08-07 | P08-02 to P08-04 | Permission drift prevalence, review frequency, WTP |
| OPP-2026-704 | Slack team members; important messages buried | W08-29 | — | Slack search/saved messages in W08-29 | P08-08 to P08-12 | P08-09 to P08-12 | Decision-specific incidence, capture adoption, WTP |
| OPP-2026-706 | Slack ops teams; overload/missed messages | W08-29 | — | Notifications/search in W08-29 | P08-08, P08-09, P08-11 | P08-08, P08-09 | Handoff-aging incidence, reminder benefit, WTP |
| OPP-2026-708 | Teams users; channel/notification overload | W08-30 | — | Native channels/search in W08-30 | P08-13 to P08-15 | P08-13 to P08-15 | Decision-registry need, frequency, WTP |
| OPP-2026-712 | GitHub issue authors/maintainers; miscommunication | W08-31 | Public OSS sample W08-31 | Issue templates/forms are observable host alternatives | P08-18 to P08-21 | P08-18 to P08-21 | Acceptance-checklist effectiveness, private-team transfer, WTP |
| OPP-2026-713 | GitHub reviewers/authors; repeated revisions | W08-32 | Public OSS sample W08-32 | Native checks/comments/reviews | P08-18 to P08-21 | P08-18 to P08-21 | Evidence-bundle benefit and WTP |
| OPP-2026-715 | Dropbox teams/external collaborators; sharing/sync friction | W08-33 | — | Dropbox sharing and manual checklist W08-33 | P08-22, P08-23 | P08-22, P08-23 | Missing-file incidence, benefit, WTP |
| OPP-2026-716 | Dropbox team file owners; sync conflicts/version limits | W08-33 | — | Native version/history/organization W08-33 | P08-22, P08-23 | P08-22, P08-23 | Digest adoption, frequency, WTP |
| OPP-2026-717 | Shopify merchant operations; partial-fulfillment communication | W08-34 | Single merchant only | Flow/tags/export described in W08-34 | P08-24 to P08-27 | P08-24 to P08-27 | Prevalence, paid gap, WTP |
| OPP-2026-718 | Shopify returns/reporting teams; state reconciliation | W08-35 | Single discussion only | Native returns/reporting workflow W08-35 | P08-24 to P08-27 | P08-24 to P08-27 | Prevalence, packet benefit, WTP |
| OPP-2026-719 | Shopify Plus compliance/catalog teams; audit-detail gap | W08-36 | Single enterprise case only | Admin activity/API workarounds W08-36 | P08-25 to P08-27 | P08-24, P08-26, P08-27 | SMB transfer, actor attribution feasibility, WTP |

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

Confidence in API/policy feasibility is high for the bounded paths recorded. Problem evidence ranges from high-quality empirical GitHub research to low-confidence single Shopify cases. Confidence in product opportunity attractiveness is low because no direct WTP, paid conversion, or representative prevalence research was authorized. T08 therefore presents bounded candidates, not recommendations.

## Quality and lifecycle

The complete first draft scored 86/100. Earlier Codex review sections are now correctly labeled Internal Governance Simulation. External Governance Cycle 1 assigned the authoritative 84/100 and opened EXT-GOV-01 plus T08-EXT-B02. Correction Cycle 2 adds nine workflow-evidence sources, removes nine API-only concepts, and creates a two-axis problem/feasibility coverage record. The new creator execution score is 100/100; no new independent Governance score is claimed. See [QUALITY_SCORE_HISTORY.md](QUALITY_SCORE_HISTORY.md) and [CORRECTION_LOG.md](CORRECTION_LOG.md).

## Recommended next action

External Governance re-review requested. Keep every candidate unranked and stop before Gate 2, due diligence, validation, product selection, PRD, or implementation.
