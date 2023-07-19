from abc import ABC, abstractmethod
from trip.tripMetaData import TripMetaData


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, trip_meta_data: TripMetaData) -> float:
        pass
