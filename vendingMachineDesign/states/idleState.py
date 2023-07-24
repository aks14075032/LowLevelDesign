from vendingMachineDesign.states.vendingMachineState import VendingMachineState
from vendingMachineDesign.states.selectingItemState import SelectingItemState


class IdleState(VendingMachineState):
    def __init__(self):
        self.selected_item = None

    def select_item(self, item):
        print(f'Selected item: {item.name}')
        self.selected_item = item
        return SelectingItemState(self.selected_item)  # Return an instance of SelectingItemState

    def insert_coin(self, amount):
        print("Please select an item first")
        return self

    def dispense_item(self):
        print("Please select an item and make payment first")
        return self
