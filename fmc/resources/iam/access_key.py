from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties,
        OptionalProperties
        )

class AccessKey(ResourceBase):
    Type = "AWS::IAM::AccessKey"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "UserName"
        ])
    @OptionalProperties([
        "Serial",
        "Status"
        ])
    def __init__(self, **kwargs):
        super(AccessKey, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
