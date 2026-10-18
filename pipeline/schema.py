class TransactionRecord:
    """Represent a validated retail transaction."""

    def __init__(
        self,
        branch_id="",
        transaction_date="",
        customer_tier="",
        item_count=0,
        revenue=0.0,
    ):
        """Initialize the transaction attributes."""

        self.branch_id = branch_id
        self.transaction_date = transaction_date
        self.customer_tier = customer_tier
        self.item_count = item_count
        self.revenue = revenue

    def __repr__(self):
        """Return a readable representation of the transaction."""

        return (
            f"TransactionRecord("
            f"branch_id={self.branch_id!r}, "
            f"transaction_date={self.transaction_date!r}, "
            f"customer_tier={self.customer_tier!r}, "
            f"item_count={self.item_count!r}, "
            f"revenue={self.revenue!r})"
        )

        