from fmc.resources.base import ResourceBase
from fmc.decorators import (
        OptionalProperties,
        RequiredArguments,
        RequiredProperties
        )

class Environment(ResourceBase):
    Type = "AWS::ElasticBeanstalk::Environment"

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
        super(Environment, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
