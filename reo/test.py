import unittest
from mock import ANY

from reo import reo


class ReoTests(unittest.TestCase):

    def test_ok(self):
        result = reo(
            4, (
                (4, 1, 1),
                (4, 2, 1),
                (3, 2, -1),
                (4, 3, -1)
            ))

        self.assertEqual(result, [ANY] * 4)
        for value in result:
            self.assertNotEqual(value, None)

    def test_ok1(self):
        result = reo(
            6, (
                (2, 1, 1),
                (3, 1, 1),
                (2, 3, -1),
                (3, 2, -1),
                (4, 2, 1),
                (5, 2, 1),
                (6, 5, 1),
                (6, 4, -1),
                (5, 4, -1),
                (4, 3, -1)
            ))

        self.assertEqual(result, [ANY] * 6)
        for value in result:
            self.assertNotEqual(value, None)

    def test_fail(self):
        result = reo(
            2, (
                (1, 2, -1),
                (2, 1, -1),
            ))

        self.assertEqual(result, [])
