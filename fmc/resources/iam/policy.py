from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiresOneOf,
        RequiredProperties
        )

class Policy(ResourceBase):
    Type = "AWS::IAM::Policy"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "PolicyDocument",
        "PolicyName"
        ])
    @RequiresOneOf([
        "Groups",
        "Roles",
        "Users"
        ])
    def __init__(self, **kwargs):
        super(Policy, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
