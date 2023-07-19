from Strategy.pricingStrategy import PricingStrategy
from trip.tripMetaData import TripMetaData
from common import Util


class RatingBasedPricingStrategy(PricingStrategy):
    def calculate_price(self, trip_meta_data) -> float:
        if Util.is_high_rating(trip_meta_data.get_rider_rating()):
            price = 55.0
        else:
            price = 65.0
        print(f'Based on rating strategy, price is {price}', )
        return price

