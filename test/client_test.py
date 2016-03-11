import unittest
from moto import mock_cloudformation
import fmc

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        eb = fmc.resource("ElasticBeanstalk")
        eb_app = eb.Application(
                    LogicalID = "TestApplication"
                )

        stack_repr = eb_app.representation()
        stack_repr["AWSTemplateFormatVersion"] = "2010-09-09"

        self.stack = type('Stack', (object,), {
            "name": "TestStack"
            })

        self.stack.resources = [eb_app]
        self.client = fmc.client()
        self.stack_repr = stack_repr

    def test_stack_representation(self):
        representation = self.client.stack_representation(
                self.stack
                )

        self.assertDictEqual(
                self.stack_repr,
                representation
                )

    @mock_cloudformation
    def test_validate_stack(self):
        self.skipTest("validate_template not implemented in moto")

    @mock_cloudformation
    def test_create_stack(self):
        self.skipTest("validate_template not implemented in moto")

    @mock_cloudformation
    def test_delete_stack(self):
        expected = {
                'ResponseMetadata': {
                    'HTTPStatusCode': 200,
                    'RequestId': '5ccc7dcd-744c-11e5-be70-example'
                    }
                }

        result = self.client.delete_stack(
                self.stack
                )

        self.assertDictEqual(
                expected,
                result
                )

if __name__ == "__main__":
    unittest.main()
