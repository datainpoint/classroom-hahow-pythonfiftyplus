import unittest
import json
import ipynb.fs.full.exercises as ex

class TestDataTypes(unittest.TestCase):
    def test_015_retrieve_the_first_and_last_element(self):
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
    def test_016_retrieve_the_first_three_characters(self):
        self.assertEqual(ex.retrieve_the_first_three_characters("Python"), "Pyt")
        self.assertEqual(ex.retrieve_the_first_three_characters("Reticulate"), "Ret")
        self.assertEqual(ex.retrieve_the_first_three_characters("Anaconda"), "Ana")
        self.assertEqual(ex.retrieve_the_first_three_characters("Skywalker"), "Sky")
        self.assertEqual(ex.retrieve_the_first_three_characters("Anakin"), "Ana")
    def test_017_retrieve_the_middle_element(self):
        self.assertEqual(ex.retrieve_the_middle_element([2, 3, 5]), 3)
        self.assertEqual(ex.retrieve_the_middle_element([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ex.retrieve_the_middle_element([2, 3, 5, 7, 11, 13, 17]), 7)
        self.assertEqual(ex.retrieve_the_middle_element([1, 2, 3]), 2)
        self.assertEqual(ex.retrieve_the_middle_element([-1, 0, 1]), 0)
    def test_018_retrieve_the_middle_three_characters(self):
        self.assertEqual(ex.retrieve_the_middle_three_characters("Steve"), "tev")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Stark"), "tar")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Natasha"), "tas")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Skywalker"), "wal")
        self.assertEqual(ex.retrieve_the_middle_three_characters("Hawkeye"), "wke")
    def test_019_find_taipei_citys_zip_code(self):
        self.assertEqual(ex.find_taipei_citys_zip_code("中正區"), 100)
        self.assertEqual(ex.find_taipei_citys_zip_code("大同區"), 103)
        self.assertEqual(ex.find_taipei_citys_zip_code("中山區"), 104)
        self.assertEqual(ex.find_taipei_citys_zip_code("松山區"), 105)
        self.assertEqual(ex.find_taipei_citys_zip_code("大安區"), 106)
    def test_020_find_country_iso_codes(self):
        self.assertEqual(ex.find_country_iso_codes("Taiwan"), {'alpha2': 'TW', 'alpha3': 'TWN'})
        self.assertEqual(ex.find_country_iso_codes("Japan"), {'alpha2': 'JP', 'alpha3': 'JPN'})
        self.assertEqual(ex.find_country_iso_codes("United States"), {'alpha2': 'US', 'alpha3': 'USA'})
        self.assertEqual(ex.find_country_iso_codes("Czech Republic"), {'alpha2': 'CZ', 'alpha3': 'CZE'})
        self.assertEqual(ex.find_country_iso_codes("Lithuania"), {'alpha2': 'LT', 'alpha3': 'LTU'})
        self.assertEqual(ex.find_country_iso_codes("Slovakia"), {'alpha2': 'SK', 'alpha3': 'SVK'})
        self.assertEqual(ex.find_country_iso_codes("Poland"), {'alpha2': 'PL', 'alpha3': 'POL'})
    def test_021_find_number_of_differences(self):
        self.assertEqual(ex.find_number_of_differences({5, 5, 6, 6}, {5, 6, 7, 8}), 2)
        self.assertEqual(ex.find_number_of_differences({1, 3, 5, 7, 9}, {2, 3, 5, 7}), 3)
        self.assertEqual(ex.find_number_of_differences({1, 3, 5, 7, 9}, {1, 3, 5, 7, 9}), 0)
        self.assertEqual(ex.find_number_of_differences({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}), 10)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestDataTypes)
runner = unittest.TextTestRunner(verbosity=2)
if __name__ == '__main__':
    test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
with open("exercise_index.json", "r") as content:
    exercise_index = json.load(content)
chapter_index = 2
chapter_name = exercise_index[chapter_index]["chapter_name"]
number_of_total_questions = 0
number_of_completed_questions = 0
for i in range(len(exercise_index)):
    number_of_total_questions += exercise_index[i]["number_of_exercises"]
    if i < chapter_index:
        number_of_completed_questions += exercise_index[i]["number_of_exercises"]
number_of_completed_questions += number_of_successes
chapter_percentage = number_of_successes * 100 / number_of_test_runs
overall_percentage = number_of_completed_questions * 100 / number_of_total_questions
print("你在「{}」章節的練習題完成率為 ... {:.2f}% ({}/{})".format(chapter_name, chapter_percentage, number_of_successes, number_of_test_runs))
print("整體課程的累計完成率為 ... {:.2f}% ({}/{})".format(overall_percentage, number_of_completed_questions, number_of_total_questions))
print("很不錯唷，我們繼續往下個章節：「{}」前進！".format(exercise_index[chapter_index + 1]["chapter_name"]))