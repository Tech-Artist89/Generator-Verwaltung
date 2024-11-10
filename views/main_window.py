# views/main_window.py
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QDialog
from PySide6.QtGui import QPixmap
from controllers.entry_controller import EntryController
from views.add_entry_dialog import AddEntryDialog
from views.password_generator_dialog import PasswordGeneratorDialog
from views.password_list_view import PasswordListView
from utils.path_utils import get_resource_path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Passwortmanager")
        self.setGeometry(100, 100, 960, 540)

        # Controller für Datenbankoperationen
        self.entry_controller = EntryController()

        # Hauptlayout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Hintergrundbild
        self.background_label = QLabel(self)
        pixmap = QPixmap(get_resource_path("assets/images/passwort-generator.jpg"))
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())
        self.background_label.lower()

        # Titel und Beschreibung
        title_label = QLabel("Passwortmanager")
        title_label.setObjectName("title_label")
        layout.addWidget(title_label)

        description_label = QLabel("Verwalten und generieren Sie sichere Passwörter.")
        description_label.setObjectName("description_label")
        layout.addWidget(description_label)

        # Buttons für verschiedene Funktionen
        generate_password_button = QPushButton("Passwort generieren")
        generate_password_button.clicked.connect(self.open_password_generator)
        layout.addWidget(generate_password_button)

        show_passwords_button = QPushButton("Gespeicherte Passwörter anzeigen")
        show_passwords_button.clicked.connect(self.show_password_list)
        layout.addWidget(show_passwords_button)

    def open_add_entry_dialog(self, first_name="", last_name="", password=""):
        add_entry_dialog = AddEntryDialog(self, first_name=first_name, last_name=last_name, password=password)
        if add_entry_dialog.exec() == QDialog.Accepted:
            entry_data = add_entry_dialog.get_entry_data()
            self.entry_controller.add_entry(
                title=entry_data["title"],
                first_name=entry_data["first_name"],
                last_name=entry_data["last_name"],
                password=entry_data["password"],
                url=entry_data["url"],
                notes=entry_data["notes"]
            )

    def open_password_generator(self):
        password_generator_dialog = PasswordGeneratorDialog(self)
        if password_generator_dialog.exec() == QDialog.Accepted:
            generated_password = password_generator_dialog.get_generated_password()
            first_name, last_name = password_generator_dialog.get_generated_name()
            self.open_add_entry_dialog(first_name=first_name, last_name=last_name, password=generated_password)

    def show_password_list(self):
        password_list_view = PasswordListView(self.entry_controller)
        password_list_view.exec()

    def resizeEvent(self, event):
        self.background_label.setGeometry(self.rect())
        super().resizeEvent(event)
