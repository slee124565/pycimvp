import unittest

from pycimvp import read_module_meta


class TestPYCIMVP(unittest.TestCase):

    def test_my_function(self):
        meta = read_module_meta()
        self.assertTrue(meta.get('__version__'))


if __name__ == '__main__':
    unittest.main()
