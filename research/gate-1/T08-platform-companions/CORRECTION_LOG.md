---
status: in-review
version: 0.2.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T08 Correction Log

| Correction ID | First-draft finding | Targeted correction | Files | Verification | Status |
|---|---|---|---|---|---|
| C-08-001 | Policy/source dates were not consistently explicit. | Added update date or “date unavailable,” access date, scope, confidence, and limitation for all sources. | SOURCE_REGISTER.md | 27 official records complete. | resolved |
| C-08-002 | API feasibility claims lacked stable source IDs. | Added C08 and P08 IDs; mapped all candidate paths. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | Every material path is traceable. | resolved |
| C-08-003 | A fallback was missing and others were vague. | Added non-private-API manual, export, component, ICS, email, CSV, or repository-native fallback per candidate. | OPPORTUNITY_INDEX.md | 20 of 20 rows include fallback. | resolved |
| C-08-004 | API availability could be mistaken for demand. | Added explicit feasibility-vs-demand distinction and opportunity-attractiveness ceiling. | Report, gaps, summary | No popularity, installs, revenue, demand, or WTP numbers claimed. | resolved |
| C-08-005 | Platform permission and review burdens were unevenly recorded. | Added scope/consent, admin, review, protected-data, and install controls. | Report, index, exclusions | Every candidate has a policy/dependency risk. | resolved |
| C-08-006 | Rate, expiry, delivery, and shutdown risks needed platform-specific treatment. | Added Gmail/Calendar watches, Slack limits/disablement, Graph throttling/subscriptions, GitHub limits, Dropbox unknown limits, Shopify costs/versions. | Report, source register, index | Six-host feasibility matrix is complete. | resolved |
| C-08-007 | Search choices were not reproducible enough for governance. | Added 13 query classes, official-domain rule, rejections, and re-check protocol. | SEARCH_LOG.md | Query-to-source paths visible. | resolved |
| C-08-008 | Lifecycle/link hygiene needed completion. | Linked all nine artifacts and set corrected package to in-review 0.2.0. | All nine files | Repository validation and tests to be recorded in THREAD_SUMMARY.md. | resolved |

No Opportunity Score was created or altered.

## Independent Governance review record

| Review | Governance score | Critical blockers | Point loss | Required correction | Status |
|---|---:|---:|---:|---|---|
| Governance Cycle 1, 2026-07-22 | 99/100 | 0 | 1 — claim-level evidence and traceability | G08-GOV-001: assign exactly one explicit claim type to every candidate problem statement, while keeping platform-feasibility evidence separate from demand status | open |
| Governance Cycle 2, 2026-07-22 | 96/100 | 1 | 4 — one traceability point and three rigor points | G08-GOV-001 explicit-type request implemented, but G08-GOV-002 opened because all 20 hypothesis labels lack measure, success threshold, kill threshold, and time box | open; creator correction required |
| Governance Cycle 3, 2026-07-22 | 100/100 | 0 | 0 | G08-GOV-002 resolved: 20/20 report and index rows use the complete shared assumption treatment; C08-12 is complete; C08-13 retains its separate full hypothesis contract | resolved; Governance complete |
| Governance Cycle 4, 2026-07-22 | 100/100 | 0 | 0 | Final lifecycle verification: all nine artifacts in-review v0.2.1; complete claim treatments preserved; checks and 20+20 candidate rows pass | resolved; Governance complete |

No source artifact was rewritten by Governance. Independent validation passed: repository validator, three unit tests, and git diff check.

## Creator response to Governance Cycle 1

| Correction ID | Governance finding | Targeted creator correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-08-009 | G08-GOV-001; one traceability point lost. | Assigned exactly one explicit problem/workflow claim type, hypothesis, to all 20 candidates in both candidate tables; preserved official feasibility sources, confidence, demand/WTP and attractiveness uncertainty. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | 20 of 20 report rows and 20 of 20 index rows carry the same single explicit type. | resolved; Governance rescore requested |

## Governance Cycle 2 correction request

| Finding | Required correction | Source artifacts for Creator | Governance verification | Status |
|---|---|---|---|---|
| G08-GOV-002 | Complete the mandatory falsification contract for each hypothesis, or use a valid assumption/inference treatment. A shared assumption protocol may cover the 20 rows if it unambiguously names the Strategy Agent owner, impact if wrong, and planned review/test. Do not manufacture thresholds or direct demand evidence. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, and any dependent summary/gap wording | Confirm exactly one valid claim type per row; rerun validator, tests, diff, nine-artifact and 20-candidate checks; independently rescore | open |

Governance did not rewrite the source research. Independent validation passed, but the critical claim-treatment blocker prevents a 100/100 Governance score.

## Governance Cycle 3 disposition

G08-GOV-002 is resolved. Independent validation passed: repository validator, three unit tests, `git diff --check`, exactly nine artifacts, exactly 20 index candidates, and exactly 20 report candidates. No critical blocker remains and the latest Governance score is 100/100. Historical lower scores and correction requests remain above as the audit trail.

Final lifecycle verification also passed at 100/100: all nine artifacts are `in-review` v0.2.1, all claim treatments remain conformant, and no blocker reopened.

## Creator response to Governance Cycle 2

| Correction ID | Governance finding | Targeted creator correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-08-010 | G08-GOV-002; all 20 candidate hypotheses lacked per-claim falsification contracts. | Relabeled all 20 candidate problem/workflow statements as assumptions and applied one unambiguous shared protocol naming the Strategy Agent owner, impact if wrong, and separately authorized future review/test. Also completed C08-12 assumption treatment. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | 20 of 20 report rows and 20 of 20 index rows carry assumption type; the shared protocol is present in both; C08-12 includes owner, impact, and planned review/test. | resolved; Governance Cycle 3 requested |
| C-08-011 | Completed review-candidate lifecycle needed a consistent post-correction patch version. | Advanced all nine artifacts from version 0.2.0 to patch version 0.2.1 while retaining in-review status. | All nine artifact front matters | All nine files are in-review at 0.2.1. | resolved |
