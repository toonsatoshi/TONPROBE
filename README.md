# TONPROBE

TONPROBE is a modular vulnerability-research pipeline for TON bug-bounty scope targets.

## Status

This repository now includes a full project scaffold for:

- configuration and rule definitions (`config/`)
- ingestion, static analysis, semantic analysis, dynamic analysis, and finding workflows (`tonprobe/`)
- test placeholders (`tests/`)
- helper scripts (`scripts/`)
- CI automation (`.github/workflows/ci.yml`)

## Quickstart

1. Copy `.env.example` to `.env` and set environment paths.
2. Bootstrap a local development environment:

   ```bash
   make setup
   ```

3. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

4. Run checks locally:

   ```bash
   make ci
   ```

5. Run CLI:

```bash
tonprobe run
```

## Developer automation

- `make setup` creates `.venv`, upgrades pip, and installs package + dev tools.
- `make lint` runs bytecode compilation and Ruff linting.
- `make test` executes the pytest suite.
- `make format` applies Ruff formatting.
- `make ci` runs lint + tests.

GitHub Actions executes the same lint and test steps for pushes and pull requests across Python 3.11 and 3.12.

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
