"""Static analysis orchestration."""

from dataclasses import dataclass

from tonprobe.ingestion.engine import IngestionArtifact


@dataclass(frozen=True, slots=True)
class StaticFinding:
    """A finding emitted by a static analyzer."""

    source: str
    detector: str
    severity: str
    confidence: float


class StaticEngine:
    """Very small baseline static analyzer.

    This gives the project a real execution path while deeper analyzers are built.
    """

    def analyze(self, artifacts: list[IngestionArtifact]) -> list[StaticFinding]:
        findings: list[StaticFinding] = []
        for artifact in artifacts:
            if artifact.language == "unknown":
                continue
            detector = f"baseline_{artifact.language}"
            severity = "medium" if artifact.language in {"cpp", "func"} else "low"
            findings.append(
                StaticFinding(
                    source=str(artifact.source),
                    detector=detector,
                    severity=severity,
                    confidence=0.55,
                )
            )
        return findings
