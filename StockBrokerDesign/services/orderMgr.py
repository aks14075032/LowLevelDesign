from StockBrokerDesign.services.orderValidation import OrderValidation
from StockBrokerDesign.services.orderExecution import OrderExecution


class OrderManager:
    def __init__(self):
        self.order_list = {}

    @staticmethod
    def place_order(user_id, order):
        if OrderValidation().validate_order(user_id, order):
            OrderExecution().place_order(user_id, order)
