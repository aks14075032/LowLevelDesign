
class Order:
    def __init__(self, txn_type, price, order_type, quantity, stock):
        self.txn_type = txn_type
        self.price = price
        self.order_type = order_type
        self.quantity = quantity
        self.stock = stock

    def get_txn_type(self):
        return self.txn_type
