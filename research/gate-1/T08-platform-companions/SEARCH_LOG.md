---
status: in-review
version: 0.2.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Search Log

## Protocol

- Run/access date: 2026-07-22.
- Domain restriction: official developer/documentation domains only for feasibility and policy claims.
- Required checks: API/component path, permissions/scopes, app review/distribution, rate/change behavior, platform-control risk, and fallback.
- Rejected: private APIs, scraping guides, credential workarounds, growth hacks, user-count summaries, unsourced API-limit tables, and third-party policy interpretations.

## Query log

| Run | Query | Purpose | Official results used | Limitation/rejection |
|---:|---|---|---|---|
| 1 | site:developers.google.com/workspace marketplace oauth verification restricted scopes official | Verify Google review and scope path | P08-01 through P08-04 | No Google usage/popularity figures collected. |
| 2 | site:developers.google.com/workspace/gmail/api/guides push notifications official | Verify Gmail event route and limits | P08-05 | No mailbox scraping or private interface considered. |
| 3 | site:developers.google.com/workspace/calendar/api/guides push notifications official | Verify Calendar route and delivery limits | P08-06 | Dropped notifications/expiry retained as risks. |
| 4 | site:developers.google.com/workspace/drive/api/guides manage changes official | Verify Drive change-log route | P08-07 | Change log is not treated as a complete revision diff. |
| 5 | site:api.slack.com rate limits events scopes official 2025 | Verify Slack event and limit path | P08-08, P08-09 | Newly changed Marketplace distinction retained. |
| 6 | site:api.slack.com interactivity shortcuts modals official Slack | Verify user-invoked interaction | P08-10 | Confirmation and acknowledgement constraints retained. |
| 7 | site:docs.slack.dev marketplace review distribution official | Verify distribution/review | P08-11, P08-12 | Approval is not treated as demand. |
| 8 | site:learn.microsoft.com graph permissions throttling Teams official | Verify permissions/admin/rate path | P08-13 through P08-15 | No single throttle generalized across services. |
| 9 | site:learn.microsoft.com graph Outlook mail calendar change notifications official | Verify Outlook event routes | P08-16 | Shared-mailbox permission caveat retained. |
| 10 | site:learn.microsoft.com graph OneDrive driveitem delta official | Verify OneDrive/SharePoint path | P08-17 | Delta latest-state semantics retained. |
| 11 | site:docs.github.com apps permissions rate limits marketplace official | Verify GitHub route and distribution | P08-18 through P08-21 | OAuth app path deprioritized in favor of granular GitHub Apps. |
| 12 | site:developers.dropbox.com oauth scopes rate limits app review official | Verify Dropbox scope/limit path | P08-22, P08-23 | Exact limits unavailable; no estimate substituted. |
| 13 | site:shopify.dev app review protected customer data rate limits official | Verify Shopify review/data/limit path | P08-24 through P08-27 | No store counts, revenue, or demand figures collected. |

## Reproduction guidance

Open each canonical URL in [SOURCE_REGISTER.md](SOURCE_REGISTER.md), confirm the page is still current, then compare the candidate’s stated path and risk in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md). A future implementation review must verify the exact endpoints, scopes, API version, app type, tenant/account type, plan, review status, and terms on that future date.
