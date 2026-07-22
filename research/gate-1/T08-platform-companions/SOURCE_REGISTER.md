---
status: in-review
version: 0.2.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Source Register

Every source is an official platform/developer source. Access date: 2026-07-22. “Date unavailable” is deliberate when the current page did not expose a reliable publication/update date.

| ID | Official source | Publication/update date | Scope / geography | Supports | Confidence and limitation |
|---|---|---|---|---|---|
| P08-01 | [Google Workspace Marketplace — Configure OAuth](https://developers.google.com/workspace/marketplace/configure-oauth-consent-screen) | Updated 2026-06-03 | Public Workspace apps; generally global | C08-01, C08-02 | high; review applicability depends on scopes and app type. |
| P08-02 | [Google Identity — Restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification) | Updated 2026-07-18 | Google account data; exceptions listed by Google | C08-01 | high; exact scopes and assessment need re-check for final design. |
| P08-03 | [Google Workspace Marketplace program policies](https://developers.google.com/workspace/marketplace/terms/policies) | Updated 2025-08-28 | Marketplace listings | C08-02 | high; policy is dynamic and platform-controlled. |
| P08-04 | [Google Workspace user data and developer policy](https://developers.google.com/workspace/workspace-api-user-data-developer-policy) | Date unavailable | Sensitive/restricted Workspace user data | C08-01, C08-02 | high; legal applicability and exceptions vary. |
| P08-05 | [Gmail API — Configure push notifications](https://developers.google.com/workspace/gmail/api/guides/push) | 2026-06; day unavailable | Gmail API | C08-03; OPP-700, 701 | high; watch renewal, dropped-event, per-user notification constraints. |
| P08-06 | [Google Calendar API — Push notifications](https://developers.google.com/workspace/calendar/api/guides/push) | 2026-04; day unavailable | Calendar resources | C08-03; OPP-702 | high; channels expire and some notifications may drop. |
| P08-07 | [Google Drive API — Track changes](https://developers.google.com/workspace/drive/api/guides/about-changes) | Updated 2026-07-17 | User and shared-drive change logs | C08-03; OPP-703 | high; reports latest state, not property delta; multiple logs may be needed. |
| P08-08 | [Slack — Events API](https://api.slack.com/apis/connections/events-api) | Date unavailable | Slack apps/workspaces | C08-04; OPP-706 | high; events are scope/visibility bound and delivery can be disabled. |
| P08-09 | [Slack — Rate limits](https://api.slack.com/apis/rate-limits) | Current; includes change effective 2025-05-29 | Slack Web and Events APIs | C08-04; OPP-704 through 706 | high; tiers and limits are subject to change. |
| P08-10 | [Slack — Shortcuts](https://api.slack.com/interactivity/shortcuts/using) | Date unavailable | Global and message shortcuts | C08-05; OPP-704, 705 | high; shortcut and guest-user limitations apply. |
| P08-11 | [Slack Developer Docs — Marketplace distribution](https://docs.slack.dev/slack-marketplace/distributing-your-app-in-the-slack-marketplace/) | Date unavailable | Commercial Marketplace distribution | C08-05 | high; manual review and accepted app types can change. |
| P08-12 | [Slack Developer Docs — Marketplace review guide](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide/) | Date unavailable | Marketplace review | C08-05 | high; approval is discretionary and not demand evidence. |
| P08-13 | [Microsoft Teams — App permissions and consent](https://learn.microsoft.com/en-us/microsoftteams/app-permissions) | 2026-05; day unavailable | Teams/Entra/Graph permissions | C08-06; OPP-707, 708 | high; admin policy and privilege levels vary by tenant. |
| P08-14 | [Microsoft Graph — Permission best practices](https://learn.microsoft.com/en-us/graph/best-practices-graph-permission) | Updated 2024-11-07 | Teams apps using Graph | C08-06 | high; least privilege does not guarantee admin approval. |
| P08-15 | [Microsoft Graph — Throttling guidance](https://learn.microsoft.com/en-us/graph/throttling) | Date unavailable | Graph services | C08-07 | high; thresholds vary by resource/request and can change. |
| P08-16 | [Microsoft Graph — Outlook change notifications](https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview) | Date unavailable | Mail, event, contact resources | C08-07; OPP-709, 710 | high; delegated/application and shared-mailbox limits differ. |
| P08-17 | [Microsoft Graph — DriveItem delta](https://learn.microsoft.com/en-us/graph/api/driveitem-delta?view=graph-rest-1.0) | Date unavailable | OneDrive/SharePoint drives | C08-07; OPP-711 | high; latest-state and permission semantics require care. |
| P08-18 | [GitHub Docs — Choosing permissions for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app) | Date unavailable | GitHub Apps | C08-08; OPP-712 through 714 | high; endpoint permissions and approval can change. |
| P08-19 | [GitHub Docs — Limiting app access and installations](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/limiting-oauth-app-and-github-app-access-requests-and-installations) | Date unavailable | GitHub organizations | C08-08 | high; organization owners can restrict or block installs. |
| P08-20 | [GitHub Docs — Best practices for creating a GitHub App](https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app) | Date unavailable | GitHub Apps and Enterprise Cloud | C08-08 | high; recommends webhooks/least privilege; enterprise behavior differs. |
| P08-21 | [GitHub Docs — Marketplace listing requirements](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app) | Date unavailable | GitHub Marketplace | C08-08 | high; listing and paid-plan rules may change. |
| P08-22 | [Dropbox — OAuth Guide](https://developers.dropbox.com/oauth-guide) | 2020-12-07 | Dropbox API, users and teams | C08-09; OPP-715, 716 | medium-high; older but current official guide; re-check scopes before build. |
| P08-23 | [Dropbox — DBX Performance Guide](https://developers.dropbox.com/dbx-performance-guide) | 2020-12-07 | Dropbox API performance | C08-09 | medium-high; exact general limits are intentionally unpublished. |
| P08-24 | [Shopify — Protected customer data](https://shopify.dev/docs/apps/launch/protected-customer-data) | Date unavailable | Public/custom Shopify apps | C08-10; OPP-717, 718 | high; levels and review criteria can change. |
| P08-25 | [Shopify — API limits](https://shopify.dev/docs/api/usage/limits) | Date unavailable | Shopify APIs and plan tiers | C08-10; OPP-717 through 719 | high; limits and manual query costs may change. |
| P08-26 | [Shopify — App review process](https://shopify.dev/docs/apps/launch/app-store-review/review-process) | Date unavailable | Shopify App Store | C08-10 | high; review is platform-controlled. |
| P08-27 | [Shopify — App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements) | Date unavailable | Shopify public apps | C08-10 | high; secure exchange and quality requirements are dynamic. |

## Freshness and conflict controls

- Google, Slack, Microsoft, GitHub, Dropbox, and Shopify policies are changing facts; every one must be re-opened before implementation or submission.
- Dropbox’s lack of published exact rate limits is preserved as a limitation, not replaced with an estimate.
- Different Microsoft resources impose different permissions and throttles; no single Graph limit is generalized.
- Platform documentation establishes feasibility and constraints only. It does not establish popularity, installs, demand, revenue, or willingness to pay.
