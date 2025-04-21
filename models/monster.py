from dataclasses import dataclass, field
from typing import List
from models.loot_item import LootItem

@dataclass
class Monster:
    id: int
    name: str
    combat_level: int
    image_path: str  # e.g., 'assets/images/goblin.png'
    total_kills: int = 0
    loot: List[LootItem] = field(default_factory=list)