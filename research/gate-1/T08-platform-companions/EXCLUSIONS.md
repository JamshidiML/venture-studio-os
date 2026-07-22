---
status: in-review
version: 0.2.1
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

