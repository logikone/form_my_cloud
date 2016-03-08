from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        OptionalProperties
        )

class Application(ResourceBase):
    Type = "AWS::ElasticBeanstalk::Application"

    @RequiredArguments([
        "LogicalID"
        ])
    @OptionalProperties([
        "ApplicationName",
        "Description"
        ])
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
