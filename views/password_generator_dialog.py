# views/password_generator_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QCheckBox, QPushButton, QLineEdit
from utils.password_generator import generate_password
from utils.username_generator import generate_username

class PasswordGeneratorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Passwort- und Benutzernamen-Generator")
        
        self.parent = parent  # Referenz auf das Hauptfenster

        layout = QVBoxLayout(self)

        # Checkbox zum Umschalten zwischen realistischen und fantasievollen Namen
        self.fantasy_name_checkbox = QCheckBox("Fantasienamen verwenden")
        layout.addWidget(self.fantasy_name_checkbox)

        # Checkbox zum Umschalten, ob ein Nachname generiert werden soll
        self.include_last_name_checkbox = QCheckBox("Nachname generieren")
        self.include_last_name_checkbox.setChecked(True)  # Standardmäßig aktiviert
        layout.addWidget(self.include_last_name_checkbox)

        # Anzeige der generierten Namen (Vorname und Nachname)
        self.first_name_output = QLineEdit()
        self.first_name_output.setReadOnly(True)
        layout.addWidget(QLabel("Generierter Vorname:"))
        layout.addWidget(self.first_name_output)

        self.last_name_output = QLineEdit()
        self.last_name_output.setReadOnly(True)
        layout.addWidget(QLabel("Generierter Nachname:"))
        layout.addWidget(self.last_name_output)

        # Button zum Generieren des Benutzernamens
        generate_username_button = QPushButton("Benutzernamen generieren")
        generate_username_button.clicked.connect(self.generate_username)
        layout.addWidget(generate_username_button)

        # Passwortgenerator
        self.length_input = QSpinBox()
        self.length_input.setRange(8, 32)
        self.length_input.setValue(12)
        layout.addWidget(QLabel("Passwortlänge:"))
        layout.addWidget(self.length_input)

        self.uppercase_checkbox = QCheckBox("Großbuchstaben verwenden (A-Z)")
        self.uppercase_checkbox.setChecked(True)
        layout.addWidget(self.uppercase_checkbox)

        self.numbers_checkbox = QCheckBox("Zahlen verwenden (0-9)")
        self.numbers_checkbox.setChecked(True)
        layout.addWidget(self.numbers_checkbox)

        self.special_checkbox = QCheckBox("Sonderzeichen verwenden (!@#$%^&*)")
        self.special_checkbox.setChecked(True)
        layout.addWidget(self.special_checkbox)

        # Generiertes Passwort anzeigen
        self.password_output = QLineEdit()
        self.password_output.setReadOnly(True)
        layout.addWidget(QLabel("Generiertes Passwort:"))
        layout.addWidget(self.password_output)

        # Button zum Generieren des Passworts
        generate_password_button = QPushButton("Passwort generieren")
        generate_password_button.clicked.connect(self.generate_password)
        layout.addWidget(generate_password_button)

        # Weiter-Button zum Öffnen des Hinzufügen-Dialogs
        self.next_button = QPushButton("Weiter zum Erstellen")
        self.next_button.clicked.connect(self.open_add_entry_dialog)
        self.next_button.setEnabled(False)  # Anfangs deaktiviert
        layout.addWidget(self.next_button)

    def generate_username(self):
        """Generiert einen zufälligen Vor- und ggf. Nachnamen und zeigt sie an."""
        use_fantasy_names = self.fantasy_name_checkbox.isChecked()
        include_last_name = self.include_last_name_checkbox.isChecked()
        
        # Benutzernamen je nach Auswahl generieren
        if include_last_name:
            username = generate_username(use_fantasy_names=use_fantasy_names)
            first_name, last_name = username.split(".")
            self.first_name_output.setText(first_name)
            self.last_name_output.setText(last_name)
        else:
            first_name = generate_username(use_fantasy_names=use_fantasy_names).split(".")[0]
            self.first_name_output.setText(first_name)
            self.last_name_output.clear()

        # Aktiviert den Weiter-Button nach dem Generieren des Benutzernamens
        self.next_button.setEnabled(True)

    def generate_password(self):
        """Generiert ein zufälliges Passwort basierend auf den Optionen."""
        length = self.length_input.value()
        use_uppercase = self.uppercase_checkbox.isChecked()
        use_numbers = self.numbers_checkbox.isChecked()
        use_special = self.special_checkbox.isChecked()
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        self.password_output.setText(password)

        # Aktiviert den Weiter-Button nach dem Generieren des Passworts
        self.next_button.setEnabled(True)

    def open_add_entry_dialog(self):
        """Öffnet den AddEntryDialog mit den generierten Daten."""
        first_name = self.first_name_output.text()
        last_name = self.last_name_output.text()
        password = self.password_output.text()

        # Öffnet den Hinzufügen-Dialog im Hauptfenster mit den generierten Daten
        self.parent.open_add_entry_dialog(first_name, last_name, password)
        self.accept()  # Schließt den Generator-Dialog
