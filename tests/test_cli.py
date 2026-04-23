import json
from pathlib import Path

import pytest

pytest.importorskip("typer")
from typer.testing import CliRunner

from tonprobe.cli import app
from tonprobe.findings.manager import Finding

runner = CliRunner()


def test_run_outputs_jsonl(monkeypatch) -> None:
    findings = [Finding("wallet.fc", "detector-x", "high", 0.8, True)]

    class StubManager:
        def run(self, targets: list[str]) -> list[Finding]:
            assert targets == ["a.fc"]
            return findings

    monkeypatch.setattr("tonprobe.cli.FindingsManager", lambda: StubManager())
    result = runner.invoke(app, ["run", "--format", "jsonl", "a.fc"])
    assert result.exit_code == 0

    payload = result.stdout.strip().splitlines()
    assert len(payload) == 1
    assert json.loads(payload[0])["detector"] == "detector-x"


def test_run_writes_output_file(monkeypatch, tmp_path: Path) -> None:
    findings = [Finding("wallet.fc", "detector-y", "medium", 0.6, False)]

    class StubManager:
        def run(self, targets: list[str]) -> list[Finding]:
            assert targets == ["contracts/wallet.fc", "api/ton.py"]
            return findings

    monkeypatch.setattr("tonprobe.cli.FindingsManager", lambda: StubManager())
    output = tmp_path / "reports" / "findings.json"

    result = runner.invoke(app, ["run", "--output", str(output)])
    assert result.exit_code == 0
    assert f"Wrote findings to {output}" in result.stdout

    rendered = json.loads(output.read_text(encoding="utf-8"))
    assert rendered[0]["severity"] == "medium"
