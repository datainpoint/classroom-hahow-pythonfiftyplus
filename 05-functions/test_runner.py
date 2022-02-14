import unittest
import ipynb.fs.full.exercises as ex
import importlib.util

class TestFunctions(unittest.TestCase):
    def test_036_calculate_circle_area(self):
        self.assertGreater(ex.calculate_circle_area(5), 78)
        self.assertGreater(ex.calculate_circle_area(6), 113)
        self.assertGreater(ex.calculate_circle_area(7), 153)
    def test_037_calculate_cylinder_volume(self):
        self.assertGreater(ex.calculate_cylinder_volume(5, 6), 470)
        self.assertGreater(ex.calculate_cylinder_volume(6, 5), 565)
        self.assertGreater(ex.calculate_cylinder_volume(7, 8), 1230)
    def test_038_count_number_of_divisors(self):
        self.assertEqual(ex.count_number_of_divisors(1), 1)
        self.assertEqual(ex.count_number_of_divisors(2), 2)
        self.assertEqual(ex.count_number_of_divisors(3), 2)
        self.assertEqual(ex.count_number_of_divisors(4), 3)
        self.assertEqual(ex.count_number_of_divisors(5), 2)
        self.assertEqual(ex.count_number_of_divisors(6), 4)
    def test_039_is_prime(self):
        self.assertFalse(ex.is_prime(1))
        self.assertTrue(ex.is_prime(2))
        self.assertTrue(ex.is_prime(3))
        self.assertFalse(ex.is_prime(4))
        self.assertTrue(ex.is_prime(5))
    def test_040_is_args_prime(self):
        self.assertEqual(ex.is_args_prime(1, 2, 3), [False, True, True])
        self.assertEqual(ex.is_args_prime(4, 5, 6), [False, True, False])
        self.assertEqual(ex.is_args_prime(7, 11, 13, 17, 19), [True, True, True, True, True])
        self.assertEqual(ex.is_args_prime(20, 21, 22, 24, 25, 26, 27), [False, False, False, False, False, False, False])
    def test_041_find_primes_in_range(self):
        self.assertEqual(ex.find_primes_in_range(1, 5), [2, 3, 5])
        self.assertEqual(ex.find_primes_in_range(6, 10), [7])
        self.assertEqual(ex.find_primes_in_range(11, 15), [11, 13])
    def test_042_find_primes_below_100(self):
        primes_below_100 = ex.find_primes_below_100()
        self.assertEqual(len(primes_below_100), 25)
        self.assertEqual(primes_below_100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    def test_043_find_the_first_n_primes(self):
        self.assertEqual(ex.find_the_first_n_primes(5), [2, 3, 5, 7, 11])
        self.assertEqual(ex.find_the_first_n_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(ex.find_the_first_n_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])
    def test_044_square_negatives_from_args(self):
        self.assertEqual(ex.square_negatives_from_args(-3, -2, -1, 0, 1, 2, 3), [9, 4, 1])
        self.assertEqual(ex.square_negatives_from_args(-3, 0, 1, 2, 3, -2, -1), [9, 4, 1])
        self.assertEqual(ex.square_negatives_from_args(0, 1, 2, 3, -1, -2, -3), [1, 4, 9])
    def test_045_uppercase_keys_values_from_kwargs(self):
        self.assertEqual(ex.uppercase_keys_values_from_kwargs(tw="twn"), {'TW': 'TWN'})
        self.assertEqual(ex.uppercase_keys_values_from_kwargs(tw="twn", jp="jpn"), {'TW': 'TWN', 'JP': 'JPN'})
        self.assertEqual(ex.uppercase_keys_values_from_kwargs(tw="twn", jp="jpn", lt="ltu"), {'TW': 'TWN', 'JP': 'JPN', 'LT': 'LTU'})

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestFunctions, 4)