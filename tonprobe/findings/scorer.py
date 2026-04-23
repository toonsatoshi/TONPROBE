"""Finding severity scoring."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tonprobe.findings.manager import Finding

_SEVERITY_BASE = {"low": 20, "medium": 50, "high": 75, "critical": 90}


def score_finding(finding: Finding) -> int:
    """Compute a 0-100 score used for review queue prioritization."""
    base = _SEVERITY_BASE.get(finding.severity, 10)
    reproduced_bonus = 10 if finding.reproduced else 0
    return min(100, base + reproduced_bonus + int(finding.confidence * 10))
