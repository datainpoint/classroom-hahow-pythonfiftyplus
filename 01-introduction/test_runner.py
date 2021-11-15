import unittest
import json
import ipynb.fs.full.suggested_answers as ex

class TestIntroduction(unittest.TestCase):
    def test_001_say_hello_to_python(self):
        self.assertEqual(ex.say_hello_to_python(), "Hello, Python!")
    def test_002_say_my_name(self):
        self.assertTrue(isinstance(ex.say_my_name(), str))
    def test_003_return_my_favorite_integer(self):
        self.assertTrue(isinstance(ex.return_my_favorite_integer(), int))
    def test_004_return_the_first_zen_of_python(self):
        self.assertEqual(ex.return_the_first_zen_of_python(), 'Beautiful is better than ugly.')
    def test_005_return_my_favorite_zen_of_python(self):
        my_favorite_zen_of_python = ex.return_my_favorite_zen_of_python()
        self.assertIsInstance(my_favorite_zen_of_python, str)
        file_path = "01-introduction/zen_of_python.txt"
        with open(file_path, 'r') as f:
            zen_of_py = f.readlines()
        zen_of_py = [s.strip() for s in zen_of_py]
        self.assertTrue(my_favorite_zen_of_python in zen_of_py)

def run_suite(test_class, chapter_index=0):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    test_results = runner.run(suite)
    number_of_failures = len(test_results.failures)
    number_of_errors = len(test_results.errors)
    number_of_test_runs = test_results.testsRun
    number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
    with open("exercise_index.json", "r") as f:
        exercise_index = json.load(f)
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
    if chapter_percentage < 100 and chapter_percentage >= 50:
        print("你已經完成了一半以上的練習，繼續加油！")
    elif chapter_percentage == 100:
        print("表現得很好，你已經完成「{}」所有習題，我們繼續往下個章節：「{}」前進！".format(exercise_index[chapter_index]["chapter_name"], exercise_index[chapter_index + 1]["chapter_name"]))
    
run_suite(TestIntroduction)