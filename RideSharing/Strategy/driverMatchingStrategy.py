from abc import ABC, abstractmethod


class DriverMatchingStrategy(ABC):
    @abstractmethod
    def match_driver(self, trip_meta_data):
        pass
