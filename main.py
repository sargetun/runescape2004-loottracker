import sys
from PySide6.QtWidgets import QApplication
from screens.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Load gothic medieval stylesheet
    with open('assets/styles.qss', 'r') as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())