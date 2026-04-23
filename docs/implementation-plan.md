# TONPROBE Implementation Plan

## Phase 0 — Foundations

- Initialize Python project layout and CLI entrypoint.
- Add configuration loader (`repos`, polling schedule, rule toggles).
- Provision SQLite migrations and baseline schema.

## Phase 1 — Ingestion MVP

- Implement repository syncing + incremental commit ingestion.
- Implement sensitive-path tagging.
- Add audit report fetch + PDF extraction pipeline.
- Add HTTP API surface crawler and persistence.

## Phase 2 — Static Analysis MVP

- Implement common finding schema + normalizer.
- Integrate CodeQL/Clang wrapper for C++.
- Build first-pass tree-sitter FunC detector set.
- Integrate Semgrep/Bandit analyzers for Python/JS.

## Phase 3 — Semantic Layer MVP

- Build message-flow graph composer.
- Add cycle and risky mode-flag checks.
- Add gas-cost abstract interpreter (coarse-grained).

## Phase 4 — Dynamic Analysis MVP

- Add private testnet orchestrator hooks.
- Build contract test generators from static findings.
- Add C++ harness runner + corpus manager.
- Add API fuzz orchestrator from discovered spec.

## Phase 5 — Findings Workflow

- Implement deduplication + clustering.
- Add severity scoring policy and analyst override.
- Generate PoC scaffolds and report skeletons.
- Ship Rich-based terminal review UI.

## Acceptance Criteria (Initial)

- New commits in tracked repositories are ingested and queryable.
- At least one analyzer per language can emit normalized findings.
- Static findings can automatically create dynamic test stubs.
- Analyst can triage and export a report draft from TUI.

