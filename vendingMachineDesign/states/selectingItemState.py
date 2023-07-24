from vendingMachineDesign.states.vendingMachineState import VendingMachineState
from vendingMachineDesign.states.processingPaymentState import ProcessingPaymentState


class SelectingItemState(VendingMachineState):
    def __init__(self, selected_item):
        self.amount_inserted = 0
        self.selected_item = selected_item

    def select_item(self, item):
        print(f'Selected item: {item.name}')
        self.selected_item = item
        return ProcessingPaymentState(self.amount_inserted, self.selected_item)

    def insert_coin(self, amount):
        self.amount_inserted += amount
        print(f"Amount inserted: {self.amount_inserted}")
        return ProcessingPaymentState(self.amount_inserted, self.selected_item)

    def dispense_item(self):
        print("Please complete payment first")
        return self
