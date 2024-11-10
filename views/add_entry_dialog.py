# views/add_entry_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class AddEntryDialog(QDialog):
    def __init__(self, parent=None, first_name="", last_name="", password=""):
        super().__init__(parent)
        self.setWindowTitle("Neues Passwort hinzufügen")
        self.resize(600, 500)

        # Layout und Eingabefelder hinzufügen
        layout = QVBoxLayout(self)

        # Titel
        self.title_input = QLineEdit()
        layout.addWidget(QLabel("Titel"))
        layout.addWidget(self.title_input)

        # Vorname und Nachname
        self.first_name_input = QLineEdit()
        self.first_name_input.setText(first_name)  # Vorname vorab ausfüllen
        layout.addWidget(QLabel("Vorname"))
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit()
        self.last_name_input.setText(last_name)  # Nachname vorab ausfüllen
        layout.addWidget(QLabel("Nachname"))
        layout.addWidget(self.last_name_input)

        # Passwort
        self.password_input = QLineEdit()
        self.password_input.setText(password)  # Passwort vorab ausfüllen
        layout.addWidget(QLabel("Passwort"))
        layout.addWidget(self.password_input)

        # URL
        self.url_input = QLineEdit()
        layout.addWidget(QLabel("URL"))
        layout.addWidget(self.url_input)

        # Notizen
        self.notes_input = QTextEdit()
        layout.addWidget(QLabel("Notizen"))
        layout.addWidget(self.notes_input)

        # Button zum Speichern
        self.save_button = QPushButton("Speichern")
        self.save_button.clicked.connect(self.accept)  # Ruft accept() auf, wenn geklickt
        layout.addWidget(self.save_button)

    def get_entry_data(self):
        # Gibt die Daten des Eintrags zurück, einschließlich der Notizen und URL
        return {
            "title": self.title_input.text(),
            "first_name": self.first_name_input.text(),
            "last_name": self.last_name_input.text(),
            "password": self.password_input.text(),
            "url": self.url_input.text(),
            "notes": self.notes_input.toPlainText()
        }
