from common import RATING


class TripMetaData:
    def __init__(self, source, dest, rider_rating):
        self.source = source
        self.destination = dest
        self.rider_rating = rider_rating
        self.driver_rating = RATING.UNASSIGNED

    def get_rider_rating(self):
        return self.rider_rating

    def get_driver_rating(self):
        return self.driver_rating

    def set_driver_rating(self, driver_rating):
        self.driver_rating = driver_rating
