from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def handle(self, level, message):
        pass
