from StockBrokerDesign.constants import *
from StockBrokerDesign.services.userMgr import UserManager


class OrderValidation:
    @staticmethod
    def validate_order(user_id, order):
        user = UserManager().get_user_info(user_id)
        if order.get_txn_type() == TXN_TYPE.BUY:
            print("Checking if user has funds to buy")
        else:
            print("Checking if user has stocks to sell")
        print("We are assuming all the orders are valid we are returning true")
        return True

