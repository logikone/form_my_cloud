import json
from datetime import datetime

from fmc.base import Base

class Version(Base):

    def __init__(self):
        self.version = "2010-09-09"

    def __repr__(self):
        return "<Format.Version: {0}>".format(
                self.version
                )

    def representation(self):
        return { "AWSTemplateFormatVersion": self.version }

#! vim: ts=4 sw=4 ft=python expandtab:
