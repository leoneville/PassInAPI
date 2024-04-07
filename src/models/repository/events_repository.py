from typing import Dict, Optional

from sqlalchemy.exc import IntegrityError, NoResultFound

from src.models.settings.connection import db_connection_handler
from src.models.entities import Events

class EventsRepository:
    def insert_event(self, events_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
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
            
            except IntegrityError:
                raise Exception("Evento já cadastrado!")

            except Exception as exception:
                db.session.rollback()
                raise exception
        
    def get_event_by_id(self, event_id: str) -> Optional[Events]:
        with db_connection_handler as db:
            try:
                event = db.session.query(Events).filter_by(id=event_id).one()

                return event
            
            except NoResultFound:
                return None