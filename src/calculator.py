from dataclasses import dataclass
from datetime import date
from events import BuyEvent, SellEvent


class Calculator:
    def __init__(self) -> None:
        pass

    def compute_adjusted_cost_base(self, purchases: list[BuyEvent]) -> int:
        return 0

    def compute_total_shares_purchased(self) -> int:
        return 0
