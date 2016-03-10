import unittest
import fmc

class ParameterTestCase(unittest.TestCase):
    def setUp(self):
        args = {
                "LogicalID": "Test",
                "Type": "String",
                "Default": "Foo",
                "NoEcho": False,
                "AllowedValues": [
                    "Foo",
                    "Bar",
                    ],
                "AllowedPattern": "*",
                "MaxLength": 3,
                "MinLength": 3,
                "MaxValue": "Foo",
                "MinValue": "Bar",
                "Description": "Test Parameter",
                "ConstraintDescription": "Foo or Bar"
                }

        self.params = fmc.parameter(
                **args
                )

    def test_representation(self):
        representation = {
                "Parameters": {
                    "Test": {
                        "Type": "String",
                        "Default": "Foo",
                        "NoEcho": False,
                        "AllowedValues": [
                            "Foo",
                            "Bar"
                            ],
                        "AllowedPattern": "*",
                        "MaxLength": 3,
                        "MinLength": 3,
                        "MaxValue": "Foo",
                        "MinValue": "Bar",
                        "Description": "Test Parameter",
                        "ConstraintDescription": "Foo or Bar"
                        }
                    }
                }

        self.assertDictEqual(
                representation,
                self.params.representation()
                )


    def test_exception(self):
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            fmc.parameter()

if __name__ == "__main__":
    unittest.main()
