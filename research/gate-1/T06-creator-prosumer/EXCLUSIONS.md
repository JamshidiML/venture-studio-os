---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T06 Exclusions

| Excluded space | Reason | Evidence or rule |
|---|---|---|
| Unauthorized social-platform scraper | Terms, privacy and dependency risk | Issue #9; C03, C10–C11 |
| Mass-DM, comment, follow or engagement automation | Spam/deception and platform abuse | Issue #9; C03 |
| Copyright circumvention, paywall bypass or media downloader | Infringement and prohibited behavior | Issue #9; C07 |
| Unlicensed content-rewrite or derivative generator | Rights and authorship risk | C06–C07 |
| Deepfake, voice-clone impersonation or deceptive synthetic persona | Abuse and consent risk | Issue #9 |
| Fake review/testimonial/engagement generator | Deceptive under FTC principles | C08 |
| Platform-specific companion requiring undocumented private API | Explicit thread boundary and fragile dependency | Issue #9; C10–C11 |
| Social-network clone or creator marketplace | Capital/network-effects mismatch | Issue #9 |
| Enterprise content-operations suite | Belongs to SMB/enterprise scope, not lightweight individual workflow | Issue #9 |
| General consumer utility unrelated to production | Reserved to T01 | Parent #3 isolation |
| Automated publication without review | Rights, factual and disclosure risk | C03, C06–C08 |
| Extension requesting all-sites access for convenience | Violates least-privilege/single-purpose discipline | C03–C04 |
| Creator-income estimator from follower counts | Unsupported, misleading and potentially discriminatory | Evidence rules |

Excluded spaces were recorded rather than silently removed or softened.

## Hypothesis Watchlist

These are not Qualified Gate 1 Candidates. Original T06 IDs remain owned and non-reusable. Every record retains its evaluation condition plus human-review, rights, permission, privacy, platform and T06/T08 scope boundary.

| Opportunity ID | Original concept | Why not qualified / consolidation status | Current confidence | Evidence searched | Missing evidence | Risk and safety constraints | Conditions for reconsideration | Original ownership |
|---|---|---|---|---|---|---|---|---|
| OPP-2026-500 | Source-and-citation capture side panel | API feasibility is not observed capture pain | low | C02–C05, C07, C13–C16; bookmarks/clippers/docs | Direct creator research-session capture failures and current workaround cost | Least privilege, rights-respecting excerpts, consent; no continuous monitoring; T06/T08 boundary | Direct workflow evidence plus minimal-permission and user-correction evaluation | T06 — Issue #9 |
| OPP-2026-501 | License-status browser capture card | Rights rules and browser capability do not establish a capture-card need | medium | C03, C07, C13–C15; sheets/metadata | Direct per-asset license-record workflow and failure evidence | User-entered status only; no permission/legal inference; least privilege | Observed workflow establishes distinct browser need and human verification | T06 — Issue #9 |
| OPP-2026-502 | Research-tab session bundle with user-selected notes | Browser docs and multi-stage context do not establish session pain | low | C03–C05, C13, C15–C16; tab groups/bookmarks/notes | Direct creator session-resume failures | Minimal tab/host access, disclosure, cross-browser test; T06/T08 boundary | Direct workflow evidence and least-privilege portability evaluation | T06 — Issue #9 |
| OPP-2026-503 | Bookmark-to-brief organizer for owned notes | Category context does not observe brief-organization pain | low | C02, C03, C07, C15–C16; read-later/docs | Direct owned-note synthesis workflow and switching friction | No full protected-page copying; citations/user excerpts; T06/T08 boundary | Direct evidence establishes bounded creator-project job | T06 — Issue #9 |
| OPP-2026-504 | Creative asset rights and expiry ledger | Creator population and copyright rules do not prove ledger demand | medium | C01, C07, C15; sheets/DAM | Direct asset-rights record/renewal workflow | Contracts authoritative; no legal determination or automated permission | Observed workflow plus counsel-reviewed human verification | T06 — Issue #9 |
| OPP-2026-505 | Credits and attribution preflight | Copyright/accessibility constraints do not establish separate preflight pain | medium | C07, C09, C15; checklists/credit docs | Direct release-credit failure workflow | Attribution never substitutes for license; human review/accessibility | Direct observation demonstrates distinct evidence owners/output | T06 — Issue #9 |
| OPP-2026-506 | Sponsorship disclosure placement checklist | FTC guidance and vendor context are not creator pain | low | C02, C08, C15; brand briefs/platform tools | Direct campaign disclosure workflow/failures by jurisdiction | No compliance certification; human review; jurisdiction-specific | Direct creator workflow plus current-jurisdiction legal review | T06 — Issue #9 |
| OPP-2026-508 | Transcript-to-show-notes outline for owned media | Rights/accessibility rules and broad workflow context do not establish outline pain | medium | C06–C07, C09, C15–C16; processors/AI | Direct episode outline workflow and human-review burden | Owned/licensed media; factual/human authorship review | Direct evidence establishes distinct input/reviewer/output and evaluation criteria | T06 — Issue #9 |
| OPP-2026-509 | Descriptive-transcript completeness checklist | Direct accessibility context exists, but its event/reviewer/output consolidate into 507 | medium | C09, C15–C17; WCAG checks/editorial review | Evidence that completeness review is operationally separate from 507 | Human visual-meaning review; no conformance guarantee | Direct evidence demonstrates a distinct reviewer/output not covered by 507 | T06 — Issue #9 |
| OPP-2026-511 | Content-reuse rights matrix | Copyright rules do not establish a reuse-decision workflow | medium | C06–C07, C15; sheets/project tools | Direct repeated permission-decision pain | No fair-use/legal determination or unauthorized derivatives | Direct workflow plus counsel-reviewed human authority/evaluation | T06 — Issue #9 |
| OPP-2026-512 | Cross-format repurposing plan for user-owned work | Multi-stage/context evidence does not observe repurposing pain | low | C02, C06–C07, C15–C16; calendars/templates/AI | Direct creator transformation-planning workflow | Owned/licensed input, human contribution/provenance, no unauthorized generation | Direct observation distinguishes planning from rights decision 511 | T06 — Issue #9 |
| OPP-2026-513 | Newsletter link/disclosure/accessibility preflight | Constraints and broad workflows do not establish newsletter-specific failures | low | C01–C02, C08–C09, C15–C16; checks/previews | Direct newsletter release workflow and failure frequency | No spam, platform companion or compliance/accessibility certification | Format-specific evidence establishes distinct event/input/reviewer/output | T06 — Issue #9 |
| OPP-2026-514 | Podcast feed-and-episode asset manifest preflight | Broad workflow context does not establish manifest demand | low | C02, C07–C09, C15–C16; docs/hosting checks | Direct podcast preflight failures | Rights/disclosure/transcript human review; file/manual only | Format-specific evidence and bounded evaluation contract | T06 — Issue #9 |
| OPP-2026-515 | Cross-platform video publish-package preflight | Staged/video context does not establish package pain | low | C02, C08–C11, C15–C17; upload screens/docs | Direct cross-platform release-package failures | Manual creator-controlled package; no required API/platform companion; T06/T08 boundary | Direct workflow evidence demonstrates distinct failure modes and manual-first evaluation | T06 — Issue #9 |
| OPP-2026-516 | Title/thumbnail test idea and result log | Vendor survey does not establish experiment-log demand | low | C02; sheets/platform analytics | Direct creator experiment-record workflow | User-import only; no scraping, clickbait or deception | Direct evidence plus truthful user-controlled evaluation | T06 — Issue #9 |
| OPP-2026-517 | Audience-feedback theme coding from user-exported comments | Category context does not observe coding pain | low | C02–C03, C15; sheets/coding tools | Direct exported-feedback review workflow | No scraping; minimize personal data; preserve minority feedback/human review | Direct evidence plus privacy/fairness evaluation | T06 — Issue #9 |
| OPP-2026-518 | Client deliverable approval journal | Population and broad practitioner context do not establish approval-journal pain | low | C01, C16; email/PM tools | Direct freelance milestone approval failures | Secure content, explicit human approval; no enterprise suite | Direct freelancer evidence demonstrates distinct lightweight job | T06 — Issue #9 |
| OPP-2026-519 | Content Credentials inspection and provenance note helper | Standard availability does not establish creator pain or adoption | medium | C06, C12, C15; C2PA inspectors/metadata viewers | Direct provenance-inspection workflow and credential availability | Absence is unknown, never fraud; credentials not authenticity proof; human authority | Direct workflow/adoption evidence plus false-assurance evaluation | T06 — Issue #9 |
