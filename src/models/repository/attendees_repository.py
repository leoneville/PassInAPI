from typing import Dict, Optional

from src.models.settings.connection import db_connection_handler
from src.models.entities import Attendees, Events
from sqlalchemy.exc import NoResultFound, IntegrityError


class AttendeesRepository:

    def insert_attendee(self, attendee_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                attendee = Attendees(
                    id=attendee_info.get("uuid"),
                    name=attendee_info.get("name"),
                    email=attendee_info.get("email"),
                    event_id=attendee_info.get("event_id")
                )
                db.session.add(attendee)
                db.session.commit()

                return attendee_info
            except IntegrityError:
                raise Exception("Participante já cadastrado!")
            except Exception as exception:
                db.session.rollback()
                raise exception

    def get_attendee_badge_by_id(self, attendee_id: str) -> Optional[Attendees]:
        with db_connection_handler as db:
            try:
                attendee = (
                    db.session
                    .query(Attendees)
                    .join(Events, Events.id == Attendees.event_id)
                    .filter(Attendees.id == attendee_id)
                    .with_entities(
                        Attendees.id,
                        Attendees.name,
                        Attendees.email,
                        Events.title
                    ).one()
                )
                return attendee

            except NoResultFound:
                return None
