---
status: in-review
version: 0.2.1
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T07 Gate 1 Market Discovery — SMB Micro-SaaS and Workflow Friction

## Executive summary

This report documents 20 unranked, screening-ready workflow wedges for small businesses and small teams. The strongest direct problem evidence concerns invoice/payment administration; official sources also establish recurring privacy, cybersecurity, employment-record, supplier-risk, and quality-documentation duties. Official paid workflow products show that businesses buy software in adjacent categories, but they do not prove willingness to pay for any candidate here. Candidate-specific demand, pricing, and unit economics remain untested.

The opportunity universe deliberately favors overlays, checklists, evidence packets, and exception queues that can begin with manual entry or CSV import. It excludes ERP replacement, payroll, tax filing, regulated accounting advice, medical records, automated employment decisions, and deep multi-year integrations. No candidate is a winner, no Opportunity Score has been assigned, and Gate 2 has not begun.

## Objective and scope

- Authorization: Parent [Issue #3](https://github.com/JamshidiML/venture-studio-os/issues/3) and child [Issue #10](https://github.com/JamshidiML/venture-studio-os/issues/10).
- Gate: 1 — market discovery only.
- Scope: narrow, repetitive administration, quoting, scheduling, documentation, quality records, customer follow-up, inventory coordination, and compliance-preparation friction for SMBs and small teams.
- Geography: United States, United Kingdom, and European Union evidence; candidate applicability is not assumed outside the cited geography.
- Source cutoff and access date: 2026-07-22.
- Candidate count: exactly 20, using OPP-2026-600 through OPP-2026-619.
- Explicit exclusions: see [EXCLUSIONS.md](EXCLUSIONS.md).

## Methodology

Research began with official government and regulator evidence, then used first-party product pages only to establish that adjacent paid categories and workflow features exist. Each source record includes date, geography, limitation, confidence, and supported claim in [SOURCE_REGISTER.md](SOURCE_REGISTER.md). Queries and selection decisions are reproducible in [SEARCH_LOG.md](SEARCH_LOG.md).

A candidate qualified when it met all of these Gate 1 conditions:

1. narrow repeated workflow owned by an identifiable SMB buyer and user;
2. at least one traceable source supporting the problem category, duty, or paid adjacent workflow;
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
| C07-12 | At least 5 of 20 workflows will be reported weekly-or-more often by a majority of a relevant future interview sample. | hypothesis | Measure: self-reported frequency; success: at least 6 of 10 relevant buyers; kill: fewer than 3 of 10; time box: 14 days after separate validation authorization | Future bounded samples | low | No outreach is authorized or performed in Gate 1. |

## Opportunity universe

| Opportunity ID | Recurring problem | Affected segment | Current alternative | Problem claim type; support | Confidence | Automatic blocker |
|---|---|---|---|---|---|---|
| OPP-2026-600 | Invoice packets fail customer requirements and enter exception loops. | B2B service SMBs | Email, PDFs, accounting notes | inference; C07-02 | medium | None identified; no accounting advice. |
| OPP-2026-601 | Owners chase overdue invoices inconsistently while protecting relationships. | Micro B2B firms | Calendar reminders and email | inference; C07-02, C07-03 | medium-high | None identified; human approves messages. |
| OPP-2026-602 | Accepted quotes lose scope details during job handoff. | Field-service teams | Printed quote and chat | inference; C07-04 | medium | None identified. |
| OPP-2026-603 | Change orders lack a clean acknowledgement trail. | Trades and project services | Email threads and revised PDFs | inference; C07-04 | medium | Must not replace legal review or contract advice. |
| OPP-2026-604 | Field photos and notes do not become timely customer updates. | Mobile service crews | Camera roll and messaging | inference; C07-04 | medium | Customer/location data minimization required. |
| OPP-2026-605 | Cancellations leave appointment capacity unused. | Appointment-based SMBs | Manual callback lists | inference; C07-04 | low-medium | Consent and messaging rules required. |
| OPP-2026-606 | Recurring visits lack a consistent completion-evidence packet. | Cleaning, maintenance, inspection services | Photos plus checklist PDFs | inference; C07-04, C07-05 | medium | Sensitive site images may be prohibited. |
| OPP-2026-607 | Waitlist backfill is slow and duplicates outreach. | Small service teams | Phone/text spreadsheet | inference; C07-04 | low-medium | Human-controlled outreach and opt-out required. |
| OPP-2026-608 | Supplier delays are discovered after customer commitments are at risk. | Small makers and installers | Inbox and spreadsheet | inference; C07-13 | medium | None identified. |
| OPP-2026-609 | Reorder suggestions lack an owner/approval trail. | Small wholesalers and workshops | Whiteboard and spreadsheet | inference; C07-13 | low-medium | No autonomous purchasing. |
| OPP-2026-610 | Purchase-order and receipt mismatches remain unassigned. | Small goods businesses | Email and accounting notes | inference; C07-02, C07-13 | medium | No bookkeeping or payment execution. |
| OPP-2026-611 | Staff cannot prove they saw the current SOP revision. | Small operational teams | Shared folder and sign-off sheet | inference; C07-05, C07-09 | medium | Identity and retention controls required. |
| OPP-2026-612 | Training and credential evidence expires without an owner. | Small employers and contractors | Calendar plus document folder | inference; C07-07, C07-08 | medium | Reminder only; no eligibility decision. |
| OPP-2026-613 | Nonconformance actions lose owners and evidence. | Small manufacturers | Spreadsheet and email | inference; C07-05, C07-08 | medium-high | Human quality authority remains accountable. |
| OPP-2026-614 | Inspection evidence is difficult to assemble for customers or auditors. | Small suppliers and service firms | PDFs and folders | inference; C07-05, C07-08 | medium | Evidence assembly only; no certification claim. |
| OPP-2026-615 | Customer promises made in calls or email are not followed through. | Owner-led service SMBs | CRM notes and memory | inference; C07-04 | low-medium | Recording/transcription consent if used. |
| OPP-2026-616 | Warranty and return cases lack a complete evidence packet. | Small product businesses | Inbox, photos, spreadsheet | inference; C07-04 | medium-low | No automated entitlement determination. |
| OPP-2026-617 | Data access/deletion requests lack a deadline and evidence trail. | UK SMBs handling personal data | Inbox and manual checklist | inference; C07-05, C07-06 | medium-high | Legal review; data minimization and access control. |
| OPP-2026-618 | Vendor security questionnaires repeatedly recreate the same evidence. | SMB suppliers to larger firms | Spreadsheets and shared folders | inference; C07-03, C07-06 | medium | No unsupported compliance attestation. |
| OPP-2026-619 | Offboarding and periodic access checks are incomplete across small teams. | Digitally enabled SMBs | Manual checklist | inference; C07-03, C07-06 | medium-high | Never collect passwords; least privilege and audit logs. |

Detailed buyer, user, frequency, workaround, integration, sales/WTP, and security records are in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md).

## Analytical interpretation

The evidence supports recurring workflow categories, not a winner. Invoice/payment administration has the best direct pain evidence in this pass. Quality, privacy, security, and employment records have strong evidence of duties or controls but weaker candidate-specific WTP evidence. Scheduling, inventory, and customer-follow-up wedges are supported mainly by the existence of paid adjacent systems and by workflow inference, so they remain lower-confidence.

Candidate diversity is intentional: five revenue/quote/payment wedges, three scheduling/field-service wedges, three supply/inventory wedges, four quality/document-control wedges, three customer/privacy evidence wedges, and two security/access wedges. Cross-category overlap is preserved for later synthesis rather than silently removed.

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

The first complete draft scored 88/100. Targeted corrections added claim IDs, field-complete candidate records, source metadata, security/legal boundaries, reproducible queries, and linked hygiene. The corrected creator self-score is 100/100; independent Governance score is pending. See [QUALITY_SCORE_HISTORY.md](QUALITY_SCORE_HISTORY.md) and [CORRECTION_LOG.md](CORRECTION_LOG.md).

## Recommended next action

Request independent Governance review of this version against the 100-point thread scorecard. Keep Gate 1 open and do not rank, select, validate, or perform due diligence on a candidate.
