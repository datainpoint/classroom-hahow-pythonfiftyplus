import unittest
import json
import ipynb.fs.full.exercises as ex
from testfunction import run_suite

class TestIntroduction(unittest.TestCase):
    def test_001_say_hello_to_python(self):
        self.assertEqual(ex.say_hello_to_python(), 'Hello, Python!')
    def test_002_say_my_name(self):
        self.assertTrue(isinstance(ex.say_my_name(), str))
    def test_003_return_my_favorite_integer(self):
        self.assertTrue(isinstance(ex.return_my_favorite_integer(), int))
    def test_004_return_the_first_zen_of_python(self):
        self.assertEqual(ex.return_the_first_zen_of_python(), 'Beautiful is better than ugly.')
    def test_005_return_my_favorite_zen_of_python(self):
        my_favorite_zen_of_python = ex.return_my_favorite_zen_of_python()
        file_path = "01-introduction/zen_of_python.txt"
        with open(file_path, 'r') as f:
            zen_of_py = f.readlines()
        zen_of_py = [s.strip() for s in zen_of_py]
        self.assertIsInstance(my_favorite_zen_of_python, str)
        self.assertTrue(my_favorite_zen_of_python in zen_of_py)
    
run_suite(TestIntroduction, 0)