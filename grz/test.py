import unittest

from grz import grz


class GrzTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            grz([
                (1, 1)
            ]),
            [1]
        )

    def test_2(self):
        self.assertEqual(
            grz([
                (1, 1),
                (2, 2)
            ]),
            [2, 5]
        )

    def test_3(self):
        self.assertEqual(
            grz([
                (5, 10),
                (16, 0),
                (5, 10)
            ]),
            [10, 26, 57]
        )

    def test_4(self):
        self.assertEqual(
            grz([
                (10, 10),
                (2, 5),
                (6, 1),
                (4, 2)
            ]),
            [10, 25, 42, 64]
        )