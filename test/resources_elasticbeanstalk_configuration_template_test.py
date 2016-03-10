import unittest
import fmc

eb = fmc.resource("ElasticBeanstalk")

class ApplicationTestCase(unittest.TestCase):
    template = {
            "LogicalID": "Test",
            "ApplicationName": "TestApplication",
            "Description": "A Test Application",
            "OptionSettings": {
                },
            "SolutionStackName": "Amazon Linux 64bit"
            }

    eb_config_template = eb.ConfigurationTemplate(**template)

    def test_instance(self):
        self.assertIsInstance(
                self.eb_config_template,
                fmc.resources.elasticbeanstalk.ConfigurationTemplate
                )

    def test_exception(self):
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            eb.ConfigurationTemplate()

        with self.assertRaises(fmc.exceptions.MissingOneOf) as cm:
            template = self.template
            template.pop("SolutionStackName")
            eb.ConfigurationTemplate(**template)

    def test_str_repr(self):
        representation = "<AWS::ElasticBeanstalk::ConfigurationTemplate: Test>"

        self.assertEqual(
                representation,
                str(self.eb_config_template)
                )

    def test_representation(self):
        representation = {
                "Resources": {
                    "Test": {
                        "Type": "AWS::ElasticBeanstalk::ConfigurationTemplate",
                        "Properties": {
                            "ApplicationName": "TestApplication",
                            "Description": "A Test Application",
                            "OptionSettings": {
                                },
                            "SolutionStackName": "Amazon Linux 64bit"
                            }
                        }
                    }
                }

        self.assertDictEqual(
                representation,
                self.eb_config_template.representation()
                )

if __name__ == "__main__":
    unittest.main()
