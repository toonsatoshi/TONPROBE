# TONPROBE

TONPROBE is a modular vulnerability-research pipeline for TON bug-bounty scope targets.

## Status

This repository now includes a full project scaffold for:

- configuration and rule definitions (`config/`)
- ingestion, static analysis, semantic analysis, dynamic analysis, and finding workflows (`tonprobe/`)
- test placeholders (`tests/`)
- helper scripts (`scripts/`)

## Quickstart

1. Copy `.env.example` to `.env` and set environment paths.
2. Install dependencies from `pyproject.toml`.
3. Run CLI:

```bash
tonprobe run
```

## CLI commands

- `tonprobe run`
- `tonprobe ingest`
- `tonprobe analyze`
- `tonprobe fuzz`
- `tonprobe review`
- `tonprobe export`

## Design docs

- `docs/design-spec.md`
- `docs/implementation-plan.md`
- `docs/database-schema.sql`
