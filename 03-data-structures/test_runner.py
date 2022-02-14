import unittest
import ipynb.fs.full.exercises as ex
import importlib.util

class TestDataStructures(unittest.TestCase):
    def test_016_retrieve_the_first_and_last_element(self):
        the_first_and_last_element = ex.retrieve_the_first_and_last_element([2, 3, 5, 7, 11])
        self.assertEqual(the_first_and_last_element["first"], 2)
        self.assertEqual(the_first_and_last_element["last"], 11)
        the_first_and_last_element = ex.retrieve_the_first_and_last_element([2, 3, 5])
        self.assertEqual(the_first_and_last_element["first"], 2)
        self.assertEqual(the_first_and_last_element["last"], 5)
        the_first_and_last_element = ex.retrieve_the_first_and_last_element(["Python", "Reticulate", "Anaconda"])
        self.assertEqual(the_first_and_last_element["first"], "Python")
        self.assertEqual(the_first_and_last_element["last"], "Anaconda")
        the_first_and_last_element = ex.retrieve_the_first_and_last_element(["Python", "Reticulate", "Anaconda", "Skywalker"])
        self.assertEqual(the_first_and_last_element["first"], "Python")
        self.assertEqual(the_first_and_last_element["last"], "Skywalker")
    def test_017_retrieve_the_first_three_characters(self):
        self.assertEqual(ex.retrieve_the_first_three_characters("Python"), "Pyt")
        self.assertEqual(ex.retrieve_the_first_three_characters("Reticulate"), "Ret")
        self.assertEqual(ex.retrieve_the_first_three_characters("Anaconda"), "Ana")
        self.assertEqual(ex.retrieve_the_first_three_characters("Skywalker"), "Sky")
        self.assertEqual(ex.retrieve_the_first_three_characters("Anakin"), "Ana")
    def test_018_remove_the_first_and_last_element(self):
        self.assertEqual(ex.remove_the_first_and_last_element([2, 3, 5, 7, 11]), [3, 5, 7])
        self.assertEqual(ex.remove_the_first_and_last_element(["Python", "Reticulate", "Anaconda"]), ["Reticulate"])
    def test_019_retrieve_the_middle_element(self):
        self.assertEqual(ex.retrieve_the_middle_element([2, 3, 5]), 3)
        self.assertEqual(ex.retrieve_the_middle_element([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ex.retrieve_the_middle_element([2, 3, 5, 7, 11, 13, 17]), 7)
        self.assertEqual(ex.retrieve_the_middle_element([1, 2, 3]), 2)
        self.assertEqual(ex.retrieve_the_middle_element([-1, 0, 1]), 0)
    def test_020_retrieve_the_middle_three_characters(self):
        self.assertEqual(ex.retrieve_the_middle_three_characters("Steve"), "tev")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Stark"), "tar")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Natasha"), "tas")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Skywalker"), "wal")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Hawkeye"), "wke")
    def test_021_find_taipei_citys_zip_code(self):
        self.assertEqual(ex.find_taipei_citys_zip_code("中正區"), 100)
        self.assertEqual(ex.find_taipei_citys_zip_code("大同區"), 103)
        self.assertEqual(ex.find_taipei_citys_zip_code("中山區"), 104)
        self.assertEqual(ex.find_taipei_citys_zip_code("松山區"), 105)
        self.assertEqual(ex.find_taipei_citys_zip_code("大安區"), 106)
    def test_022_find_country_iso_codes(self):
        self.assertEqual(ex.find_country_iso_codes("Taiwan"), {'alpha2': 'TW', 'alpha3': 'TWN'})
        self.assertEqual(ex.find_country_iso_codes("Japan"), {'alpha2': 'JP', 'alpha3': 'JPN'})
        self.assertEqual(ex.find_country_iso_codes("United States"), {'alpha2': 'US', 'alpha3': 'USA'})
        self.assertEqual(ex.find_country_iso_codes("Czech Republic"), {'alpha2': 'CZ', 'alpha3': 'CZE'})
        self.assertEqual(ex.find_country_iso_codes("Lithuania"), {'alpha2': 'LT', 'alpha3': 'LTU'})
        self.assertEqual(ex.find_country_iso_codes("Slovakia"), {'alpha2': 'SK', 'alpha3': 'SVK'})
        self.assertEqual(ex.find_country_iso_codes("Poland"), {'alpha2': 'PL', 'alpha3': 'POL'})
    def test_023_remove_duplicates(self):
        self.assertEqual(ex.remove_duplicates([5, 5, 6, 6]), [5, 6])
        self.assertEqual(ex.remove_duplicates([2, 2, 6, 6]), [2, 6])
        self.assertEqual(ex.remove_duplicates([9, 9, 8, 1]), [1, 8, 9])
    def test_024_find_number_of_intersections(self):
        self.assertEqual(ex.find_number_of_intersections({5, 5, 6, 6}, {5, 6, 7, 8}), 2)
        self.assertEqual(ex.find_number_of_intersections({1, 3, 5, 7, 9}, {2, 3, 5, 7}), 3)
        self.assertEqual(ex.find_number_of_intersections({1, 3, 5, 7, 9}, {1, 3, 5, 7, 9}), 5)
        self.assertEqual(ex.find_number_of_intersections({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}), 0)
    def test_025_find_number_of_differences(self):
        self.assertEqual(ex.find_number_of_differences({5, 5, 6, 6}, {5, 6, 7, 8}), 2)
        self.assertEqual(ex.find_number_of_differences({1, 3, 5, 7, 9}, {2, 3, 5, 7}), 3)
        self.assertEqual(ex.find_number_of_differences({1, 3, 5, 7, 9}, {1, 3, 5, 7, 9}), 0)
        self.assertEqual(ex.find_number_of_differences({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}), 10)
        
spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestDataStructures, 2)