import unittest
import fmc

class DescriptionTestCase(unittest.TestCase):
    description = fmc.description("Test Description")

    def test_string_repr(self):
        representation = "<Description: Test Description>"

        self.assertEqual(
                representation,
                str(self.description)
                )

    def test_representation(self):
        representation = {
                "Description": "Test Description"
                }

        self.assertDictEqual(
                representation,
                self.description.representation()
                )

if __name__ == "__main__":
    unittest.main()
