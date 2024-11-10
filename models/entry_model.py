# models/entry_model.py
from sqlalchemy import Column, Integer, String
from config.db_config import Base

class Entry(Base):
    __tablename__ = "entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    first_name = Column(String, nullable=True)  # Vorname
    last_name = Column(String, nullable=True)   # Nachname
    password = Column(String, nullable=False)
    url = Column(String, nullable=True)
    notes = Column(String, nullable=True)
