from fmc.base import Base

class ResourceBase(Base):
    '''
    ResourceBase

        Base class for resources.

        Provides __init__, __repr__, representation methods
        for child classes.

        Inherits from :doc:`../base`
    '''
    def __init__(self, **kwargs):
        self.LogicalID = kwargs["LogicalID"]
        self.Properties = kwargs["Properties"]
        self.doc = {
                "Resources": {
                    self.LogicalID: {
                        "Type": self.Type,
                        "Properties": self.Properties
                        }
                    }
                }

        if len(self.Properties.keys()) == 0:
            self.doc["Resources"][self.LogicalID].pop("Properties")

        if "DependsOn" in kwargs:
            self.doc["Resources"][self.LogicalID]["DependsOn"] = kwargs["DependsOn"]

    def __repr__(self):
        '''
            Returns "<{0}: {1}>" where 0 = self.Type and
            1 = self.LogicalID

        '''
        return "<{0}: {1}>".format(
                self.Type,
                self.LogicalID
                )

    def representation(self):
        '''
            Returns self.doc
        '''
        return self.doc

#! vim: ts=4 sw=4 ft=python expandtab:
