from datetime import datetime
import math


def validate_item_count(item_count):
    """Check whether the item count is a non-negative integer."""
    return type(item_count) is int and item_count >= 0


def validate_revenue(revenue):
    """Check whether revenue is a non-negative, finite number."""
    return (
        type(revenue) in (int, float)
        and math.isfinite(revenue)
        and revenue >= 0
    )


def validate_branch_id(branch_id):
    """Check that the branch ID is not missing or blank."""
    return isinstance(branch_id, str) and bool(branch_id.strip())


def validate_transaction_date(transaction_date):
    """Check that the date follows YYYY-MM-DD and is valid."""
    if not isinstance(transaction_date, str):
        return False

    try:
        parsed_date = datetime.strptime(transaction_date, "%Y-%m-%d")
        return parsed_date.strftime("%Y-%m-%d") == transaction_date
    except ValueError:
        return False


def validate_customer_tier(customer_tier):
    """Check that the customer tier is not missing or blank."""
    return isinstance(customer_tier, str) and bool(customer_tier.strip())


def validate_transaction(transaction):
    """Check all required fields of a transaction."""

    return (
        validate_branch_id(transaction.branch_id)
        and validate_transaction_date(transaction.transaction_date)
        and validate_customer_tier(transaction.customer_tier)
        and validate_item_count(transaction.item_count)
        and validate_revenue(transaction.revenue)
    )


def convert_item_count(value):
    """Convert an item count to an integer."""

    if isinstance(value, bool):
        raise ValueError("Item count cannot be a Boolean value.")

    if isinstance(value, float) and not value.is_integer():
        raise ValueError("Item count must be a whole number.")

    text = str(value).strip()

    if not text:
        raise ValueError("Item count cannot be blank.")

    return int(text)


def convert_revenue(value):
    """Convert revenue to a floating-point number."""

    if isinstance(value, bool):
        raise ValueError("Revenue cannot be a Boolean value.")

    text = str(value).strip()

    if not text:
        raise ValueError("Revenue cannot be blank.")

    revenue = float(text)

    if not math.isfinite(revenue):
        raise ValueError("Revenue must be a finite number.")

    return revenue

