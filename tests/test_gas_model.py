from tonprobe.dynamic.engine import DynamicEngine
from tonprobe.semantic.layer import SemanticIssue


def test_dynamic_engine_marks_high_impact_as_reproduced() -> None:
    issue = SemanticIssue("contract.fc", "detector", "medium", 0.7, 0.42)
    signal = DynamicEngine().validate([issue])[0]
    assert signal.reproduced is True
