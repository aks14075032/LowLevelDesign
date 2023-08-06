from bookMyShowDesign.models.event import *


class EventFactory:
    @staticmethod
    def create_event(event_type, event_id, name, venue, time, available_seats):
        if event_type == "Movie":
            return MovieEvent(event_id, name, venue, time, available_seats)
        elif event_type == "Concert":
            return ConcertEvent(event_id, name, venue, time, available_seats)
        else:
            raise ValueError("Invalid event type: " + event_type)
