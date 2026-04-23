# TONPROBE

TONPROBE is a multi-phase vulnerability research pipeline for the TON bug bounty scope.

This repository currently contains the **detailed design specification** and an implementation-oriented blueprint that breaks the design into concrete modules.

## Document map

- `docs/design-spec.md` — full system design specification.
- `docs/implementation-plan.md` — phased build plan with deliverables and milestones.
- `docs/database-schema.sql` — initial SQLite schema draft for ingestion, analysis, and findings workflows.

## Goals

- Reduce manual toil in vulnerability research.
- Keep a human-in-the-loop for triage and exploitability judgment.
- Correlate static and dynamic findings through a shared local database.

## Non-goals

- Fully autonomous vulnerability reporting without analyst validation.
- Replacing TON domain expertise with generic scanners.

