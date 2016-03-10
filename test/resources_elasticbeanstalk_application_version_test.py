import unittest
import fmc

eb = fmc.resource("ElasticBeanstalk")

class ApplicationVersionTestCase(unittest.TestCase):
    eb_app = eb.ApplicationVersion(
            LogicalID = "Test",
            ApplicationName = "TestApplication",
            Description = "A Test Application",
            SourceBundle = {
                }
            )

    def test_instance(self):
        self.assertIsInstance(
                self.eb_app,
                fmc.resources.elasticbeanstalk.ApplicationVersion
                )

    def test_exception(self):
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            eb.ApplicationVersion()

    def test_str_repr(self):
        string_repr = "<AWS::ElasticBeanstalk::ApplicationVersion: Test>"

        self.assertEqual(
                string_repr,
                str(self.eb_app)
                )

    def test_representation(self):
        representation = {
                "Resources": {
                    "Test": {
                        "Type": "AWS::ElasticBeanstalk::ApplicationVersion",
                        "Properties": {
                            "ApplicationName": "TestApplication",
                            "Description": "A Test Application",
                            "SourceBundle": {
                                }
                            }
                        }
                    }
                }

        self.assertDictEqual(
                representation,
                self.eb_app.representation()
                )

