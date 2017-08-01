import unittest

from hil import hil, hil_length_to_point


class HilLengthTests(unittest.TestCase):

    def test_3_0_3(self):
        self.assertEqual(hil_length_to_point(3, 0, 3), 5)

    def test_5_3_3(self):
        self.assertEqual(hil_length_to_point(5, 3, 3), 52)



class HilTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            hil(1, range(1, 13)),
            [
                (2, 1),
                (3, 2),
                (2, 3),
                (1, 2),
                (2, 1),
                (3, 0),
                (4, 1),
                (3, 2),
                (4, 3),
                (3, 4),
                (2, 3),
                (1, 4)
            ]
        )

    def test_3(self):
        self.assertEqual(
            hil(3, [1, 42]),
            [
                (2, 1),
                (3, 14)
            ]
        )

    def test_big(self):
        self.assertEqual(
            hil(30, [1, 2, 3]),
            [(2, 1), (3, 0), (4, 1)]
        )