from typing import Dict
import uuid


class ParticipantCreator:
    def __init__(self, participants_repository, emails_repository) -> None:
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            email_infos = {"id": email_id, "trip_id": trip_id, "email": body["email"]}

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"],
            }

            self.__emails_repository.register_email(email_infos)
            self.__participants_repository.register_participant(participant_infos)

            return {"body": {"id": participant_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
