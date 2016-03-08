from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        OptionalProperties
        )

class Group(ResourceBase):
    Type = "AWS::IAM::Group"

    @RequiredArguments([
        "LogicalID"
        ])
    @OptionalProperties([
        "ManagedPolicyArns",
        "Path",
        "Policies"
        ])
    def __init__(self, **kwargs):
        super(Group, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
