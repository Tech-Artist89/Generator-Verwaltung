# controllers/entry_controller.py
from database.database import DatabaseManager
from models.entry_model import Entry

class EntryController:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def get_all_entries(self):
        return self.db_manager.get_all_entries()

    def add_entry(self, title, first_name, last_name=None, password=None, url=None, notes=None):
        entry = Entry(
            title=title,
            first_name=first_name,
            last_name=last_name,  # last_name kann None sein
            password=password,
            url=url,
            notes=notes
        )
        self.db_manager.add_entry(entry)

    def update_entry(self, entry):
        self.db_manager.update_entry(entry)

    def delete_entry(self, entry_id):
        self.db_manager.delete_entry(entry_id)
