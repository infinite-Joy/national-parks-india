from parks.helpers import parks
import unittest


class TestHelperFunctions(unittest.TestCase):

    def test_parks(self):
        res = parks()
        self.assertEqual(res["Anshi National Park"],
                         [14.9981, 74.3587],
                         "returns the json long/lat of the parks")


if __name__ == "__main__":
    unittest.main()
