from cf.resources import (
        EBEnvironment,
        EBApplication,
        EBApplicationVersion,
        EBConfigurationTemplate,
        )

from cf.format import (
        Version
        )

from cf.client import (
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
