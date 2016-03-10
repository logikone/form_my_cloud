import unittest
from fmc.format import Version

class VersionTestCase(unittest.TestCase):
    version = Version()

    def test_str_repr(self):
        representation = "<Format.Version: 2010-09-09>"

        self.assertEqual(
                representation,
                str(self.version)
                )

    def test_representation(self):
        representation = {
                "AWSTemplateFormatVersion": "2010-09-09"
                }

        self.assertDictEqual(
                representation,
                self.version.representation()
                )

if __name__ == "__main__":
    unittest.main()
