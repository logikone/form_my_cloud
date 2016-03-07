from fmc.resources.base import ResourceBase
from fmc.decorators import RequiredArguments

class ConfigurationTemplate(ResourceBase):

    @RequiredArguments([
            "LogicalID",
            "ApplicationName"
            ])
    def __init__(self, LogicalID=None, ApplicationName=None, DependsOn=None, **kwargs):

        self.type = "AWS::ElasticBeanstalk::ConfigurationTemplate"
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
        self.doc_base = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.type,
                        "Properties": {
                            "ApplicationName": self.ApplicationName,
                            }
                        }
                    }
                }
        if self.DependsOn:
            self.doc_base["Resources"][self.LogicalID]["DependsOn"] = self.DependsOn


    def __repr__(self):
        return "<ElasticBeanstalk.ConfigurationTemplate: {0}".format(
                self.LogicalID
                )

    def representation(self):
        if self.User_Properties:
            doc = self._update_dict(
                    self.doc_base,
                    self.Properties,
                    )
        else:
            doc = self.doc_base

        return doc

