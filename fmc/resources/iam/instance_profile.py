from fmc.resources.base import ResourceBase
from fmc.decorators import RequiredArguments

class InstanceProfile(ResourceBase):

    @RequiredArguments([
        "LogicalID",
        "Path",
        "Roles"
        ])
    def __init__(self, LogicalID=None, Path=None, Roles=None):

        self.Type = "AWS::IAM::InstanceProfile"
        self.LogicalID = LogicalID
        self.Path = Path
        self.Roles = Roles
        self.Capabilities = "CAPABILITY_IAM"
        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": {
                            "Path": self.Path,
                            "Roles": self.Roles,
                            }
                        }
                    }
                }
