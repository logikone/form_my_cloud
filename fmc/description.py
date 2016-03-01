from fmc.base import Base

class Description(Base):
    def __init__(self, description):
        self.short_desc = description
        self.Description = {
                "Description": description
                }

    def __repr__(self):
        return "<Description: {0}>".format(
                self.short_desc
                )

    def representation(self):
        return self.Description
