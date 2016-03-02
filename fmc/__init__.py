from fmc.resources import (
        ElasticBeanstalk
        )

from fmc.format import (
        Version
        )

from fmc.client import Client
from fmc.description import Description
from fmc.metadata import MetaData

def client():
    return Client

def description(description):
    return Description(description)

def metadata(**kwargs):
    return MetaData(**kwargs)

def resource(name):
    if name == "ElasticBeanstalk":
        return ElasticBeanstalk

    raise ValueError("Unknown Resource Type: {0}".format(
        name))

def format(name):
    if name == "Version":
        return Version

#! vim: ts=4 sw=4 ft=python expandtab:
