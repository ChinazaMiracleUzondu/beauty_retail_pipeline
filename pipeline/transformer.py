def calculate_total_revenue(transactions):
    """Calculate total revenue from all transactions."""
    return sum(transaction.revenue for transaction in transactions)


def calculate_total_items(transactions):
    """Calculate the total number of items sold."""
    return sum(transaction.item_count for transaction in transactions)


def calculate_average_revenue(transactions):
    """Calculate average revenue per transaction."""
    if len(transactions) == 0:
        return 0.0

    total_revenue = calculate_total_revenue(transactions)
    return total_revenue / len(transactions)


def filter_active_transactions(transactions):
    """Return transactions with revenue greater than zero."""
    return list(
        filter(
            lambda transaction: transaction.revenue > 0,
            transactions
        )
    )


def calculate_revenue_with_tax(transactions, tax_rate=0.13):
    """Calculate revenue including tax without changing original data."""
    return list(
        map(
            lambda transaction: round(
                transaction.revenue * (1 + tax_rate), 2
            ),
            transactions
        )
    )


def calculate_net_margins(transactions, cost_rate=0.60):
    """Calculate net margins using an estimated cost percentage."""
    return [
        round(transaction.revenue * (1 - cost_rate), 2)
        for transaction in transactions
    ]


def calculate_gross_sales(transactions):
    """Calculate gross sales before any deductions."""
    return calculate_total_revenue(transactions)


def calculate_retention_rate(valid_count, total_count):
    """Calculate the percentage of records retained after validation."""
    if total_count == 0:
        return 0.0

    return round((valid_count / total_count) * 100, 2)


def calculate_branch_sales(transactions):
    """Calculate total revenue for each branch."""
    branch_sales = {}

    for transaction in transactions:
        branch_id = transaction.branch_id

        if branch_id not in branch_sales:
            branch_sales[branch_id] = 0.0

        branch_sales[branch_id] += transaction.revenue

    return branch_sales


def find_top_branch(transactions):
    """Find the branch generating the highest revenue."""
    branch_sales = calculate_branch_sales(transactions)

    if not branch_sales:
        return None

    return max(branch_sales, key=branch_sales.get)


def calculate_customer_tier_breakdown(transactions):
    """Count transactions belonging to each customer tier."""
    tier_counts = {}

    for transaction in transactions:
        tier = transaction.customer_tier

        if tier not in tier_counts:
            tier_counts[tier] = 0

        tier_counts[tier] += 1

    return tier_counts

