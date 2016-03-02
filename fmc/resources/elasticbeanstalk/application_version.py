from fmc.resources.base import ResourceBase
from fmc.exceptions import MissingArgument

class ApplicationVersion(ResourceBase):
    def __init__(self, LogicalID=None, ApplicationName=None,
            SourceBundle=None, Description=None, DependsOn=None):
        if not LogicalID:
            raise MissingArument("LogicalID")

        if not ApplicationName:
            raise MissingArgument("ApplicationName")

        if not SourceBundle:
            raise MissingArgument("SourceBundle")

        self.type = "AWS::ElasticBeanstalk::ApplicationVersion"
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
                        "Type": self.type,
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

    def __repr__(self):
        return "<ElasticBeanstalk.ApplicationVersion: {0}>".format(
                self.LogicalID
                )
