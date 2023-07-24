from vendingMachineDesign.states.idleState import IdleState


class VendingMachine:
    def __init__(self):
        self.current_state = IdleState()
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def select_item(self, item_name):
        if item_name in self.items:
            selected_item = self.items[item_name]
            self.current_state = self.current_state.select_item(selected_item)
        else:
            print("Item not available in the vending machine.")

    def insert_coin(self, amount):
        self.current_state = self.current_state.insert_coin(amount)

    def dispense_item(self):
        self.current_state = self.current_state.dispense_item()

    def print_available_items(self):
        print("Available items: ")
        for item in self.items.values():
            print(f"{item.name} - Price: {item.price}, Quantity: {item.quantity}")