import unittest

class FMCImportTestCase(unittest.TestCase):
    def test(self):
        try:
            import fmc
        except:
            self.fail(
                    msg = "Failed to import fmc"
                    )

if __name__ == "__main__":
    unittest.main()
