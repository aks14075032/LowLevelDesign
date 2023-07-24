from LoggingSystemDesign.loggerInterface import Logger


class InfoLogger(Logger):
    def __init__(self, next_logger = None):
        self.next_logger = next_logger

    def handle(self, level, message):
        if level == 'INFO':
            print(f'[INFO]: {message}')
        elif self.next_logger:
            self.next_logger.handle(level, message)

