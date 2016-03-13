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
        '''Test ElasticBeanstalk.ApplicationVersion Is Proper Instance'''
        self.assertIsInstance(
                self.eb_app,
                fmc.resources.elasticbeanstalk.ApplicationVersion
                )

    def test_exception(self):
        '''Test ElasticBeanstalk.ApplicationVersion Raises MissingArgument'''
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            eb.ApplicationVersion()

    def test_str_repr(self):
        '''Test ElasticBeanstalk.ApplicationVersion Object String Representation'''
        string_repr = "<AWS::ElasticBeanstalk::ApplicationVersion: Test>"

        self.assertEqual(
                string_repr,
                str(self.eb_app)
                )

    def test_representation(self):
        '''Test ElasticBeanstalk.ApplicationVersion Representation'''
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

