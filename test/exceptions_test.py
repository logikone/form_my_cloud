import unittest
import fmc

class MissingArgumentTestCase(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(fmc.exceptions.MissingArgument):
            raise fmc.exceptions.MissingArgument("Test")

    def test_str_repr(self):
        try:
            raise fmc.exceptions.MissingArgument("Test")
        except fmc.exceptions.MissingArgument as e:
            self.assertEqual(
                    str(e),
                    "The Argument 'Test' Must Be Defined"
                    )

class MissingOneOfTestCase(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(fmc.exceptions.MissingOneOf):
            raise fmc.exceptions.MissingOneOf([
                "Test1",
                "Test2",
                "Test3"
                ])

    def test_str_repr(self):
        try:
            raise fmc.exceptions.MissingOneOf([
                "Test1",
                "Test2",
                "Test3"
                ])
        except fmc.exceptions.MissingOneOf as e:
            self.assertEqual(
                    str(e),
                    "One of 'Test1, Test2, Test3' Must Be Defined"
                    )
