import unittest

import fmc
from fmc.client import Client
from fmc.description import Description
from fmc.metadata import MetaData
from fmc.parameters import Parameter

class FMCTestCase(unittest.TestCase):
    def test_client(self):
        '''Test fmc.client instantiation'''
        self.assertIsInstance(
                fmc.client(),
                Client
                )

    def test_description(self):
        '''Test fmc.description instantiation'''
        self.assertIsInstance(
                fmc.description("Description"),
                Description
                )

    def test_metadata(self):
        '''Test fmc.metadata instantiation'''
        self.assertIsInstance(
                fmc.metadata(),
                MetaData
                )

    def test_parameters(self):
        '''Test fmc.parameter instantiation'''
        self.assertIsInstance(
                fmc.parameter(
                    LogicalID = "Parameter",
                    Type = "Foo"
                    ),
                Parameter
                )

    def test_bad_resource(self):
        with self.assertRaises(ValueError) as cm:
            fmc.resource("FooBar")
