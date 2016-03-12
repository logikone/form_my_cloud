import json
import unittest
import botocore.session
from botocore.stub import Stubber
import fmc
from fmc.client import Client

class TestClient(Client):
    def __init__(self):
        session = botocore.session.get_session()
        self.cf_client = session.create_client(
                "cloudformation",
                region_name = "us-east-1"
                )

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        eb = fmc.resource("ElasticBeanstalk")
        eb_app = eb.Application(
                    LogicalID = "TestApplication"
                )

        stack_repr = eb_app.representation()
        stack_repr["AWSTemplateFormatVersion"] = "2010-09-09"

        self.stack = type("Stack", (object,), {
            "name": "TestStack"
            })

        self.stack.resources = [eb_app]
        self.client = TestClient()
        self.stack_repr = stack_repr
        self.stubber = Stubber(self.client.cf_client)

    def test_stack_representation(self):
        representation = self.client.stack_representation(
                self.stack
                )

        self.assertDictEqual(
                self.stack_repr,
                representation
                )

    def test_validate_stack(self):
        response = {
                "Parameters": [], 
                "ResponseMetadata": {
                    "HTTPStatusCode": 200, 
                    "RequestId": "0a3d9057-e7e2-11e5-90da-15b4cf62aa6b"
                    }
                }

        expected_params = {
                "TemplateBody": json.dumps({
                    "AWSTemplateFormatVersion": "2010-09-09",
                    "Resources": {
                        "TestApplication": {
                            "Type": "AWS::ElasticBeanstalk::Application"
                            }
                        }
                    })
                }

        self.stubber.add_response(
                "validate_template",
                response,
                expected_params
                )

        self.stubber.activate()

        result = self.client.validate_stack(
                self.stack
                )

        self.assertEqual(
                response,
                result
                )

    def test_create_stack(self):
        response = {
                "StackId": "string"
                }

        expected_params = {
                "StackName": self.stack.name,
                "Capabilities": [],
                "TemplateBody": json.dumps({
                    "AWSTemplateFormatVersion": "2010-09-09",
                    "Resources": {
                        "TestApplication": {
                            "Type": "AWS::ElasticBeanstalk::Application"
                            }
                        }
                    })
                }

        self.stubber.add_response(
                "create_stack",
                response,
                expected_params
                )

        self.stubber.activate()

        result = self.client.create_stack(
                self.stack,
                validate = False
                )

        self.assertDictEqual(
                result,
                response
                )

    def test_delete_stack(self):
        response = {
                "ResponseMetadata": {
                    "HTTPStatusCode": 200,
                    "RequestId": "5ccc7dcd-744c-11e5-be70-example"
                    }
                }

        expected_params = {
                "StackName": "TestStack"
                }

        self.stubber.add_response(
                "delete_stack",
                response,
                expected_params
                )

        self.stubber.activate()

        result = self.client.delete_stack(
                self.stack
                )

        self.assertDictEqual(
                response,
                result
                )

if __name__ == "__main__":
    unittest.main()
