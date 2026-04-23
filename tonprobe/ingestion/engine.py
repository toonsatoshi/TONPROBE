"""Ingestion pipeline primitives."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class IngestionArtifact:
    """Normalized representation of one ingested source path."""

    source: Path
    language: str


class IngestionEngine:
    """Collect and normalize target paths into ingestion artifacts."""

    _LANGUAGE_MAP = {
        ".py": "python",
        ".ts": "typescript",
        ".js": "javascript",
        ".cpp": "cpp",
        ".cc": "cpp",
        ".cxx": "cpp",
        ".hpp": "cpp",
        ".h": "cpp",
        ".fc": "func",
    }

    def ingest(self, targets: list[str]) -> list[IngestionArtifact]:
        """Convert user-provided targets into typed artifacts."""
        artifacts: list[IngestionArtifact] = []
        for raw_target in targets:
            source = Path(raw_target)
            language = self._LANGUAGE_MAP.get(source.suffix.lower(), "unknown")
            artifacts.append(IngestionArtifact(source=source, language=language))
        return artifacts
