from fmc.resources.base import ResourceBase
from fmc.decorators import RequiredArguments, RequiresOneOf

class Policy(ResourceBase):

    @RequiredArguments([
        "LogicalID",
        "PolicyDocument",
        "PolicyName"
        ])
    @RequiresOneOf([
        "Groups",
        "Roles",
        "Users"
        ])
    def __init__(self, LogicalID=None, Groups=None, PolicyDocument=None,
            PolicyName=None, Roles=None, Users=None):

        self.Type = "AWS::IAM::Policy"
        self.LogicalID = LogicalID
        self.Groups = Groups
        self.PolicyDocument = {
                "PolicyDocument": PolicyDocument
                }
        self.PolicyName = PolicyName
        self.Roles = Roles
        self.Users = Users
        self.Capabilities = "CAPABILITY_IAM"
        self.Properties = {
                "PolicyName": self.PolicyName,
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    }
                }

        self._update_dict(
                self.Properties,
                self.PolicyDocument
                )

        if self.Groups:
            self.Properties["Groups"] = self.Groups

        if self.Roles:
            self.Properties["Roles"] = self.Roles

        if self.Users:
            self.Properties["Users"] = self.Users

        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": self.Properties
                        }
                    }
                }
