import unittest
from parameterized import parameterized

import os

# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.sys.path.insert(0, parentdir)
from ...clients.base_client import BaseClient, BaseCreds, Clients
from ...clients.td_client import TDClient, TDCreds


class BaseCredsTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (Clients.TD.value, TDCreds),
        ]
    )
    def test_get_client(self, creds_name, expected_creds):
        creds = BaseCreds.get_creds_object(creds_name)
        self.assertIs(creds, expected_creds)
        self.assertTrue(issubclass(creds, TDCreds))

    @parameterized.expand(
        [
            ("",),
            (None,),
            ("chicken butt",),
        ]
    )
    def test_get_client_expected_not_implemented(self, creds_name):
        with self.assertRaises(NotImplementedError):
            BaseCreds.get_creds_object(creds_name)


class BaseClientTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (Clients.TD.value, TDClient),
        ]
    )
    def test_get_client(self, client_name, expected_client):
        client = BaseClient.get_client(client_name)
        self.assertIs(client, expected_client)
        self.assertTrue(issubclass(client, BaseClient))

    @parameterized.expand(
        [
            ("",),
            (None,),
            ("chicken butt",),
        ]
    )
    def test_get_client_expected_not_implemented(self, client_name):
        with self.assertRaises(NotImplementedError):
            BaseClient.get_client(client_name)


if __name__ == "__main__":
    unittest.main()
