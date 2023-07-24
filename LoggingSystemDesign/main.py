from LoggingSystemDesign.loggerChain import *

logger_chain = create_logger_chain()
logger_chain.handle('INFO', 'This is an informational message.')
logger_chain.handle('WARNING', 'This is a warning message.')
logger_chain.handle('ERROR', 'This is an error message.')
