from PySide6.QtWidgets import QMainWindow, QStackedWidget, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from screens.base_screen import BaseScreen
from screens.monster_list import MonsterListScreen
from storage.json_storage import JSONStorage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RuneScape Loot Tracker")
        self.resize(800, 600)

        # Load data
        self.storage = JSONStorage()
        self.monsters, self.kills = self.storage.load_all()

        # Central widget and layout
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        # Navigation bar
        nav_bar = QHBoxLayout()
        self.btn_monsters = QPushButton("Monsters")
        self.btn_kills = QPushButton("Add Kill")
        self.btn_stats = QPushButton("Statistics")
        nav_bar.addWidget(self.btn_monsters)
        nav_bar.addWidget(self.btn_kills)
        nav_bar.addWidget(self.btn_stats)

        # Stacked widget for screens
        self.stack = QStackedWidget()
        self.screen_monsters = MonsterListScreen(self.monsters)
        self.screen_kills = BaseScreen()   # TODO: replace with KillEntryScreen
        self.screen_stats = BaseScreen()   # TODO: replace with StatsScreen
        self.stack.addWidget(self.screen_monsters)
        self.stack.addWidget(self.screen_kills)
        self.stack.addWidget(self.screen_stats)

        # Assemble layout
        main_layout.addLayout(nav_bar)
        main_layout.addWidget(self.stack)

        # Connect navigation buttons
        self.btn_monsters.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_kills.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_stats.clicked.connect(lambda: self.stack.setCurrentIndex(2))
