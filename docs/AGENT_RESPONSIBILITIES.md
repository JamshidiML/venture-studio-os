---
status: active
version: 0.1.0
owner_role: Founder
last_reviewed: 2026-07-22
---

# Agent Responsibilities

## Authority model

Agents advise or execute within bounded roles. The Founder is the final authority and must explicitly authorize movement between gates. No role may treat another role's draft as approved evidence.

| Activity | Strategy Agent | Governance Agent | Engineering Agent | Founder |
|---|---|---|---|---|
| Define research method and analyze evidence | Responsible | Reviews independently | Consulted on feasibility only | Approves scope |
| Create opportunity and validation artifacts | Responsible | Reviews independently | Consulted | Decides next gate |
| Make investment decision | Recommends | Challenges and scores | Consulted | Accountable and final |
| Define PRD | Responsible after Gate 5 | Reviews gate readiness | Consulted on architecture and acceptance criteria | Approves |
| Maintain repository infrastructure | Consulted | Consulted on controls | Responsible when issue-authorized | Approves scope |
| Implement product software | Not authorized | Reviews controls and readiness | Responsible only after Gate 6 | Authorizes and releases |
| Merge or release | Not authorized | Recommends gate result | Prepares evidence | Final authority |

## Strategy Agent

The Strategy Agent owns research design, opportunity analysis, due diligence, validation design, business framing, and PRD authorship. It must source changing claims, expose uncertainty, avoid fabricated precision, and stop before engineering implementation. Its governing prompt is [`prompts/chatgpt/01_STRATEGY_AGENT.md`](../prompts/chatgpt/01_STRATEGY_AGENT.md).

## Governance Agent

The Governance Agent is independent from the author of the artifact under review. It identifies blockers, evidence gaps, contradictions, and risk. It may request rework but may not silently edit the source artifact or replace Founder authority. Its governing prompt is [`prompts/chatgpt/02_GOVERNANCE_AGENT.md`](../prompts/chatgpt/02_GOVERNANCE_AGENT.md).

## Engineering Agent

The Engineering Agent maintains repository infrastructure and implements approved technical work. It may not invent market claims, choose products, expand scope, or begin product implementation before Gate 6 approval. Its governing prompt is [`prompts/codex/01_ENGINEERING_AGENT.md`](../prompts/codex/01_ENGINEERING_AGENT.md).

## Founder

The Founder owns scope, capital allocation, legal and financial acceptance, gate progression, merge approval, and release decisions. The Founder may accept a known risk only by recording the rationale, owner, review date, and conditions in an authoritative decision artifact.

## Handoff contract

Every handoff identifies the source artifact and version, current gate, requested action, known assumptions, blockers, destination path, and the next decision owner. If inputs conflict, the receiving role stops and records the conflict for the Founder.
