from tonprobe.ingestion.engine import IngestionEngine


def test_ingestion_maps_known_extensions() -> None:
    artifacts = IngestionEngine().ingest(["contract.fc", "api.py", "README"])
    assert [artifact.language for artifact in artifacts] == ["func", "python", "unknown"]
