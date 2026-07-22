---
status: in-review
version: 0.4.0
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

## Hypothesis Watchlist

These seven records were part of the 14-candidate Cycle-2 auditable universe but are not Qualified Gate 1 Candidates in Cycle 3. They remain owned by T07 and retain their complete Issue #10 candidate contracts for possible future research. They are not withdrawn, ranked, selected, or authorized for Gate 2.

### Preserved Issue #10 candidate contracts

| ID | Original concept; buyer / user; claim type | Workflow frequency and workaround | Evidence searched | Integration reality and fallback | Sales route and WTP evidence | Legal / security / safety constraints | Current confidence |
|---|---|---|---|---|---|---|---|
| OPP-2026-609 | Low-stock reorder review packet; owner / stock coordinator; problem type: inference | Frequency unverified; whiteboard or spreadsheet | S07-15 and S07-16; supplier-delay and inventory-cost evidence, not approval-trail pain | Read-only inventory CSV; human approval; fallback reorder worksheet | Wholesaler/maker communities; candidate WTP untested | No autonomous purchase, payment, or forecasting claim; audit approvals | low |
| OPP-2026-612 | Training/credential evidence calendar; owner / admin and worker; problem type: inference | Monthly plus expiry events; calendar and folders | S07-07, S07-08 recurring employer duties; S07-11 vendor category | Manual/CSV dates and document links; fallback reminder export | Employer advisers/trade bodies; paid training category S07-11, candidate WTP untested | Reminder/evidence only; no employment, eligibility, leave, payroll, or pension decision | medium |
| OPP-2026-613 | Nonconformance follow-up queue; quality owner / action owner; problem type: inference | Per defect/audit finding; spreadsheet and email | S07-09 QMS guidance plus S07-11 and S07-12 vendor alternatives | CSV/manual record; optional QMS export later; fallback action log | MEP/quality consultants; paid inspection category S07-11 | Human quality approval; tamper-evident history; sensitive customer data controls | medium-high |
| OPP-2026-614 | Audit/inspection evidence binder; quality owner / admin; problem type: inference | Per audit/customer request; folders and PDFs | S07-09 audit/QMS context plus S07-11 and S07-12 vendor alternatives | Selected-file links and exports; no certificate generation; fallback indexed ZIP/PDF | Quality consultants and supplier networks; paid category proxy S07-11 | No certification guarantee; access, redaction, retention, provenance | medium |
| OPP-2026-617 | Data-rights request tracker; owner/privacy lead / admin; problem type: inference | Event-driven with deadlines; inbox and checklist | S07-05 and S07-06 UK privacy duties and controls | Manual intake and evidence links; no broad data scanning; fallback regulator checklist | MSPs/privacy advisers; no direct WTP evidence | Legal review required; identity verification, least privilege, audit log, deletion | medium-high |
| OPP-2026-618 | Vendor-security evidence reuse library; owner/security lead / proposal admin; problem type: inference | Per questionnaire/renewal; spreadsheets and folders | S07-03, S07-04, and S07-06 security controls; procurement need remains inferred | Curated evidence snippets/files; no automatic attestations; fallback export bundle | MSPs/quality consultants; no direct WTP evidence | Never assert unsupported compliance; strict access, expiry, provenance | medium |
| OPP-2026-619 | Access-review and offboarding checklist; owner/IT lead / manager; problem type: inference | Per joiner/leaver plus periodic review; manual list | S07-03, S07-04, and S07-06 access-control guidance | Manual system register first; verified admin APIs only later; fallback signed checklist | MSP channel; adjacent security spend only, WTP untested | Never collect passwords; least privilege, MFA, audit history, human revocation | medium-high |

### Qualification gap and reconsideration record

| ID | Why not currently qualified | Missing evidence | Conditions required for reconsideration | Original Thread ownership |
|---|---|---|---|---|
| OPP-2026-609 | Inventory-cost context does not directly establish reorder approval-trail or ownership pain. | Observed SMB reorder review workflow, failure frequency, impact, buyer/user behavior, and candidate WTP. | Independent SMB workflow evidence must observe the bounded approval/ownership failure; autonomous purchasing remains prohibited. | T07 — SMB micro-SaaS |
| OPP-2026-612 | Employer duties and vendor training features do not directly establish evidence-expiry pain. | Observed expiry/evidence workflow, missed-event frequency, current workaround dissatisfaction, and WTP. | Direct or clearly adjacent SMB workflow evidence must support the bounded calendar job; no eligibility or employment decision may be added. | T07 — SMB micro-SaaS |
| OPP-2026-613 | QMS guidance and vendor features establish a category and constraints, not owner-loss pain. | Observed nonconformance follow-up failure, recurrence, impact, and independent alternative/friction evidence. | Independent small-manufacturer workflow evidence must support the proposed queue while preserving human quality authority. | T07 — SMB micro-SaaS |
| OPP-2026-614 | Audit duties and vendor features do not establish evidence-assembly burden at the proposed granularity. | Observed evidence-assembly workflow, time/failure burden, current alternative dissatisfaction, and WTP. | Independent SMB workflow evidence must show recurring binder assembly pain; no certification or compliance guarantee may be claimed. | T07 — SMB micro-SaaS |
| OPP-2026-617 | Privacy duties are legal/context evidence, not direct evidence of request-tracking pain. | Observed SMB data-rights workflow, missed-deadline/evidence-trail failure, recurrence, and buyer authority. | Independent privacy-lead/admin workflow evidence plus jurisdiction-specific legal review is required; identity, minimization, and audit controls remain mandatory. | T07 — SMB micro-SaaS |
| OPP-2026-618 | Security-control guidance does not establish repeated questionnaire rework or a paid gap. | Observed questionnaire reuse workflow, rework frequency, approval authority, current alternatives, and WTP. | Independent supplier workflow evidence must establish recurring rework; unsupported attestations remain prohibited. | T07 — SMB micro-SaaS |
| OPP-2026-619 | Access-control guidance does not establish offboarding incompleteness in small teams. | Observed joiner/leaver/access-review failures, frequency, impact, current workaround, and buyer authority. | Independent SMB/MSP workflow evidence must support the bounded checklist; password collection and autonomous revocation remain prohibited. | T07 — SMB micro-SaaS |

External Governance Cycle 3 re-review requested
