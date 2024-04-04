from typing import Dict, Optional
from src.models.settings.connection import db_connection_handler
from src.models.entities import Events

class EventsRepository:
    def insert_event(self, events_info: Dict) -> Dict:
        with db_connection_handler as db:
            event = Events(
                id=events_info.get("uuid"),
                title=events_info.get("title"),
                details=events_info.get("details"),
                slug=events_info.get("slug"),
                maximum_attendees=events_info.get("maximum_attendees"),
            )
            db.session.add(event)
            db.session.commit()

            return events_info
        
    def get_event_by_id(self, event_id: str) -> Optional[Events]:
        with db_connection_handler as db:
            event = db.session.query(Events).filter_by(id=event_id).first()

            return event