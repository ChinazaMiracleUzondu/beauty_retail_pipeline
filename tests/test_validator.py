from pipeline.validator import validate_item_count, validate_revenue

def test_valid_item_count():
    assert validate_item_count(5) is True

def test_invalid_item_count():
    assert validate_item_count(-5) is False

def test_valid_revenue():
    assert validate_revenue(150.75) is True

def test_invalid_revenue():
    assert validate_revenue("hello") is False
    