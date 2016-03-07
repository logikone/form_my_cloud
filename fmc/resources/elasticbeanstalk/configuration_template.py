from fmc.resources.base import ResourceBase
from fmc.decorators import RequiredArguments

class ConfigurationTemplate(ResourceBase):

    @RequiredArguments([
            "LogicalID",
            "ApplicationName"
            ])
    def __init__(self, LogicalID=None, ApplicationName=None, DependsOn=None, **kwargs):

        self.Type = "AWS::ElasticBeanstalk::ConfigurationTemplate"
        self.LogicalID = LogicalID
        self.ApplicationName = ApplicationName
        self.User_Properties = kwargs
        self.DependsOn = DependsOn
        self.Properties = {
                "Resources":{
                    self.LogicalID: {
                        "Properties": self.User_Properties
                        }
                    }
                }
        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": {
                            "ApplicationName": self.ApplicationName,
                            }
                        }
                    }
                }

        if self.DependsOn:
            self.doc["Resources"][self.LogicalID]["DependsOn"] = self.DependsOn

        if self.User_Properties:
            self._update_dict(
                    self.doc,
                    self.Properties,
                    )
