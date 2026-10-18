from pipeline.transformer import (
    calculate_total_revenue,
    calculate_total_items,
    calculate_average_revenue,
    calculate_gross_sales,
    calculate_retention_rate,
    calculate_branch_sales,
    find_top_branch,
    calculate_customer_tier_breakdown,
    filter_active_transactions,
    calculate_revenue_with_tax,
    calculate_net_margins,
)


class SalesReporter:
    """Generate summary reports for retail transactions."""

    def __init__(self, transactions, total_raw_records=None):
        """Store transactions and the original record count."""
        self.transactions = transactions

        if total_raw_records is None:
            total_raw_records = len(transactions)

        self.total_raw_records = total_raw_records

    def generate_report(self):
        """Calculate and return retail sales metrics."""

        transactions = self.transactions

        total_transactions = len(transactions)
        total_items = calculate_total_items(transactions)
        total_revenue = calculate_total_revenue(transactions)
        average_revenue = calculate_average_revenue(transactions)

        gross_sales = calculate_gross_sales(transactions)

        retention_rate = calculate_retention_rate(
            total_transactions,
            self.total_raw_records
        )

        branch_sales = calculate_branch_sales(transactions)
        top_branch = find_top_branch(transactions)

        customer_tiers = calculate_customer_tier_breakdown(
            transactions
        )

        active_transactions = filter_active_transactions(
            transactions
        )

        revenue_with_tax = calculate_revenue_with_tax(
            transactions
        )

        net_margins = calculate_net_margins(
            transactions
        )

        return {
            "total_transactions": total_transactions,
            "total_items": total_items,
            "total_revenue": total_revenue,
            "average_revenue": average_revenue,
            "gross_sales": gross_sales,
            "retention_rate": retention_rate,
            "branch_sales": branch_sales,
            "top_branch": top_branch,
            "customer_tiers": customer_tiers,
            "active_transactions": len(active_transactions),
            "revenue_with_tax": revenue_with_tax,
            "net_margins": net_margins,
        }

    def display_report(self):
        """Display a formatted retail sales report."""

        report = self.generate_report()

        print("\nBEAUTY RETAIL SALES REPORT")
        print("-" * 35)

        print("Total Transactions:", report["total_transactions"])
        print("Total Items Sold:", report["total_items"])

        print(
            "Total Revenue: $",
            round(report["total_revenue"], 2)
        )

        print(
            "Average Revenue: $",
            round(report["average_revenue"], 2)
        )

        print(
            "Gross Sales: $",
            round(report["gross_sales"], 2)
        )

        print(
            "Clean Record Retention:",
            report["retention_rate"],
            "%"
        )

        print("Top Performing Branch:", report["top_branch"])

        print("\nSALES BY BRANCH")

        for branch, revenue in report["branch_sales"].items():
            print(branch, ": $", round(revenue, 2))

        print("\nCUSTOMER TIER BREAKDOWN")

        for tier, count in report["customer_tiers"].items():
            print(tier, ":", count, "transactions")

        print(
            "\nActive Transactions:",
            report["active_transactions"]
        )

        print(
            "Total Revenue Including Tax: $",
            round(sum(report["revenue_with_tax"]), 2)
        )

        print(
            "Estimated Total Net Margin: $",
            round(sum(report["net_margins"]), 2)
        )

        print("-" * 35)
