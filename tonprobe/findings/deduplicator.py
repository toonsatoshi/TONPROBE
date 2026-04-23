"""Finding deduplication helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tonprobe.findings.manager import Finding


def deduplicate_findings(findings: list[Finding]) -> list[Finding]:
    """Remove duplicate findings by (source, detector) while keeping order."""
    unique: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    for finding in findings:
        key = (finding.source, finding.detector)
        if key in seen:
            continue
        seen.add(key)
        unique.append(finding)
    return unique
