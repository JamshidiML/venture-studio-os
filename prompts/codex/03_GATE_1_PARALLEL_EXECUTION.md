---
status: active
version: 0.1.0
owner_role: Engineering Agent
last_reviewed: 2026-07-22
---

# Codex Gate 1 Parallel Execution Contract

## Mission

Coordinate ten independent Gate 1 market-discovery execution threads in `JamshidiML/venture-studio-os` using Parent Issue #3 and child Issues #4 through #13.

Do not collapse the work into one thread, one branch, or one combined report. Do not begin Gate 2, select a product, perform due diligence, validate an MVP, create a PRD, or implement product software.

## Required startup

1. Read merged `main` and confirm Foundation commit `5d98c570c866405d8b63698bcacc81dce04e8236` is present.
2. Read Issues #3–#13 and the repository governance documents.
3. Confirm the ten pre-created branches exist.
4. Create or use exactly ten isolated worktrees/execution contexts, one per child issue.
5. Start all ten threads without waiting for another thread's output.

## Thread mapping

| Thread | Issue | Branch |
|---|---:|---|
| T01 | #4 | `gate1/t01-consumer-utilities` |
| T02 | #5 | `gate1/t02-aging-accessibility` |
| T03 | #6 | `gate1/t03-household-economics` |
| T04 | #7 | `gate1/t04-learning-career` |
| T05 | #8 | `gate1/t05-wellbeing` |
| T06 | #9 | `gate1/t06-creator-prosumer` |
| T07 | #10 | `gate1/t07-smb-micro-saas` |
| T08 | #11 | `gate1/t08-platform-companions` |
| T09 | #12 | `gate1/t09-family-household` |
| T10 | #13 | `gate1/t10-ai-native-whitespace` |

## Per-thread execution

Each thread must:

- follow its GitHub issue exactly
- follow `prompts/chatgpt/03_MARKET_DISCOVERY.md`
- follow `docs/EVIDENCE_AND_CONFIDENCE_RULES.md`
- use current sources and record access/publication dates
- create every required artifact in its assigned output directory
- use only its reserved opportunity-ID range
- run repository validation and relevant tests
- maintain `QUALITY_SCORE_HISTORY.md` and `CORRECTION_LOG.md`
- self-score with `templates/THREAD_QUALITY_SCORECARD.md`
- open a separate draft PR linked to its child issue
- remain unmerged

If current external research access is unavailable, do not invent sources or market findings. Record the exact access blocker, complete only repository work that remains valid, and report the honest evidence ceiling.

## Quality loop

For every thread:

1. Produce the first complete draft.
2. Calculate the creator Artifact Quality Score.
3. Request independent Governance review.
4. Apply only evidenced corrections.
5. Rerun validation and update score history.
6. Repeat until Governance awards 100/100 with no critical blocker, or records an evidence ceiling requiring Founder action.

Do not change the Opportunity Score to force a perfect Artifact Quality Score.

## Isolation requirements

- No thread may edit another thread's output directory.
- No thread may reuse another thread's opportunity IDs.
- Shared-policy changes require a separate orchestration PR and must not be hidden inside a research PR.
- Cross-thread duplicates are preserved and mapped only during final synthesis.
- Do not merge, rebase onto another thread, or cherry-pick research content across threads.

## Final Codex report

After creating all ten draft PRs, return one consolidated report containing:

1. thread ID and scope
2. issue link
3. branch
4. worktree/execution-context path or identifier
5. head commit SHA
6. draft PR link
7. candidate count
8. creator score history
9. latest Governance score, if available
10. blockers or evidence ceiling
11. validation results
12. confirmation that all PRs remain draft and unmerged

Also provide a compact executive summary of what was built. Do not produce the Gate 1 final market synthesis until all ten threads have completed their review loops.