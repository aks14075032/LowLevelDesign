from Strategy.driverMatchingStrategy import DriverMatchingStrategy
from Driver.driverMgr import DriverMgr


class LeastTimeBasedStrategy(DriverMatchingStrategy):
    def match_driver(self, trip_meta_data):
        driver_mgr = DriverMgr.get_driver_mgr()

        if len(driver_mgr.get_drivers_map()) == 0:
            print("No Driver !! Please Wait for sometime")

        print("Using Quadtree Searching for nearest cab, using driver manager to get and send notification")

        driver = list(driver_mgr.get_drivers_map().values())[0]

        print('Setting ', driver.get_drive_name(), 'as driver')
        trip_meta_data.set_driver_rating(driver.get_rating())
        return driver
