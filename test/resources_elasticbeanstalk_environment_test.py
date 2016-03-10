import unittest
import fmc

eb = fmc.resource("ElasticBeanstalk")

class EnvironmentTestCase(unittest.TestCase):
    template = {
            "LogicalID": "Test",
            "ApplicationName": "TestApplication",
            "Description": "A Test Application",
            "OptionSettings": {
                },
            "SolutionStackName": "Amazon Linux 64bit",
            "CNAMEPrefix": "test",
            "EnvironmentName": "TestEnvironment",
            "Tags": {
                },
            "TemplateName": "TestTemplate",
            "Tier": "t2.nano",
            "VersionLabel": "v1"
            }

    eb_environment = eb.Environment(**template)

    def test_instance(self):
        self.assertIsInstance(
                self.eb_environment,
                fmc.resources.elasticbeanstalk.Environment
                )

    def test_exception(self):
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            eb.Environment()

    def test_str_repr(self):
        representation = "<AWS::ElasticBeanstalk::Environment: Test>"

        self.assertEqual(
                representation,
                str(self.eb_environment)
                )

    def test_representation(self):
        representation = {
                "Resources": {
                    "Test": {
                        "Type": "AWS::ElasticBeanstalk::Environment",
                        "Properties": {
                            "ApplicationName": "TestApplication",
                            "Description": "A Test Application",
                            "OptionSettings": {
                                },
                            "SolutionStackName": "Amazon Linux 64bit",
                            "CNAMEPrefix": "test",
                            "EnvironmentName": "TestEnvironment",
                            "Tags": {
                                },
                            "TemplateName": "TestTemplate",
                            "Tier": "t2.nano",
                            "VersionLabel": "v1"
                            }
                        }
                    }
                }

        self.assertDictEqual(
                representation,
                self.eb_environment.representation()
                )

if __name__ == "__main__":
    unittest.main()
