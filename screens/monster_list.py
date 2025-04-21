from PySide6.QtWidgets import QVBoxLayout, QListWidget, QListWidgetItem, QLabel
from screens.base_screen import BaseScreen
from models.monster import Monster

class MonsterListScreen(BaseScreen):
    def __init__(self, monsters: list[Monster], parent=None):
        super().__init__(parent)
        self.monsters = monsters
        layout = QVBoxLayout(self)

        header = QLabel("Monster List")
        layout.addWidget(header)

        self.list_widget = QListWidget()
        for m in self.monsters:
            item = QListWidgetItem(f"{m.name} (Lvl {m.combat_level}) - Kills: {m.total_kills}")
            self.list_widget.addItem(item)
        layout.addWidget(self.list_widget)