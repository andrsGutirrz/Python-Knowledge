import unittest


class SampleTest(unittest.TestCase):

    def setUp(self) -> None:
        print("Runs at start, once")

    def tearDown(self) -> None:
        print("Runs at the end, once")

    def test_not_found(self):
        self.assertTrue(True)

    def test_found(self):
        self.assertTrue(True)
