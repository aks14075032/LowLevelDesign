from StockBrokerDesign.services.exchangeConnector import ExchangeConnector


class OrderExecution:
    def place_order(self, user_id, order):
        exchange_connector = ExchangeConnector.get_exchange_connector_instance()
        exchange_connector.send_order_to_exchange(user_id, order)

