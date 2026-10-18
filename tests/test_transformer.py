from pipeline.schema import TransactionRecord
from pipeline.transformer import (
    calculate_total_revenue,
    calculate_total_items,
    calculate_average_revenue,
)


def create_sample_transactions():
    """Create two transactions for testing."""
    transaction1 = TransactionRecord()
    transaction1.revenue = 100.0
    transaction1.item_count = 3

    transaction2 = TransactionRecord()
    transaction2.revenue = 200.0
    transaction2.item_count = 5

    return [transaction1, transaction2]


def test_total_revenue():
    transactions = create_sample_transactions()
    assert calculate_total_revenue(transactions) == 300.0


def test_total_items():
    transactions = create_sample_transactions()
    assert calculate_total_items(transactions) == 8


def test_average_revenue():
    transactions = create_sample_transactions()
    assert calculate_average_revenue(transactions) == 150.0


def test_average_revenue_empty():
    assert calculate_average_revenue([]) == 0.0
