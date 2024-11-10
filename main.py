# main.py
import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from config.db_config import engine, Base

# Tabellen erstellen, falls noch nicht vorhanden
Base.metadata.create_all(engine)

# Anwendung starten
app = QApplication(sys.argv)

# QSS-Datei laden
with open("assets/styles.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
window.show()
sys.exit(app.exec())
