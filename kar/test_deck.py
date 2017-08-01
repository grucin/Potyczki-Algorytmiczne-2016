import unittest

from deck import decks


class DeckTests(unittest.TestCase):

    def test_5_5(self):
        result = decks(5, (
            (1, 5, 1),
            (2, 5, 1),
            (3, 5, 1),
            (4, 5, 1),
            (5, 5, 1)
        ))
        self.assertEqual(result, 1)

    def test_2_2(self):
        result = decks(2, ((1, 1, 1), (1, 2, 1)))
        self.assertEqual(result, 0)

    def test_1_1(self):
        result = decks(1, ((1, 1, -1),))
        self.assertEqual(result, -1)

    def test_big(self):
        k = 10000
        result = decks(k, [(i, max(1, i - i % 2), 1) for i in xrange(1, k+1)])
        self.assertEqual(result, 0)