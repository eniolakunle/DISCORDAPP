from enum import Enum


class Clients(Enum):
    TD = "TD Ameritrade"


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
    def get_creds_object(client_name: str):
        from .td_client import TDCreds

        CLASS_MAP = {Clients.TD.value: TDCreds}
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

        CLASS_MAP = {Clients.TD.value: TDClient}
        client = CLASS_MAP.get(client_name, None)
        if client:
            return client
        raise NotImplementedError(f"{client_name} not implemented yet")

    @staticmethod
    def _get_access_token():
        raise NotImplementedError("_get_access_token not implemented")

    @staticmethod
    def _build_order_body():
        raise NotImplementedError("_build_order_body not implemented")

    def get_transactions(self):
        raise NotImplementedError("get_transactions not implemented")

    def get_symbol_quote(self):
        raise NotImplementedError("get_symbol_quote not implemented")

    def place_order(self):
        raise NotImplementedError("place_order not implemented")

    def get_orders(self):
        raise NotImplementedError("get_orders not implemented")

    def get_positions(self):
        raise NotImplementedError("get_positions not implemented")


def main():
    n = 1
    pass


if __name__ == "__main__":
    main()
