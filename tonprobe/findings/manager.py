"""Finding aggregation and pipeline orchestration."""

from dataclasses import dataclass

from tonprobe.dynamic.engine import DynamicEngine
from tonprobe.findings.deduplicator import deduplicate_findings
from tonprobe.findings.scorer import score_finding
from tonprobe.ingestion.engine import IngestionEngine
from tonprobe.semantic.layer import SemanticLayer
from tonprobe.static.engine import StaticEngine


@dataclass(frozen=True, slots=True)
class Finding:
    """User-facing finding."""

    source: str
    detector: str
    severity: str
    confidence: float
    reproduced: bool


class FindingsManager:
    """Coordinates all steps and outputs prioritized findings."""

    def __init__(self) -> None:
        self.ingestion = IngestionEngine()
        self.static = StaticEngine()
        self.semantic = SemanticLayer()
        self.dynamic = DynamicEngine()

    def run(self, targets: list[str]) -> list[Finding]:
        artifacts = self.ingestion.ingest(targets)
        static_findings = self.static.analyze(artifacts)
        issues = self.semantic.enrich(static_findings)
        dynamic_signals = self.dynamic.validate(issues)

        reproduced_by_key = {
            (signal.source, signal.detector): signal.reproduced
            for signal in dynamic_signals
        }
        findings = [
            Finding(
                source=issue.source,
                detector=issue.detector,
                severity=issue.severity,
                confidence=issue.confidence,
                reproduced=reproduced_by_key.get((issue.source, issue.detector), False),
            )
            for issue in issues
        ]

        deduplicated = deduplicate_findings(findings)
        return sorted(deduplicated, key=score_finding, reverse=True)
