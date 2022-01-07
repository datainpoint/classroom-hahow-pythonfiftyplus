import unittest
import json
import ipynb.fs.full.exercises as ex
import numpy as np
import pandas as pd

class TestPandas(unittest.TestCase):
    def test_81_create_first_five_evens_index(self):
        first_five_evens_index = ex.create_first_five_evens_index()
        self.assertEqual(first_five_evens_index.size, 5)
        self.assertEqual(first_five_evens_index[0], 0)
        self.assertEqual(first_five_evens_index[-1], 8)
    def test_82_create_a_str_index(self):
        a_str_index = ex.create_a_str_index()
        self.assertEqual(a_str_index.size, 5)
        self.assertEqual(a_str_index[0], '1st')
        self.assertEqual(a_str_index[-1], '5th')
    def test_83_create_first_five_evens_series(self):
        first_five_evens_series = ex.create_first_five_evens_series()
        self.assertEqual(first_five_evens_series.size, 5)
        self.assertEqual(first_five_evens_series[0], 0)
        self.assertEqual(first_five_evens_series[-1], 8)
        self.assertIsInstance(first_five_evens_series, pd.core.series.Series)
    def test_84_update_first_five_evens_series_index(self):
        updated_first_five_evens_series_index = ex.update_first_five_evens_series_index()
        self.assertIsInstance(updated_first_five_evens_series_index, pd.core.series.Series)
        self.assertEqual(updated_first_five_evens_series_index.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        self.assertEqual(updated_first_five_evens_series_index.values, np.array([0, 2, 4, 6, 8]))
    def test_85_create_first_five_odds_series(self):
        first_five_odds_series = ex.create_first_five_odds_series()
        self.assertIsInstance(first_five_odds_series, pd.core.series.Series)
        self.assertEqual(first_five_odds_series.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        self.assertEqual(first_five_odds_series.values, np.array([1, 3, 5, 7, 9]))
    def test_86_create_first_five_primes_series(self):
        first_five_primes_series = ex.create_first_five_primes_series()
        self.assertIsInstance(first_five_primes_series, pd.core.series.Series)
        self.assertEqual(first_five_primes_series.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        self.assertEqual(first_five_primes_series.values, np.array([2, 3, 5, 7, 11]))
    def test_87_create_first_five_integer_dataframe(self):
        first_five_integer_dataframe = ex.create_first_five_integer_dataframe()
        self.assertIsInstance(first_five_integer_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(first_five_integer_dataframe.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        self.assertEqual(first_five_integer_dataframe.shape, (5, 3))
    def test_88_create_lord_of_the_rings_dataframe(self):
        lord_of_the_rings_dataframe = ex.create_lord_of_the_rings_dataframe()
        self.assertIsInstance(lord_of_the_rings_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(lord_of_the_rings_dataframe.shape, (3, 4))
    def test_89_create_dark_knight_dataframe(self):
        dark_knight_dataframe = ex.create_dark_knight_dataframe()
        self.assertIsInstance(dark_knight_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(dark_knight_dataframe.shape, (3, 4))
    def test_90_summarize_dataframe_with_dict(self):
        lord_of_the_rings_dataframe = ex.create_lord_of_the_rings_dataframe()
        dark_knight_dataframe = ex.create_dark_knight_dataframe()
        summary = ex.summarize_dataframe_with_dict(lord_of_the_rings_dataframe)
        self.assertEqual(summary["shape"], (3, 4))
        self.assertEqual(summary["columns"], pd.Index(['title', 'director', 'imdb_rating', 'release_year']))
        summary = ex.summarize_dataframe_with_dict(dark_knight_dataframe)
        self.assertEqual(summary["shape"], (3, 4))
        self.assertEqual(summary["columns"], pd.Index(['title', 'director', 'imdb_rating', 'release_year']))

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
        elif chapter_index == 13:
            print("太令人佩服，你已經完成「Python 的 50+ 練習」的第三階段：Python 資料科學的基礎，距離完課只剩下最後一哩路！")
    elif chapter_percentage == 100 and chapter_index == 19:
        print("恭喜完課，你已經完成「{}」所有習題，能夠堅持到底完成所有的教學影片與練習題真是非常了不起！後面已經沒有練習題了，你現在是一位擅長寫程式處理資料的分析師！")
    elif chapter_percentage >= 50:
        print("你已經完成「{}」章節一半以上的練習，繼續加油！".format(chapter_name))
    
run_suite(TestPandas, 10)