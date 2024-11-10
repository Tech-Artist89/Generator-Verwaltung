# models/history_model.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from config.db_config import Base

class PasswordHistory(Base):
    __tablename__ = 'password_history'

    history_id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey('entries.entry_id'))
    old_password = Column(String(255), nullable=False)
    changed_at = Column(TIMESTAMP)
