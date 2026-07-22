---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T04 Correction Log

| Cycle | Finding | Correction applied | Files | Result |
|---:|---|---|---|---|
| 1→2 | Source metadata was distributed and some sources were insufficiently bounded | Centralized dates, access date, geography, confidence and limitations; rejected SEO market sizes and rankings | SOURCE_REGISTER.md, SEARCH_LOG.md | Source-quality loss recovered |
| 1→2 | Candidate claims were not uniformly traceable | Added source IDs, claim type and confidence to every candidate | OPPORTUNITY_INDEX.md | 20/20 candidates traceable |
| 1→2 | Segmentation was inconsistent | Added learner segment, workflow cadence and current alternative for every row | OPPORTUNITY_INDEX.md | Coverage audit complete |
| 1→2 | WTP and retention risked unsupported interpretation | Marked WTP unknown; labeled retention as hypothesis; added evidence gaps | OPPORTUNITY_INDEX.md, EVIDENCE_GAPS.md | No invented demand or price |
| 1→2 | Educational integrity, AI accuracy, privacy, content rights and high-stakes hiring boundaries needed stronger treatment | Added per-row constraints, 12 explicit exclusions and report safety synthesis | EXCLUSIONS.md, MARKET_DISCOVERY_REPORT.md | Critical blocker resolved |
| 1→2 | Search was not fully reproducible | Logged 12 ordered searches/checks, retained sources and rejected source classes | SEARCH_LOG.md | Reproducibility score restored |
| 2→3 | GOV-T04-B001 found incomplete treatment of repeat-use statements labeled as hypotheses | Relabeled live research claims as assumptions; named Strategy Agent as owner; recorded impact if wrong and separately authorized Gate 5 review/test; preserved all unknowns and Opportunity Scores | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EVIDENCE_GAPS.md, QUALITY_SCORE_HISTORY.md | Creator correction complete; internal simulation re-review requested |
| 3→4 | Completed review candidate still declared the incomplete `draft` lifecycle state | Set all nine artifacts to `status: in-review` and version `0.2.1`; recorded the lifecycle-only correction | All nine T04 artifacts | Lifecycle metadata aligned; internal simulation re-verification requested |
| 4→5 | External Governance scored the artifact 94/100 and found broad sources did not independently support many specific rehearsal, tracking, portfolio and vocabulary workflows | Added direct learner/jobseeker/participant-derived language sources, downgraded weak mappings, added a six-class candidate coverage matrix and explicit adjacent-candidate boundaries | SOURCE_REGISTER.md, SEARCH_LOG.md, MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EVIDENCE_GAPS.md | External findings remediated; re-review requested |
| 4→5 | Prior Codex-authored reviews were labeled independent even though Codex created the artifacts | Relabeled the preserved reviews as `Internal Pre-review` / `Internal Governance Simulation`; recorded external score and point loss without deleting audit history | CORRECTION_LOG.md, QUALITY_SCORE_HISTORY.md, THREAD_SUMMARY.md | EXT-GOV-01 remediation applied; external disposition pending |

No correction changed another thread, reused an Opportunity ID, ranked candidates, selected a winner or began Gate 2.

## Internal Governance Simulation Correction Request — G1

The G1–G3 material below was produced by Codex in the creator execution context. It is retained unchanged in substance as an **Internal Pre-review**, not independent Governance evidence.

| Review | Finding | Required correction | Source artifacts to revise by Creator | Governance verification | Status |
|---|---|---|---|---|---|
| G1 | GOV-T04-B001: retention statements are called hypotheses without measure, success threshold, kill threshold, and time box; the report explicitly defers required fields. | Complete the evidence-rule hypothesis contract or relabel as properly treated assumptions/inferences. Preserve unknown demand and do not invent evidence or thresholds. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, and any dependent gap/summary wording | Re-run text scan for `hypothesis`, repository validation, tests, and internal rescore. | creator correction applied; internal simulation re-review pending |

The internal simulation did not apply this correction or rewrite any Strategy artifact.

## Internal Governance Simulation Re-review — G2

| Review | Blocker disposition | Verification | Governance score | Status |
|---|---|---|---:|---|
| G2 | GOV-T04-B001 resolved: live repeat-use claims are validly treated as assumptions with owner, impact, and planned review/test; candidate 314 and evidence-gap wording align. | Re-read all nine artifacts; `hypothesis` scan found no incomplete live claim; validator, 3 tests, whitespace, nine-file, and 20-candidate checks passed. | 100/100 | closed |

The internal simulation made no source-content correction during re-review.

## Internal Governance Simulation Lifecycle Re-verification — G3

| Review | Lifecycle correction verified | Research invariants | Score / blockers | Status |
|---|---|---|---|---|
| G3 | All nine artifacts are consistently `in-review` at `v0.2.1`; Creator Cycle 4 and correction `3→4` are recorded. | 13 sources, 20 assigned candidates, confidence, evidence ceiling, Opportunity Scores, boundaries, and gate authority unchanged. | 100/100; 0 open | closed |

The internal simulation appended audit evidence only and made no research-content edit.

## External Governance Correction Cycle 2

Authoritative review: PR #20 external review submitted 2026-07-22. Latest external Artifact Quality Score: **94/100**.

| External finding | Correction applied | Verification target | Status |
|---|---|---|---|
| `EXT-GOV-01`: Codex-authored reviews were not independent | Relabeled all preserved G1–G3 review sections and summary references as Internal Pre-review / Internal Governance Simulation | No live claim treats the internal 100/100 as an independent score | remediation applied; external re-review pending |
| Direct learner, jobseeker and language-worker evidence was too broad | Added L14 direct 2024 learner survey, L15 direct DWP claimant/workflow research and bounded L16 participant-derived language barrier evidence | Source register classification and report findings separate direct evidence from context | applied |
| Candidate/source mapping needed to distinguish broad participation/barrier evidence from specific workflows | Added a 20-row, six-class coverage matrix with explicit `None` entries | 20/20 assigned candidates appear exactly once | applied |
| Overlap across 300–302, 306–309 and 315–319 needed clarification, consolidation or replacement | Added cluster boundary/consolidation triggers; downgraded several weak candidates to low confidence | Adjacent-candidate boundary table and revised rows | applied |
| External six-point loss needed a durable register | Added the authoritative external point-loss register to QUALITY_SCORE_HISTORY.md | Loss totals equal six and score remains 94 until external re-review | applied |

External Governance re-review requested.
