from skills.trend_scout import fetch_trends

def test_trend_data_contract() -> None:
    """
    Assert the trend scout returns the correct JSON structure.
    This defines the 'Empty Slot' for the AI implementation.
    """
    data = fetch_trends()
    
    # This will FAIL because fetch_trends returns {}
    assert "viral_potential" in data, "Contract Violation: 'viral_potential' key missing from output."
    assert "topic" in data, "Contract Violation: 'topic' key missing from output."