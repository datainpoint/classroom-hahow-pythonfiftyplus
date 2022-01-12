import unittest
import json
import ipynb.fs.full.exercises as ex
import pandas as pd
import sqlite3

class TestImport(unittest.TestCase):
    def test_111_import_txt_file(self):
        txt_file = ex.import_txt_file()
        self.assertIsInstance(txt_file, list)
        self.assertEqual(len(txt_file), 5)
    def test_112_import_json_file_as_list(self):
        json_file_as_list = ex.import_json_file_as_list()
        self.assertIsInstance(json_file_as_list, list)
        self.assertEqual(len(json_file_as_list), 34)
    def test_113_import_json_file_as_dataframe(self):
        json_file_as_dataframe = ex.import_json_file_as_dataframe()
        self.assertIsInstance(json_file_as_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(json_file_as_dataframe.shape, (34, 12))
    def test_114_import_csv_file(self):
        csv_file = ex.import_csv_file()
        self.assertIsInstance(csv_file, pd.core.frame.DataFrame)
        self.assertEqual(csv_file.shape, (250, 6))
    def test_115_import_xlsx_file_movies(self):
        xlsx_file_movies = ex.import_xlsx_file_movies()
        self.assertIsInstance(xlsx_file_movies, pd.core.frame.DataFrame)
        self.assertEqual(xlsx_file_movies.shape, (250, 6))
    def test_116_import_xlsx_file_casting(self):
        xlsx_file_casting = ex.import_xlsx_file_casting()
        self.assertIsInstance(xlsx_file_casting, pd.core.frame.DataFrame)
        self.assertEqual(xlsx_file_casting.shape, (3584, 3))
    def test_117_import_xlsx_file_actors(self):
        xlsx_file_actors = ex.import_xlsx_file_actors()
        self.assertIsInstance(xlsx_file_actors, pd.core.frame.DataFrame)
        self.assertEqual(xlsx_file_actors.shape, (3108, 2))
    def test_118_import_database_table_movies(self):
        database_table_movies = ex.import_database_table_movies()
        self.assertIsInstance(database_table_movies, pd.core.frame.DataFrame)
        self.assertEqual(database_table_movies.shape, (250, 6))
    def test_119_import_database_table_casting(self):
        database_table_casting = ex.import_database_table_casting()
        self.assertIsInstance(database_table_casting, pd.core.frame.DataFrame)
        self.assertEqual(database_table_casting.shape, (3584, 3))
    def test_120_import_database_table_actors(self):
        database_table_actors = ex.import_database_table_actors()
        self.assertIsInstance(database_table_actors, pd.core.frame.DataFrame)
        self.assertEqual(database_table_actors.shape, (3108, 2))

def run_suite(test_class, chapter_index):
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
    print("整體課程練習題的累計完成率為 ... {:.2f}% ({}/{})".format(overall_percentage, number_of_completed_questions, number_of_total_questions))
    if chapter_percentage == 100 and chapter_index < 19:
        print("表現得很好，你已經完成「{}」所有習題，我們繼續往下個章節：「{}」前進！".format(exercise_index[chapter_index]["chapter_name"], exercise_index[chapter_index + 1]["chapter_name"]))
        if chapter_index == 4:
            print("太棒了，你已經完成「Python 的 50+ 練習」的第一階段：Python 程式設計的基礎觀念，接下來還有三個階段等你來挑戰！")
        elif chapter_index == 8:
            print("表現得非常好，你已經完成「Python 的 50+ 練習」的第二階段：Python 程式設計的進階觀念，接著讓我們邁向資料科學！")
        elif chapter_index == 12:
            print("太令人佩服，你已經完成「Python 的 50+ 練習」的第三階段：Python 資料科學的基礎，距離完課只剩下最後一哩路！")
    elif chapter_percentage == 100 and chapter_index == 19:
        print("恭喜完課，你已經完成「{}」所有習題，能夠堅持到底完成所有的教學影片與練習題真是非常了不起！後面已經沒有練習題了，你現在是一位擅長寫程式處理資料的分析師！")
    elif chapter_percentage >= 50:
        print("你已經完成「{}」章節一半以上的練習，繼續加油！".format(chapter_name))
    
run_suite(TestImport, 13)