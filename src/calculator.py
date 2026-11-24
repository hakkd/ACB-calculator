from dataclasses import dataclass
from datetime import date


@dataclass
class PurchaseEvent:
    """Class for stock purchase events"""

    symbol: str
    price: int
    n_shares: int
    purchase_date: date


class Calculator:
    def __init__(self) -> None:
        pass

    def compute_adjusted_cost_base(self, purchases: list[PurchaseEvent]) -> int:
        return 0

    def compute_total_shares_purchased(self) -> int:
        return 0
