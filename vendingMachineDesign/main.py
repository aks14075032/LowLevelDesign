from vendingMachineDesign.models.item import Item
from vendingMachineDesign.models.vendingMachine import VendingMachine

vending_machine = VendingMachine()
item1 = Item("Chocolates", 10, 10)
item2 = Item("Drink", 5, 20)

vending_machine.add_item(item1)
vending_machine.add_item(item2)

vending_machine.print_available_items()

vending_machine.select_item("Chocolates")

vending_machine.insert_coin(10)
vending_machine.insert_coin(5)

vending_machine.dispense_item()
vending_machine.print_available_items()
