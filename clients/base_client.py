class GetException(Exception):
    pass


class PostException(Exception):
    pass


class TokenException(Exception):
    pass


class BaseCreds:
    def __init__(self):
        raise NotImplementedError("Creds not implemented")

    @staticmethod
    def get_creds(client_name: str):
        from .td_client import TDCreds

        CLASS_MAP = {"TD Ameritrade": TDCreds}
        client = CLASS_MAP.get(client_name, None)
        if client:
            return client
        raise NotImplementedError(f"{client_name} creds not implemented yet")


class BaseClient:
    def __init__(self):
        pass

    @staticmethod
    def get_client(client_name: str):
        from .td_client import TDClient

        CLASS_MAP = {"TD Ameritrade": TDClient}
        client = CLASS_MAP.get(client_name, None)
        if client:
            return client
        raise NotImplementedError(f"{client_name} not implemented yet")

    @staticmethod
    def _get_access_token():
        raise NotImplementedError("_get_access_token not implemented")

    @staticmethod
    def _build_order_body(symbol: str, quantity: int, instruction: str):
        raise NotImplementedError("_build_order_body not implemented")

    def get_transactions(self):
        raise NotImplementedError("get_transactions not implemented")

    def get_symbol_quote(self, symbol: str):
        raise NotImplementedError("get_symbol_quote not implemented")

    def place_order(self, symbol, quantity: int):
        raise NotImplementedError("place_order not implemented")

    def get_orders(self):
        raise NotImplementedError("get_orders not implemented")

    def get_positions(self):
        raise NotImplementedError("get_positions not implemented")


def main():
    pass


if __name__ == "__main__":
    main()
