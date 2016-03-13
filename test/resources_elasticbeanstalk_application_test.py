import unittest
import fmc

eb = fmc.resource("ElasticBeanstalk")

class ApplicationTestCase(unittest.TestCase):

    def test_instance(self):
        '''Test ElasticBeanstalk.Application Is Proper Instance'''
        eb_app = eb.Application(
                LogicalID = "Test"
                )
        self.assertIsInstance(eb_app, fmc.resources.elasticbeanstalk.Application)

    def test_exception(self):
        '''Test ElasticBeanstalk.Application Raises MissingArgument'''
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            eb.Application()

    def test_str_repr(self):
        '''Test ElasticBeanstalk.Application Object String Representation'''
        eb_app = eb.Application(
                LogicalID = "Test"
                )

        representation = "<AWS::ElasticBeanstalk::Application: Test>"

        self.assertEqual(
                representation,
                str(eb_app)
                )

    def test_representation(self):
        '''Test ElasticBeanstalk.Application Representation'''
        eb_app = eb.Application(
                LogicalID = "Test",
                ApplicationName = "TestApplication",
                Description = "A Test Application",
                DependsOn = "Something Else?"
                )
        representation = {
                "Resources": {
                    "Test": {
                        "Type": "AWS::ElasticBeanstalk::Application",
                        "Properties": {
                            "ApplicationName": "TestApplication",
                            "Description": "A Test Application"
                            },
                        "DependsOn": "Something Else?"
                        }
                    }
                }

        self.assertDictEqual(
                representation,
                eb_app.representation()
                )
