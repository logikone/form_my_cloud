import unittest
from fmc.format import Version

class VersionTestCase(unittest.TestCase):
    version = Version()

    def test_str_repr(self):
        '''Test Format.Version Object String Representation'''
        representation = "<Format.Version: 2010-09-09>"

        self.assertEqual(
                representation,
                str(self.version)
                )

    def test_representation(self):
        '''Test Format.Version Representation'''
        representation = {
                "AWSTemplateFormatVersion": "2010-09-09"
                }

        self.assertDictEqual(
                representation,
                self.version.representation()
                )

if __name__ == "__main__":
    unittest.main()
