from dataclasses import dataclass

@dataclass
class InventoryItem_Example:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

    @dataclass
    class Audit_ErrorHandling:
        """Class for keeping track of an item in inventory."""
        name: str
        unit_price: float
        quantity_on_hand: int = 0

        def error_completedetails(self) -> str:
            return self.unit_price * self.quantity_on_hand