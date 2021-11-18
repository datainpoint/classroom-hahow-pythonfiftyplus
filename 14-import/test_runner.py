import unittest
import json
import ipynb.fs.full.exercises as ex
import pandas

class TestImport(unittest.TestCase):
    def test_098_import_txt_file(self):
        txt_file = ex.import_txt_file()
        self.assertIsInstance(txt_file, list)
        self.assertEqual(len(txt_file), 5)
    def test_099_import_json_file(self):
        json_file = ex.import_json_file()
        self.assertIsInstance(json_file, list)
        self.assertEqual(len(json_file), 250)
    def test_100_import_csv_file(self):
        csv_file = ex.import_csv_file()
        self.assertIsInstance(csv_file, pandas.core.frame.DataFrame)
        self.assertEqual(csv_file.shape, (250, 4))
    def test_101_import_excel_file(self):
        excel_file = ex.import_excel_file()
        self.assertIsInstance(excel_file, pandas.core.frame.DataFrame)
        self.assertEqual(excel_file.shape, (250, 4))
    def test_102_import_excel_file(self):
        database_table = ex.import_database_table()
        self.assertIsInstance(database_table, pandas.core.frame.DataFrame)
        self.assertEqual(database_table.shape, (250, 6))

def run_suite(test_class, chapter_index=13):
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
    
run_suite(TestImport)