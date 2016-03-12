import json
import unittest
from fmc import cli

class CliTestCase(unittest.TestCase):
    def test_get_options(self):
        self.skipTest("TODO")

    def test_main(self):
        self.skipTest("TODO")

    def tests__dumps(self):
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
