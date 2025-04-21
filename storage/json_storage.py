import json
from pathlib import Path
from typing import List, Tuple
from datetime import datetime
from models.monster import Monster
from models.kill_record import KillRecord
from models.loot_item import LootItem

class JSONStorage:
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.monsters_file = self.data_dir / 'monsters.json'
        self.kills_file = self.data_dir / 'kills.json'

    def load_monsters(self) -> List[Monster]:
        if not self.monsters_file.exists():
            return []
        with open(self.monsters_file, 'r', encoding='utf-8') as f:
            raw = json.load(f)
        return [Monster(**m) for m in raw]

    def save_monsters(self, monsters: List[Monster]):
        with open(self.monsters_file, 'w', encoding='utf-8') as f:
            json.dump([m.__dict__ for m in monsters], f, indent=2)

    def load_kills(self) -> List[KillRecord]:
        if not self.kills_file.exists():
            return []
        raw = json.load(self.kills_file)
        records = []
        for r in raw:
            r['timestamp'] = datetime.fromisoformat(r['timestamp'])
            loot = [LootItem(**l) for l in r['loot_obtained']]
            records.append(KillRecord(monster_id=r['monster_id'], timestamp=r['timestamp'], loot_obtained=loot))
        return records

    def save_kills(self, kills: List[KillRecord]):
        serializable = []
        for k in kills:
            serializable.append({
                'monster_id': k.monster_id,
                'timestamp': k.timestamp.isoformat(),
                'loot_obtained': [li.__dict__ for li in k.loot_obtained]
            })
        with open(self.kills_file, 'w', encoding='utf-8') as f:
            json.dump(serializable, f, indent=2)

    def load_all(self) -> Tuple[List[Monster], List[KillRecord]]:
        return self.load_monsters(), self.load_kills()

    def save_all(self, monsters: List[Monster], kills: List[KillRecord]):
        self.save_monsters(monsters)
        self.save_kills(kills)