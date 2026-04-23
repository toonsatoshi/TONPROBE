from tonprobe.findings.manager import FindingsManager


def test_pipeline_returns_sorted_findings() -> None:
    findings = FindingsManager().run(["a.fc", "b.py", "unknown.file"])
    assert [finding.detector for finding in findings] == ["baseline_func", "baseline_python"]
