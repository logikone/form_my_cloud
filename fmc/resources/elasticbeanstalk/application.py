from fmc.resources.base import ResourceBase
from fmc.decorators import RequiredArguments

class Application(ResourceBase):

    @RequiredArguments(["LogicalID"])
    def __init__(self, LogicalID=None, ApplicationName=None, Description=None):

        self.LogicalID = LogicalID
        self.ApplicationName = ApplicationName
        self.Description = Description
        self.Properties = {}
        self.Type = "AWS::ElasticBeanstalk::Application"
        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": self.Properties
                        }
                    }
                }
        if self.ApplicationName:
            self.Properties["ApplicationName"] = self.ApplicationName

        if self.Description:
            self.Properties["Description"] = self.Description

        if len(self.Properties.keys()) == 0:
            print self.doc
            self.doc["Resources"][self.LogicalID].pop("Properties")
