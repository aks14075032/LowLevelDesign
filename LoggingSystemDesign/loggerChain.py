from LoggingSystemDesign.infoLogger import InfoLogger
from LoggingSystemDesign.warningLogger import WarningLogger
from LoggingSystemDesign.errorLogger import ErrorLogger


def create_logger_chain():
    error_logger = ErrorLogger()
    warning_logger = WarningLogger(error_logger)
    info_logger = InfoLogger(warning_logger)

    return info_logger