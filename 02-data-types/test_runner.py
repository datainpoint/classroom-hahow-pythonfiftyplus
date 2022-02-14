import unittest
import ipynb.fs.full.exercises as ex
import importlib.util

class TestDataTypes(unittest.TestCase):
    def test_006_convert_km_to_mile(self):
        self.assertTrue(ex.convert_km_to_mile(42.195) > 26)
        self.assertTrue(ex.convert_km_to_mile(42.195) < 27)
        self.assertTrue(ex.convert_km_to_mile(21.095) > 13)
        self.assertTrue(ex.convert_km_to_mile(21.095) < 14)
    def test_007_convert_fahrenheit_to_celsius(self):
        self.assertTrue(ex.convert_fahrenheit_to_celsius(212) >= 100.0)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(32) >= 0.0)
    def test_008_calculate_bmi(self):
        self.assertTrue(ex.calculate_bmi(206, 113) >= 26)
        self.assertTrue(ex.calculate_bmi(206, 113) < 27)
        self.assertTrue(ex.calculate_bmi(211, 110) >= 24)
        self.assertTrue(ex.calculate_bmi(211, 110) < 25)
        self.assertTrue(ex.calculate_bmi(201, 104) >= 25)
        self.assertTrue(ex.calculate_bmi(201, 104) < 26)
    def test_009_show_integer_with_commas_and_digits(self):
        self.assertEqual(ex.show_integer_with_commas_and_digits(1000), "1,000.00")
        self.assertEqual(ex.show_integer_with_commas_and_digits(10000), "10,000.00")
        self.assertEqual(ex.show_integer_with_commas_and_digits(100000), "100,000.00")
        self.assertEqual(ex.show_integer_with_commas_and_digits(1000000), "1,000,000.00")
        self.assertEqual(ex.show_integer_with_commas_and_digits(10000000), "10,000,000.00")
    def test_010_convert_one_usd_to_another_currency(self):
        self.assertEqual(ex.convert_one_usd_to_another_currency("NTD", 28), "1.00 USD = 28.00 NTD")
        self.assertEqual(ex.convert_one_usd_to_another_currency("KRW", 1196), "1.00 USD = 1,196.00 KRW")
        self.assertEqual(ex.convert_one_usd_to_another_currency("JPY", 112), "1.00 USD = 112.00 JPY")
    def test_011_is_positive(self):
        self.assertFalse(ex.is_positive(-2))
        self.assertFalse(ex.is_positive(-1))
        self.assertFalse(ex.is_positive(0))
        self.assertTrue(ex.is_positive(1))
        self.assertTrue(ex.is_positive(2))
    def test_012_has_two_digits(self):
        self.assertFalse(ex.has_two_digits(8))
        self.assertFalse(ex.has_two_digits(9))
        self.assertFalse(ex.has_two_digits(100))
        self.assertTrue(ex.has_two_digits(10))
        self.assertTrue(ex.has_two_digits(99))
    def test_013_is_odd(self):
        self.assertFalse(ex.is_odd(0))
        self.assertFalse(ex.is_odd(2))
        self.assertFalse(ex.is_odd(4))
        self.assertTrue(ex.is_odd(1))
        self.assertTrue(ex.is_odd(3))
    def test_014_is_a_divisor(self):
        self.assertFalse(ex.is_a_divisor(2, 3))
        self.assertFalse(ex.is_a_divisor(3, 4))
        self.assertTrue(ex.is_a_divisor(1, 3))
        self.assertTrue(ex.is_a_divisor(3, 3))
        self.assertTrue(ex.is_a_divisor(1, 4))
        self.assertTrue(ex.is_a_divisor(2, 4))
        self.assertTrue(ex.is_a_divisor(4, 4))
    def test_015_contain_vowels(self):
        self.assertTrue(ex.contain_vowels("python"))
        self.assertTrue(ex.contain_vowels("anaconda"))
        self.assertTrue(ex.contain_vowels("reticulate"))
        self.assertFalse(ex.contain_vowels("pythn"))
        self.assertFalse(ex.contain_vowels("ncnd"))
        self.assertFalse(ex.contain_vowels("rtclt"))
        
spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestDataTypes, 1)