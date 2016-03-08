from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties,
        OptionalProperties,
        RequiresOneOf
        )

class ConfigurationTemplate(ResourceBase):
    Type = "AWS::ElasticBeanstalk::ConfigurationTemplate"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "ApplicationName"
        ])
    @OptionalProperties([
        "Description",
        "OptionSettings",
        ])
    @RequiresOneOf([
        "EnvironmentId",
        "SolutionStackName",
        "SourceConfiguration"
        ])
    def __init__(self, **kwargs):
        super(ConfigurationTemplate, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
