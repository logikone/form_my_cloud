from cf.resources.base import ResourceBase

class Environment(ResourceBase):
    def __init__(self, ApplicationName, Properties=None):
        self.type = "AWS::ElasticBeanstalk::Environment"
        self.ApplicationName = ApplicationName
        self.Properties = {
                "Properties": Properties
                }
        self.doc_base = {
                "Type": self.type,
                "Properties": {
                    "ApplicationName": self.ApplicationName,
                    }
                }

    def __repr__(self):
        return "<ElasticBeanstalk.Environment: {0}>".format(self.ApplicationName)

    def to_json(self):
        if self.Properties["Properties"]:
            doc = self._update_dict(
                    self.doc_base,
                    self.Properties,
                    )
        else:
            doc = self.doc_base

        return self.serialize(doc)

#! vim: ts=4 sw=4 ft=python expandtab:
