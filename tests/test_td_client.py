from .fixtures import TD_MOCK_POSITIONS
from parameterized import parameterized
import unittest

import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from td_client import TDClient


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
