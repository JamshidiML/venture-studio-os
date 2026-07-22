---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T06 Opportunity Index

This is an unranked universe of exactly 20 creator/prosumer workflows. Browser/API details are constraints, not implementation authorization. WTP is unknown unless explicitly evidenced; none is evidenced here. Each stated repeat-use mechanism is an **assumption** owned by the Strategy Agent. Impact if wrong: it cannot support candidate advancement or a retention claim. Planned review/test: only after a separately authorized Gate 5 issue, define a consented workflow study for the relevant release/project cadence; no measure or threshold is authorized at Gate 1.

| ID | Recurring problem / candidate workflow | Segment and frequency | Current alternatives | Evidence basis; type; confidence | WTP status | Repeat-use mechanism assumption | Rights, permission or platform constraint |
|---|---|---|---|---|---|---|---|
| OPP-2026-500 | Source-and-citation capture side panel | Researchers, writers and video essayists; daily | Bookmarks, note clippers, documents | C13–C14; technical feasibility only, workflow assumption; low | Unknown | Each research session creates captures | Chrome sidePanel is verified, but page capture needs least-privilege activeTab/scripting review; respect page rights |
| OPP-2026-501 | License-status browser capture card | Designers, editors and producers; per asset | Spreadsheets, metadata notes | C03, C07; inference; medium | Unknown | Every acquired asset creates a record | User enters/links license; tool must not infer permission from availability |
| OPP-2026-502 | Research-tab session bundle with user-selected notes | Writers and knowledge workers; daily/weekly | Tab groups, bookmarks, notes | C03–C05, C13; policy/technical feasibility only, workflow assumption; low | Unknown | Save/resume session loop | Minimize tabs/host access; cross-browser behavior unverified |
| OPP-2026-503 | Bookmark-to-brief organizer for owned notes | Newsletter writers and analysts; weekly | Read-later apps, documents | C02, C15; category context only, workflow assumption; low | Unknown | Issue/project cycles | Do not copy full protected pages; citations and user-selected excerpts only |
| OPP-2026-504 | Creative asset rights and expiry ledger | Freelancers and small creator teams; per project | Spreadsheets, DAM tools | C01, C07; inference; medium | Unknown | New asset/project and renewal events | No legal determination; contracts remain authoritative |
| OPP-2026-505 | Credits and attribution preflight | Video, podcast and visual creators; per release | Manual checklists, end-credit docs | C07, C09; inference; medium | Unknown | Every publication | Attribution does not substitute for a license; accessibility of credits |
| OPP-2026-506 | Sponsorship disclosure placement checklist | Influencers, podcasters and newsletter writers; per campaign | Brand briefs, notes, platform tools | C02, C08; inference; high for compliance context, low for demand | Unknown | Each sponsored post/campaign | Jurisdiction-specific; no auto-certification of compliance |
| OPP-2026-507 | Local caption QA workspace for creator-owned media | Video creators and editors; per video | Platform caption editor, text editor | C09, C17; direct accessibility-work context, workspace inference; medium | Unknown | Every video release | Local file/manual paste is primary; optional caption API requires owner authorization and remains non-essential |
| OPP-2026-508 | Transcript-to-show-notes outline for owned media | Podcasters and video creators; per episode | Word processors, AI chat | C06–C07, C09; inference; medium | Unknown | Every episode | Owned/licensed media only; human authorship and factual review |
| OPP-2026-509 | Descriptive-transcript completeness checklist | Accessible-media producers; per release | WCAG checklist, editorial review | C09, C17; direct accessibility-work context, checklist inference; medium | Unknown | Release preflight | Human review required for visual meaning; no conformance guarantee |
| OPP-2026-510 | Alt-text draft review queue | Visual creators and newsletter publishers; per asset | CMS fields, documents, AI chat | C06, C09, C17; direct accessibility-work context, queue inference; medium | Unknown | Each image/publication | Human confirmation; context-specific accessibility and no biometric inference |
| OPP-2026-511 | Content-reuse rights matrix | Multi-format creators; per campaign | Spreadsheets, project tools | C06–C07; inference; medium | Unknown | Every repurposing decision | No fair-use determination or unauthorized derivative generation |
| OPP-2026-512 | Cross-format repurposing plan for user-owned work | Writers, podcasters and video creators; weekly | Content calendars, templates, AI chat | C02, C06–C07, C15–C16; multi-stage/category context, planner inference; low | Unknown | Recurring publication cadence | User-owned/licensed input only; preserve human contribution and provenance |
| OPP-2026-513 | Newsletter link/disclosure/accessibility preflight | Independent newsletter writers; weekly/monthly | Checklists, email-platform previews | C08–C09, C15–C16; constraint/workflow context, preflight inference; low | Unknown | Every issue | No spam automation; checks remain human-reviewed; not a platform companion |
| OPP-2026-514 | Podcast feed-and-episode asset manifest preflight | Independent podcasters; weekly/seasonal | Documents, hosting checklists | C08–C09, C15–C16; constraint/workflow context, preflight inference; low | Unknown | Every episode | Rights, sponsor disclosure, transcript and feed metadata; file/manual workflow only |
| OPP-2026-515 | Cross-platform video publish-package preflight | Video creators; per video | Platform upload screens, documents | C08–C09, C15–C17; direct staged-work context, package inference; low | Unknown | Every release | Produces a creator-controlled package; no platform-specific companion or required API; authorized sync optional only |
| OPP-2026-516 | Title/thumbnail test idea and result log | Video/newsletter creators; per release | Spreadsheets, platform analytics | C02; assumption; low | Unknown | Publication experiments | No clickbait, deception or scraped analytics; user-imported data only |
| OPP-2026-517 | Audience-feedback theme coding from user-exported comments | Creators with owned/exported feedback; monthly | Spreadsheets, qualitative coding tools | C02–C03; inference; low | Unknown | Monthly review cycle | No unauthorized scraping; minimize personal data; keep minority feedback visible |
| OPP-2026-518 | Client deliverable approval journal | Freelance creators; per client milestone | Email, project-management tools | C01; assumption; low | Unknown | Milestone approvals and revisions | Not an enterprise operations suite; secure client content and explicit approvals |
| OPP-2026-519 | Content Credentials inspection and provenance note helper | Photographers, designers and editors; per asset | C2PA inspection tools, metadata viewers | C06, C12; inference; medium | Unknown | Each AI-assisted or provenance-sensitive asset | Credentials may be absent or stripped; never label absence as fraud or authenticity proof |

## Coverage and dependency check

- Segments: researchers/writers, visual creators, video creators, podcasters, newsletter writers, influencers and freelancers.
- Cadence: daily capture, weekly/monthly editorial cycles, per-asset, per-campaign, per-episode and per-client milestone.
- Browser candidates 500–503 have verified surface documentation but no assumed store approval or cross-browser parity.
- API-dependent workflows 507 and 515 require authorization and retain manual/offline fallbacks; no quota extension is assumed.
- No candidate scrapes platforms, evades rights, automates spam, creates deepfakes, clones a social network or acts as a platform-specific companion.

## T06 / T08 boundary check

| Candidate family | T06-owned creator workflow | Explicit T08 boundary |
|---|---|---|
| 500–503 browser capture | Narrow, user-invoked capture of user-selected research/notes for a creator project; no persistent account integration | Any generic browser/platform companion, cross-account workspace integration, continuous monitoring or broad host permission belongs to T08 or is excluded |
| 507 caption QA | Local file or manual-paste QA for creator-owned media; authorized platform sync is optional and non-essential | A YouTube-specific companion, channel-management tool or OAuth-dependent caption manager belongs to T08 |
| 515 publish package | Generates a creator-controlled cross-platform checklist/package for manual upload | A companion that operates one platform's publishing workflow, analytics or account state belongs to T08 |

## Preflight differentiation and consolidation rules

| Candidates | Distinct retained job | Consolidation trigger |
|---|---|---|
| 505–506 | 505 checks credits/attribution records; 506 checks sponsorship disclosure placement | Consolidate only if direct research shows creators maintain one compliance checklist with no separate evidence/owners |
| 507, 509–510 | 507 reviews timed captions; 509 checks descriptive transcript coverage; 510 queues context-specific image descriptions | Preserve only where media/input and reviewer differ; otherwise consolidate into one accessibility QA primitive |
| 511–512 | 511 records whether reuse is permitted; 512 plans transformations after permission is established | Consolidate if creators do not separate rights decisions from repurposing plans |
| 513–515 | Format-specific composite release contexts: newsletter, podcast and cross-platform video package | Replace with shared primitives if direct workflow research fails to show format-specific failure modes; none is treated as independently demanded today |

## Candidate-to-source coverage matrix

`None` means no direct evidence. API documentation, population counts, regulation, standards and vendor features are not direct creator pain.

| Candidate | Direct problem evidence | Contextual / population evidence | Current-alternative evidence | Technical feasibility | Legal / privacy / safety / platform | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|
| 500 | None | C02, C15–C16 | Bookmarks, clippers, documents | C13–C14 only | C03–C05, C07 | Capture pain, side-panel preference, cadence |
| 501 | None | C15 | Sheets, metadata notes | C13–C14 only | C03, C07 | Browser-card need and rights-record frequency |
| 502 | None | C15–C16 | Tab groups, bookmarks, notes | C05, C13 | C03–C04 | Session-bundle pain and portability |
| 503 | None | C02, C15–C16 | Read-later apps, documents | Not researched | C03, C07 | Bookmark-to-brief pain and cadence |
| 504 | None | C01, C15 | Sheets, DAM tools | Not researched | C07 | Rights/expiry ledger demand |
| 505 | None | C15 | Checklists, credit documents | Not researched | C07, C09 | Separate credits-preflight pain |
| 506 | None | C02, C15 | Brand briefs, platform tools | Not researched | C08 | Disclosure-checklist demand |
| 507 | C17 accessibility production barriers | C15–C16 | Platform editor, text editor | Local file/manual viable; C11 optional | C09, C11 | QA workspace preference/WTP |
| 508 | None | C15–C16 | Word processors, AI | Not researched | C06–C07, C09 | Outline pain and human-review value |
| 509 | C17 staged accessibility work | C15–C16 | WCAG checklist, editorial review | Not researched | C09 | Separate completeness-check pain |
| 510 | C17 accessibility work | C15–C16 | CMS fields, documents, AI | Not researched | C06, C09 | Review-queue pain and cadence |
| 511 | None | C15 | Sheets, project tools | Not researched | C06–C07 | Reuse-matrix demand |
| 512 | None | C02, C15–C16 multi-stage workflow context | Calendars, templates, AI | Not researched | C06–C07 | Repurposing-plan pain |
| 513 | None | C01–C02, C15–C16 multi-stage workflow context | Checklists, previews | Not researched | C08–C09 | Newsletter-specific failure frequency |
| 514 | None | C02, C15–C16 multi-stage workflow context | Documents, hosting checklists | Not researched | C07–C09 | Podcast manifest/preflight demand |
| 515 | None | C02, C15–C17 staged/video/accessibility context | Upload screens, documents | Manual package viable; C10–C11 non-essential | C08–C11 | Cross-platform package pain/WTP |
| 516 | None | C02 | Sheets, platform analytics | User-import only | No scraping/deception | Experiment-log demand |
| 517 | None | C02, C15 | Sheets, coding tools | User-export only | C03; privacy/minority visibility | Theme-coding pain and cadence |
| 518 | None | C01, C16 | Email, PM tools | Not researched | Client-data privacy | Approval-journal pain |
| 519 | None | C15 | C2PA inspectors, metadata viewers | C12 standard only | C06, C12 | Adoption, provenance-note demand |
