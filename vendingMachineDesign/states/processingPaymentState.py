from vendingMachineDesign.states.vendingMachineState import VendingMachineState


class ProcessingPaymentState(VendingMachineState):
    def __init__(self, amount_inserted, selected_item):
        self.amount_inserted = amount_inserted
        self.selected_item = selected_item

    def select_item(self, item):
        print("Payment processing, cannot change item selection.")
        return self

    def insert_coin(self, amount):
        self.amount_inserted += amount
        print(f"Amount inserted: {self.amount_inserted}")
        return self

    def dispense_item(self):
        if self.amount_inserted >= self.selected_item.price:
            from vendingMachineDesign.states.idleState import IdleState
            print("Payment completed. Dispensing item.")
            self.selected_item.quantity -= 1
            return IdleState()
        else:
            print("Insufficient amount. Please insert more coins.")
            return self
