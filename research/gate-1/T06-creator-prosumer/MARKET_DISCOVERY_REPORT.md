---
status: in-review
version: 0.4.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# Creator and Prosumer Workflows — Gate 1 Discovery

## Executive Summary

- **The original 20-ID universe is now separated without selecting a product.** Two accessibility workflows qualify for Gate 1 investigation; eighteen unsupported or consolidated concepts remain fully preserved in the Hypothesis Watchlist.
- **Independent and direct workflow evidence now supplements population/vendor context.** ILO documents platform-shaped creative work; ACM practitioner research observes multi-stage workflows; interviews with disabled Kenyan video creators expose accessibility and collaboration barriers. These sources still do not establish demand for a particular preflight, capture tool or browser extension.
- **Rights, permissions and human review are hard constraints.** Copyright, FTC endorsement guidance, W3C accessibility requirements, Chrome extension policy, YouTube authorization/quota rules and C2PA limitations materially narrow feasible concepts.
- **No platform access was invented.** Browser APIs were verified in current first-party documentation; store approval, host access, OAuth scopes, quota extensions and cross-browser parity remain unresolved until later authorization.

## Objective and scope

- Authority: Parent [#3](https://github.com/JamshidiML/venture-studio-os/issues/3) and child [#9](https://github.com/JamshidiML/venture-studio-os/issues/9)
- Gate: 1 — market discovery
- Scope: creators, freelancers, prosumers and knowledge workers using lightweight web apps, browser extensions and personal publishing/production tools
- Geography: U.S. creator and legal context; globally relevant web standards; first-party browser/platform policies
- Source cutoff/access date: 2026-07-22
- IDs: OPP-2026-500 through OPP-2026-519 only
- Excluded: SMB enterprise operations, education, platform companions, social clones, circumvention, spam, deepfakes, deceptive engagement and unrelated consumer/finance/health tools

## Methodology

Research first established creator context, then sought direct practitioner evidence and verified legal, accessibility, extension and API constraints. Cycle 3 qualifies only direct observed problem evidence or clearly adjacent observed workflow evidence. Creator population, broad multi-stage context, rights rules, standards, API documentation and platform feasibility do not independently qualify a tool. Unsupported ideas remain auditable in the Hypothesis Watchlist; no extension or integration is authorized.

See [SOURCE_REGISTER.md](SOURCE_REGISTER.md), [SEARCH_LOG.md](SEARCH_LOG.md), [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md), [EXCLUSIONS.md](EXCLUSIONS.md) and [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md) for the audit trail.

## Evidence-backed findings

### A real creator segment exists, but tool demand is not quantified

The U.S. Census Bureau identifies 1,043,306 individual proprietorships in independent artists, writers and performers in 2023 among the gig-related industries it highlighted (C01). Patreon’s 2025 vendor survey covers 1,007 creators across multiple formats (C02). ILO independently describes how platform control, instability and IP/fair-compensation concerns shape creative work (C15). **Inference:** multi-format individual workflows are a valid discovery scope. **Limitation:** none measures pain frequency or WTP for these candidates.

### Direct practitioner evidence confirms multi-stage and accessibility work, not candidate demand

An ACM study directly captured interviews, project videos and survey responses from creative practitioners working across GenAI project stages (C16). Interviews with 20 Kenyan video creators with sensory impairments found staged and collaborative creation shaped by accessibility and infrastructure barriers (C17). These sources strengthen the existence of creator-controlled multi-stage and accessibility work. They do not independently validate browser capture (500–503), rights ledgers, composite release preflights or paid demand.

### Rights and disclosure checks recur across creator workflows

Copyright grants owners exclusive reproduction, distribution and derivative-work rights (C07); the Copyright Office’s AI report preserves a human-authorship threshold (C06). FTC’s revised guides make disclosure placement and deceptive reviews material (C08). **Inference:** these constraints support exploring rights ledgers, attribution checks, reuse matrices and sponsor-disclosure preflights as candidate workflows, not automated legal advice.

### Accessibility is a production task, not a one-click claim

W3C guidance distinguishes captions, transcripts and description of visual information and notes that automatic captions need editing (C09). C17 adds direct creator evidence that accessibility work is staged and collaborative. Cycle 3 consolidated 509 into 507. Qualified 507 covers time-based media caption/transcript QA; qualified 510 remains distinct because its event, input and output concern contextual image alt text. Both require human review, certify no conformance and assume no platform API.

### Browser extensions can support capture workflows only under least privilege

Chrome documents side-panel and storage surfaces (C13–C14), while store policies require a narrow single purpose, minimal permissions, disclosure and consent (C03–C04). MDN documents meaningful browser differences (C05). **Implication:** browser candidates must minimize host access, provide transparent data handling and treat cross-browser support as unverified.

### Platform APIs are optional dependencies, not assumed infrastructure

YouTube’s current documentation requires OAuth for caption operations and separates listing from download (C11); quota beyond the default requires compliance audit (C10). Candidates keep manual or file-based fallbacks and do not assume arbitrary caption access, scraping or quota extension.

### Provenance standards help record claims but do not prove truth

C2PA 2.2 defines Content Credentials structures (C12). Candidate 519 may inspect or annotate available credentials, but missing credentials remain unknown and a credential is not itself proof that content is truthful.

## Opportunity universe

The original universe contains **2 Qualified Gate 1 Candidates** and **18 Hypothesis Watchlist Candidates**. [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md) contains the qualified set, distinctness test, T06/T08 boundary and full status matrix; [EXCLUSIONS.md](EXCLUSIONS.md) preserves every watchlist contract. No ranking, winner selection or Gate 2 action occurred.

## Risks, assumptions and unknowns

1. **Assumption:** creators may value preflight and traceability workflows enough to change existing spreadsheet/checklist habits. Owner: Strategy Agent. Impact if wrong: the workflow candidates have no switching rationale and cannot advance on this basis. Planned review/test: consented workflow and switching-cost research only after separate authorization; evidence is not yet direct.
2. **Assumption:** per-release and per-project events may create ethical repeat use. Owner: Strategy Agent. Impact if wrong: the repeat-use mechanisms cannot support advancement or a retention claim. Planned review/test: only if a later Gate 5 issue separately authorizes validation, define a consented event-cadence study before treating this as a hypothesis; no measure or threshold is authorized at Gate 1.
3. **Unknown:** candidate-specific WTP; creator population and direct-fan interest are not payment evidence for software.
4. **Risk:** an extension can lose trust or approval if it over-requests access or handles browsing data beyond a single purpose.
5. **Risk:** rights, disclosure and accessibility helpers can create false assurance unless their output is explicitly user-reviewed.
6. **Evidence ceiling:** only 507 and 510 qualify, and only for investigation. The other 18 IDs remain watchlisted; qualified rows still lack representative demand, WTP, retention and effect evidence.

## Confidence assessment

Confidence is **high for the cited legal, policy, standards and API constraints**, **medium for the existence of a diverse creator segment**, and **low for candidate-specific pain intensity, WTP, retention and switching behavior**. The vendor survey’s incentives reduce independence and are visible in the register.

## Recommended next action

Request external Governance Cycle 3 re-review of the qualified/watchlist distinction and accessibility consolidation. Do not rank candidates, begin due diligence or validation, write a PRD, build an extension or implement software.

External Governance Cycle 3 re-review requested
