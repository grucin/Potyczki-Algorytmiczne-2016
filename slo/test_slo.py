import unittest

from slo import slo


class Tests(unittest.TestCase):

    def test_out(self):
        self.assertEqual(slo(2, 10), 'NIE')

    def test_acb(self):
        self.assertEqual(slo(3, 7), 'acb')

    def test_bca(self):
        self.assertEqual(slo(3, 13), 'bca')

    def test_acac(self):
        self.assertEqual(slo(4, 12), 'acac')
