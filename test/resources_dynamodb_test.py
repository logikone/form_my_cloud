import unittest
import fmc

dynamo = fmc.resource("DynamoDB")

class TableTestCase(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            dynamo.Table()

    def test_representation(self):
        table = dynamo.Table(
                LogicalID = "Test",
                AttributeDefinitions = {},
                KeySchema = {},
                ProvisionedThroughput = {},
                GlobalSecondaryIndexes = {},
                LocalSecondaryIndexes = {},
                StreamSpecificaion = {},
                TableName = "TestTable"
                )

        string_repr = "<AWS::DynamoDB::Table: Test>"
        representation = {
                'Resources': {
                    'Test': {
                        'Type': 'AWS::DynamoDB::Table',
                        'Properties': {
                            'GlobalSecondaryIndexes': {},
                            'AttributeDefinitions': {},
                            'LocalSecondaryIndexes': {},
                            'ProvisionedThroughput': {},
                            'TableName': 'TestTable',
                            'KeySchema': {}
                            }
                        }
                    }
                }

        self.assertEqual(
                str(table),
                string_repr
                )

        self.assertDictEqual(
                representation,
                table.representation()
                )

if __name__ == "__main__":
    unittest.main()
