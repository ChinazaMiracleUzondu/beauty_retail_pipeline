from pipeline.schema import TransactionRecord
from pipeline.reporter import SalesReporter


def test_sales_report():
    # Create the first transaction
    transaction1 = TransactionRecord()
    transaction1.item_count = 3
    transaction1.revenue = 100.0

    # Create the second transaction
    transaction2 = TransactionRecord()
    transaction2.item_count = 5
    transaction2.revenue = 200.0

    # Generate a report
    transactions = [transaction1, transaction2]
    reporter = SalesReporter(transactions)
    report = reporter.generate_report()

    # Check the results
    assert report["total_transactions"] == 2
    assert report["total_items"] == 8
    assert report["total_revenue"] == 300.0
    assert report["average_revenue"] == 150.0


def test_empty_sales_report():
    reporter = SalesReporter([])
    report = reporter.generate_report()

    assert report["total_transactions"] == 0
    assert report["total_items"] == 0
    assert report["total_revenue"] == 0
    assert report["average_revenue"] == 0.0
