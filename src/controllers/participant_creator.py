from typing import Dict
import uuid


class ParticipantCreator:
    def __init__(self, participants_repository) -> None:
        self.__participants_repository = participants_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            trip_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": body["emails_to_invite_id"],
                "name": body["name"],
            }

            self.__participants_repository.register_participant(trip_infos)

            return {"body": {"id": participant_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
