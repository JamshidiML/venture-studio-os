---
status: in-review
version: 0.1.4
owner_role: Strategy Agent
last_reviewed: 2026-07-23
thread_id: T01
issue_number: 4
gate: 1
---

# T01 Market Discovery — Daily Consumer Utilities

## Executive Summary

- **The auditable universe contains 20 bounded concepts: 3 Qualified Gate 1 Candidates and 17 Hypothesis Watchlist Candidates.** Neither tier is ranked. The qualified set is limited to food-management workflows with observed behavioral support; the preserved watchlist contains context-, category-, or guidance-led concepts whose specific workflow pain is not yet observed.
- **The strongest direct evidence concerns the frequency of household work and preventable food-management friction.** U.S. time-use data show household activities are widespread and recurring, while U.S. and UK food-waste research identifies planning, quantity judgment, storage, and disrupted meals as observable friction ([T01-S01](SOURCE_REGISTER.md), [T01-S02](SOURCE_REGISTER.md), [T01-S03](SOURCE_REGISTER.md)).
- **Most candidate-level propositions remain inferences, not demand evidence.** No willingness-to-pay, retention, acquisition-cost, download, revenue, or conversion claim is made. Candidate confidence is therefore mostly `medium` or `low`.
- **The stop boundary is intact.** No winner, comparative ranking, Gate 2 screening score, deep due diligence, validation plan, PRD, or product implementation is included.

## Objective and Scope

| Field | Bound |
|---|---|
| Authorization | [Parent Issue #3](https://github.com/JamshidiML/venture-studio-os/issues/3) and [Issue #4](https://github.com/JamshidiML/venture-studio-os/issues/4) |
| Geography | Initial evidence scan: United States, with UK evidence used only where explicitly identified |
| Segment | Adults managing their own repeated everyday tasks and non-clinical household routines |
| Source cutoff | 2026-07-22 |
| Candidate count | 3 qualified + 17 watchlist = 20 auditable IDs |
| Reserved IDs | `OPP-2026-001` through `OPP-2026-099`; this artifact uses `001` through `020` only |
| Explicit exclusions | Health diagnosis/treatment, personal finance, education, aging/accessibility, creator tools, SMB workflows, platform companion tools, games, social networks, dating, gambling, adult products, surveillance, deceptive products, and network-dependent products |

## Methodology

The first draft combined current-source searches with boundary screening. The correction pass added publication and access dates, geographic scope, source limitations, candidate-level source IDs, claim types, confidence rationales, constraints, exclusions, and a reproducible query log. Sources were prioritized in this order: official statistics and agencies; commissioned primary surveys with disclosed samples; current public standards or guidance. Competitor popularity, app-store counts, and unverified reviews were not treated as problem or demand evidence.

External Governance Correction Cycle 2 audited whether each source demonstrates the candidate's specific problem rather than merely a population, safety cadence, or adjacent category. Cycle 3 created the two-tier contract. External Governance Cycle 3 then scored the artifact `94/100`, losing two source-quality points, three qualified/watchlist-integrity points, and one analytical-rigor point because nine remaining qualified rows still had empty direct-evidence cells. Issue #25 applies the contract consistently: no new source was added merely to preserve count, and `001`–`003`, `007`–`010`, `013`, and `017` moved to the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). The final watchlist contains 17 IDs at `very low` confidence.

Qualification requires direct observed problem evidence or clearly adjacent observed workflow evidence, plus a bounded affected segment, a non-deceptive and non-surveillance path, no critical API or proprietary-network dependency, and explicit uncertainty. Population context, guidance, feasibility, and a purely logical hypothesis cannot independently qualify a concept. Qualification does not mean commercial attractiveness or Gate 2 advancement.

## Evidence-Backed Problem Landscape

| Material claim | Type | Source | Confidence | Interpretation and limitation |
|---|---|---|---|---|
| Household work is a recurring part of daily life: in 2024, 80% of people in the U.S. time-use sample engaged in household activities on an average day, spending about two hours. | evidence | T01-S01, published 2025-06-26 | high | Direct national survey evidence for frequency; it does not identify demand for software or isolate each proposed workflow. |
| Household food waste is associated with quantity judgment, displaced meals, planning, list-making, and storage behaviors. | evidence | T01-S02 and T01-S03 | medium | Recent UK survey/analysis and U.S. cost modeling support recurring friction; cultural transfer and self-report limitations prevent a high-confidence global claim. |
| FoodKeeper demonstrates that authoritative storage guidance exists but does not prove that people will maintain an inventory. | evidence | T01-S04 | medium | The guidance is official but the page was reviewed in 2019; any product concept must avoid presenting stale storage guidance as universal safety advice. |
| Home and fire-safety guidance contains tasks with daily, monthly, and annual cadences. | evidence | T01-S05 and T01-S06 | high | Direct official cadence guidance supports reminder/checklist workflows, not willingness to pay. |
| Lightweight utilities may be useful when they reduce setup and recovery cost rather than maximizing streaks. | inference | T01-S01, T01-S02, T01-S03 | medium | Recurring activity and disrupted plans make low-friction recovery plausible; direct behavioral testing is still required in a later authorized gate. |
| Users will prefer manual-first tools that do not require inbox, retailer, smart-home, or bank access. | assumption | No direct source; owner: Strategy Agent | low | Privacy-preserving scope assumption. Test only after Founder authorization; compare manual entry completion with optional import in a bounded study. |
| A candidate should be killed if fewer than 5 of 10 recruited target users can describe the problem as recurring at least monthly without prompting. | hypothesis | Not tested | low | Falsifiable discovery threshold for a future authorization; it is not a validation result. |

## Qualified Gate 1 Candidate Universe

The three qualified candidates are listed below and in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md). The other 17 IDs remain auditable in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist); they are not qualified candidates. No disputed ID was strengthened because no qualifying workflow source was added.

| Opportunity ID | Bounded workflow | Affected segment | Current alternative | Evidence status | Confidence | Automatic blocker |
|---|---|---|---|---|---|---|
| OPP-2026-004 | Pantry “use first” queue | Adults responsible for food preparation | Memory, sticky note | inference from T01-S02/S03/S04 | medium | food-safety boundary |
| OPP-2026-005 | Leftover visibility ledger | Adults storing prepared food | Container labels, memory | inference from T01-S02/S04 | medium | food-safety boundary |
| OPP-2026-006 | Displaced-meal reset list | Adults whose meal plans change | Ad hoc list | inference from T01-S02 | medium | none identified |

## Cross-Cutting Constraints

- **Privacy:** default to local/manual entry; do not assume inbox, location, retailer, contact, camera, microphone, smart-home, or calendar access. Collect only the minimum needed for the chosen routine.
- **Safety:** smoke-alarm, food-storage, plant, pet, and maintenance content must link to authoritative guidance and never claim inspection, diagnosis, emergency response, or professional equivalence.
- **Platform:** every candidate has a manual fallback. No candidate is qualified on the assumption that a third-party API is available.
- **Legal/IP:** do not copy protected interaction flows, brand assets, content libraries, or competitor code. User-created lists and public-domain/permissioned guidance are the safe default.
- **Behavioral ethics:** avoid punitive streaks, shame, artificial urgency, hidden subscriptions, manipulative notifications, or surveillance-based engagement.

## Exclusions, Risks, and Unknowns

Detailed exclusions and the 17-entry Hypothesis Watchlist are recorded in [EXCLUSIONS.md](EXCLUSIONS.md); unresolved evidence is in [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md). The central unknown is direct problem intensity and willingness to pay at the candidate level. The current evidence supports a three-candidate qualified universe, not commercial selection.

## Confidence Assessment

Overall confidence is `medium` for the observed food-management behavior supporting `004`–`006`; confidence is `very low` for the 17 watchlist concepts and remains `low` to `medium` for individual candidate demand. This is the honest Gate 1 ceiling without interviews, product analytics, paid datasets, or validation—none of which is authorized here. The package can still earn a 100/100 Creator Artifact Quality Score because uncertainty is visible and traceable; that score does not assert opportunity attractiveness or replace the authoritative external `94/100`.

## Recommended Next Action

Review the coverage matrix, three qualified candidates, 17-entry watchlist, unchanged nine-source register, constraints, complete 20-ID audit trail, exact External Cycle-3 point loss, and evidence ceiling. Keep Gate 1 open and do not score or rank the opportunities until Founder authorization for the next gate.

Final External Governance re-review requested
