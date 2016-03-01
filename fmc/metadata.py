from fmc.base import Base

class MetaData(Base):
    def __init__(self, Init=None, Interface=None,
            Designer=None, **kwargs):

        self.metadata = {
                "Metadata": {
                    }
                }

        for key, val in kwargs.iteritems():
            self.metadata["Metadata"][key] = val

        if Init:
            self.metadata["Metadata"]["AWS::CloudFormation::Init"] = Init

        if Interface:
            self.metadata["Metadata"]["AWS::CloudFormation::Interface"] = Interface

        if Designer:
            self.metadata["Metadata"]["AWS::CloudFormation::Designer"] = Designer

    def __repr__(self):
        return "<MetaData>"

    def representation(self):
        return self.metadata
