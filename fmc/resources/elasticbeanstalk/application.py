from fmc.resources.base import ResourceBase
from fmc.exceptions import MissingArgument

class Application(ResourceBase):
    def __init__(self, LogicalID=None, ApplicationName=None, Description=None):
        if not LogicalID:
            raise MissingArument("LogicalID")

        self.LogicalID = LogicalID
        self.ApplicationName = ApplicationName
        self.Description = Description
        self.Properties = {}
        self.type = "AWS:::ElasticBeanstalk::Application"
        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.type,
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

    def __repr__(self):
        return "<ElasticBeanstalk.Application: {0}>".format(
                self.LogicalID
                )

    def representation(self):
        return self.doc
