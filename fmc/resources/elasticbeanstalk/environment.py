from fmc.resources.base import ResourceBase
from fmc.decorators import (
        OptionalProperties,
        RequiredArguments,
        RequiredProperties
        )

class Environment(ResourceBase):

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "ApplicationName"
        ])
    @OptionalProperties([
        "CNAMEPrefix",
        "Description",
        "EnvironmentName",
        "OptionSettings",
        "SolutionStackName",
        "Tags",
        "TemplateName",
        "Tier",
        "VersionLabel"
        ])
    def __init__(self, **kwargs):

        self.Type = "AWS::ElasticBeanstalk::Environment"
        self.LogicalID = kwargs["LogicalID"]
        self.ApplicationName = kwargs["ApplicationName"]
        self.Properties = kwargs["Properties"]
        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": self.Properties
                        }
                    }
                }

        if "DependsOn" in kwargs:
            self.doc["Resources"][self.LogicalID]["DependsOn"] = kwargs["DependsOn"]

#! vim: ts=4 sw=4 ft=python expandtab:
