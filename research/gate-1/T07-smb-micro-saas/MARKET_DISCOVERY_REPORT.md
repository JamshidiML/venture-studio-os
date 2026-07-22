---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T07 Gate 1 Market Discovery — SMB Micro-SaaS and Workflow Friction

## Executive summary

This report documents 14 unranked workflow wedges for small businesses and small teams after External Governance Correction Cycle 2 removed six concepts that lacked sufficient problem evidence. The strongest direct problem evidence concerns invoice/payment administration. Direct but bounded survey or user evidence now also covers supplier delays, supply/inventory pressure, quote/job splitting, scheduling friction, and field-photo synchronization. Official guidance establishes privacy, cybersecurity, employer-record, supplier-risk, and quality-documentation duties; those duties remain contextual or constraint evidence, not proof of user pain. Candidate-specific demand, pricing, and unit economics remain untested.

The opportunity universe deliberately favors overlays, checklists, evidence packets, and exception queues that can begin with manual entry or CSV import. It excludes ERP replacement, payroll, tax filing, regulated accounting advice, medical records, automated employment decisions, and deep multi-year integrations. No candidate is a winner, no Opportunity Score has been assigned, and Gate 2 has not begun.

## Objective and scope

- Authorization: Parent [Issue #3](https://github.com/JamshidiML/venture-studio-os/issues/3) and child [Issue #10](https://github.com/JamshidiML/venture-studio-os/issues/10).
- Gate: 1 — market discovery only.
- Scope: narrow, repetitive administration, quoting, scheduling, documentation, quality records, customer follow-up, inventory coordination, and compliance-preparation friction for SMBs and small teams.
- Geography: United States, United Kingdom, and European Union evidence; candidate applicability is not assumed outside the cited geography.
- Source cutoff and access date: 2026-07-22.
- Candidate count: 14 retained candidates within OPP-2026-600 through OPP-2026-619; six withdrawn concepts are preserved in [EXCLUSIONS.md](EXCLUSIONS.md).
- Explicit exclusions: see [EXCLUSIONS.md](EXCLUSIONS.md).

## Methodology

Research began with official government and regulator evidence, then used first-party product pages only to establish that adjacent paid categories and workflow features exist. Each source record includes date, geography, limitation, confidence, and supported claim in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). Queries and selection decisions are reproducible in [SEARCH_LOG.md](SEARCH_LOG.md).

A candidate qualified when it met all of these Gate 1 conditions:

1. narrow repeated workflow owned by an identifiable SMB buyer and user;
2. at least one traceable source supporting the problem, category, duty, or current alternative, with those evidence roles kept separate;
3. a founder-buildable first path that is not an ERP or system-of-record replacement;
4. an explicit low-scope integration path and manual or CSV fallback;
5. legal, privacy, and security constraints recorded;
6. candidate-specific demand and willingness-to-pay uncertainty left visible.

## Material claims

| Claim ID | Claim | Type | Support | Geography | Confidence | Limitation |
|---|---|---|---|---|---|---|
| C07-01 | The U.S. has 34,752,434 small businesses and 81.9% are nonemployer firms. | evidence | S07-01, published 2024-07-23 | U.S. | high | Establishes a broad segment, not demand for any wedge. |
| C07-02 | In the 2024 UK study, administrative errors and technical failures were reported contributors to late payments, and small businesses more often reported customers paying beyond agreed terms. | evidence | S07-02, published 2024-09-19 | UK surveyed businesses | high | Self-reported survey; sector effects were not definitive. |
| C07-03 | Micro firms in that study often avoided formal collection to protect customer relationships. | evidence | S07-02 | UK micro businesses | high | Does not prove automated reminders improve payment. |
| C07-04 | Paid field-service products offer quoting, scheduling, customer communication, invoicing, and follow-up workflows. | evidence | S07-10, accessed 2026-07-22 | Vendor-defined market | medium | Vendor page proves availability and category spend, not unmet need or candidate WTP. |
| C07-05 | Paid inspection platforms offer inspection, report, training, asset, and document-control capabilities. | evidence | S07-11 and S07-12 | Vendor-defined market | medium | Product availability is not evidence of a competitive gap. |
| C07-06 | NIST and ICO publish SMB-specific cybersecurity, privacy, processor, retention, and information-security guidance. | evidence | S07-03, S07-04, S07-05, S07-06 | U.S. and UK | high | Guidance applicability varies by business, data, and jurisdiction. |
| C07-07 | UK employers face recurring record and communication duties, including annual-leave/holiday-pay records from 2026 and workplace-pension duties. | evidence | S07-07 and S07-08 | UK employers | high | This report does not interpret law or automate entitlement decisions. |
| C07-08 | NIST MEP describes quality-management systems and supplier-risk work as relevant to small manufacturers. | evidence | S07-09 and S07-13 | U.S. manufacturers | medium-high | Evidence is sector-specific and not a prevalence estimate. |
| C07-09 | A CSV-first overlay should usually impose less migration and integration burden than replacing an SMB system of record. | inference | C07-04 through C07-08 | SMB software adoption | medium | Must be tested against real stacks and switching costs. |
| C07-10 | Compliance-oriented candidates should assemble evidence and human review queues, not make legal, payroll, accounting, safety, or employment decisions. | inference | Scope boundaries plus S07-03 through S07-09 | Multi-jurisdictional | high | Product counsel would still be required before launch. |
| C07-11 | Buyers will prefer a narrow wedge over another all-in-one suite. | assumption | Owner: Strategy Agent | Initial target segments | low | Impact if wrong: narrow-wedge preference cannot support candidate advancement. If later authorized, test by buyer interviews and purchase-intent behavior before Gate 2 scoring. |
| C07-12 | At least 4 of 14 retained workflows will be reported weekly-or-more often by a majority of a relevant future interview sample. | hypothesis | Measure: self-reported frequency; success: at least 6 of 10 relevant buyers for at least four workflows; kill: fewer than 3 workflows meet that threshold; time box: 14 days after separate validation authorization | Future bounded samples | low | No outreach is authorized or performed in Gate 1. |
| C07-13 | Census BTOS/SBPS results show that U.S. small businesses directly reported domestic and foreign supplier delays, although reported incidence declined by the latest 2023 period discussed. | evidence | S07-15 | U.S. businesses | high | Supports supplier-delay occurrence, not a software remedy or current 2026 prevalence. |
| C07-14 | In NFIB's 2024 member survey, cost of supplies/inventories was a highly ranked owner problem. | evidence | S07-16 | U.S. NFIB small-business owners | medium-high | Membership sample and advocacy context; does not establish reorder-process friction. |
| C07-15 | Current verified field-service user reviews describe quote/job splitting and scheduling limitations alongside use of scheduling, quotes, invoices, and customer communication. | evidence | S07-17, S07-18 | Self-selected field-service software reviewers | medium | Qualitative/self-selected evidence; no prevalence, causality, or candidate WTP claim. |
| C07-16 | A 2026 hands-on editorial test reported field-photo synchronization friction in a field-service workflow. | evidence | S07-19 | One editorial test | medium | Single-product observation; cannot be generalized to all field-service teams. |

## Opportunity universe

| Opportunity ID | Recurring problem | Affected segment | Current alternative | Problem claim type; support | Confidence | Automatic blocker |
|---|---|---|---|---|---|---|
| OPP-2026-600 | Invoice packets fail customer requirements and enter exception loops. | B2B service SMBs | Email, PDFs, accounting notes | inference; C07-02 | medium | None identified; no accounting advice. |
| OPP-2026-601 | Owners chase overdue invoices inconsistently while protecting relationships. | Micro B2B firms | Calendar reminders and email | inference; C07-02, C07-03 | medium-high | None identified; human approves messages. |
| OPP-2026-602 | Accepted quotes need manual restructuring or context repair when converted into multiple jobs. | Small field-service teams | Field-service suite plus manual notes | inference; C07-15 | medium | Direct evidence is product-specific and self-selected. |
| OPP-2026-604 | Field photos can fail to synchronize into the office job record promptly. | Mobile service crews | Field-service suite, camera roll, manual retry | inference; C07-16 | medium-low | Customer/location data minimization required; single-test evidence only. |
| OPP-2026-605 | Scheduling changes and route constraints require repeated manual reshuffling. | Small field-service teams | Field-service calendar plus manual adjustment | inference; C07-15 | medium-low | Cancellation-capacity recovery itself remains unsupported and was narrowed out. |
| OPP-2026-606 | Recurring visits need a consistent completion-evidence packet across job forms and photos. | Cleaning, maintenance, inspection services | Job forms/photos in field-service or inspection suites | inference; C07-15, C07-16 | low-medium | Current-alternative evidence is stronger than unmet-gap evidence. |
| OPP-2026-608 | Supplier delays are discovered after customer commitments are at risk. | Small makers and installers | Inbox and spreadsheet | inference; C07-13 | medium | Direct evidence establishes delays, not discovery timing or the proposed workflow. |
| OPP-2026-609 | Inventory pressure creates a need to review reorder decisions and ownership. | Small wholesalers and workshops | Whiteboard and spreadsheet | inference; C07-14 | low | Survey supports cost pressure, not the approval-trail problem; no autonomous purchasing. |
| OPP-2026-612 | Training and credential evidence expires without an owner. | Small employers and contractors | Calendar plus document folder | inference; C07-07, C07-08 | medium | Reminder only; no eligibility decision. |
| OPP-2026-613 | Nonconformance actions lose owners and evidence. | Small manufacturers | Spreadsheet and email | inference; C07-05, C07-08 | medium-high | Human quality authority remains accountable. |
| OPP-2026-614 | Inspection evidence is difficult to assemble for customers or auditors. | Small suppliers and service firms | PDFs and folders | inference; C07-05, C07-08 | medium | Evidence assembly only; no certification claim. |
| OPP-2026-617 | Data access/deletion requests lack a deadline and evidence trail. | UK SMBs handling personal data | Inbox and manual checklist | inference; C07-05, C07-06 | medium-high | Legal review; data minimization and access control. |
| OPP-2026-618 | Vendor security questionnaires repeatedly recreate the same evidence. | SMB suppliers to larger firms | Spreadsheets and shared folders | inference; C07-03, C07-06 | medium | No unsupported compliance attestation. |
| OPP-2026-619 | Offboarding and periodic access checks are incomplete across small teams. | Digitally enabled SMBs | Manual checklist | inference; C07-03, C07-06 | medium-high | Never collect passwords; least privilege and audit logs. |

Detailed buyer, user, frequency, workaround, integration, sales/WTP, and security records are in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

## Candidate-to-source coverage matrix

`—` means no qualifying evidence was found. Vendor features and regulatory duties are never counted as direct problem evidence.

| Candidate | Direct problem evidence | Context / population evidence | Current-alternative evidence | Technical feasibility evidence | Legal / privacy / safety / platform evidence | Unsupported assumption or hypothesis |
|---|---|---|---|---|---|---|
| OPP-2026-600 | S07-02: invoicing/admin errors | S07-01 | S07-10 vendor invoicing feature | —; CSV/PDF path is inference | S07-03 to S07-06 controls | Exact preflight failure rate and WTP |
| OPP-2026-601 | S07-02: payment delay and relationship restraint | S07-01 | S07-10 vendor reminder feature | —; CSV path is inference | Contact/privacy controls inferred from S07-05, S07-06 | Message effectiveness and WTP |
| OPP-2026-602 | S07-17: user-reported quote/job splitting friction | S07-18 | S07-10, S07-17 field-service suite | —; import path is inference | Customer/site-data controls | Prevalence, severity, WTP |
| OPP-2026-604 | S07-19: field-photo sync friction in one test | S07-18 | S07-10, S07-19 field-service suite | S07-19 demonstrates an incumbent path, not this wedge | Image/location privacy controls | Generalizability and WTP |
| OPP-2026-605 | S07-17: scheduling/route limitations | S07-18 | S07-10, S07-17 field-service calendar | —; calendar import is inference | Consent/anti-spam boundary | Frequency, avoided capacity loss, WTP |
| OPP-2026-606 | S07-17, S07-19: job forms/photo workflow observations | S07-18 | S07-10 to S07-12 | Incumbent paths exist; wedge feasibility untested | Image/site privacy; no certification | Unmet gap, packet frequency, WTP |
| OPP-2026-608 | S07-15: directly reported supplier delays | S07-16 | Inbox/spreadsheet is assumption | —; CSV/forwarding path is inference | Supplier confidentiality | Discovery timing, severity, WTP |
| OPP-2026-609 | —; S07-16 is inventory-cost context only | S07-15, S07-16 | Whiteboard/spreadsheet is assumption | —; CSV path is inference | No autonomous purchasing | Approval-trail problem, frequency, WTP |
| OPP-2026-612 | —; S07-07, S07-08 establish duties | S07-07, S07-08 | S07-11 vendor training feature | —; calendar/file path is inference | Employment/eligibility boundary | Expiry pain, frequency, WTP |
| OPP-2026-613 | —; S07-09 establishes QMS category | S07-09 | S07-11, S07-12 vendor QMS features | —; CSV path is inference | Human quality authority | Action-loss frequency, WTP |
| OPP-2026-614 | —; S07-09 establishes audit category | S07-09 | S07-11, S07-12 vendor inspection features | —; file export is inference | No certification guarantee | Assembly burden, frequency, WTP |
| OPP-2026-617 | —; S07-05, S07-06 establish privacy duties | S07-05, S07-06 | Inbox/checklist is assumption | — | Direct legal/privacy constraint evidence S07-05, S07-06 | Workflow pain, frequency, WTP |
| OPP-2026-618 | —; S07-03, S07-04 establish security controls | S07-03, S07-04 | Spreadsheet/folder is assumption | — | Security/attestation constraints S07-03, S07-04, S07-06 | Rework frequency, WTP |
| OPP-2026-619 | —; S07-03, S07-04 establish access controls | S07-03, S07-04 | Manual checklist is assumption | — | Least-privilege controls S07-03, S07-04, S07-06 | Incompleteness rate, WTP |

## Analytical interpretation

The evidence supports recurring workflow categories, not a winner. Invoice/payment administration has the best direct pain evidence in this pass. Quality, privacy, security, and employment records have strong evidence of duties or controls but weaker candidate-specific WTP evidence. Scheduling, inventory, and customer-follow-up wedges are supported mainly by the existence of paid adjacent systems and by workflow inference, so they remain lower-confidence.

Candidate diversity remains broad, but evidence quality now controls inclusion. Six unsupported concepts were withdrawn rather than preserved for numerical symmetry. The 14 retained rows include payment, field-service, supply/inventory, employer-record, quality, privacy, and security workflows; seven still lack direct candidate-level problem evidence and are explicitly low-confidence assumptions/inferences.

## Legal, safety, privacy, integration, and sales boundaries

- Default to manual entry or CSV import; an API is optional until officially verified for a named implementation.
- Store the minimum customer, staff, supplier, and site data; encrypt in transit and at rest; use role-based access, audit logs, deletion controls, and incident response.
- Do not automate employee eligibility, leave/pay calculations, payment execution, tax/accounting treatment, safety certification, legal conclusions, or customer entitlement.
- A product touching regulated evidence must say “prepare for human review,” not “guarantee compliance.”
- Likely founder distribution routes are trade associations, accountants/bookkeepers as non-advisory channels, MSPs, quality consultants, and vertical service communities; these are assumptions, not validated channels.
- Adjacent paid products are WTP proxies only. No price, conversion, or customer-demand claim is made.

## Risks, assumptions, and unknowns

The full register is [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md). The highest-impact gaps are candidate-specific workflow frequency, verified buyer authority, direct WTP, incumbent feature overlap, real export/API availability, implementation burden, jurisdiction-specific legal review, and founder distribution access.

## Confidence assessment

Overall confidence is medium. Source quality is high for the claims official sources actually make. Confidence in opportunity attractiveness is low to medium because no interviews, usage telemetry, purchase tests, or competitor teardown were authorized. This evidence ceiling does not prevent a complete Gate 1 artifact because uncertainty is explicit and no candidate is advanced.

## Quality and lifecycle

The first complete draft scored 88/100. Earlier Codex review sections are now correctly labeled Internal Governance Simulation. External Governance Cycle 1 assigned the authoritative 92/100 and opened EXT-GOV-01. Correction Cycle 2 adds independent workflow evidence, removes six unsupported concepts, and makes the evidence-role matrix auditable. The new creator execution score is 100/100; no new independent Governance score is claimed. See [QUALITY_SCORE_HISTORY.md](QUALITY_SCORE_HISTORY.md) and [CORRECTION_LOG.md](CORRECTION_LOG.md).

## Recommended next action

External Governance re-review requested. Keep Gate 1 open and do not rank, select, validate, or perform due diligence on a candidate.
