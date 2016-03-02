from fmc.base import Base

class ResourceBase(Base):
    def __init__(self):
        pass

    def representation(self):
        return self.doc
