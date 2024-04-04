import pytest
from src.models.settings.connection import db_connection_handler as db
from .events_repository import EventsRepository

db.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "meu-uuid-2",
        "title": "meu titulo",
        "slug": "meu-slug-2",
        "maximum_attendees": 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

def test_get_event_by_id():
    event_id = "meu-uuid-2"

    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response.as_dict())