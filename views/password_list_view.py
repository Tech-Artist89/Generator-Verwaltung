# views/password_list_view.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QListWidgetItem, QSplitter, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from views.password_detail_view import PasswordDetailWidget
from controllers.entry_controller import EntryController


class PasswordListView(QDialog):
    def __init__(self, entry_controller, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gespeicherte Passwörter")
        self.resize(800, 600)

        # Hintergrundbild hinzufügen
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/images/passwort-generator.jpg")  # Pfad zum Bild
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.resize(self.size())  # Hintergrundbild an Fenstergröße anpassen

        # Haupt-Layout und Splitter
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Keine Ränder, um das Bild vollflächig zu zeigen
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # Passwortliste links
        self.entry_controller = entry_controller
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.show_password_detail)
        splitter.addWidget(self.list_widget)
        splitter.setStretchFactor(0, 1)

        # Detailansicht rechts
        self.detail_widget = PasswordDetailWidget(self.entry_controller)
        self.detail_widget.entry_deleted.connect(self.load_entries)
        splitter.addWidget(self.detail_widget)
        splitter.setStretchFactor(1, 2)

        # Passwort-Einträge laden
        self.load_entries()

        # Hintergrund in den Hintergrund setzen
        self.background_label.lower()

    def load_entries(self):
        # Alle Einträge laden und in der Liste anzeigen
        entries = self.entry_controller.get_all_entries()
        self.list_widget.clear()
        for entry in entries:
            display_title = entry.title
            item = QListWidgetItem(display_title)
            item.setData(Qt.UserRole, entry)
            self.list_widget.addItem(item)

    def show_password_detail(self, item):
        # Zeigt die Details des ausgewählten Passworts an
        entry = item.data(Qt.UserRole)
        self.detail_widget.display_entry(entry)

    def resizeEvent(self, event):
        # Passt das Hintergrundbild an, wenn das Fenster neu skaliert wird
        self.background_label.resize(self.size())
        super().resizeEvent(event)
