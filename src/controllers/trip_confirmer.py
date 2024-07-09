from typing import Dict


class TripConfirmer:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def confirm_trip(self, trip_id) -> Dict:
        try:
            self.__trip_repository.update_trip_status(trip_id)

            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
