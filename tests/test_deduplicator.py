from tonprobe.findings.deduplicator import deduplicate_findings
from tonprobe.findings.manager import Finding


def test_deduplicator_keeps_first_occurrence() -> None:
    findings = [
        Finding("a.fc", "d1", "low", 0.3, False),
        Finding("a.fc", "d1", "low", 0.9, True),
    ]
    deduped = deduplicate_findings(findings)
    assert deduped == [findings[0]]
