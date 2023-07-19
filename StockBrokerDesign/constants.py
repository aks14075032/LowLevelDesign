from enum import Enum


class TXN_TYPE(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class ORDER_TYPE(Enum):
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'


class EXCHANGE(Enum):
    NSE = 'NSE'
    BSE = 'BSE'


class ORDER_STATUS(Enum):
    OPEN = 'OPEN'
    PARTIALLY_DONE = 'PARTIALLY_DONE'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'


