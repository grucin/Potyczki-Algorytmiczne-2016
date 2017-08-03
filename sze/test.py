import unittest

from sze import sze


class SzeTests(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(
            sze(2, ((3, 8, 3), (2, 5, 2), (3, 7, 3))), 1)

    def test_ok_full(self):
        self.assertEqual(
            sze(3, (
                (0, 9, 6),
                (0, 8, 6),
                (0, 9, 6),
                (4, 8, 3),
                (5, 7, 2),
                (4, 9, 4)
            )), 1)
        
    def test_kamil(self):
        self.assertEqual(
            sze(2, (
                (0, 3, 1),
                (0, 7, 3),
                (1, 2, 1), 
                (1, 2, 1),
                (0, 1, 1),
                (3, 6, 3),
                (3, 6, 3)
            )), 1)

    def test_fail(self):
        self.assertEqual(sze(1, ((0, 1, 1), (0, 1, 1))), 0)
