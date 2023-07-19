from threading import Lock
from Strategy.defaultPricingStrategy import DefaultPricingStrategy
from Strategy.leastTimeBasedStrategy import LeastTimeBasedStrategy
from Strategy.ratingBasedPricingStrategy import RatingBasedPricingStrategy


class StrategyMgr:
    strategyMgrInstance = None
    mtx = Lock()

    @staticmethod
    def get_strategy_instance():
        if not StrategyMgr.strategyMgrInstance:
            with StrategyMgr.mtx:
                if not StrategyMgr.strategyMgrInstance:
                    StrategyMgr.strategyMgrInstance = StrategyMgr()
        return StrategyMgr.strategyMgrInstance

    def get_pricing_strategy(self, meta_data):
        return RatingBasedPricingStrategy()

    def get_driver_matching_strategy(self, meta_data):
        return LeastTimeBasedStrategy()
