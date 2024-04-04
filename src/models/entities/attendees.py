from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone


class Attendees(Base):
    __tablename__ = 'attendees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    event_id = Column(String,  ForeignKey("events.id"), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

