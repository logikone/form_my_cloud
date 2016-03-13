import unittest
import fmc

eb = fmc.resource("ElasticBeanstalk")

class ConfigurationTemplateTestCase(unittest.TestCase):
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
        '''Test ElasticBeanstalk.ConfigurationTemplate Is Proper Instance'''
        self.assertIsInstance(
                self.eb_config_template,
                fmc.resources.elasticbeanstalk.ConfigurationTemplate
                )

    def test_missing_argument_exception(self):
        '''Test ElasticBeanstalk.ConfigurationTemplate Raises MissingArgument'''
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            eb.ConfigurationTemplate()

    def test_missing_one_of_exception(self):
        '''Test ElasticBeanstalk.ConfigurationTemplate Raises MissingOneOf'''
        with self.assertRaises(fmc.exceptions.MissingOneOf) as cm:
            template = self.template
            template.pop("SolutionStackName")
            eb.ConfigurationTemplate(**template)

    def test_str_repr(self):
        '''Test ElasticBeanstalk.ConfigurationTemplate Object String Representation'''
        representation = "<AWS::ElasticBeanstalk::ConfigurationTemplate: Test>"

        self.assertEqual(
                representation,
                str(self.eb_config_template)
                )

    def test_representation(self):
        '''Test ElasticBeanstalk.ConfigurationTemplate Representation'''
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
