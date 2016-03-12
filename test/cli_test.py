import json
import unittest
from fmc.client import Client
#from fmc import cli

class TestClient(Client):
    def __init__(self):
        session = botocore.session.get_session()
        self.cf_client = session.create_client(
                "cloudformation",
                region_name = "us-east-1"
                )

class CliTestCase(unittest.TestCase):
    def test_get_options(self):
        self.skipTest("TODO")

    def test_main(self):
        self.skipTest("TODO")

    def tests__dumps(self):
        self.skipTest("TODO")
        #result = cli._dumps({
        #    "Foo": "Bar"
        #    })

        #expected = json.dumps({
        #    "Foo": "Bar"
        #    },
        #    indent = 4,
        #    sort_keys = True
        #    )

        #self.assertEqual(
        #        expected,
        #        result
        #        )
