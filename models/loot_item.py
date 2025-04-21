from dataclasses import dataclass

@dataclass
class LootItem:
    name: str
    quantity: int = 0
    drop_rate: float = 0.0  # optional metadata