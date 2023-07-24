from abc import abstractmethod, ABC


class VendingMachineState(ABC):
    @abstractmethod
    def select_item(self, item):
        pass

    @abstractmethod
    def insert_coin(self, amount):
        pass

    @abstractmethod
    def dispense_item(self):
        pass
