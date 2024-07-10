import pytest
import uuid
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
email_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interacao com o banco")
def test_register_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    email_infos = {
        "id": email_id,
        "trip_id": trip_id,
        "title": "Ir pro Hotel",
        "occurs_at": "02-07-2024",
    }

    activities_repository.register_activity(email_infos)


@pytest.mark.skip(reason="interacao com o banco")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print(activities)

    assert isinstance(activities, list)
    assert isinstance(activities[0], tuple)
