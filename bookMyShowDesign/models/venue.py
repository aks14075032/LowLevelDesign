from abc import ABC, abstractmethod


class Venue(ABC):
    def __init__(self, venue_id, name, location):
        self.venue_id = venue_id
        self.name = name
        self.location = location

    @abstractmethod
    def get_venue_type(self):
        pass


class Theatre(Venue):
    def get_venue_type(self):
        return "Theater"


class ConcertHall(Venue):
    def get_venue_type(self):
        return "Hall"
