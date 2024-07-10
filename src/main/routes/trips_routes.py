from flask import jsonify, Blueprint, request
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participants_finder import ParticipantsFinder
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    email_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trip_repository, email_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    controller = TripFinder(trip_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["PUT"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    controller = TripConfirmer(trip_repository)

    response = controller.confirm_trip(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/link", methods=["POST"])
def create_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_links_from_trip(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find_links_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/participant", methods=["POST"])
def create_participant(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantCreator(participants_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def find_participants_from_trip(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantsFinder(participants_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/participant/<participantId>/confirm", methods=["PUT"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(participants_repository)

    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]
