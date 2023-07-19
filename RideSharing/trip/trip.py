from common import TRIP_STATUS


class Trip:
    next_trip_id = 1

    def __init__(self, rider, driver, srcloc, dstloc, price, pricing_strategy, driver_matching_strategy):
        self.rider = rider
        self.driver = driver
        self.srcloc = srcloc
        self.dstloc = dstloc
        self.status = TRIP_STATUS.DRIVER_ON_THE_WAY
        self.trip_id = Trip.next_trip_id
        Trip.next_trip_id += 1
        self.price = price
        self.pricing_strategy = pricing_strategy
        self.driver_matching_strategy = driver_matching_strategy

    def get_trip_id(self):
        return self.trip_id

    def display_trip_details(self):
        print()
        print("Trip id -", self.trip_id)
        print("Rider -", self.rider.get_rider_name())
        print("Driver -", self.driver.get_drive_name())
        print("Price -", self.price)
        print("Locations -", self.srcloc.latitude, ",", self.srcloc.longitude, "and",
              self.dstloc.latitude, ",", self.dstloc.longitude)



