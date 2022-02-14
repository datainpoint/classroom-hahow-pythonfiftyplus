import unittest
import ipynb.fs.full.exercises as ex
import importlib.util

class TestClasses(unittest.TestCase):
    def test_046_reverse_str(self):
        self.assertEqual(ex.reverse_str("eye"), 'eye')
        self.assertEqual(ex.reverse_str("dad"), 'dad')
        self.assertEqual(ex.reverse_str("dye"), 'eyd')
        self.assertEqual(ex.reverse_str("mad"), 'dam')
    def test_047_is_palindrome(self):
        self.assertTrue(ex.is_palindrome("eye"))
        self.assertTrue(ex.is_palindrome("dad"))
        self.assertFalse(ex.is_palindrome("dye"))
        self.assertFalse(ex.is_palindrome("mad"))
    def test_048_PalindromeMethods(self):
        palindrome_methods = ex.PalindromeMethods()
        self.assertEqual(palindrome_methods.reverse_str("eye"), 'eye')
        self.assertEqual(palindrome_methods.reverse_str("dad"), 'dad')
        self.assertEqual(palindrome_methods.reverse_str("dye"), 'eyd')
        self.assertEqual(palindrome_methods.reverse_str("mad"), 'dam')
        self.assertTrue(palindrome_methods.is_palindrome("eye"))
        self.assertTrue(palindrome_methods.is_palindrome("dad"))
        self.assertFalse(palindrome_methods.is_palindrome("dye"))
        self.assertFalse(palindrome_methods.is_palindrome("mad"))
    def test_049_Palindrome(self):
        palindrome = ex.Palindrome("eye")
        self.assertEqual(palindrome.original_str, 'eye')
        self.assertEqual(palindrome.reversed_str, 'eye')
        self.assertTrue(palindrome.is_palindrome())
        palindrome = ex.Palindrome("dye")
        self.assertEqual(palindrome.original_str, 'dye')
        self.assertEqual(palindrome.reversed_str, 'eyd')
        self.assertFalse(palindrome.is_palindrome())
    def test_050_collect_divisors_as_set(self):
        self.assertEqual(ex.collect_divisors_as_set(3), {1, 3})
        self.assertEqual(ex.collect_divisors_as_set(6), {1, 2, 3, 6})
        self.assertEqual(ex.collect_divisors_as_set(4), {1, 2, 4})
        self.assertEqual(ex.collect_divisors_as_set(8), {1, 2, 4, 8})
    def test_051_find_common_divisors(self):
        self.assertEqual(ex.find_common_divisors(3, 6), {1, 3})
        self.assertEqual(ex.find_common_divisors(4, 8), {1, 2, 4})
    def test_052_find_the_max_common_divisor(self):
        self.assertEqual(ex.find_the_max_common_divisor(3, 6), 3)
        self.assertEqual(ex.find_the_max_common_divisor(4, 8), 4)
        self.assertEqual(ex.find_the_max_common_divisor(6, 8), 2)
    def test_053_CommonDivisorMethods(self):
        common_divisor_methods = ex.CommonDivisorMethods()
        self.assertEqual(common_divisor_methods.collect_divisors_as_set(3), {1, 3})
        self.assertEqual(common_divisor_methods.collect_divisors_as_set(6), {1, 2, 3, 6})
        self.assertEqual(common_divisor_methods.find_common_divisors(3, 6), {1, 3})
        self.assertEqual(common_divisor_methods.find_the_max_common_divisor(6, 8), 2)
    def test_054_CommonDivisors(self):
        common_divisors = ex.CommonDivisors(3, 6)
        self.assertEqual(common_divisors.x_divisors, {1, 3})
        self.assertEqual(common_divisors.y_divisors, {1, 2, 3, 6})
        self.assertEqual(common_divisors.find_common_divisors(), {1, 3})
        self.assertEqual(common_divisors.find_the_max_common_divisor(), 3)
        common_divisors = ex.CommonDivisors(4, 8)
        self.assertEqual(common_divisors.x_divisors, {1, 2, 4})
        self.assertEqual(common_divisors.y_divisors, {1, 2, 4, 8})
        self.assertEqual(common_divisors.find_common_divisors(), {1, 2, 4})
        self.assertEqual(common_divisors.find_the_max_common_divisor(), 4)
    def test_055_PrimeJudger(self):
        prime_judger = ex.PrimeJudger(1)
        self.assertEqual(prime_judger.x, 1)
        self.assertEqual(prime_judger.count_number_of_divisors(), 1)
        self.assertFalse(prime_judger.is_prime())
        prime_judger = ex.PrimeJudger(2)
        self.assertEqual(prime_judger.x, 2)
        self.assertEqual(prime_judger.count_number_of_divisors(), 2)
        self.assertTrue(prime_judger.is_prime())
        prime_judger = ex.PrimeJudger(4)
        self.assertEqual(prime_judger.x, 4)
        self.assertEqual(prime_judger.count_number_of_divisors(), 3)
        self.assertFalse(prime_judger.is_prime())

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestClasses, 5)