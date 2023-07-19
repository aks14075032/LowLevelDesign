from threading import Lock
from trip.tripMetaData import TripMetaData
from Strategy.strategyMgr import StrategyMgr
from trip.trip import Trip


class TripMgr:
    TripMgrInstance = None
    mtx = Lock()

    def __init__(self):
        self.trips_info = {}
        self.trip_meta_data_info = {}

    @staticmethod
    def get_trip_mgr_instance():
        if not TripMgr.TripMgrInstance:
            with TripMgr.mtx:
                TripMgr.TripMgrInstance = TripMgr()
        return TripMgr.TripMgrInstance

    def create_trip(self, p_rider, source, destination):
        meta_data = TripMetaData(source, destination, p_rider.get_rating())
        strategy_mgr = StrategyMgr.get_strategy_instance()

        pricing_strategy = strategy_mgr.get_pricing_strategy(meta_data)
        driver_matching_strategy = strategy_mgr.get_driver_matching_strategy(meta_data)

        driver = driver_matching_strategy.match_driver(meta_data)
        price = pricing_strategy.calculate_price(meta_data)

        trip = Trip(p_rider, driver, source, destination, price, pricing_strategy, driver_matching_strategy)

        trip_id = trip.get_trip_id()
        self.trips_info[trip_id] = trip
        self.trip_meta_data_info[trip_id] = meta_data

    def get_trips_map(self):
        return self.trips_info
