---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T06 Opportunity Index

The original 20-ID universe is preserved as **2 Qualified Gate 1 Candidates** and **18 Hypothesis Watchlist Candidates**. Only the creator-accessibility production family has direct observed workflow evidence. Creator population, multi-stage context, rights rules, standards, API documentation and platform feasibility do not independently qualify other concepts. Complete watchlist contracts are in [EXCLUSIONS.md](EXCLUSIONS.md); no ID is deleted, reused or renumbered.

WTP, demand and repeat use are unknown. Browser/API details are constraints, not implementation authorization. No browser extension or platform integration is authorized.

## Qualified Gate 1 Candidates

| ID | Bounded workflow | User event | Input | Human reviewer | Output | Evidence / confidence | Evaluation and safety boundary |
|---|---|---|---|---|---|---|---|
| OPP-2026-507 | Local time-based-media accessibility QA workspace, consolidating caption QA and descriptive-transcript completeness | Creator prepares one owned/authorized video for release | Local or manually pasted video, caption and descriptive-transcript material | Creator/editor or designated accessibility reviewer | Human-reviewed issue list and corrected creator-controlled caption/transcript files | C17 directly observes staged, collaborative accessibility production; C09 defines distinct caption/transcript work; medium | Evaluate only completion, reviewer correction and workflow fit under later authorization; no conformance certification, automated truth claim or required API; local/manual primary |
| OPP-2026-510 | Context-specific alt-text draft review queue | Creator prepares an image/visual asset for publication | Creator-owned image plus publication context and optional human/AI draft | Visual creator/editor or designated accessibility reviewer | Human-approved contextual alt-text record | C17 directly observes creator accessibility work; C09 distinguishes image descriptions from time-based media; medium | Evaluate only review/correction workflow under later authorization; no automated conformance, biometric inference or unreviewed publication |

## Accessibility consolidation decision

| Original ID | Cycle 3 resolution | Distinctness test |
|---|---|---|
| 507 | Qualified canonical time-based-media workflow; absorbs 509's descriptive-transcript completeness job | Per-video event; time-based media/caption/transcript input; creator/accessibility reviewer; corrected timed-text/transcript output |
| 509 | Consolidated into 507 and preserved as a non-reusable watchlist record | Its release event, reviewer and output do not remain sufficiently independent from 507 |
| 510 | Retained as a distinct qualified workflow | Per-image/visual event; image + publication-context input; visual/accessibility reviewer; approved contextual alt-text output |

## Coverage and integrity check

- Qualified IDs: 507 and 510.
- Watchlist IDs: 500–506, 508–509 and 511–519.
- Qualified `2` + watchlist `18` = original auditable universe `20`; all IDs remain within 500–519.
- Every qualified and watchlist record preserves human review, rights, permission, privacy and platform constraints.

## T06 / T08 boundary check

| Candidate family | T06-owned creator workflow | Explicit T08 boundary |
|---|---|---|
| 500–503 browser capture — watchlist | Only narrow, user-invoked capture of user-selected research/notes for a creator project could belong to T06; no persistent account integration | Generic browser/platform companions, cross-account integration, continuous monitoring or broad host permission belong to T08 or remain excluded |
| 507 accessibility QA — qualified | Local file or manual-paste QA for creator-owned media; optional authorized sync is non-essential | A YouTube-specific companion, channel manager or OAuth-dependent caption manager belongs to T08 |
| 515 publish package — watchlist | Only a creator-controlled checklist/package for manual upload could belong to T06 | A companion operating one platform's publishing workflow, analytics or account state belongs to T08 |

## Candidate-to-source coverage and status matrix

`None` means no direct evidence. API documentation, population counts, regulation, standards and vendor features are not creator pain.

| ID | Cycle 3 status | Direct / adjacent qualifying evidence | Context / alternatives | Feasibility | Rights / permission / safety / platform | Unsupported assumption |
|---|---|---|---|---|---|---|
| 500 | Watchlist | None | C02, C15–C16; bookmarks/clippers | C13–C14 only | C03–C05, C07; T06/T08 boundary | Capture pain, side-panel preference, cadence |
| 501 | Watchlist | None | C15; sheets/metadata | C13–C14 only | C03, C07 | Browser-card and rights-record need |
| 502 | Watchlist | None | C15–C16; tabs/bookmarks/notes | C05, C13 | C03–C04; T06/T08 boundary | Session-bundle pain/portability |
| 503 | Watchlist | None | C02, C15–C16; read-later/docs | Not researched | C03, C07; T06/T08 boundary | Bookmark-to-brief pain/cadence |
| 504 | Watchlist | None | C01, C15; sheets/DAM | Not researched | C07; no legal determination | Rights/expiry ledger demand |
| 505 | Watchlist | None | C15; checklists/credits docs | Not researched | C07, C09 | Credits-preflight pain |
| 506 | Watchlist | None | C02, C15; brand briefs/platform tools | Not researched | C08; no compliance certification | Disclosure-checklist demand |
| 507 | Qualified — canonical time-based media | C17 staged accessibility production; C09 adjacent task definition | C15–C16; platform/text editors | Local/manual; C11 optional only | C09, C11; human review; T06/T08 boundary | Workspace preference, WTP and effect |
| 508 | Watchlist | None | C15–C16; processors/AI | Not researched | C06–C07, C09 | Outline pain and review value |
| 509 | Watchlist — consolidated into 507 | C17 accessibility context, but no distinct post-consolidation job | C15–C16; checklists/review | Not researched | C09; human review | Separate completeness-check need |
| 510 | Qualified — image accessibility | C17 accessibility production; C09 adjacent image-description task | C15–C16; CMS/docs/AI | Not researched | C06, C09; human confirmation/no biometrics | Queue preference, cadence and effect |
| 511 | Watchlist | None | C15; sheets/project tools | Not researched | C06–C07; no fair-use determination | Reuse-matrix demand |
| 512 | Watchlist | None | C02, C15–C16; calendars/templates | Not researched | C06–C07; owned/licensed input | Repurposing-plan pain |
| 513 | Watchlist | None | C01–C02, C15–C16; checks/previews | Not researched | C08–C09; no spam/platform companion | Newsletter-specific failures |
| 514 | Watchlist | None | C02, C15–C16; docs/host checks | Not researched | C07–C09; file/manual only | Podcast preflight demand |
| 515 | Watchlist | None | C02, C15–C17; upload screens/docs | Manual package possible; APIs non-essential | C08–C11; T06/T08 boundary | Cross-platform package pain/WTP |
| 516 | Watchlist | None | C02; sheets/platform analytics | User-import only | No scraping/deception | Experiment-log demand |
| 517 | Watchlist | None | C02, C15; sheets/coding tools | User-export only | C03; privacy/minority visibility | Theme-coding pain/cadence |
| 518 | Watchlist | None | C01, C16; email/PM tools | Not researched | Client-data privacy; no enterprise suite | Approval-journal pain |
| 519 | Watchlist | None | C15; C2PA inspectors/viewers | C12 standard only | C06, C12; absence is unknown | Adoption and provenance-note demand |
