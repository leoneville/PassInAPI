from dataclasses import dataclass
from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from datetime import datetime, timezone

@dataclass
class Attendees(Base):
    __tablename__ = 'attendees'

    id: str = Column(String, primary_key=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
    event_id: str = Column(String,  ForeignKey("events.id"), nullable=False, unique=True)
    created_at: datetime = Column(DateTime, default=func.now())

    def __repr__(self) -> str:
        return f"<Attendees: id={self.id}, name={self.name}, email={self.email}, event_id={self.event_id}>"

