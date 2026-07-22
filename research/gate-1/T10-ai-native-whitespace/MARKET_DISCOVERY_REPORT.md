---
status: in-review
version: 0.2.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T10 Gate 1 Market Discovery — AI-Native Underserved Workflows

## Executive summary

This thread identifies 20 non-ranked AI-native workflow inferences for researchers, public-interest teams, technical knowledge stewards, archives, and other small expert groups. The candidates focus on high-context transformations that were costly to perform manually: document-to-structure conversion, evidence provenance, cross-document consistency, uncertainty marking, and human-review queues.

Current primary evidence supports three bounded conclusions. First, generative AI exposure is task-level and job transformation is more likely than whole-job replacement. Second, contemporary systems can process long, multimodal documents and produce complex work artifacts, but capability remains jagged and evaluation-sensitive. Third, hallucination, transparency, privacy, copyright, and agent reliability require human oversight and measurable task-specific quality bars. None of this proves candidate demand, willingness to pay, unit economics, or defensibility.

Every candidate therefore specifies a concrete user and old workflow, a proposed lawful data path, human authority, a complete measurable quality hypothesis, a unit-cost risk, a candidate-specific privacy/security treatment, a complete defensibility hypothesis, and a non-AI fallback. No generic chatbot, autonomous high-stakes decision, or candidate belonging primarily to T01–T09 is included.

## Objective and scope

- Authorization: Parent Issue [#3](https://github.com/JamshidiML/venture-studio-os/issues/3), child Issue [#13](https://github.com/JamshidiML/venture-studio-os/issues/13)
- Gate: 1 — market discovery only
- Geography: global technical evidence with US/EU regulatory sources; candidate validation must be local
- Source cutoff and access date: 2026-07-22
- Candidate IDs: `OPP-2026-900` through `OPP-2026-919`
- Exclusions: generic chatbots, thin wrappers, medical/legal/financial advice, high-stakes autonomy, surveillance, impersonation, spam, credential harvesting, copyright circumvention, and opportunities primarily assigned to T01–T09

## Methodology

Research combined official labor/task studies, model-provider evaluation and capability documentation, academic benchmark synthesis, independent agent evaluation, US risk-management guidance, and EU regulatory guidance. Source selection favored current primary evidence and explicit limitations. Candidate generation applied five filters:

1. a concrete existing job with a recognizable input and output;
2. an enabling capability that changed recently (multimodal documents, structured extraction, longer context, tool use, or iterative synthesis);
3. a task-specific measurable quality bar;
4. mandatory human authority for consequential output;
5. a non-AI fallback and no primary ownership by T01–T09.

Source details are in [SOURCE_REGISTER.md](SOURCE_REGISTER.md); queries and negative findings are in [SEARCH_LOG.md](SEARCH_LOG.md). No model benchmark, API call, customer interview, price test, or prototype was executed.

## Material evidence register

| Claim | Type | Source | Scope/date | Confidence | Limitation |
|---|---|---|---|---|---|
| Generative AI exposure varies by task and transformation/augmentation is more plausible than whole-job automation. | evidence | T10-S01, T10-S02, T10-S03 | global occupational index and provider usage studies, 2025–2026 | high | Exposure and observed usage are not productivity, demand, or welfare outcomes. |
| Frontier models can create realistic knowledge-work artifacts and multimodal document systems can extract text, tables, charts, and structure. | evidence | T10-S04, T10-S08, T10-S09 | provider evaluations/docs, current at source date | medium | Provider evidence may not generalize; one-shot results and documented capability are not production reliability. |
| Capability is jagged and benchmark validity, hallucination, and agent completion remain material limitations. | evidence | T10-S05, T10-S06, T10-S11 | academic/independent benchmark synthesis, 2026 | high | Some benchmark results emphasize software or synthetic tasks. |
| GenAI deployment should include risk identification, measurement, governance, and evaluation. | evidence | T10-S07, T10-S12 | NIST cross-sector guidance, 2024 updated 2026 | high | Voluntary framework; implementation is context-dependent. |
| EU AI rules create documentation, transparency, copyright, and risk obligations for relevant providers/deployers. | evidence | T10-S10 | EU, obligations applying 2025–2026 | high | Candidate applicability depends on role and design; not legal advice. |
| Provenance-first, human-reviewed document workflows are safer investigation targets than autonomous decisions. | inference | T10-S04–S12 | cross-source inference | medium | User value, costs, and workflow adoption are untested. |

## Opportunity universe

[OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md) defines 20 candidates across four capability clusters. None is ranked or recommended as a winner.

| ID range | Cluster | Candidates | Common enabling capability |
|---|---|---:|---|
| OPP-2026-900..904 | evidence and provenance | 5 | long-document extraction, citation mapping, structured output |
| OPP-2026-905..909 | research and public knowledge | 5 | multilingual/multimodal synthesis with audit trails |
| OPP-2026-910..914 | data and technical stewardship | 5 | schema inference, consistency checking, document vision |
| OPP-2026-915..919 | review queues and traceable transformations | 5 | cross-document comparison, uncertainty scoring, human escalation |

## Analytical observations

1. **The opportunity unit is a bounded task, not a profession.** ILO and provider usage evidence support augmentation and uneven task exposure; autonomous job replacement is not assumed.
2. **Evaluation is part of the candidate, not a later add-on.** Each concept needs reference cases, field-level accuracy or recall, provenance coverage, and a human rejection path.
3. **Document understanding is enabling but not sufficient.** Official APIs describe PDF and multimodal processing; candidate viability still depends on data rights, layout variance, cost, privacy, and domain-specific error tolerance.
4. **Human oversight must be operational.** “Human in the loop” means named decision authority, surfaced uncertainty, source access, editable structured output, and a non-AI workflow.
5. **Defensibility remains a hypothesis.** Each candidate names a specific approved workflow asset and uses the shared measure, success threshold, kill threshold, and six-week time box in the D-contract in [OPPORTUNITY_INDEX.md](OPPORTUNITY_INDEX.md). None was tested here.

## Legal, safety, privacy, and platform constraints

- Do not use confidential, personal, copyrighted, or licensed documents without a documented lawful data path.
- Preserve source location, transformation history, model/version metadata, and human approval for consequential outputs.
- Define task-specific failure costs; block autonomous action when an error could affect rights, safety, employment, finance, health, or legal status.
- Test multilingual and accessibility performance rather than extrapolating from English benchmarks.
- Provide export and non-AI fallback to limit vendor lock-in and model/API shutdown risk.
- Treat provider benchmark and documentation claims as bounded evidence, not guarantees.
- Obtain legal review for AI Act, privacy, copyright, records-management, and sector duties before deployment.

## Exclusions

Rejected spaces and neighboring-thread boundaries are recorded in [EXCLUSIONS.md](EXCLUSIONS.md). The set excludes generic assistants, autonomous agents making high-stakes decisions, and concepts whose main value is a consumer habit, learning, health, creator, SMB-admin, platform-companion, or family workflow.

## Risks, assumptions, and unknowns

- Direct user pain, buying authority, and willingness to pay are unmeasured.
- Production accuracy, latency, cost, and data residency were not benchmarked.
- Provider documentation changes and multi-vendor parity are not assured.
- Human review may erase time savings on high-error or high-context cases.
- Rights to ingest source documents vary by repository, license, and jurisdiction.
- Workflow-specific defensibility remains untested under the D-contract. Acquisition paths remain Strategy Agent-owned assumptions under the R-contract, with failure impact and a planned separately authorized two-week review.

See [EVIDENCE_GAPS.md](EVIDENCE_GAPS.md) for the honest evidence ceiling and later tests.

## Confidence assessment

Confidence is **high** that model capability and adoption are advancing unevenly and require task-level evaluation. Confidence is **medium** that provenance-first document workflows are technically investigable. Confidence is **low** for candidate-specific demand, production reliability, unit cost, channel, and defensibility. No candidate advances beyond Gate 1.

## Recommended next action

Request independent Governance re-review of corrected version 0.2.0. Do not rank a winner, benchmark or build models, conduct due diligence, define an MVP, or implement software without separate Founder authorization.
