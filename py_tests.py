import unittest

from pycimvp import read_module_meta


class TestPYCIMVP(unittest.TestCase):

    def test_my_function(self):
        self.assertTrue(read_module_meta())
