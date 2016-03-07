from fmc.resources.base import ResourceBase
from fmc.exceptions import MissingArgument, MissingOneOf

class Policy(ResourceBase):
    def __init__(self, LogicalID=None, Groups=None, PolicyDocument=None,
            PolicyName=None, Roles=None, Users=None):

        if not LogicalID:
            raise MissingArgument("LogicalID")
    
        if not PolicyDocument:
            raise MissingArgument("PolicyDocument")
    
        if not PolicyName:
            raise MissingArgument("PolicyName")

        if not Groups and not Roles and not Users:
            raise MissingOneOf(
                    [
                        "Groups",
                        "Roles",
                        "Users",
                        ],
                    "IAM.Policy",
                    )
    
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
