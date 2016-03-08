from fmc.decorators import (
        RequiredArguments,
        RequiredProperties,
        OptionalProperties
        )

class Parameter(object):

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "Type"
        ])
    @OptionalProperties([
        "Default",
        "NoEcho",
        "AllowedValues",
        "AllowedPattern",
        "MaxLength",
        "MinLength",
        "MaxValue",
        "MinValue",
        "Description",
        "ConstraintDescription"
        ])
    def __init__(self, **kwargs):
        self.LogicalID = kwargs["LogicalID"]
        self.Properties = kwargs["Properties"]
        self.doc = {
                "Parameters": {
                    self.LogicalID: self.Properties
                    }
                }

    def representation(self):
        return self.doc
