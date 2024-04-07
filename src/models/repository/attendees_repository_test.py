import pytest

from uuid import uuid4
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Nova inserção no banco")
def test_insert_attendee():
    event_id = "meu-uuid"
    attendees_info = {
        "uuid": uuid4().hex,
        "name": "attendee name",
        "email": "email@email.com",
        "event_id": event_id
    }

    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendee_id = "378a9366b1714dfe93b6b8828a8e404e"
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(response)
