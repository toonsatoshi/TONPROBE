"""Semantic layer used to enrich static findings with execution context."""

from dataclasses import dataclass

from tonprobe.static.engine import StaticFinding


@dataclass(frozen=True, slots=True)
class SemanticIssue:
    """Static finding plus semantic impact signal."""

    source: str
    detector: str
    severity: str
    confidence: float
    impact_score: float


class SemanticLayer:
    """Adds a lightweight impact score on top of static findings."""

    _SEVERITY_WEIGHT = {"low": 0.25, "medium": 0.6, "high": 0.85, "critical": 1.0}

    def enrich(self, findings: list[StaticFinding]) -> list[SemanticIssue]:
        enriched: list[SemanticIssue] = []
        for finding in findings:
            weight = self._SEVERITY_WEIGHT.get(finding.severity, 0.2)
            impact_score = round(weight * finding.confidence, 3)
            enriched.append(
                SemanticIssue(
                    source=finding.source,
                    detector=finding.detector,
                    severity=finding.severity,
                    confidence=finding.confidence,
                    impact_score=impact_score,
                )
            )
        return enriched
