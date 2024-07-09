import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
email_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interacao com o banco")
def test_register_email():
    conn = db_connection_handler.get_connection()
    emails_repository = EmailsToInviteRepository(conn)

    email_infos = {"id": email_id, "trip_id": trip_id, "email": "osvaldo@email.com"}

    emails_repository.register_email(email_infos)


@pytest.mark.skip(reason="interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_repository = EmailsToInviteRepository(conn)

    emails = emails_repository.find_emails_from_trip(trip_id)
    print(emails)
