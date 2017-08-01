import unittest

from jed import jed, jed_count



class JedTests(unittest.TestCase):

    def test_6(self):
        self.assertEqual(eval(jed(6)), 6)

    def test_10(self):
        self.assertEqual(eval(jed(10)), 10)

    def test_101(self):
        expr = jed(101)
        self.assertEqual(eval(expr), 101)
        self.assertLessEqual(jed_count(expr), 100)
