from typing import Dict, Optional
from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

class Events(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False, unique=True)
    maximum_attendees = Column(Integer)

    def __init__(self, id: str, title: str, details: Optional[str], slug: str, maximum_attendees: Optional[int]) -> None:
        self.id = id
        self.title = title
        self.details = details
        self.slug = slug
        self.maximum_attendees = maximum_attendees

    def as_dict(self) -> Dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"<Events {self.id}>"