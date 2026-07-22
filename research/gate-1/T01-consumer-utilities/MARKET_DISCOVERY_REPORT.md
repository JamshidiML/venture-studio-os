---
status: in-review
version: 0.1.3
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T01
issue_number: 4
gate: 1
---

# T01 Market Discovery — Daily Consumer Utilities

## Executive Summary

- **The auditable universe contains 20 bounded concepts: 12 Qualified Gate 1 Candidates and 8 Hypothesis Watchlist Candidates.** Neither tier is ranked. The qualified set covers recurring home upkeep, food-use routines, personal organization, and errands; the preserved watchlist contains concepts whose specific workflow pain is not yet observed.
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
| Candidate count | 12 qualified + 8 watchlist = 20 auditable IDs |
| Reserved IDs | `OPP-2026-001` through `OPP-2026-099`; this artifact uses `001` through `020` only |
| Explicit exclusions | Health diagnosis/treatment, personal finance, education, aging/accessibility, creator tools, SMB workflows, platform companion tools, games, social networks, dating, gambling, adult products, surveillance, deceptive products, and network-dependent products |

## Methodology

The first draft combined current-source searches with boundary screening. The correction pass added publication and access dates, geographic scope, source limitations, candidate-level source IDs, claim types, confidence rationales, constraints, exclusions, and a reproducible query log. Sources were prioritized in this order: official statistics and agencies; commissioned primary surveys with disclosed samples; current public standards or guidance. Competitor popularity, app-store counts, and unverified reviews were not treated as problem or demand evidence.

External Governance Correction Cycle 2 audited whether each source demonstrates the candidate's specific problem rather than merely a population, safety cadence, or adjacent category. Cycle 3 applies the resulting two-tier contract. No new source was added merely to increase source count. Eight weak candidates (`011`, `012`, `014`–`016`, `018`–`020`) moved to the full [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist) at `very low` confidence and may not be promoted without direct problem evidence.

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

The 12 qualified candidates are listed below and in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md). The other eight IDs remain auditable in the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist); they are not qualified candidates.

| Opportunity ID | Bounded workflow | Affected segment | Current alternative | Evidence status | Confidence | Automatic blocker |
|---|---|---|---|---|---|---|
| OPP-2026-001 | Recurring home-maintenance cadence | Renters/homeowners managing routine checks | Calendar, paper checklist | inference from T01-S01/S05 | medium | none identified |
| OPP-2026-002 | Smoke-alarm test record | Residents responsible for alarms | Calendar reminder, handwritten date | inference from T01-S06 | medium | safety disclaimer required |
| OPP-2026-003 | Filter and consumable replacement tracker | Households with replaceable filters | Packaging notes, calendar | inference from T01-S05 | medium | no device-control claim |
| OPP-2026-004 | Pantry “use first” queue | Adults responsible for food preparation | Memory, sticky note | inference from T01-S02/S03/S04 | medium | food-safety boundary |
| OPP-2026-005 | Leftover visibility ledger | Adults storing prepared food | Container labels, memory | inference from T01-S02/S04 | medium | food-safety boundary |
| OPP-2026-006 | Displaced-meal reset list | Adults whose meal plans change | Ad hoc list | inference from T01-S02 | medium | none identified |
| OPP-2026-007 | Household consumables cadence | Adults replenishing non-financial supplies | Memory, shopping list | inference from T01-S01 | low | avoid retailer lock-in |
| OPP-2026-008 | Clothing-care memory | People managing garment-specific care | Labels, notes | inference from T01-S01 | low | no fabric-safety guarantee |
| OPP-2026-009 | Cleaning-zone rotation | Adults doing repeated housework | Paper rotation, generic tasks | inference from T01-S01 | medium | none identified |
| OPP-2026-010 | Declutter micro-session queue | Adults breaking home organization into short sessions | Notes, timer | inference from T01-S01 | low | no clinical framing |
| OPP-2026-013 | Errand batch queue | Adults grouping repeated local errands | Notes, calendar | inference from T01-S01 | medium | no location surveillance |
| OPP-2026-017 | Seasonal home reset calendar | Renters/homeowners rotating seasonal tasks | Calendar, paper list | inference from T01-S05 | medium | jurisdiction/climate variation |

## Cross-Cutting Constraints

- **Privacy:** default to local/manual entry; do not assume inbox, location, retailer, contact, camera, microphone, smart-home, or calendar access. Collect only the minimum needed for the chosen routine.
- **Safety:** smoke-alarm, food-storage, plant, pet, and maintenance content must link to authoritative guidance and never claim inspection, diagnosis, emergency response, or professional equivalence.
- **Platform:** every candidate has a manual fallback. No candidate is qualified on the assumption that a third-party API is available.
- **Legal/IP:** do not copy protected interaction flows, brand assets, content libraries, or competitor code. User-created lists and public-domain/permissioned guidance are the safe default.
- **Behavioral ethics:** avoid punitive streaks, shame, artificial urgency, hidden subscriptions, manipulative notifications, or surveillance-based engagement.

## Exclusions, Risks, and Unknowns

Detailed exclusions and the eight-entry Hypothesis Watchlist are recorded in [EXCLUSIONS.md](EXCLUSIONS.md); unresolved evidence is in [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md). The central unknown is direct problem intensity and willingness to pay at the candidate level. The current evidence supports a 12-candidate qualified universe, not commercial selection.

## Confidence Assessment

Overall confidence is `medium` for the existence and recurrence of household-work and food-management friction; `low` to `medium` for individual candidate demand. This is the honest Gate 1 ceiling without interviews, product analytics, paid datasets, or validation—none of which is authorized here. The package can still earn a 100/100 Creator Artifact Quality Score because uncertainty is visible and traceable; that score does not assert opportunity attractiveness.

## Recommended Next Action

Review the coverage matrix, 12 qualified candidates, eight-entry watchlist, source classifications, constraints, complete 20-ID audit trail, and evidence ceiling. Keep Gate 1 open and do not score or rank the opportunities until Founder authorization for the next gate.

External Governance Cycle 3 re-review requested
