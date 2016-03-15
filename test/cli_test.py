import json
import unittest
from fmc.client import Client
from fmc import cli

class TestClient(Client):
    def __init__(self):
        session = botocore.session.get_session()
        self.cf_client = session.create_client(
                "cloudformation",
                region_name = "us-east-1"
                )

class CliTestCase(unittest.TestCase):
    def test_get_options(self):
        '''Test Get Options w/ Args Passed'''
        result = cli.get_options(["validate", "basic"])

        self.assertTrue(result)

    def test_main(self):
        '''Test Main Handler'''
        self.skipTest("TODO")

    def tests__dumps(self):
        '''Test _dumps Serialization Helper'''
        result = cli._dumps({
            "Foo": "Bar"
            })

        expected = json.dumps({
            "Foo": "Bar"
            },
            indent = 4,
            sort_keys = True
            )

        self.assertEqual(
                expected,
                result
                )
