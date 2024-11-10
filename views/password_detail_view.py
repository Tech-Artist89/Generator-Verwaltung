# views/password_detail_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox, QTextEdit
from PySide6.QtCore import Qt, Signal, QUrl
from PySide6.QtGui import QDesktopServices

class PasswordDetailWidget(QWidget):
    entry_deleted = Signal()

    def __init__(self, entry_controller, parent=None):
        super().__init__(parent)
        self.entry_controller = entry_controller
        self.current_entry = None

        # Layout für die Detailansicht
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Titel
        self.title_label = QLabel("Titel:")
        self.title_input = QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)

        # Vorname und Nachname
        self.first_name_label = QLabel("Vorname:")
        self.first_name_input = QLineEdit()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)

        self.last_name_label = QLabel("Nachname:")
        self.last_name_input = QLineEdit()
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)

        # Passwort
        self.password_label = QLabel("Passwort:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Passwort standardmäßig verbergen
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Checkbox zum Anzeigen/Verbergen des Passworts
        self.show_password_checkbox = QCheckBox("Passwort anzeigen")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        layout.addWidget(self.show_password_checkbox)

        # URL als klickbarer Link
        self.url_label = QLabel("URL:")
        self.url_display = QLabel()
        self.url_display.setOpenExternalLinks(True)  # Aktiviert das Öffnen von Links im Browser
        self.url_display.linkActivated.connect(self.open_url)  # Verbindung zum URL-Öffner
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_display)

        # Notizen (Textfeld für mehrere Zeilen)
        self.notes_label = QLabel("Notizen:")
        self.notes_input = QTextEdit()  # Verwende QTextEdit für mehrzeilige Notizen
        layout.addWidget(self.notes_label)
        layout.addWidget(self.notes_input)

        # Button-Leiste für Speichern und Löschen
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Speichern")
        self.save_button.clicked.connect(self.save_changes)
        button_layout.addWidget(self.save_button)

        self.delete_button = QPushButton("Löschen")
        self.delete_button.clicked.connect(self.delete_entry)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

    def display_entry(self, entry):
        """Zeigt die Details des Eintrags in der Detailansicht an."""
        self.current_entry = entry
        self.title_input.setText(entry.title)
        self.first_name_input.setText(entry.first_name)
        self.last_name_input.setText(entry.last_name if entry.last_name else "")
        self.password_input.setText(entry.password)
        # URL als klickbaren Link setzen
        self.url_display.setText(f'<a href="{entry.url}">{entry.url}</a>') if entry.url else self.url_display.clear()
        self.notes_input.setPlainText(entry.notes if entry.notes else "")

    def open_url(self, url):
        """Öffnet die URL im Standardbrowser."""
        QDesktopServices.openUrl(QUrl(url))

    def toggle_password_visibility(self):
        """Schaltet die Passwortanzeige zwischen Klartext und verbergen um."""
        if self.show_password_checkbox.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)  # Passwort im Klartext anzeigen
        else:
            self.password_input.setEchoMode(QLineEdit.Password)  # Passwort verbergen

    def save_changes(self):
        """Speichert Änderungen am aktuellen Eintrag."""
        if self.current_entry:
            self.current_entry.title = self.title_input.text()
            self.current_entry.first_name = self.first_name_input.text()
            self.current_entry.last_name = self.last_name_input.text() or None
            self.current_entry.password = self.password_input.text()
            self.current_entry.url = self.url_display.text()  # Hier kann url_display Text verwendet werden
            self.current_entry.notes = self.notes_input.toPlainText()
            self.entry_controller.update_entry(self.current_entry)

    def delete_entry(self):
        """Löscht den aktuellen Eintrag."""
        if self.current_entry:
            self.entry_controller.delete_entry(self.current_entry.entry_id)
            self.clear_fields()
            self.entry_deleted.emit()

    def clear_fields(self):
        """Löscht die Eingabefelder nach dem Löschen des Eintrags."""
        self.title_input.clear()
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.password_input.clear()
        self.url_display.clear()
        self.notes_input.clear()
        self.current_entry = None
