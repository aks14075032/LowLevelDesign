from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(self, event_id, name, venue, time, available_seats):
        self.event_id = event_id
        self.name = name
        self.venue = venue
        self.time = time
        self.available_seats = available_seats

    def has_available_seats(self, number_of_tickets):
        return self.available_seats >= number_of_tickets

    def book_seats(self, number_of_tickets):
        if self.has_available_seats(number_of_tickets):
            self.available_seats -= number_of_tickets
            return True
        else:
            return False

    @abstractmethod
    def get_event_type(self):
        pass


class MovieEvent(Event):
    def get_event_type(self):
        return "Movie Event"


class ConcertEvent(Event):
    def get_event_type(self):
        return "Concert Event"
