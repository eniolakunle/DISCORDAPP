from .fixtures import TD_MOCK_POSITIONS
from parameterized import parameterized
import unittest

import os

from ...clients.td_client import TDClient

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
# from clients.td_client import TDClient


class MockTDClient:
    def __init__(self):
        pass

    def get_positions(self):
        return TD_MOCK_POSITIONS


class TDClientTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (-5, "SELL_TO_CLOSE"),
            (-4, "SELL_TO_CLOSE"),
            (-3, "SELL_TO_CLOSE"),
            (-2, "SELL_TO_CLOSE"),
            (-1, "SELL_TO_CLOSE"),
            (0, "BUY_TO_OPEN"),
            (1, "BUY_TO_OPEN"),
            (2, "BUY_TO_OPEN"),
            (3, "BUY_TO_OPEN"),
            (4, "BUY_TO_OPEN"),
            (5, "BUY_TO_OPEN"),
        ]
    )
    def test_get_instruction(self, amount, expected_instruction):
        output = TDClient._get_instruction(amount)
        self.assertEqual(output, expected_instruction)

    @parameterized.expand(
        [("XYZ", 1, "BUY_TO_OPEN"), (None, 0, "CHICKEN"), ("ABC", 2, "SELL_TO_CLOSE")]
    )
    def test_build_order_body(self, symbol, amount, instruction):
        body = TDClient._build_order_body(symbol, amount, instruction)
        order = body["orderLegCollection"][0]
        self.assertEqual(order["instruction"], instruction)
        self.assertEqual(order["quantity"], amount)
        self.assertEqual(order["instrument"]["symbol"], symbol)

    @parameterized.expand(
        [
            (
                {
                    "symbol": "MSFT_052022P255",
                    "description": "MSFT May 20 2022 255 Put",
                    "openInterest": 3321,
                    "expirationDay": -1,
                    "expirationMonth": -1,
                    "expirationYear": -1,
                    "daysToExpiration": 9,
                },
                True,
            ),
            (
                {
                    "symbol": "MSFT_052022P255",
                    "description": "SYMBOL NOT FOUND",
                    "openInterest": 3321,
                    "expirationDay": 20,
                    "expirationMonth": 5,
                    "expirationYear": 2022,
                    "daysToExpiration": 9,
                },
                True,
            ),
            (
                {
                    "symbol": "MSFT_052022P255",
                    "description": "SYMBOL NOT FOUND",
                    "openInterest": 3321,
                    "expirationDay": -1,
                    "expirationMonth": -1,
                    "expirationYear": -1,
                    "daysToExpiration": 9,
                },
                False,
            ),
        ]
    )
    def test_validate_option_quote(self, quote, result):
        output = TDClient._validate_option_quote(quote)
        self.assertEqual(output, result)


if __name__ == "__main__":
    unittest.main()
