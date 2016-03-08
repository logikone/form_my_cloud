from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties
        )

class UserToGroupAddition(ResourceBase):
    Type = "AWS::IAM::UserToGroupAddition"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "GroupName",
        "Users"
        ])
    def __init__(self, **kwargs):
        super(UserToGroupAddition, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
