# views/entry_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class EntryView(QWidget):
    def __init__(self, entry, parent=None):
        super().__init__(parent)
        self.entry = entry
        self.setWindowTitle("Passwortdetails")
        layout = QVBoxLayout(self)

        # Anzeigen von Details des Eintrags
        layout.addWidget(QLabel(f"Title: {self.entry.title}"))
        layout.addWidget(QLabel(f"Username: {self.entry.username}"))
        layout.addWidget(QLabel(f"URL: {self.entry.url if self.entry.url else 'Keine'}"))
        layout.addWidget(QLabel(f"Notizen: {self.entry.notes if self.entry.notes else 'Keine'}"))

        # Passwort-Anzeige
        password_label = QLabel(f"Passwort: {self.entry.password}")
        layout.addWidget(password_label)

        # Button zum Bearbeiten oder Löschen des Eintrags (noch nicht implementiert)
        edit_button = QPushButton("Bearbeiten")
        layout.addWidget(edit_button)
        delete_button = QPushButton("Löschen")
        layout.addWidget(delete_button)
