import unittest
from tools import findPrimes

# Testing on the findPrimes function (90% of the application, __main__.py only collects inputs to pass to this function)
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

    #   Test 1 to make sure error handling is working properly (valid int, param 1)
    def test_valid_input(self):
        test_param_1 = '790g'
        test_param_2 = '7920'
        result = findPrimes(test_param_1, test_param_2)
        self.assertIsInstance(result, ValueError)
    #   Test 2 to make sure error handling is working properly (valid int, param 2)
    def test_valid_input_2(self):
        test_param_1 = '7900'
        test_param_2 = '792g'
        result = findPrimes(test_param_1, test_param_2)
        self.assertIsInstance(result, ValueError)
    
    #   Test 3 to make sure error handling is working properly (negative int)
    def test_valid_input_3(self):
        test_param_1 = '-7900'
        test_param_2 = '7920'
        result = findPrimes(test_param_1, test_param_2)
        self.assertEqual(result, ValueError)

    #   Test: if there are no prime numbers in range, return None
    def test_no_primes(self):
        test_param_1 = "7902"
        test_param_2 = "7905"
        result = findPrimes(test_param_1, test_param_2)
        self.assertEqual(result, None)

    #   Test to make sure a range of a prime number to itself, returns itself
    def test_prime_range_to_self(self):
        test_param_1 = "7901"
        test_param_2 = "7901"
        result = findPrimes(test_param_1, test_param_2)
        self.assertEqual(result, [int(test_param_1)])


unittest.main()