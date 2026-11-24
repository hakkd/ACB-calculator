from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Literal


@dataclass(frozen=True)
class StockEvent:
    symbol: str
    event_date: date
    quantity: Decimal
    unit_price_cad: Decimal
    fees_cad: Decimal = Decimal("0")


@dataclass(frozen=True)
class BuyEvent(StockEvent):
    kind: Literal["BUY"] = "BUY"

    @property
    def total_cost_cad(self) -> Decimal:
        return self.quantity * self.unit_price_cad + self.fees_cad


@dataclass(frozen=True)
class SellEvent(StockEvent):
    kind: Literal["SELL"] = "SELL"
    is_sell_to_cover: bool = False

    @property
    def gross_proceeds_cad(self) -> Decimal:
        return self.quantity * self.unit_price_cad - self.fees_cad
