# database/database.py
from config.db_config import SessionLocal
from models.entry_model import Entry

class DatabaseManager:
    def __init__(self):
        self.session = SessionLocal()

    def add_entry(self, entry):
        self.session.add(entry)
        self.session.commit()

    def get_all_entries(self):
        return self.session.query(Entry).all()

    def update_entry(self, entry):
        self.session.commit()

    def delete_entry(self, entry_id):
        entry = self.session.query(Entry).filter(Entry.entry_id == entry_id).first()
        if entry:
            self.session.delete(entry)
            self.session.commit()
