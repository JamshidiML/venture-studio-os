---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T07 Opportunity Index

This is the unranked set of seven Qualified Gate 1 Candidates. External Governance Correction Cycle 2 withdrew six unsupported concepts; Cycle 3 moved seven guidance/category-led concepts to the [Hypothesis Watchlist](EXCLUSIONS.md#hypothesis-watchlist). “WTP evidence” records only direct evidence found or an explicitly weak proxy. No Opportunity Score, rank, winner, or Gate 2 recommendation is present.

| ID | Wedge; buyer / user; problem claim type | Workflow frequency and workaround | Evidence basis | Integration reality and fallback | Sales route and WTP evidence | Legal / security reality | Confidence |
|---|---|---|---|---|---|---|---|
| OPP-2026-600 | Invoice-requirement preflight; owner/finance lead / admin; problem type: inference | Per B2B invoice; email, PDF, accounting notes | S07-02 directly reports invoicing/admin errors | Read-only CSV/PDF intake; no ledger writes; fallback checklist export | Bookkeepers or B2B service communities; direct WTP absent, paid invoicing is only adjacent proxy S07-10 | Financial/customer data; encrypt, RBAC, retention; never advise accounting treatment | medium |
| OPP-2026-601 | Relationship-aware payment chase queue; owner / admin; problem type: inference | Weekly to daily where overdue; calendar plus ad hoc email | S07-02 direct payment and relationship evidence | Import receivables CSV; user approves every message; fallback reminder list | Bookkeepers/trade groups; direct WTP absent, paid reminder feature proxy S07-10 | No payment execution, harassment, or autonomous messaging; contact data minimization | medium-high |
| OPP-2026-602 | Quote-to-job restructuring checklist; service owner / dispatcher and crew lead; problem type: inference | Per accepted complex quote; field-service suite plus manual notes | S07-17 directly reports difficulty splitting quotes into multiple jobs; S07-18 is category context | CSV/PDF or user entry; optional verified CRM API later; fallback printable handoff | Vertical trade communities; adjacent paid category S07-10/S07-17, candidate WTP untested | Customer/site data; field-level permissions and deletion | medium |
| OPP-2026-604 | Job-photo synchronization exception queue; owner / field technician; problem type: inference | Per photo-bearing visit; field-service suite plus camera roll/manual retry | S07-19 directly observed delayed field-photo sync in one editorial test | Mobile upload; optional job ID import; fallback local retry list/PDF | Field-service communities; adjacent software spend only | Faces, addresses, location and customer consent; redaction and retention needed | medium-low |
| OPP-2026-605 | Schedule/route reshuffle board; owner / scheduler; problem type: inference | Daily as schedules change; field-service calendar and manual adjustment | S07-17 directly reports scheduling/route friction; cancellation recovery was narrowed out | Calendar CSV/manual slots; no auto-booking required; fallback call sheet | Vertical field-service communities; direct candidate WTP absent | Messaging consent, opt-out, time-zone controls; no dark patterns | medium-low |
| OPP-2026-606 | Recurring-visit evidence packet; operations owner / mobile worker; problem type: inference | Per recurring visit; field-service job forms/photos plus folders | S07-17/S07-19 observe job-form/photo workflows; S07-10 to S07-12 are current alternatives | Mobile checklist and export; optional calendar import; fallback PDF packet | Cleaning/maintenance consultants; paid adjacent categories only | Site sensitivity, image consent, least privilege, configurable retention | low-medium |
| OPP-2026-608 | Supplier lead-time exception board; owner / purchasing coordinator; problem type: inference | Weekly/daily for active orders; inbox plus spreadsheet | S07-15 directly reports supplier delays; late discovery remains inferred | CSV and forwarded confirmations; optional vendor portal/API later; fallback exception export | Small-manufacturer networks; no direct WTP evidence | Supplier confidentiality, access control, no automatic commitment changes | medium |

## Coverage check

- The seven qualified IDs and seven watchlist IDs are unique and confined to OPP-2026-600 through OPP-2026-619; together they equal the 14-candidate Cycle-2 auditable universe. Earlier withdrawn IDs 603, 607, 610, 611, 615, and 616 remain separately documented in [EXCLUSIONS.md](EXCLUSIONS.md).
- Each qualified and watchlist record preserves buyer, user, frequency, workaround, evidence, integration/fallback, sales/WTP, legal/security, and confidence.
- No candidate depends on another Gate 1 thread.
- Weak WTP or workflow evidence is carried into [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md), not concealed.
