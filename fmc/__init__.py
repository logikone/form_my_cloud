from fmc.resources import (
        EBEnvironment,
        EBApplication,
        EBApplicationVersion,
        EBConfigurationTemplate,
        )

from fmc.format import (
        Version
        )

from fmc.client import (
        Client
        )

def client():
    return Client

def resource(name):
    if name == "EBEnvironment":
        return EBEnvironment

def format(name):
    if name == "Version":
        return Version
