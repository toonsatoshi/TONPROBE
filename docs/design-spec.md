# TON Bug Bounty Tool — Detailed Design Specification

## System Overview

The tool is a multi-phase vulnerability research pipeline purpose-built for the TON bug bounty scope. It is designed to run on a Linux workstation or server with an optional local TON private testnet.

The system is composed of five subsystems that operate both independently and in sequence:

1. Ingestion Engine
2. Static Analysis Engine
3. TON Semantic Layer
4. Dynamic Analysis Engine
5. Findings Manager

All subsystems read/write through a shared local database so static findings can inform dynamic testcase generation and dynamic evidence can raise or lower static confidence.

The tool is intentionally **human-in-the-loop**. It automates parsing, indexing, matching, and scaffold generation while leaving exploitability judgment and report quality control to researchers.

## Ingestion Engine

The ingestion engine runs as a background daemon with configurable polling.

### Source repositories

It maintains local clones for in-scope projects including:

- `ton-blockchain/ton` (C++)
- `wallet-contract`
- `multisig-contract`
- `nominator-pool`
- `token-contract`
- `dns-contract`
- `mytonctrl`
- `ton-http-api`
- `pytonlib`
- `ton-wallet`
- `tonweb`
- `tonweb-mnemonic`

Each cycle:

- performs `git fetch`
- computes diffs from last ingested commit
- stores commit metadata and changed files
- tags security-sensitive paths (e.g., `elector`, `nominator`, `config`, `bridge`, `wallet`, `mnemonic`, `crypto`) for priority review

### Audit report ingestion

- Fetches known public audit URLs weekly.
- Converts PDFs to plain text (`pdfminer`).
- Extracts vulnerability classes, affected functions, and severities.
- Uses lightweight keyword extraction plus optional LLM summarization for normalized historical bug patterns.

### HTTP API surface ingestion

- Crawls TON Center API docs and linked references.
- Extracts endpoint paths, methods, parameters, and example responses.
- Builds/stores a partial OpenAPI-like artifact used by dynamic API fuzzing.

## Static Analysis Engine

The static engine exposes language-specific analyzers under a common output schema.

Each finding includes:

- repository
- file path
- line/range
- rule ID
- human-readable description
- severity estimate
- confidence score

### C++ analyzer

- Runs CodeQL + Clang Static Analyzer.
- Extends default security queries with TON-specific checks:
  - integer arithmetic on coin values without overflow checks
  - discarded validator/Catchain error returns
  - unchecked casts from generic TL-B data
  - allocation/cleanup mismatches in DHT and ADNL paths
- Parses SARIF into normalized findings.
- Builds call-graph JSON (Catchain/Validator transitions) via Clang LibTooling.

### FunC analyzer

Custom analyzer based on tree-sitter FunC grammar:

- checks bounce handling in `recv_internal`
- verifies safe unknown-opcode default branch behavior
- flags risky arithmetic on value/token operations
- records `send_raw_message` edges for message-flow graphing
- finds storage writes reachable from public handlers without authorization checks
- caches AST artifacts in DB for incremental runs

### Python analyzer

- Runs Semgrep TON-focused rules:
  - hardcoded keys/mnemonics
  - unsanitized subprocess usage (`mytonctrl`)
  - risky `pickle`/`yaml.load` usage (`pytonlib`)
  - TLS verification disabled in requests
- Runs Bandit and merges output into normalized schema.

### JavaScript analyzer

- Runs Semgrep checks for:
  - `Math.random` in wallet/key/mnemonic-sensitive paths
  - unsafe `eval` / `Function`
  - prototype pollution merge patterns
  - unsafe `JSON.parse` flows on raw RPC responses
- Applies higher-priority entropy-source checks for mnemonic libraries.

## TON Semantic Layer

Encodes TON-specific behavioral risk models beyond generic static tooling.

Produces:

1. annotated inter-contract message-flow graph
2. gas exhaustion risk model

### Message-flow graph

Uses:

- `send_raw_message` edges from FunC analyzer
- known relationships from official TON docs

Checks for:

- async cycles resembling re-entrancy risk patterns
- mode `64` / `128` send-before-state-commit hazards
- inconsistent auth checks across mixed privilege sender paths

Exports DOT for visualization and JSON for programmatic use.

### Gas exhaustion model

- Performs AST-based abstract interpretation with approximate per-op gas costs.
- Flags unbounded work dependent on user-controlled loop bounds.
- Flags send-then-expensive-continuation patterns without gas reserve safeguards.

## Dynamic Analysis Engine

Requires local TON private testnet for contract execution and sanitizer-instrumented builds for C++.

### Testnet provisioner

- Brings up minimal private network (validators/full node/lite client) via Docker + mytonctrl.
- Exposes control API for deploy/send/query/reset operations.
- Resets state between runs for reproducibility.

### C++ fuzzing subsystem

- Compiles with `-fsanitize=address,undefined,thread` and libFuzzer.
- Maintains harnesses for ADNL packets, Catchain proposals, TonLib call sequences, TL-B messages.
- Shares and merges corpora using LLVM profiling data.
- Triggers targeted fuzzing on new commits using static call-graph guidance.

### Smart contract dynamic subsystem

Uses Blueprint sandbox to generate and execute:

- invariant tests (e.g., supply conservation, epoch-boundary transitions, stake accounting)
- adversarial tests synthesized from static findings (bounce/opcode/auth issues)

### HTTP API fuzzing subsystem

- Reconstructs API surface from ingested spec.
- Uses Atheris for malformed/edge-case parameter generation.
- Prioritizes hashes, addresses, and arbitrary data fields.
- Detects stack traces, schema breaks, and potential internal state leakage.

## Findings Manager

Output layer that aggregates, deduplicates, scores, and packages researcher-ready artifacts.

### Deduplication and clustering

- exact match: file + line + rule
- fuzzy match: description + snippet similarity
- cluster-level review queue with all static/dynamic evidence attached

### Severity tiers

- Critical: plausible direct fund loss or network-level compromise
- High: major disruption/privilege escalation with partial exploit chain
- Medium: constrained impact logic flaws
- Low: informational/defense-in-depth and out-of-scope low-impact items

### PoC scaffolds

For high/critical reviewed findings, generate:

- Blueprint exploit test templates (contracts)
- minimal reproducer harnesses (C++)
- `curl` or Python script skeletons (API)

Template fields align with bounty submission expectations: issue description, exploitation path, and reproducible steps.

### Storage and review UI

- Stores findings, evidence, statuses, and analyst notes in SQLite.
- Terminal triage UI (Rich) supports queue management, false-positive marking, and report export.

