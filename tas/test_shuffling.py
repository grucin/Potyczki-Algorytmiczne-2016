import unittest

from shuffling import shuffling


class ShufflingTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(shuffling(2, 1, [2, 4, 1, 5]), [5, 1, 4, 2])