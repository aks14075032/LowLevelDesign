from threading import Lock


class DriverMgr:
    driverMgrInstance = None  # Used for Singleton Pattern
    mtx = Lock()

    def __init__(self):
        self.driversMap = {}

    @staticmethod
    def get_driver_mgr():
        if not DriverMgr.driverMgrInstance:
            with DriverMgr.mtx:
                if not DriverMgr.driverMgrInstance:
                    DriverMgr.driverMgrInstance = DriverMgr()
        return DriverMgr.driverMgrInstance

    def add_driver(self, p_driver_name, p_driver):
        self.driversMap[p_driver_name] = p_driver

    def get_driver(self, p_driver_name):
        return self.driversMap[p_driver_name]

    def get_drivers_map(self):
        return self.driversMap
