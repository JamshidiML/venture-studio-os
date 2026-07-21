---
status: active
version: 0.1.0
owner_role: Governance Agent
last_reviewed: 2026-07-22
---

# Evidence and Confidence Rules

## Claim types

Every material claim must use exactly one type.

| Type | Meaning | Minimum treatment |
|---|---|---|
| `evidence` | Directly supported by an identified source or observed result | Record source, publication or observation date, access date when relevant, and scope |
| `inference` | Reasoned conclusion derived from cited evidence | Link supporting evidence and explain the reasoning |
| `assumption` | Working condition accepted temporarily without proof | Name the owner, impact, and planned test or review |
| `hypothesis` | Falsifiable prediction to test | State measure, success threshold, kill threshold, and time box |

Labels are not interchangeable. Repeating an assumption does not turn it into evidence.

## Confidence

Use `high`, `medium`, or `low` confidence and explain the rating.

- `high` — multiple relevant, recent, independent sources or a strong direct observation agree; material limitations are understood.
- `medium` — evidence is relevant but limited by recency, sample, independence, or indirect measurement.
- `low` — evidence is sparse, old, indirect, conflicting, or primarily assumption-based.

Confidence describes support for a claim, not enthusiasm for an opportunity. A precise number with weak provenance remains low confidence.

## Source record

For each external fact, record title or source owner, URL or repository path, publication or observation date, access date when useful, claim supported, geography or segment, and limitations. Use ISO dates. If no date is available, record `date unavailable` and lower confidence rather than inventing one.

## Quantitative claims

- Preserve units, currency, time period, geography, denominator, and calculation method.
- Separate reported values from estimates and scenarios.
- Use ranges when inputs do not justify point precision.
- Never invent revenue, downloads, user counts, conversion, market size, or willingness to pay.
- Identify material exclusions and avoid adding incomparable figures.

## Evidence freshness and conflicts

Changing facts must be checked at the time of use. Stale evidence may remain for history but must be marked with its date and limitations. Conflicting credible sources are shown together; the author explains the conflict instead of selecting the most favorable value silently.

## Identifiers and traceability

Opportunities use stable IDs in the form `OPP-YYYY-NNN`. The ID remains fixed through screening, due diligence, validation, decision, and product-definition artifacts. Artifacts link claims to sources and later decisions back to the reviewed artifact version.

## Sensitive evidence

Collect only data needed for the authorized question. Do not place credentials, unnecessary personal data, private interview recordings, or licensed source content in the repository. Summaries must preserve consent, confidentiality, and source limitations.
