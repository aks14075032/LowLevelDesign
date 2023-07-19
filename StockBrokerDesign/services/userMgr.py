class UserManager:
    def __init__(self):
        self.user_info = {}
        self.order_details = {}

    def get_user_info(self, user_id):
        return self.user_info.get(user_id)

    def add_user(self, user_id, user_details):
        self.user_info[user_id] = user_details
        print("User added Successfully")

    def add_stock_to_user(self, user_id, order_details):
        if user_id not in self.order_details:
            self.order_details[user_id] = []
        self.order_details[user_id].append(order_details)

    def get_user_order_details(self, user_id):
        for order in self.order_details[user_id]:
            print(f'You bought, #{order.stock.name} stock with #{order.quantity} worth {order.price}')