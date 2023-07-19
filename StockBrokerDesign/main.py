from StockBrokerDesign.models.stock import Stock
from StockBrokerDesign.models.user import User
from StockBrokerDesign.models.order import Order
from StockBrokerDesign.constants import *
from StockBrokerDesign.services.orderMgr import OrderManager
from StockBrokerDesign.services.userMgr import UserManager

reliance_stock = Stock("Reliance", 2800.9, EXCHANGE.NSE)
tata_power = Stock("TATA POWER", 238, EXCHANGE.BSE)

akshay = User(1, 1000)
user_mgr = UserManager()
user_mgr.add_user(1, akshay)

first_buy_order = Order(TXN_TYPE.BUY, 5601.8, ORDER_TYPE.MARKET, 2, reliance_stock)

order_mgr = OrderManager()
order_mgr.place_order(1, first_buy_order)

user_mgr.add_stock_to_user(1, first_buy_order)
user_mgr.get_user_order_details(1)

first_sell_order = Order(TXN_TYPE.SELL, 5601.9, ORDER_TYPE.LIMIT, 2, reliance_stock)

order_mgr.place_order(1, first_sell_order)
