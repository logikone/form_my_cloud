from fmc.resources.base import ResourceBase
from fmc.decorators import RequiredArguments

class ApplicationVersion(ResourceBase):

    @RequiredArguments([
        "LogicalID",
        "ApplicationName",
        "SourceBundle"
        ])
    def __init__(self, LogicalID=None, ApplicationName=None,
            SourceBundle=None, Description=None, DependsOn=None):

        self.Type = "AWS::ElasticBeanstalk::ApplicationVersion"
        self.LogicalID = LogicalID
        self.ApplicationName = ApplicationName
        self.SourceBundle = SourceBundle
        self.Description = Description
        self.DependsOn = DependsOn
        self.Properties = {
                "ApplicationName": self.ApplicationName,
                "SourceBundle": self.SourceBundle,
                }

        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": self.Properties
                        }
                    }
                }

        if self.Description:
            self.Properties["Description"] = self.Description

        if self.DependsOn:
            self.doc["Resources"][self.LogicalID]["DependsOn"] = self.DependsOn

        if len(self.Properties.keys()) == 0:
            print self.doc
            self.doc["Resources"][self.LogicalID].pop("Properties")
