---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T07 Correction Log

| Correction ID | Cycle-1 finding | Targeted change | Files affected | Verification | Status |
|---|---|---|---|---|---|
| C-07-001 | Dynamic and vendor sources could be mistaken for equally strong evidence. | Added publication/update date or “date unavailable,” access date, geography, confidence, and source-specific limitations. | SOURCE_REGISTER.md, MARKET_DISCOVERY_REPORT.md | All 14 sources have complete metadata. | resolved |
| C-07-002 | Material claims lacked stable traceability. | Added C07 claim IDs and source IDs; mapped opportunity rows to support. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | Every material claim and candidate has a source or explicit inference. | resolved |
| C-07-003 | First-draft candidate records did not uniformly expose every Issue #10 field. | Added buyer, user, frequency, workaround, integration/fallback, sales route, WTP evidence, legal/security, and confidence. | OPPORTUNITY_INDEX.md | Exactly 20 field-complete rows. | resolved |
| C-07-004 | WTP proxies risked overstatement. | Labeled paid adjacent products as weak proxies and recorded direct WTP as absent. | All research artifacts | No price, revenue, market-size, or demand claim remains. | resolved |
| C-07-005 | Compliance and employment wedges needed stronger stop boundaries. | Added human-review, no-advice, no-decision, privacy, access, retention, and audit controls. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EXCLUSIONS.md | Each relevant candidate has explicit controls. | resolved |
| C-07-006 | Search selection was not fully reproducible. | Added 11 query runs, source priority, rejection rules, and re-check guidance. | SEARCH_LOG.md | Query-to-source path is visible. | resolved |
| C-07-007 | Uncertainty could be read as implicit readiness. | Added a 10-item evidence-gap register and explicit attractiveness ceiling. | EVIDENCE_GAPS.md, THREAD_SUMMARY.md | No ranking, winner, or Gate 2 action appears. | resolved |
| C-07-008 | Artifact links and lifecycle state needed final hygiene. | Linked all nine artifacts, set version 0.2.0 and in-review, and prepared validation. | All nine files | Repository validation and tests to be recorded in THREAD_SUMMARY.md. | resolved |

No correction changed an Opportunity Score; none was calculated.

## Internal Governance Simulation record (non-independent)

The Codex-produced records below were originally labeled “Independent Governance.” They are preserved verbatim in substance but relabeled because the same execution system created and reviewed the artifacts; they are internal pre-review history and not authoritative Governance scores.

| Review | Governance score | Critical blockers | Point loss | Required correction | Status |
|---|---:|---:|---:|---|---|
| Internal Simulation Cycle 1, 2026-07-22 | 99/100 | 0 | 1 — claim-level evidence and traceability | G07-GOV-001: assign exactly one explicit repository claim type to every candidate problem/workflow statement, preserving sources, confidence and attractiveness uncertainty | open |
| Internal Simulation Cycle 2, 2026-07-22 | 100/100 | 0 | 0 | G07-GOV-001 resolved: 20/20 report rows and 20/20 index rows then exposed one inference type with existing support and uncertainty preserved | resolved internally; superseded by external review |
| Internal Simulation Cycle 3, 2026-07-22 | 100/100 | 0 | 0 | Final lifecycle and C07-11 verification: all nine artifacts were in-review v0.2.1; complete assumption treatment; checks and 20+20 candidate rows passed | resolved internally; superseded by external review |

No source artifact was rewritten during the internal simulation. Internal validation passed: repository validator, three unit tests, and git diff check.

## Creator response to Internal Simulation Cycle 1

| Correction ID | Governance finding | Targeted creator correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-07-009 | G07-GOV-001; one traceability point lost. | Assigned exactly one explicit problem/workflow claim type, inference, to all 20 candidates in both candidate tables; preserved sources, confidence, WTP and attractiveness uncertainty. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md | 20 of 20 report rows and 20 of 20 index rows carry the same single explicit type. | resolved; Governance rescore requested |
| C-07-010 | Lifecycle consistency and C07-11 assumption treatment required final clarification. | Added C07-11 impact if wrong and advanced all nine completed review-candidate artifacts from version 0.2.0 to patch version 0.2.1 while retaining in-review status. | MARKET_DISCOVERY_REPORT.md and all nine artifact front matters | C07-11 now includes owner, impact if wrong, and planned test; all nine files are in-review at 0.2.1. | resolved |

## Internal Simulation Cycle 2 disposition

G07-GOV-001 was resolved within the internal simulation. Internal validation passed: repository validator, three unit tests, `git diff --check`, exactly nine artifacts, and exactly 20 then-current candidates. No internal blocker remained and the internal simulation score was 100/100.

Final internal lifecycle verification also passed at 100/100: all nine artifacts were `in-review` v0.2.1, C07-11 had complete assumption treatment, and no internal blocker reopened. This was not an independent external review.

## External Governance Cycle 1 — authoritative review

External review submitted on PR #18 on 2026-07-22 assigned **92/100**. This score supersedes all internal simulation scores for Governance authority.

### External point-loss register

| Dimension | Awarded | Points lost | External finding | Correction Cycle 2 disposition |
|---|---:|---:|---|---|
| Scope compliance and exclusions | 10/10 | 0 | Scope and stop boundaries were compliant. | Preserved. |
| Source quality and freshness | 17/20 | 3 | Direct workflow evidence was thin beyond payment; vendor/category sources carried too much weight. | Added S07-15 through S07-19; vendor, direct-user, contextual, and feasibility roles separated. |
| Claim-level evidence and traceability | 14/15 | 1 | Candidate-to-source coverage was not auditable by evidence role. | Added a six-axis candidate-to-source coverage matrix for all retained candidates. |
| Opportunity coverage and diversity | 13/15 | 2 | Several concepts were maintained without sufficient support. | Withdrew IDs 603, 607, 610, 611, 615, and 616; retained count changed 20 → 14. |
| Analytical rigor and uncertainty | 14/15 | 1 | Weak category support was not consistently distinguished from direct pain. | Downgraded unsupported rows and recorded exact unsupported assumptions per candidate. |
| Legal, safety, privacy, and platform | 10/10 | 0 | Boundaries were adequate. | Preserved; matrix now shows constraint-only support. |
| Reproducibility | 10/10 | 0 | Search record was adequate. | Added five current query records. |
| Hygiene | 4/5 | 1 | Prior Codex reviews were mislabeled independent and external status was absent. | Relabeled history, recorded EXT-GOV-01, bumped all artifacts to in-review v0.3.0. |
| **Total** | **92/100** | **8** | **EXT-GOV-01 opened.** | **External Governance re-review requested.** |

### External findings and creator corrections

| Correction ID | External finding | Targeted correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-07-011 | EXT-GOV-01: no independent external Governance re-review exists for the corrected package. | Recorded the external 92/100 as authoritative and kept the blocker open. | QUALITY_SCORE_HISTORY.md, EVIDENCE_GAPS.md, THREAD_SUMMARY.md | No internal score is presented as external. | open; external re-review requested |
| C-07-012 | Candidate-source coverage did not distinguish independent direct support. | Added the required direct/context/alternative/feasibility/legal/unsupported matrix. | MARKET_DISCOVERY_REPORT.md | Every retained candidate has all six evidence-role cells. | resolved for creator cycle |
| C-07-014 | Direct workflow evidence was weak for scheduling/cancellations, quote-to-job, field photos, inventory/reorder, promises, and warranty. | Added verifiable direct survey/user/editorial evidence with publication/access dates; narrowed scheduling; withdrew unsupported promise/warranty and other concepts; downgraded inventory/reorder assumptions. | SOURCE_REGISTER.md, SEARCH_LOG.md, MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EXCLUSIONS.md | Sources S07-15 through S07-19; retained count 14. | resolved for creator cycle |
| C-07-015 | Vendor features were not sufficiently separated from independent problem/WTP evidence. | Labeled vendor pages as current-alternative evidence only and direct user/research sources separately; no direct WTP inferred. | All evidence artifacts | Coverage matrix and source limits expose role and ceiling. | resolved for creator cycle |
| C-07-016 | External eight-point loss and every finding had to be logged. | Added this complete point-loss register and correction table. | CORRECTION_LOG.md, QUALITY_SCORE_HISTORY.md | Eight lost points reconcile to 92/100. | resolved |
| C-07-017 | Prior Codex “Independent Governance” labels were invalid. | Relabeled prior sections as Internal Governance Simulation/Internal Pre-review without deleting scores or findings. | CORRECTION_LOG.md, QUALITY_SCORE_HISTORY.md, THREAD_SUMMARY.md | Audit history remains present and non-authoritative. | resolved |
| C-07-018 | Lifecycle/version/external status needed consistent correction. | Bumped all nine artifacts to version 0.3.0, retained `status: in-review`, and added EXT-GOV-01. | All nine artifacts | 9/9 lifecycle headers match. | resolved |

## External Governance Cycle 2 re-review and Correction Cycle 3

External Governance re-reviewed PR #18 on 2026-07-22 and assigned **95/100** with dimensions **10, 19, 15, 13, 13, 10, 10, 5**. It externally resolved **EXT-GOV-01** and verified the Cycle-2 source, withdrawal, matrix, and CI corrections. The remaining completion finding was **EXT2-T07-01**: candidates 609, 612–614, and 617–619 were still guidance/category-led rather than supported by direct or clearly adjacent observed SMB workflows.

| Correction ID | Cycle-2 external finding | Targeted Cycle-3 correction | Files changed | Verification | Status |
|---|---|---|---|---|---|
| C-07-019 | EXT-GOV-01 required external disposition. | Recorded the external 95/100 re-review and its explicit closure of EXT-GOV-01. | QUALITY_SCORE_HISTORY.md, CORRECTION_LOG.md, EVIDENCE_GAPS.md, THREAD_SUMMARY.md | No internal score is presented as external; 95/100 remains authoritative. | externally resolved |
| C-07-020 | EXT2-T07-01 found seven guidance/category-led candidates in the retained set. | Kept 600, 601, 602, 604, 605, 606, and 608 qualified; moved 609, 612–614, and 617–619 to the Hypothesis Watchlist. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EXCLUSIONS.md, EVIDENCE_GAPS.md | Qualified 7 + watchlist 7 = prior auditable universe 14; prior withdrawals remain separate. | creator-resolved; external Cycle-3 confirmation pending |
| C-07-021 | Watchlist movement must not erase candidate contracts or safety/sales analysis. | Preserved each watchlist ID, concept, buyer/user, frequency/workaround, evidence, integration/fallback, sales route/WTP, legal/security/safety constraints, confidence, evidence gap, reconsideration conditions, and T07 ownership. | EXCLUSIONS.md | Seven complete Issue #10 contract rows and seven qualification-gap rows are present. | resolved for creator cycle |
| C-07-022 | Coverage and lifecycle must match the final split. | Added Cycle-3 status to all 14 matrix rows; updated all counts; advanced all nine artifacts to in-review version 0.4.0. | All nine artifacts | Matrix, lifecycle, assigned-range, uniqueness, validator, tests, and diff checks prepared for final verification. | resolved for creator cycle |

No source was added, removed, or replaced in Cycle 3. No Opportunity Score was created or altered.

External Governance Cycle 3 re-review requested
