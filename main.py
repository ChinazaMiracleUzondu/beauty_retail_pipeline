from pipeline.ingestion import load_transactions
from pipeline.reporter import SalesReporter


def main():
    """Run the beauty retail data processing pipeline."""

    # Load and validate transactions from the CSV file
    valid_transactions, total_raw_records = load_transactions(
        "data/transactions.csv",
        include_count=True
    )

    # Create the sales reporter
    reporter = SalesReporter(
        valid_transactions,
        total_raw_records=total_raw_records
    )

    # Display the complete sales report
    reporter.display_report()


if __name__ == "__main__":
    main()
