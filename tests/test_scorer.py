from tonprobe.findings.manager import Finding
from tonprobe.findings.scorer import score_finding


def test_scorer_increases_with_reproduction() -> None:
    unreproduced = Finding("a.fc", "det", "medium", 0.5, False)
    reproduced = Finding("a.fc", "det", "medium", 0.5, True)
    assert score_finding(reproduced) > score_finding(unreproduced)
