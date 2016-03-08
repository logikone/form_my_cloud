from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties,
        OptionalProperties
        )

class ManagedPolicy(ResourceBase):
    Type = "AWS::IAM::ManagedPolicy"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "PolicyDocument"
        ])
    @OptionalProperties([
        "Description",
        "Groups",
        "Path",
        "Roles",
        "Users"
        ])
    def __init__(self, **kwargs):
        super(ManagedPolicy, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
