from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        OptionalProperties
        )

class User(ResourceBase):
    Type = "AWS::IAM::User"

    @RequiredArguments([
        "LogicalID"
        ])
    @OptionalProperties([
        "Groups",
        "LoginProfile",
        "ManagedPolicyArns",
        "Path",
        "Policies",
        ])
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
