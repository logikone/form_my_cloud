from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties
        )

class InstanceProfile(ResourceBase):
    Type = "AWS::IAM::InstanceProfile"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "Path",
        "Roles"
        ])
    def __init__(self, **kwargs):
        super(InstanceProfile, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
