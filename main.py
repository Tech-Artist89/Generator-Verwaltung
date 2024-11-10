# main.py
import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from config.db_config import engine, Base
from utils.path_utils import get_resource_path

# Anwendung starten
app = QApplication(sys.argv)

# QSS-Datei laden und anwenden
with open(get_resource_path("assets/styles.qss"), "r") as f:
    app.setStyleSheet(f.read())

# Datenbanktabellen erstellen, falls nicht vorhanden
Base.metadata.create_all(engine)

# Hauptfenster initialisieren und anzeigen
window = MainWindow()
window.show()

# Qt-Event-Loop starten
sys.exit(app.exec())
