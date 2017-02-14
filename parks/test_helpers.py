from helpers import parks
import unittest


class TestHelperFunctions(unittest.TestCase):

    def test_parks(self):
        self.assertEqual(parks(),
                         "1",
                         "returns the json long/lat of the parks")


if __name__ == "__main__":
    unittest.main()
