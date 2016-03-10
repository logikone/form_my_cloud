import unittest
import fmc

class MetaDataTestCase(unittest.TestCase):
    def setUp(self):
        self.metadata = fmc.metadata(
                Instances = {
                    "Description": "Instances"
                    },
                Databases = {
                    "Description": "Databases"
                    },
                Init = {
                    "Description": "Init",
                    },
                Interface = {
                    "Description": "Interface",
                    },
                Designer = {
                    "Description": "Designer",
                    },
                )

    def test_str_repr(self):
        self.assertEqual(
                "<MetaData>",
                str(self.metadata)
                )

    def test_representation(self):
        representation = {
                "Metadata": {
                    "Instances": {
                        "Description": "Instances"
                        },
                    "Databases": {
                        "Description": "Databases"
                        },
                    "AWS::CloudFormation::Init": {
                        "Description": "Init"
                        },
                    "AWS::CloudFormation::Interface": {
                        "Description": "Interface"
                        },
                    "AWS::CloudFormation::Designer": {
                        "Description": "Designer"
                        }
                    }
                }

        self.assertDictEqual(
                representation,
                self.metadata.representation()
                )

if __name__ == "__main__":
    unittest.main()
