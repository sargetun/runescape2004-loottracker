from PySide6.QtWidgets import QWidget

class BaseScreen(QWidget):
    """
    Base class for all screens. Provides common setup.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # common styling or layout can go here