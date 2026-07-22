---
status: in-review
version: 0.1.2
owner_role: Strategy Agent
last_reviewed: 2026-07-22
thread_id: T02
issue_number: 5
gate: 1
---

# T02 Exclusions

| Space considered | Decision | Reason / rule |
|---|---|---|
| Diagnosis, symptom interpretation, treatment recommendation, or clinical decision support | excluded | Explicit clinical boundary; high safety and regulatory risk. |
| Medication dosing, adherence claims, prescription reconciliation, or pharmacy integration | excluded | Issue #5 excludes prescription management requiring clinical integration; medication errors can cause harm. |
| Fall, seizure, wandering, or emergency detection/dispatch | excluded | Would create emergency-response reliance and surveillance risk. |
| Covert location, camera, microphone, device-activity, or home-presence monitoring | excluded | No informed consent; disproportionate privacy and abuse risk. |
| Caregiver dashboard with default or irreversible visibility | excluded | Violates care-recipient agency and revocable consent. |
| Insurance eligibility, underwriting, or benefits determination | excluded | Finance/regulatory boundary and risk of discriminatory decisions. |
| Professional home-care staffing or agency workflow | excluded | SMB/professional operations belong outside T02. |
| Generic family calendar or household command center | excluded | Family coordination belongs to T09 unless specifically bounded to a care-recipient consent workflow. |
| General habit tracker for all consumers | excluded | T01 scope. |
| Bank, bill, or savings organizer for older adults | excluded | The user segment does not override T03's finance boundary. |
| Accessibility overlay injected into third-party websites | excluded | Platform dependency, technical limitations, and T08 overlap; may create false conformance claims. |
| Credential vault or “helper logs in for you” product | excluded | Credential handling, fraud, coercion, and account-terms risk. |
| AI companion presented as a person, therapist, or replacement for human care | excluded | Deception, dependency, and clinical/wellbeing boundary. |
| Age-based persuasion, fear marketing, or cognitive-friction upsells | excluded | Exploits vulnerable users and violates Issue #5. |
| Automatic legal-form or public-benefit eligibility advice | excluded | Legal/jurisdictional risk and overclaiming. |

Cross-thread duplicates must be mapped only during final synthesis. No excluded concept received a T02 opportunity ID.
