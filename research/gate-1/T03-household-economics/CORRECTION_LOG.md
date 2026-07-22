---
status: in-review
version: 0.1.4
owner_role: Strategy Agent
last_reviewed: 2026-07-23
thread_id: T03
issue_number: 6
gate: 1
---

# T03 Correction Log

| Correction ID | Cycle-1 loss / blocker | Targeted correction | Verification | Status |
|---|---|---|---|---|
| T03-C01 | Integration/legal boundaries (-1) | Added exclusions for bank/open banking, inbox/retailer scraping, custody, execution, legal determinations, and affiliate rankings. | 15 explicit exclusion rows plus manual fallbacks. | resolved |
| T03-C02 | Freshness/current-law gap (-5 plus T03-B01) | Added March 2026 FTC rulemaking source, recorded 2024 rule vacatur, and removed stale current-law premise. | T03-S03 and currency note explicitly state vacatur. | resolved |
| T03-C03 | Claim traceability (-4) | Added source IDs and evidence/inference/assumption/hypothesis treatment to material claims and all candidate rows. | 20/20 candidates trace to sources. | resolved |
| T03-C04 | National evidence versus impact (-4) | Added limitations that SHED/CFPB/EPA evidence is not candidate demand, market size, WTP, or realized savings. | Report, source register, and evidence gaps align. | resolved |
| T03-C05 | Legal/privacy/platform controls (-4) | Added jurisdiction, advice, custody/execution, manual fallback, security, calculation transparency, and trust rules. | Candidate-specific constraint column plus cross-cutting controls. | resolved |
| T03-C06 | Search reproducibility (-3) | Added exact queries, current-law follow-up, inclusion/exclusion, and searches not converted into claims. | 12 query rows and explicit no-bank/API rule. | resolved |

No Opportunity Score was changed or created to obtain the Artifact Quality Score.

## Internal Pre-review (not independent)

| Review ID | Finding | Required correction | Verification | Status |
|---|---|---|---|---|
| T03-G01 | A prior Codex self-review simulated 100/100 and checked creator blocker T03-B01. | Preserve as internal audit history; do not treat it as independent Governance. | Relabeled here, in score history, and in summary. | superseded by external review |

## External Governance Review — Cycle 1

Authoritative external score: `92/100`. Critical blockers: `EXT-GOV-01` and `T03-EXT-B02`.

### External Point-Loss Register

| Dimension | Maximum | External award | Lost | Finding |
|---|---:|---:|---:|---|
| Scope compliance and exclusions | 10 | 10 | 0 | no loss |
| Source quality and freshness | 20 | 18 | 2 | candidate 219 lacked the dedicated current Cooling-Off Rule source |
| Claim-level evidence and traceability | 15 | 14 | 1 | candidate 219 pointed to a general returns source |
| Opportunity coverage and diversity | 15 | 13 | 2 | source coverage for weak workflows was not explicit |
| Analytical rigor and uncertainty | 15 | 14 | 1 | broad context needed explicit downgrade treatment |
| Legal, safety, privacy, and platform constraints | 10 | 9 | 1 | cooling-off locations, exclusions, and deadline lacked authoritative candidate linkage |
| Reproducibility of search method | 10 | 10 | 0 | no loss |
| Clarity and repository hygiene | 5 | 4 | 1 | same-process Codex review mislabeled independent |
| **Total** | **100** | **92** | **8** | **external score is authoritative** |

| Review ID | External finding / required correction | Applied correction | Verification | Status |
|---|---|---|---|---|
| EXT-GOV-01 | Prior Codex review was not independent. | Relabeled all surviving references as Internal Pre-review/Simulation while preserving history. | External Cycle-2 review explicitly marked this blocker resolved. | externally resolved |
| T03-EXT-B02 | Candidate 219 cited a general returns page instead of dedicated current Cooling-Off Rule authority. | Added T03-S13, the FTC September 2025 article, and made it the exclusive candidate-219 rule source. | External Cycle-2 review verified the dedicated source, locations, exclusions, third-business-day deadline, jurisdiction limits, and no-advice boundary. | externally resolved |
| T03-EXT-C01 | Record limited covered locations, exclusions, three-business-day deadline, and September 2025 publication. | T03-S13 and candidate 219 now state all four; matrix separates legal authority from checklist adoption. | SOURCE_REGISTER.md, OPPORTUNITY_INDEX.md | resolved internally |
| T03-EXT-C02 | Strengthen, downgrade, or remove 205, 211, 215, and 218. | Downgraded all four to `very low` and named their absent direct evidence. | MARKET_DISCOVERY_REPORT.md, OPPORTUNITY_INDEX.md, EVIDENCE_GAPS.md | resolved internally |
| T03-EXT-C03 | Add candidate-to-source matrix and log exact eight-point loss. | Added 20/20 source coverage and the dimension-level register above. | OPPORTUNITY_INDEX.md, QUALITY_SCORE_HISTORY.md | resolved internally |

## Authoritative External Governance Re-review — Cycle 2

Authoritative external score: `95/100` (`10 + 19 + 15 + 12 + 14 + 10 + 10 + 5`). `EXT-GOV-01` and `T03-EXT-B02` were externally resolved. The remaining five-point loss comprised one source-quality point, three opportunity-coverage points, and one analytical-rigor point because four explicitly unsupported workflows remained in the qualified universe.

| Review ID | External finding / required correction | Cycle-3 resolution | Verification | Status |
|---|---|---|---|---|
| EXT2-T03-01 | IDs 205, 211, 215, and 218 remained unsupported hypotheses inside a report describing all 20 concepts as qualified; move them to a watchlist and keep legal guidance separate from direct pain. | Retained the then-current 16-candidate set and moved all four named IDs to the full Hypothesis Watchlist without deletion or renumbering. | External Cycle-3 review verified the watchlist, full universe, Cooling-Off Rule record, lifecycle, and CI. | externally resolved |
| C3-T03-01 | Cycle 3 must preserve candidate 219's dedicated FTC source and narrow rule treatment while creating the two-tier universe. | Kept T03-S13, limited covered locations, exclusions, midnight-of-third-business-day deadline, jurisdiction/state-law caveat, no-advice/no-submission boundary, and legal-guidance classification intact; versioned all nine artifacts to 0.1.3 and retained `status: in-review`. | External Cycle-3 review confirmed the Cycle-2 completion finding and prior blockers resolved. | externally resolved |

No source was added or removed in Cycle 3. No Opportunity Score was created or inflated.

## Authoritative External Governance Review — Cycle 3

Authoritative external score: `94/100` (`10 + 19 + 15 + 11 + 14 + 10 + 10 + 5`). The exact six-point loss was one source-quality point, four qualified/watchlist-integrity points, and one analytical-rigor point. `EXT-GOV-01` and `EXT2-T03-01` were externally confirmed resolved; `T03-EXT-B02` remains resolved.

| Dimension | Maximum | External award | Lost | Finding |
|---|---:|---:|---:|---|
| Scope compliance and exclusions | 10 | 10 | 0 | no loss |
| Source quality and freshness | 20 | 19 | 1 | multiple remaining qualified rows lacked direct or clearly adjacent workflow evidence |
| Claim-level evidence and traceability | 15 | 15 | 0 | no loss |
| Opportunity coverage and qualified/watchlist integrity | 15 | 11 | 4 | regulation, guidance, standards, context, feasibility, or asserted alternatives were treated as qualification |
| Analytical rigor and uncertainty | 15 | 14 | 1 | the stated qualification rule was not consistently applied |
| Legal, safety, privacy, and platform constraints | 10 | 10 | 0 | no loss; Cooling-Off Rule boundary remained correct |
| Reproducibility and CI | 10 | 10 | 0 | no loss |
| Clarity and repository governance | 5 | 5 | 0 | no loss |
| **Total** | **100** | **94** | **6** | **external score is authoritative** |

| Review ID | External finding / required correction | Final correction | Verification | Status |
|---|---|---|---|---|
| EXT-GOV-03-T03 | IDs 203, 206–210, 212–214, 216–217, and 219 remained qualified despite only regulatory/guidance, general-cost, standards, feasibility, or asserted-alternative support. | Moved all 12 IDs to the existing Hypothesis Watchlist; retained only 200–202 and 204, whose complaint/bill-difficulty evidence directly or clearly adjacently supports the bounded workflows. | All nine artifacts show `4 qualified + 16 watchlist = 20`; the matrix has four qualified and 16 watchlist statuses; EXCLUSIONS.md holds 16 complete contracts and preserves candidate 219's legal record. | creator-resolved; final external verification pending |
| FINAL-T03-01 | Issue #25 requires exact decisions, lost-point history, source changes, evidence ceiling, lifecycle bump, and frozen-thread integrity while preserving T03-S13. | Strengthened IDs: none. Moved: 203, 206–210, 212–214, 216–217, 219. Sources: 13 → 13 (+0/−0). Versioned all nine artifacts to 0.1.4 and retained `in-review`. | Repository validator passed (32/37, links/placeholders clean), unit tests passed 3/3, diff check passed, artifact/lifecycle/range/ID/matrix/watchlist-contract audits passed, and T03-S13/legal-boundary text remains complete; frozen, PR, and CI checks continue through publish. | creator-resolved; local validation passed; final external verification pending |

No source was added, removed, or reclassified in the final correction. Candidate 219 retains T03-S13, covered locations, exclusions, the midnight-of-third-business-day deadline, jurisdiction/state-law caveat, and no-advice/no-submission constraints. No Opportunity Score was created or inflated.

Final External Governance re-review requested
