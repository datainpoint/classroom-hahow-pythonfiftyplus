import unittest
import ipynb.fs.full.exercises as ex
import importlib.util

class TestControlFlows(unittest.TestCase):
    def test_026_find_bmi_category(self):
        self.assertEqual(ex.find_bmi_category(32.90), 'Obese')
        self.assertEqual(ex.find_bmi_category(26.63), 'Overweight')
        self.assertEqual(ex.find_bmi_category(24.83), 'Normal weight')
        self.assertEqual(ex.find_bmi_category(17.58), 'Underweight')
    def test_027_check_data_type(self):
        self.assertEqual(ex.check_data_type(0), 'int')
        self.assertEqual(ex.check_data_type(1.0), 'float')
        self.assertEqual(ex.check_data_type(False), 'bool')
        self.assertEqual(ex.check_data_type(True), 'bool')
        self.assertEqual(ex.check_data_type('5566'), 'str')
        self.assertEqual(ex.check_data_type(None), 'NoneType')
    def test_028_check_data_structure_type(self):
        self.assertEqual(ex.check_data_structure_type([5, 5, 6, 6]), 'list')
        self.assertEqual(ex.check_data_structure_type((5, 5, 6, 6)), 'tuple')
        self.assertEqual(ex.check_data_structure_type({5, 6}), 'set')
        self.assertEqual(ex.check_data_structure_type({'title': 'The Shawshank Redemption', 'year': 1994}), 'dict')
    def test_029_retrieve_middle_elements(self):
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5]), 3)
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7]), (3, 5))
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7, 11, 13]), (5, 7))
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7, 11, 13, 17]), 7)
    def test_030_calculate_median(self):
        self.assertEqual(ex.calculate_median([9, 8, 3, 6, 7, 3, 1]), 6)
        self.assertAlmostEqual(ex.calculate_median([1, 3, 2, 5, 4, 9, 8, 6]), 4.5)
        self.assertEqual(ex.calculate_median([5, 6, 7]), 6)
        self.assertAlmostEqual(ex.calculate_median([3, 4, 5, 6]), 4.5)
    def test_031_calculate_mean(self):
        self.assertAlmostEqual(ex.calculate_mean([5, 5, 6, 6]), 5.5)
        self.assertAlmostEqual(ex.calculate_mean([5, 3, 4]), 4.0)
        self.assertAlmostEqual(ex.calculate_mean([4, 3]), 3.5)
        self.assertAlmostEqual(ex.calculate_mean([4]), 4.0)
    def test_032_create_first_100_fizz_buzz(self):
        first_100_fizz_buzz = ex.create_first_100_fizz_buzz()
        self.assertEqual(len(first_100_fizz_buzz), 100)
        self.assertEqual(first_100_fizz_buzz[0], 1)
        self.assertEqual(first_100_fizz_buzz[1], 2)
        self.assertEqual(first_100_fizz_buzz[2], 'Fizz')
        self.assertEqual(first_100_fizz_buzz[3], 4)
        self.assertEqual(first_100_fizz_buzz[4], 'Buzz')
        self.assertEqual(first_100_fizz_buzz[13], 14)
        self.assertEqual(first_100_fizz_buzz[14], 'Fizz Buzz')
        self.assertEqual(first_100_fizz_buzz[-1], 'Buzz')
        self.assertEqual(first_100_fizz_buzz[-2], 'Fizz')
        self.assertEqual(first_100_fizz_buzz[-11], 'Fizz Buzz')
    def test_033_create_fizz_buzz_slice(self):
        self.assertEqual(ex.create_fizz_buzz_slice(1, 5), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(ex.create_fizz_buzz_slice(11, 15), [11, 'Fizz', 13, 14, 'Fizz Buzz'])
        self.assertEqual(ex.create_fizz_buzz_slice(25, 30), ['Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz'])
    def test_034_collect_divisors(self):
        self.assertEqual(ex.collect_divisors(2), [1, 2])
        self.assertEqual(ex.collect_divisors(3), [1, 3])
        self.assertEqual(ex.collect_divisors(4), [1, 2, 4])
        self.assertEqual(ex.collect_divisors(8), [1, 2, 4, 8])
        self.assertEqual(ex.collect_divisors(9), [1, 3, 9])
    def test_035_safe_divide(self):
        self.assertAlmostEqual(ex.safe_divide(10, 2), 5.0)
        self.assertAlmostEqual(ex.safe_divide(0, 2), 0.0)
        self.assertAlmostEqual(ex.safe_divide(10, 0), 'division by zero')

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestControlFlows, 3)