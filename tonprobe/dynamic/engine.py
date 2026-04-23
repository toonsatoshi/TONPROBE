"""Dynamic validation primitives."""

from dataclasses import dataclass

from tonprobe.semantic.layer import SemanticIssue


@dataclass(frozen=True, slots=True)
class DynamicSignal:
    """Result of executing one dynamic validation case."""

    source: str
    detector: str
    reproduced: bool


class DynamicEngine:
    """Marks issues as reproduced based on impact score threshold."""

    def validate(self, issues: list[SemanticIssue]) -> list[DynamicSignal]:
        return [
            DynamicSignal(
                source=issue.source,
                detector=issue.detector,
                reproduced=issue.impact_score >= 0.3,
            )
            for issue in issues
        ]
