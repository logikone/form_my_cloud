from fmc.base import Base

class ResourceBase(Base):
    def __init__(self):
        pass

    def __repr__(self):
        return "<{0}: {1}>".format(
                self.Type,
                self.LogicalID
                )

    def representation(self):
        return self.doc
