import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())


# @pytest.mark.skip(reason="interacao com o banco")
def test_register_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "www.foobar.com",
        "title": "foobar",
    }

    links_repository.register_link(link_infos)


# @pytest.mark.skip(reason="interacao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    emails = links_repository.find_links_from_trip(trip_id)
    print(emails)
