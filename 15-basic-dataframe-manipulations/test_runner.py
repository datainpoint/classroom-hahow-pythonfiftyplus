import unittest
import json
import ipynb.fs.full.exercises as ex
import pandas as pd

class TestBasicDataframeManipulations(unittest.TestCase):
    def test_121_import_movies_csv(self):
        movies_csv = ex.import_movies_csv()
        self.assertIsInstance(movies_csv, pd.core.frame.DataFrame)
        self.assertEqual(movies_csv.shape, (250, 6))
    def test_122_ShowHeadAndTail(self):
        show_head_and_tail = ex.ShowHeadAndTail()
        self.assertEqual(show_head_and_tail.show_head().shape, (10, 6))
        self.assertEqual(show_head_and_tail.show_tail().shape, (10, 6))
    def test_123_describe_dataframes_numeric_columns(self):
        dataframes_numeric_columns = ex.describe_dataframes_numeric_columns()
        self.assertIsInstance(dataframes_numeric_columns, pd.core.frame.DataFrame)
        self.assertEqual(dataframes_numeric_columns.shape, (8, 4))
    def test_124_describe_selected_numeric_columns(self):
        selected_numeric_columns = ex.describe_selected_numeric_columns()
        self.assertIsInstance(selected_numeric_columns, pd.core.frame.DataFrame)
        self.assertEqual(selected_numeric_columns.shape, (8, 3))
    def test_125_describe_filtered_stats(self):
        filtered_stats = ex.describe_filtered_stats()
        self.assertIsInstance(filtered_stats, pd.core.frame.DataFrame)
        self.assertEqual(filtered_stats.shape, (6, 4))
    def test_126_filter_christopher_nolans_movies(self):
        christopher_nolans_movies = ex.filter_christopher_nolans_movies()
        self.assertIsInstance(christopher_nolans_movies, pd.core.frame.DataFrame)
        self.assertEqual(christopher_nolans_movies.shape, (7, 6))
    def test_127_filter_christopher_nolans_steven_spielbergs_movies(self):
        christopher_nolans_steven_spielbergs_movies = ex.filter_christopher_nolans_steven_spielbergs_movies()
        self.assertIsInstance(christopher_nolans_steven_spielbergs_movies, pd.core.frame.DataFrame)
        self.assertEqual(christopher_nolans_steven_spielbergs_movies.shape, (13, 6))
    def test_128_count_movies_by_years(self):
        movies_by_years = ex.count_movies_by_years()
        self.assertIsInstance(movies_by_years, pd.core.series.Series)
        self.assertEqual(movies_by_years.shape, (85,))
    def test_129_count_movies_by_directors(self):
        movies_by_directors = ex.count_movies_by_directors()
        self.assertIsInstance(movies_by_directors, pd.core.series.Series)
        self.assertEqual(movies_by_directors.shape, (10,))
    def test_130_calculate_movie_hours_and_minutes(self):
        movie_hours_and_minutes = ex.calculate_movie_hours_and_minutes()
        self.assertIsInstance(movie_hours_and_minutes, pd.core.frame.DataFrame)
        self.assertEqual(movie_hours_and_minutes.shape, (250, 3))

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
            print("真是令人佩服，你已經完成「Python 的 50+ 練習」的第三階段：Python 資料科學的基礎，距離完課只剩下最後一哩路！")
    elif chapter_percentage == 100 and chapter_index == 19:
        print("恭喜完課，你已經完成「Python 的 50+ 練習」所有習題，能夠堅持到底完成所有的教學影片與練習題真是非常了不起！後面已經沒有練習題了，你現在是一位擅長寫程式處理資料的分析師！")
    elif chapter_percentage >= 50:
        print("你已經完成「{}」章節一半以上的練習，繼續加油！".format(chapter_name))
    
run_suite(TestBasicDataframeManipulations, 14)