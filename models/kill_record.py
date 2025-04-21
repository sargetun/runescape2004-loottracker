from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from models.loot_item import LootItem

@dataclass
class KillRecord:
    monster_id: int
    timestamp: datetime = field(default_factory=datetime.now)
    loot_obtained: List[LootItem] = field(default_factory=list)