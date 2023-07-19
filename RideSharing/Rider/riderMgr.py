from threading import Lock


class RiderMgr:
    riderMgrInstance = None  # Singleton Pattern
    mtx = Lock()

    def __init__(self):
        self.ridersMap = {}

    @staticmethod
    def get_rider_mgr():
        if not RiderMgr.riderMgrInstance:
            with RiderMgr.mtx:
                if not RiderMgr.riderMgrInstance:
                    RiderMgr.riderMgrInstance = RiderMgr()
        return RiderMgr.riderMgrInstance

    def get_rider(self, d_rider_name):
        return self.ridersMap[d_rider_name]

    def add_rider(self, d_rider_name, d_rider):
        self.ridersMap[d_rider_name] = d_rider
