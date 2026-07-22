---
status: in-review
version: 0.2.0
owner_role: Strategy Agent
last_reviewed: 2026-07-22
---

# T10 Source Register

All sources were accessed on 2026-07-22. Provider sources are used for documented capabilities, evaluations, or observed platform usage and are explicitly limited for commercial interest and generalizability.

| ID | Source | Publisher/date | Geography/scope | Material support | Limitations | Confidence |
|---|---|---|---|---|---|---|
| T10-S01 | [Generative AI and Jobs: A Refined Global Index of Occupational Exposure](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) | International Labour Organization; 2025-05-20 | Global task/occupation exposure | Task-level exposure and job transformation framing. | Exposure is modeled potential, not adoption or outcomes. | high |
| T10-S02 | [Anthropic Economic Index: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) | Anthropic; 2026-01 | Sampled Claude usage | Distinguishes augmentation, automation, autonomy, complexity, and task success. | One provider's users; privacy-preserving classifier and selection limits. | medium |
| T10-S03 | [Anthropic Economic Index: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) | Anthropic; 2026-06-26 | Claude conversation/API usage | Shows increasingly long-running agentic use and measurement-method changes. | Provider-authored observational data; not causal productivity evidence. | medium |
| T10-S04 | [Measuring model performance on real-world tasks — GDPval](https://openai.com/index/gdpval/) | OpenAI; 2025-09-25 | 1,320 tasks across 44 US occupations | Realistic file-rich professional deliverables and expert grading; explicit one-shot limits. | Provider-authored; selected occupations/tasks; not production deployment. | medium |
| T10-S05 | [2026 AI Index — Technical Performance](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance) | Stanford HAI; 2026 | Cross-model benchmark synthesis | Capability gains, jagged performance, benchmark saturation, and agent failure rates. | Aggregates heterogeneous benchmarks; some provider-reported inputs. | high |
| T10-S06 | [2026 AI Index — Responsible AI](https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai) | Stanford HAI; 2026 | Cross-model safety/transparency evidence | Hallucination, language, transparency, incident, and safety measurement gaps. | Benchmark definitions vary; not candidate-specific. | high |
| T10-S07 | [AI RMF: Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | NIST; 2024-07-26, updated 2026-04-08 | Cross-sector risk management | Risk identification, measurement, governance, and evaluation expectations. | Voluntary and non-prescriptive. | high |
| T10-S08 | [Gemini API document understanding](https://ai.google.dev/gemini-api/docs/document-processing) | Google AI for Developers; current 2026 documentation | PDF/multimodal document processing | Documents text, image, chart, table, long-PDF, and structured extraction capability. | Vendor-specific limits/features may change; no accuracy guarantee. | high |
| T10-S09 | [OpenAI API models](https://developers.openai.com/api/docs/models) | OpenAI; current at access | Current platform model modalities/tools | Documents text/image input, multilingual/vision, and available tool categories. | Vendor documentation; model names, costs, and limits change. | high |
| T10-S10 | [EU general-purpose AI obligations](https://digital-strategy.ec.europa.eu/en/factpages/general-purpose-ai-obligations-under-ai-act) | European Commission; obligations from 2025-08-02 | EU GPAI providers | Documentation, copyright, transparency, risk, incident, and cybersecurity duties. | Downstream candidate applicability requires legal analysis. | high |
| T10-S11 | [Task-Completion Time Horizons of Frontier AI Models](https://metr.org/time-horizons/) | METR; updated 2026-05-08 | Frontier agents on software tasks | Independent evidence that agent reliability depends on task duration and remains bounded. | Software-task suite; cannot be generalized directly to document workflows. | high |
| T10-S12 | [NIST AI Resource Center](https://airc.nist.gov/) | NIST; current at access | AI testing/evaluation resources | Supports testing, evaluation, verification, and validation as operational requirements. | Resource hub, not performance evidence. | high |

## Source conflicts and interpretation

- Capability documentation (T10-S08/S09) is read alongside independent/jagged-performance evidence (T10-S05/S06/S11).
- Provider work-task studies (T10-S02–S04) demonstrate observed use or benchmark performance, not market demand or net productivity.
- No market-size, revenue, user-count, price, or customer-demand figure is used.
- Candidate confidence remains low where evidence is only cross-workflow inference.
