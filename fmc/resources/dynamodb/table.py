from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties,
        OptionalProperties
        )

class Table(ResourceBase):
    Type = "AWS::DynamoDB::Table"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "AttributeDefinitions",
        "KeySchema",
        "ProvisionedThroughput"
        ])
    @OptionalProperties([
        "GlobalSecondaryIndexes",
        "LocalSecondaryIndexes",
        "StreamSpecification",
        "TableName"
        ])
    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
