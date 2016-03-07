from fmc.resources.base import ResourceBase
from fmc.exceptions import MissingArgument

class Role(ResourceBase):
    def __init__(self, LogicalID=None, AssumeRolePolicyDocument=None,
            ManagedPolicyArns=None, Path=None, Policies=None):
        if not LogicalID:
            raise MissingArgument("LogicalID")

        if not AssumeRolePolicyDocument:
            raise MissingArgument("AssumeRolePolicyDocument")

        self.Type = "AWS::IAM::Role"
        self.LogicalID = LogicalID
        self.AssumeRolePolicyDocument = AssumeRolePolicyDocument
        self.ManagedPolicyArns = ManagedPolicyArns
        self.Path = Path
        self.Policies = Policies
        self.Capabilities = "CAPABILITY_IAM"
        self.Properties = {
                "AssumeRolePolicyDocument": self.AssumeRolePolicyDocument
                }

        if self.ManagedPolicyArns:
            self.Properties["ManagedPolicyArns"] = self.ManagedPolicyArns

        if self.Path:
            self.Properties["Path"] = self.Path

        if self.Policies:
            self.Properties["Policies"] = self.Policies

        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": self.Properties,
                        }
                    }
                }
