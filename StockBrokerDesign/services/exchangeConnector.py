from threading import Lock


class ExchangeConnector:
    ExchangeConnectorInstance = {}
    mtx = Lock()

    @staticmethod
    def get_exchange_connector_instance():
        if not ExchangeConnector.ExchangeConnectorInstance:
            with ExchangeConnector.mtx:
                if not ExchangeConnector.ExchangeConnectorInstance:
                    ExchangeConnector.ExchangeConnectorInstance = ExchangeConnector()
        return ExchangeConnector.ExchangeConnectorInstance

    @staticmethod
    def send_order_to_exchange(user_id, order):
        print("Order is sent to exchange")
