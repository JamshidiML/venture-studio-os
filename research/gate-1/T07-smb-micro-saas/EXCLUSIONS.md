---
status: in-review
version: 0.3.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T07 Exclusions

| Excluded space | Reason and boundary applied | Evidence or authority |
|---|---|---|
| Enterprise ERP replacement | Violates the narrow, founder-buildable wedge and integration boundary. | Issue #10 |
| Payroll, tax filing, bookkeeping decisions, regulated accounting advice | Explicitly excluded; financial workflows here stop at evidence and exception preparation. | Issue #10 |
| Pension contribution or eligibility engine | Would enter payroll/regulated employment decisions; OPP-612 is reminder/evidence only. | Issue #10; S07-08 |
| Automated leave entitlement or holiday-pay calculation | High consequence and jurisdiction-dependent; only evidence/calendar support is permitted. | Issue #10; S07-07 |
| Automated hiring, firing, performance, or worker-eligibility decisions | High-stakes employment decisions are prohibited. | Issue #10 |
| Medical records or clinical workflow | Explicitly outside scope. | Issue #10 |
| Tax/VAT submission or penalty optimization | Tax filing and advice are excluded even though administrative friction exists. | Issue #10 |
| Autonomous debt collection or payment execution | Creates relationship, conduct, and financial risk; OPP-601 requires human approval. | S07-02 and scope restrictions |
| Legal contract generator or change-order enforceability opinion | Evidence trails may support human review but cannot provide legal advice. | Scope restrictions |
| Safety/quality certification issuer | A tool cannot certify compliance or replace qualified human authority. | S07-09 |
| Autonomous purchasing/reorder execution | OPP-609 is an approval packet, not a purchasing agent. | Founder-buildable and safety boundary |
| Broad CRM, field-service suite, inventory system, or all-in-one SMB OS | Too broad; likely competes as a system of record and requires deep migration. | Issue #10 |
| Creator/prosumer, general consumer, education, health, finance, accessibility, or platform companions | Reserved for other independent threads. | Issue #10 and Parent #3 |
| Unauthorized scraping, credential collection, or private APIs | Security and platform-risk boundary. | Evidence rules and Issue #10 |

Rejected concepts remain excluded even if they appear commercially attractive. Nothing here authorizes Gate 2.

## Correction Cycle 2 candidate withdrawals

These rows are preserved for audit history and are no longer counted as retained candidates.

| Opportunity ID | Withdrawn concept | Reason |
|---|---|---|
| OPP-2026-603 | Change-order acknowledgement ledger | Vendor quote features did not establish acknowledgement-trail pain; legal/workflow evidence was insufficient. |
| OPP-2026-607 | Waitlist backfill coordinator | Scheduling-category availability did not establish duplicated waitlist outreach or its frequency. |
| OPP-2026-610 | Purchase-order/receipt mismatch triage | Late-payment and supply-risk sources did not establish unassigned PO/receipt mismatch pain. |
| OPP-2026-611 | SOP revision acknowledgement | Inspection/document-control vendor features established an alternative, not direct acknowledgement failure. |
| OPP-2026-615 | Customer promise tracker | No direct evidence established lost promises in the specified owner-led SMB segment. |
| OPP-2026-616 | Warranty/return evidence packet | No source established packet-assembly pain; a broad field-service product page was not qualifying evidence. |
