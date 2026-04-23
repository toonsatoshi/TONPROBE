-- TONPROBE initial SQLite schema

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS repositories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    url TEXT NOT NULL,
    language TEXT,
    enabled INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS commits (
    id INTEGER PRIMARY KEY,
    repository_id INTEGER NOT NULL,
    commit_hash TEXT NOT NULL,
    author TEXT,
    authored_at TEXT,
    ingested_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    message TEXT,
    diff_text TEXT,
    UNIQUE(repository_id, commit_hash),
    FOREIGN KEY(repository_id) REFERENCES repositories(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS commit_files (
    id INTEGER PRIMARY KEY,
    commit_id INTEGER NOT NULL,
    file_path TEXT NOT NULL,
    change_type TEXT,
    is_sensitive INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(commit_id) REFERENCES commits(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS audit_reports (
    id INTEGER PRIMARY KEY,
    repository_id INTEGER,
    source_url TEXT NOT NULL,
    fetched_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    report_text TEXT,
    normalized_summary_json TEXT,
    FOREIGN KEY(repository_id) REFERENCES repositories(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS api_specs (
    id INTEGER PRIMARY KEY,
    source_name TEXT NOT NULL,
    fetched_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    spec_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS findings (
    id INTEGER PRIMARY KEY,
    source_engine TEXT NOT NULL,
    repository_id INTEGER,
    file_path TEXT,
    line_start INTEGER,
    line_end INTEGER,
    rule_id TEXT NOT NULL,
    severity TEXT,
    confidence REAL,
    description TEXT NOT NULL,
    evidence_json TEXT,
    status TEXT NOT NULL DEFAULT 'new',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(repository_id) REFERENCES repositories(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS finding_clusters (
    id INTEGER PRIMARY KEY,
    cluster_key TEXT NOT NULL UNIQUE,
    title TEXT,
    severity TEXT,
    analyst_notes TEXT,
    status TEXT NOT NULL DEFAULT 'triage'
);

CREATE TABLE IF NOT EXISTS finding_cluster_members (
    cluster_id INTEGER NOT NULL,
    finding_id INTEGER NOT NULL,
    PRIMARY KEY(cluster_id, finding_id),
    FOREIGN KEY(cluster_id) REFERENCES finding_clusters(id) ON DELETE CASCADE,
    FOREIGN KEY(finding_id) REFERENCES findings(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS message_flow_edges (
    id INTEGER PRIMARY KEY,
    repository_id INTEGER,
    contract_name TEXT NOT NULL,
    from_function TEXT,
    destination TEXT,
    opcode TEXT,
    mode_flags TEXT,
    bounce_safe INTEGER,
    metadata_json TEXT,
    FOREIGN KEY(repository_id) REFERENCES repositories(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS dynamic_runs (
    id INTEGER PRIMARY KEY,
    run_type TEXT NOT NULL,
    target TEXT,
    started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ended_at TEXT,
    status TEXT,
    output_log TEXT
);
