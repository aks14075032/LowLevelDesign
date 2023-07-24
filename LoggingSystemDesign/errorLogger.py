from LoggingSystemDesign.loggerInterface import Logger


class ErrorLogger(Logger):
    def __init__(self, next_logger=None):
        self.next_logger = next_logger

    def handle(self, level, message):
        if level == 'ERROR':
            print(f'[ERROR]: {message}')
        elif self.next_logger:
            self.next_logger.handle(level, message)

