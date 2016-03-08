from fmc.resources.base import ResourceBase
from fmc.decorators import (
        RequiredArguments,
        RequiredProperties,
        OptionalProperties
        )

class Role(ResourceBase):
    Type = "AWS::IAM::Role"

    @RequiredArguments([
        "LogicalID"
        ])
    @RequiredProperties([
        "AssumeRolePolicyDocument"
        ])
    @OptionalProperties([
        "ManagedPolicyArns",
        "Path",
        "Policies"
        ])
    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)

#! vim: ts=4 sw=4 ft=python expandtab:
