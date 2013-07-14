import unittest

from functions import function1, IncorrectParameterTypeException


class TestFunction1(unittest.TestCase):

    def test_not_list_type(self):
        self.assertRaises(IncorrectParameterTypeException, function1, 'a')

    def test_blank_list(self):
        self.assertEquals([], function1([]))

    def test_one_item(self):
        self.assertEquals([0], function1([0]))
        self.assertEquals([0], function1([9]))
        self.assertEquals([0], function1([-10]))

    def test_two_items(self):
        self.assertEquals([-.5, .5], function1([0, 1]))
        self.assertEquals([-2.5, 2.5], function1([3, 8]))

    def test_three_items(self):
        input = [1, 9, 9, 10, 10, 10, 10, 11]
        output = [-7.75, .25, .25, 1.25, 1.25, 1.25, 1.25, 2.25]
        self.assertEquals(output, function1(input))


if __name__ == '__main__':
    unittest.main(verbosity=2)
