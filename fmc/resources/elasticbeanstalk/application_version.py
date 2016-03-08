from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties,
        OptionalProperties
        )

class ApplicationVersion(ResourceBase):
    Type = "AWS::ElasticBeanstalk::ApplicationVersion"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "ApplicationName",
        "SourceBundle"
        ])
    @OptionalProperties([
        "Description"
        ])
    def __init__(self, **kwargs):
        super(ApplicationVersion, self).__init__(**kwargs)
