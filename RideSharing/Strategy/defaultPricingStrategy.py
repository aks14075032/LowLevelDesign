from Strategy.pricingStrategy import PricingStrategy


class DefaultPricingStrategy(PricingStrategy):
    def calculate_price(self, trip_meta_data) -> float:
        print("Based on default strategy, price is 100")
        return 100.0
