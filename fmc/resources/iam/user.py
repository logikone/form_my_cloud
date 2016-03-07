from fmc.resources.base import ResourceBase
from fmc.decorators import RequiredArguments

class User(ResourceBase):

    @RequiredArguments(["LogicalID"])
    def __init__(self, LogicalID=None, Groups=None, LoginProfile=None,
            ManagedPolicyArns=None, Path=None, Policies=None):

        self.Type = "AWS::IAM::User"
        self.LogicalID = LogicalID
        self.Groups = Groups
        self.LoginProfile = LoginProfile
        self.ManagedPolicyArns = ManagedPolicyArns
        self.Path = Path
        self.Policies = Policies
        self.Properties = {}

        if self.Groups:
            self.Properties["Groups"] = self.Groups

        if self.LoginProfile:
            self.Properties["LoginProfile"] = self.LoginProfile

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
                        "Properties": self.Properties
                        }
                    }
                }
