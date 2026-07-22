---
status: in-review
version: 0.4.0
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

## Internal Governance Simulation record (non-independent)

The Codex-produced records below were originally labeled “Independent Governance.” They are preserved verbatim in substance but relabeled because the same execution system created and reviewed the artifacts; they are internal pre-review history and not authoritative Governance scores.

| Review | Governance score | Critical blockers | Point loss | Required correction | Status |
|---|---:|---:|---:|---|---|
| Internal Simulation Cycle 1, 2026-07-22 | 99/100 | 0 | 1 — claim-level evidence and traceability | G08-GOV-001: assign exactly one explicit claim type to every candidate problem statement, while keeping platform-feasibility evidence separate from demand status | open |
| Internal Simulation Cycle 2, 2026-07-22 | 96/100 | 1 | 4 — one traceability point and three rigor points | G08-GOV-001 explicit-type request implemented, but G08-GOV-002 opened because all 20 hypothesis labels lack measure, success threshold, kill threshold, and time box | open; creator correction required |
| Internal Simulation Cycle 3, 2026-07-22 | 100/100 | 0 | 0 | G08-GOV-002 resolved: 20/20 then-current report and index rows used the complete shared assumption treatment; C08-12 was complete; C08-13 retained its separate full hypothesis contract | resolved internally; superseded by external review |
| Internal Simulation Cycle 4, 2026-07-22 | 100/100 | 0 | 0 | Final lifecycle verification: all nine artifacts were in-review v0.2.1; complete claim treatments preserved; checks and 20+20 candidate rows passed | resolved internally; superseded by external review |

No source artifact was rewritten during the internal simulation. Internal validation passed: repository validator, three unit tests, and git diff check.

## Creator response to Internal Simulation Cycle 1

| Correction ID | Governance finding | Targeted creator correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-08-009 | G08-GOV-001; one traceability point lost. | Assigned exactly one explicit problem/workflow claim type, hypothesis, to all 20 candidates in both candidate tables; preserved official feasibility sources, confidence, demand/WTP and attractiveness uncertainty. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | 20 of 20 report rows and 20 of 20 index rows carry the same single explicit type. | resolved; Governance rescore requested |

## Internal Simulation Cycle 2 correction request

| Finding | Required correction | Source artifacts for Creator | Governance verification | Status |
|---|---|---|---|---|
| G08-GOV-002 | Complete the mandatory falsification contract for each hypothesis, or use a valid assumption/inference treatment. A shared assumption protocol may cover the 20 rows if it unambiguously names the Strategy Agent owner, impact if wrong, and planned review/test. Do not manufacture thresholds or direct demand evidence. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, and any dependent summary/gap wording | Confirm exactly one valid claim type per row; rerun validator, tests, diff, nine-artifact and 20-candidate checks; independently rescore | open |

The internal simulation did not rewrite the source research. Internal validation passed, but the internal claim-treatment blocker prevented a 100/100 simulation score.

## Internal Simulation Cycle 3 disposition

G08-GOV-002 was resolved within the internal simulation. Internal validation passed: repository validator, three unit tests, `git diff --check`, exactly nine artifacts, exactly 20 then-current index candidates, and exactly 20 then-current report candidates. No internal blocker remained and the internal simulation score was 100/100. Historical lower scores and correction requests remain above as the audit trail.

Final internal lifecycle verification also passed at 100/100: all nine artifacts were `in-review` v0.2.1, all claim treatments remained conformant, and no internal blocker reopened. This was not an independent external review.

## Creator response to Internal Simulation Cycle 2

| Correction ID | Governance finding | Targeted creator correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-08-010 | G08-GOV-002; all 20 candidate hypotheses lacked per-claim falsification contracts. | Relabeled all 20 candidate problem/workflow statements as assumptions and applied one unambiguous shared protocol naming the Strategy Agent owner, impact if wrong, and separately authorized future review/test. Also completed C08-12 assumption treatment. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | 20 of 20 report rows and 20 of 20 index rows carry assumption type; the shared protocol is present in both; C08-12 includes owner, impact, and planned review/test. | resolved; Governance Cycle 3 requested |
| C-08-011 | Completed review-candidate lifecycle needed a consistent post-correction patch version. | Advanced all nine artifacts from version 0.2.0 to patch version 0.2.1 while retaining in-review status. | All nine artifact front matters | All nine files are in-review at 0.2.1. | resolved |

## External Governance Cycle 1 — authoritative review

External review submitted on PR #19 on 2026-07-22 assigned **84/100**. This score supersedes all internal simulation scores for Governance authority and opened **EXT-GOV-01** plus **T08-EXT-B02**.

### External point-loss register

| Dimension | Awarded | Points lost | External finding | Correction Cycle 2 disposition |
|---|---:|---:|---|---|
| Scope compliance and exclusions | 10/10 | 0 | Scope and stop boundaries were compliant. | Preserved. |
| Source quality and freshness | 15/20 | 5 | Nearly all sources were API/policy pages rather than user-problem evidence. | Added W08-28 through W08-36 across all six hosts; feasibility sources remain separately labeled. |
| Claim-level evidence and traceability | 12/15 | 3 | Problem support and technical feasibility were conflated. | Added a per-candidate two-axis matrix with separate problem and feasibility columns. |
| Opportunity coverage and diversity | 12/15 | 3 | Concepts lacked segment, observable friction, and evidence-backed alternatives; arbitrary count was preserved. | Withdrew nine API-only concepts; 20 → 11; added segment/friction/alternative mapping. |
| Analytical rigor and uncertainty | 11/15 | 4 | API availability carried too much opportunity weight and evidence ceiling was understated. | Downgraded five retained rows to assumptions, isolated OPP-711 as direct-evidence absent, and retained both external blockers pending re-review. |
| Legal, safety, privacy, and platform | 10/10 | 0 | Platform controls were strong. | Preserved and separated as constraint evidence. |
| Reproducibility | 10/10 | 0 | Search record was adequate for feasibility. | Added nine reproducible problem-evidence searches. |
| Hygiene | 4/5 | 1 | Prior Codex reviews were mislabeled independent and external status was absent. | Relabeled history, recorded external blockers, bumped all artifacts to in-review v0.3.0. |
| **Total** | **84/100** | **16** | **EXT-GOV-01 and T08-EXT-B02 opened.** | **External Governance re-review requested.** |

### External findings and creator corrections

| Correction ID | External finding | Targeted correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-08-012 | EXT-GOV-01: no independent external Governance re-review exists for version 0.3.0. | Recorded authoritative external 84/100 and kept the blocker open. | QUALITY_SCORE_HISTORY.md, EVIDENCE_GAPS.md, THREAD_SUMMARY.md | No internal score is presented as external. | open; external re-review requested |
| C-08-013 | T08-EXT-B02: nearly all original sources were API/policy pages rather than user problems. | Added nine independent/direct-user problem sources covering all six hosts; kept bounded limitations explicit. | SOURCE_REGISTER.md, SEARCH_LOG.md, MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | W08-28 through W08-36 present; source roles explicit. | open pending external determination |
| C-08-014 | Each host needed independent problem/workflow evidence or unsupported concepts had to be downgraded/removed. | Removed IDs 700, 701, 702, 705, 707, 709, 710, 711, 714; downgraded 703, 704, 706, 708; supported the remaining inferences with W08 sources. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EXCLUSIONS.md, EVIDENCE_GAPS.md | Candidate count 20 → 11; six hosts remain represented. | resolved for creator cycle |
| C-08-015 | Problem evidence and technical feasibility required a two-axis map. | Added a candidate matrix with separate direct-problem and technical-feasibility fields plus context and constraint roles. | MARKET_DISCOVERY_REPORT.md | 11/11 retained candidates mapped; API docs never appear in the direct-problem column. | resolved |
| C-08-016 | Every candidate needed alternatives, observable friction, and user segments. | Added all three fields to the coverage matrix; rewrote retained rows to match the cited friction. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | 11/11 rows expose segment, friction, and alternative. | resolved |
| C-08-017 | Candidate count had to be reassessed rather than preserved at 20. | Withdrew nine concepts and preserved their IDs/reasons in exclusions. | EXCLUSIONS.md, MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, THREAD_SUMMARY.md | Before 20; after 11; no ID reuse. | resolved |
| C-08-018 | External 16-point loss and both blockers had to be logged. | Added complete point-loss register; EXT-GOV-01 and T08-EXT-B02 remain open. | CORRECTION_LOG.md, QUALITY_SCORE_HISTORY.md, EVIDENCE_GAPS.md | Lost points reconcile to 84/100. | resolved |
| C-08-019 | Prior Codex “Independent Governance” labels were invalid. | Relabeled prior sections as Internal Governance Simulation/Internal Pre-review without deleting scores or findings. | CORRECTION_LOG.md, QUALITY_SCORE_HISTORY.md, THREAD_SUMMARY.md | Audit history remains present and non-authoritative. | resolved |
| C-08-020 | Lifecycle/version/external status needed consistent correction. | Bumped all nine artifacts to version 0.3.0, retained `status: in-review`, and added external blockers. | All nine artifacts | 9/9 lifecycle headers match. | resolved |

## External Governance Cycle 2 re-review and Correction Cycle 3

External Governance re-reviewed PR #19 on 2026-07-22 and assigned **97/100** with dimensions **10, 19, 15, 14, 14, 10, 10, 5**. It externally resolved **EXT-GOV-01** and **T08-EXT-B02**, verifying the Cycle-2 problem-evidence model, withdrawals, two-axis matrix, and CI. The remaining completion finding was **EXT2-T08-01**: candidates 703, 704, 706, and 708 still inferred exact Drive/Slack/Teams jobs from broad friction, and Shopify evidence remained single-case.

| Correction ID | Cycle-2 external finding | Targeted Cycle-3 correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-08-021 | EXT-GOV-01 and T08-EXT-B02 required external disposition. | Recorded the external 97/100 re-review and explicit closure of both blockers. | QUALITY_SCORE_HISTORY.md, CORRECTION_LOG.md, EVIDENCE_GAPS.md, THREAD_SUMMARY.md | No internal score is presented as external; 97/100 remains authoritative. | externally resolved |
| C-08-022 | EXT2-T08-01 found four assumption-led candidates in the retained set. | Kept 712, 713, 715, 716, 717, 718, and 719 qualified; moved 703, 704, 706, and 708 to the Hypothesis Watchlist. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EXCLUSIONS.md, EVIDENCE_GAPS.md | Qualified 7 + watchlist 4 = prior auditable universe 11; prior withdrawals remain separate. | creator-resolved; external Cycle-3 confirmation pending |
| C-08-023 | Shopify evidence was direct but single-case. | Stated in the report, matrix, summary, and gaps that W08-34–W08-36 establish investigability only, not prevalence, demand, or WTP. | MARKET_DISCOVERY_REPORT.md, EVIDENCE_GAPS.md, THREAD_SUMMARY.md | All three Shopify matrix rows carry the explicit single-case limit. | resolved for creator cycle |
| C-08-024 | Watchlist movement must retain the two-axis platform contract. | Preserved each watchlist ID, concept, exact evidence searched, API feasibility, current alternative, permissions/policy/distribution/shutdown risk, fallback, confidence, missing evidence, reconsideration conditions, and T08 ownership. | EXCLUSIONS.md | Four complete Issue #11 contract rows and four qualification-gap rows are present. | resolved for creator cycle |
| C-08-025 | Coverage and lifecycle must match the final split. | Added Cycle-3 status to all 11 matrix rows; updated all counts; advanced all nine artifacts to in-review version 0.4.0. | All nine artifacts | Matrix, lifecycle, assigned-range, uniqueness, validator, tests, and diff checks prepared for final verification. | resolved for creator cycle |

No source was added, removed, or replaced in Cycle 3. No Opportunity Score was created or altered.

External Governance Cycle 3 re-review requested
