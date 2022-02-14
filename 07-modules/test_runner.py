import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
from palindromefunctions import reverse_str
from palindromefunctions import is_palindrome
from palindromeclass import Palindrome
from mymodules.palindromefunctions import reverse_str as mm_reverse_str
from mymodules.palindromefunctions import is_palindrome as mm_is_palindrome
from mymodules.palindromeclass import Palindrome as MmPalindrome

class TestModules(unittest.TestCase):
    def test_056_functions_in_module(self):
        self.assertEqual(reverse_str("eye"), 'eye')
        self.assertEqual(reverse_str("dad"), 'dad')
        self.assertEqual(reverse_str("dye"), 'eyd')
        self.assertEqual(reverse_str("mad"), 'dam')
        self.assertTrue(is_palindrome("eye"))
        self.assertTrue(is_palindrome("dad"))
        self.assertFalse(is_palindrome("dye"))
        self.assertFalse(is_palindrome("mad"))
    def test_057_classes_in_module(self):
        palindrome = Palindrome("eye")
        self.assertEqual(palindrome.original_str, 'eye')
        self.assertEqual(palindrome.reversed_str, 'eye')
        self.assertTrue(palindrome.is_palindrome())
        palindrome = Palindrome("dye")
        self.assertEqual(palindrome.original_str, 'dye')
        self.assertEqual(palindrome.reversed_str, 'eyd')
        self.assertFalse(palindrome.is_palindrome())
    def test_058_folder_as_module(self):
        self.assertEqual(mm_reverse_str("eye"), 'eye')
        self.assertEqual(mm_reverse_str("dad"), 'dad')
        self.assertEqual(mm_reverse_str("dye"), 'eyd')
        self.assertEqual(mm_reverse_str("mad"), 'dam')
        self.assertTrue(mm_is_palindrome("eye"))
        self.assertTrue(mm_is_palindrome("dad"))
        self.assertFalse(mm_is_palindrome("dye"))
        self.assertFalse(mm_is_palindrome("mad"))
        palindrome = MmPalindrome("eye")
        self.assertEqual(palindrome.original_str, 'eye')
        self.assertEqual(palindrome.reversed_str, 'eye')
        self.assertTrue(palindrome.is_palindrome())
        palindrome = MmPalindrome("dye")
        self.assertEqual(palindrome.original_str, 'dye')
        self.assertEqual(palindrome.reversed_str, 'eyd')
        self.assertFalse(palindrome.is_palindrome())

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestModules, 6)