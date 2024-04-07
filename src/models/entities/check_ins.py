from dataclasses import dataclass
from datetime import datetime, timezone

from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

@dataclass
class CheckIns(Base):
    __tablename__ = "check_ins"

    id:int = Column(Integer, primary_key=True)
    created_at: datetime = Column(DateTime, default=func.now())
    attendeeId: str = Column(String, ForeignKey('attendees.id'), nullable=False, unique=True)

    def __init__(self, attendeeId: str):
        self.attendeeId = attendeeId

    def __repr__(self) -> str:
        return f"<CheckIns: id={self.id}, created_at={self.created_at}, attendeeId={self.attendeeId}>"