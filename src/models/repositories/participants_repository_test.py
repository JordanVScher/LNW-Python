import pytest
import uuid
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interacao com o banco")
def test_register_participant():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "João",
    }

    participant_repository.register_participant(participant_infos)


@pytest.mark.skip(reason="interacao com o banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participants = participant_repository.find_participants_from_trip(trip_id)
    print(participants)

    assert isinstance(participants, list)


@pytest.mark.skip(reason="interacao com o banco")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participant_repository.update_participant_status(participant_id)
