from fmc.resources import (
        ElasticBeanstalk,
        IAM,
        DynamoDB,
        )

from fmc.format import (
        Version
        )

from fmc.client import Client
from fmc.description import Description
from fmc.metadata import MetaData
from fmc.parameters import Parameter

def client():
    return Client()

def description(description):
    return Description(description)

def metadata(**kwargs):
    return MetaData(**kwargs)

def parameter(**kwargs):
    return Parameter(**kwargs)

def resource(name):
    if name == "ElasticBeanstalk":
        return ElasticBeanstalk
    if name == "IAM":
        return IAM
    if name == "DynamoDB":
        return DynamoDB

    raise ValueError("Unknown Resource Type: {0}".format(
        name))

def format(name):
    if name == "Version":
        return Version

#! vim: ts=4 sw=4 ft=python expandtab:
