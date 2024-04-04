from datetime import datetime, timezone

from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    attendeeId = Column(String, ForeignKey('attendees.id'), nullable=False, unique=True)