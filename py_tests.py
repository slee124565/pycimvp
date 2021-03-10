import unittest

from pycimvp import my_function


class TestPYCIMVP(unittest.TestCase):

    def test_my_function(self):
        self.assertTrue(my_function())
