from tonprobe.semantic.layer import SemanticLayer
from tonprobe.static.engine import StaticFinding


def test_semantic_enrichment_applies_weighted_impact() -> None:
    finding = StaticFinding("contract.fc", "baseline_func", "medium", 0.5)
    issue = SemanticLayer().enrich([finding])[0]
    assert issue.impact_score == 0.3
