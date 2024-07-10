from typing import Dict, Tuple, List
from sqlite3 import Connection


class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def register_activity(self, email_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO activities
                  (id, trip_id, title, occurs_at)
                VALUES
                  (?, ?, ?, ?)
            """,
            (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["title"],
                email_infos["occurs_at"],
            ),
        )
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute("""SELECT * from activities WHERE trip_id = ?""", (trip_id,))
        trip = cursor.fetchall()
        return trip
