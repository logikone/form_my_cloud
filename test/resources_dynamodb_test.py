import unittest
import fmc

dynamo = fmc.resource("DynamoDB")

class TableTestCase(unittest.TestCase):
    def setUp(self):
        self.table = dynamo.Table(
                LogicalID = "Test",
                AttributeDefinitions = {},
                KeySchema = {},
                ProvisionedThroughput = {},
                GlobalSecondaryIndexes = {},
                LocalSecondaryIndexes = {},
                StreamSpecificaion = {},
                TableName = "TestTable"
                )

        self.string_repr = "<AWS::DynamoDB::Table: Test>"
        self.representation = {
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

    def test_exception(self):
        '''Test DynamoDB.Table Raises MissingArgument'''
        with self.assertRaises(fmc.exceptions.MissingArgument) as cm:
            dynamo.Table()

    def test_representation(self):
        '''Test DynamoDB.Table Representation'''
        self.assertDictEqual(
                self.representation,
                self.table.representation()
                )

    def test_str_repr(self):
        '''Test DynamoDB.Table Object String Representation'''
        self.assertEqual(
                str(self.table),
                self.string_repr
                )

if __name__ == "__main__":
    unittest.main()
