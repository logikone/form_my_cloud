from fmc.resources.base import ResourceBase
from fmc.exceptions import MissingArgument

class InstanceProfile(ResourceBase):
    def __init__(self, LogicalID=None, Path=None, Roles=None):
        if not LogicalID:
            raise MissingArgument("LogicalID")

        if not Path:
            raise MissingArgument("Path")

        if not Roles:
            raise MissingArgument("Roles")

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
