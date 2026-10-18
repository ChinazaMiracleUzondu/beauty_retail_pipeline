import csv

from pipeline.schema import TransactionRecord
from pipeline.validator import (
    validate_transaction,
    convert_item_count,
    convert_revenue,
)


def load_transactions(file_path, include_count=False):
    """Read CSV transactions and reject invalid records."""

    transactions = []
    total_raw_records = 0

    # Open the CSV file
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Check that all required columns exist
        required_columns = {
            "branch_id",
            "transaction_date",
            "customer_tier",
            "item_count",
            "revenue",
        }

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError("CSV file is missing required columns.")

        # Read each transaction
        for row in reader:
            total_raw_records += 1

            try:
                # Read and clean text values
                branch_id = row["branch_id"].strip()
                transaction_date = row["transaction_date"].strip()
                customer_tier = row["customer_tier"].strip()

                # Convert numeric values
                item_count = convert_item_count(row["item_count"])
                revenue = convert_revenue(row["revenue"])

            except (ValueError, TypeError, KeyError, AttributeError):
                print("Skipping transaction with missing or invalid data:", row)
                continue

            # Create a transaction object
            transaction = TransactionRecord()

            transaction.branch_id = branch_id
            transaction.transaction_date = transaction_date
            transaction.customer_tier = customer_tier
            transaction.item_count = item_count
            transaction.revenue = revenue

            # Reject records that fail validation
            if not validate_transaction(transaction):
                print("Skipping transaction with invalid values:", row)
                continue

            # Store the valid transaction
            transactions.append(transaction)

    # Optionally return the original record count
    if include_count:
        return transactions, total_raw_records

    return transactions
