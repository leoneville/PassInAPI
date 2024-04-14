from typing import Dict, Optional

from sqlalchemy.exc import IntegrityError, NoResultFound

from src.models.settings.connection import db_connection_handler
from src.models.entities import Events, Attendees
from src.errors.error_types.http_conflict import HttpConflictError


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
                raise HttpConflictError("Evento já cadastrado!")

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

    def count_event_attendees(self, event_id: str) -> Dict:
        with db_connection_handler as db:
            event_count = (
                db.session
                .query(Events)
                .join(Attendees, Events.id == Attendees.event_id)
                .filter(Events.id == event_id)
                .with_entities(
                    Events.maximum_attendees,
                    Attendees.id
                ).all()
            )

            if not event_count:
                return {
                    "maximumAttendees": 0,
                    "attendeesAmount": 0
                }

            return {
                "maximumAttendees": event_count[0].maximum_attendees,
                "attendeesAmount": len(event_count)
            }
