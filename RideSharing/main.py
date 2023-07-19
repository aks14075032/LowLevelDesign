from Rider.rider import Rider
from Driver.driver import Driver
from Models.location import Location
from trip.tripMgr import TripMgr
from common import RATING
from Rider.riderMgr import RiderMgr
from Driver.driverMgr import DriverMgr

akshay_rider = Rider("Akshay", RATING.THREE_STARS)
rahul_rider = Rider("Rahul", RATING.FIVE_STARS)

rider_manager = RiderMgr.get_rider_mgr()
rider_manager.add_rider("akshay", akshay_rider)
rider_manager.add_rider("rahul", rahul_rider)

pintu_driver = Driver("Pintu", RATING.THREE_STARS)
chintu_driver = Driver("Chintu", RATING.FIVE_STARS)

driver_mgr = DriverMgr.get_driver_mgr()

driver_mgr.add_driver("pintu", pintu_driver)
driver_mgr.add_driver("chintu", chintu_driver)

trip_mgr = TripMgr.get_trip_mgr_instance()

print("Creating Trip for Akshay from location(10, 10) to (30, 30)")
trip_mgr.create_trip(akshay_rider, Location(10, 10), Location(30, 30))

print("Creating Trip for rahul from location(120, 120) to (250, 250)")
trip_mgr.create_trip(rahul_rider, Location(10, 10), Location(30, 30))

# Display all trip

trips_map = trip_mgr.get_trips_map()

for trip in trips_map.values():
    trip.display_trip_details()

