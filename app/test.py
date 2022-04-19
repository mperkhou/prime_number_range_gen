import unittest
from tools import findPrimes

class testApp(unittest.TestCase):
    #   Test the range provided in the instructions
    def test_range_1(self):
        test_param_1 = '7900'
        test_param_2 = '7920'
        result = findPrimes(test_param_1, test_param_2)
        self.assertEqual(result, [7901, 7907, 7919])

    #   Test to make sure order doesn't matter for upper & lower bounds
    def test_range_reverse(self):
        test_param_1 = 7900
        test_param_2 = 7920
        result = findPrimes(test_param_2, test_param_1)
        self.assertEqual(result, [7901, 7907, 7919])

    #   Test 1 to make sure error handling is working properly (str not int)
    def test_valid_input(self):
        test_param_1 = '790g'
        test_param_2 = '7920'
        result = findPrimes(test_param_1, test_param_2)
        self.assertIsInstance(result, ValueError)
    #   Test 2 to make sure error handling is working properly (negative int)
    def test_valid_input_2(self):
        test_param_1 = '-7900'
        test_param_2 = '7920'
        result = findPrimes(test_param_1, test_param_2)
        self.assertEqual(result, ValueError)

unittest.main()