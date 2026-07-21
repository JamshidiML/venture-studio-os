---
status: active
version: 0.1.0
owner_role: Engineering Agent
last_reviewed: 2026-07-22
---

# Codex Repository Maintenance

## Authorization

Use with [`01_ENGINEERING_AGENT.md`](01_ENGINEERING_AGENT.md) when an approved GitHub issue requests documentation, templates, repository structure, or validation automation. It does not authorize market research, product selection, product implementation, or strategic artifact approval.

## Inputs

- approved issue and acceptance criteria
- authoritative repository artifacts named by the issue
- clean understanding of current branch and worktree changes

## Method

1. Inspect the issue, repository tree, authoritative inputs, and local status.
2. State a concise implementation plan and create `agent/<description>` from the default branch.
3. Make the smallest complete, internally linked change.
4. Preserve role boundaries, lifecycle states, ISO dates, and stable opportunity IDs.
5. Add dependency-free deterministic checks where practical.
6. Run repository validation and relevant tests, then review the complete diff.
7. Commit only scoped files, push the branch, and open a linked draft pull request.

## Stop conditions

Stop and record a blocker when requirements conflict, an authoritative artifact is missing, the worktree contains inseparable unrelated changes, or the requested change would cross a stage-gate boundary. Never resolve those conditions by inventing evidence or silently expanding scope.

## Output contract

Report branch, commit, draft PR, complete file tree, checks and results, assumptions, blockers, rollback, and recommended next governance action. Do not merge.
