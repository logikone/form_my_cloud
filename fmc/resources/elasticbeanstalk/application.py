from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        OptionalProperties
        )

class Application(ResourceBase):

    @RequiredArguments([
        "LogicalID"
        ])
    @OptionalProperties([
        "ApplicationName",
        "Description"
        ])
    def __init__(self, **kwargs):

        self.LogicalID = kwargs["LogicalID"]
        self.Properties = kwargs["Properties"]
        self.Type = "AWS::ElasticBeanstalk::Application"
        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": self.Properties
                        }
                    }
                }

        if len(self.Properties.keys()) == 0:
            print self.doc
            self.doc["Resources"][self.LogicalID].pop("Properties")
