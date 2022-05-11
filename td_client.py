from http import HTTPStatus
import json
import logging
from typing import Tuple, Union
import requests
from requests.exceptions import HTTPError
from td_endpoints import *

ACCOUNT_ID = 253873290
CONSUMER_KEY = "GIGBDGR7AKWXVZV3JGGLJ9AAHS1U5AWO"


class GetException(Exception):
    pass


class PostException(Exception):
    pass


class TokenException(Exception):
    pass


class TDClient:
    def __init__(self):
        self.access_token = self._get_access_token()
        self.header = {"Authorization": f"Bearer {self.access_token}"}

    def _get_error_message(self, e: HTTPError):
        error = bytes.decode(e.response.content)
        error = json.loads(error)["error"]
        return error

    def _check_response(self, r: requests.models.Response):
        try:
            r.raise_for_status()
            if response := r.text:
                logging.info(f"TD Response: {response}")
            return r
        except HTTPError:
            raise

    def _get_access_token(self):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": TDEndpointData.TD_TOKEN.get("refresh_token"),
            "client_id": CONSUMER_KEY,
        }
        r = requests.post(TDEndpointData.GET_TOKEN, data=data)
        access_token = r.json().get("access_token")
        if not access_token:
            raise TokenException("No access token, invalid credentials.")
        return access_token

    def _build_option_body(self, symbol: str, quantity: None, instruction: str = None):
        body = TDEndpointData.BUY_OPTION_BODY
        first_order = body["orderLegCollection"][0]
        first_order["instrument"]["symbol"] = symbol
        if quantity:
            first_order["quantity"] = quantity
        if instruction:
            first_order["instruction"] = instruction
        return body

    def _place_option_order(
        self, symbol: str, quantity: int = None, instruction: str = None
    ) -> Tuple[str, HTTPStatus]:
        body = self._build_option_body(symbol, quantity, instruction)
        link = TDEndpointData.PLACE_ORDER.format(accountID=ACCOUNT_ID)
        try:
            r = self._send_post(link, json=body)
            return (
                "Order successfully placed, please check brokerage to confirm status.",
                HTTPStatus.OK,
            )
        except PostException as e:
            return (f"There was an error: {e}", HTTPStatus.BAD_REQUEST)

    def _validate_option_quote(self, option_quote: dict) -> bool:
        invalid_values = ["SYMBOL NOT FOUND", "-1"]
        keys_to_check = [
            "description",
            "expirationDay",
            "expirationMonth",
            "expirationYear",
        ]
        if all(
            str(option_quote.get(key)).upper() in invalid_values
            for key in keys_to_check
        ):
            return False
        return True

    def _send(self, type: str, link: str, **kwargs):
        if type == "get":
            r = requests.get(link, **kwargs, headers=self.header)
            _exec = GetException
        elif type == "post":
            r = requests.post(link, **kwargs, headers=self.header)
            _exec = PostException
        else:
            raise NotImplementedError(f"Boy implement that: {type}")
        try:
            return self._check_response(r)
        except HTTPError as e:
            error = self._get_error_message(e)
            raise _exec(error)

    def _send_get(self, link: str, **kwargs):
        return self._send("get", link, **kwargs)

    def _send_post(self, link: str, **kwargs):
        return self._send("post", link, **kwargs)

    def get_transactions(self) -> dict:
        r = self._send_get(TDEndpointData.GET_TRANSACTIONS.format(accountID=ACCOUNT_ID))
        json_response = r.json()
        if json_response:
            return json_response
        else:
            raise GetException("No transactions")

    def _get_account_info(self, type: str) -> Union[dict, list]:
        params = {"fields": type}
        r = self._send_get(
            TDEndpointData.GET_ACCOUNTS.format(accountID=ACCOUNT_ID),
            params=params,
        )
        account = r.json().get("securitiesAccount")
        if type == "positions":
            items = account.get("positions")
        elif type == "orders":
            items = account.get("orderStrategies")
        if items:
            return items
        raise GetException(f"No {type}")

    def get_symbol_quote(self, symbol: str):
        symbol_quote_link = TDEndpointData.GET_QUOTE.format(symbol=symbol)
        r = self._send_get(symbol_quote_link)
        json_response = r.json()
        if json_response:
            return json_response[symbol]
        else:
            raise GetException("Couldn't get data for ticker.")

    def place_order(self, symbol, quantity: int = 1):
        # if negative quanitity, attempt to sell
        instruction = "SELL_TO_CLOSE" if quantity < 0 else None
        quantity = abs(quantity)
        option_quote = self.get_symbol_quote(symbol)
        if option_quote:
            if self._validate_option_quote(option_quote):
                response = self._place_option_order(
                    symbol, quantity=quantity, instruction=instruction
                )
                return response
            else:
                raise GetException("Symbol Not Found")
        else:
            raise GetException("Didn't get option data, may be expired.")

    def get_orders(self):
        return self._get_account_info("orders")

    def get_positions(self):
        return self._get_account_info("positions")


def main():
    client = TDClient()
    # client.buy_option("IWM_042922P195")
    client.get_orders()
    n = 1


if __name__ == "__main__":
    main()