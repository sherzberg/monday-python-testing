from unittest.mock import Mock, patch
import unittest

from helpers import cwd


class TestFunctions(unittest.TestCase):

    @patch('os.getcwd')
    def test_simple_patch_mock(self, my_mock):
        self.fail()


if __name__ == '__main__':
    unittest.main(verbosity=2)
