from fmc.resources.base import ResourceBase

class Environment(ResourceBase):
    def __init__(self, LogicalID, ApplicationName, Properties=None):
        self.type = "AWS::ElasticBeanstalk::Environment"
        self.LogicalID = LogicalID
        self.ApplicationName = ApplicationName
        self.User_Properties = Properties
        self.Properties = {
                "Resources":{
                    self.LogicalID: {
                        "Properties": Properties
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

    def __repr__(self):
        return "<ElasticBeanstalk.Environment: {0}>".format(
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

#! vim: ts=4 sw=4 ft=python expandtab:
