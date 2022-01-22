import unittest
import json
import ipynb.fs.full.exercises as ex
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import pandas as pd

class TestWorkingWithDateTime(unittest.TestCase):
    def test_141_create_date_object(self):
        self.assertEqual(ex.create_date_object(2021, 12, 31), date(2021, 12, 31))
        self.assertEqual(ex.create_date_object(2022, 1, 1), date(2022, 1, 1))
    def test_142_create_time_object(self):
        self.assertEqual(ex.create_time_object(23, 59, 59), time(23, 59, 59))
        self.assertEqual(ex.create_time_object(0, 0, 1), time(0, 0, 1))
    def test_143_create_datetime_object(self):
        d = ex.create_date_object(2021, 12, 31)
        t = ex.create_time_object(23, 59, 59)
        self.assertEqual(ex.create_datetime_object(d, t), datetime(2021, 12, 31, 23, 59, 59))
        d = ex.create_date_object(2022, 1, 1)
        t = ex.create_time_object(0, 0, 1)
        self.assertEqual(ex.create_datetime_object(d, t), datetime(2022, 1, 1, 0, 0, 1))
    def test_144_get_yesterdays_date(self):
        self.assertEqual(ex.get_yesterdays_date("2022-01-02"), date(2022, 1, 1))
        self.assertEqual(ex.get_yesterdays_date("2022-01-01"), date(2021, 12, 31))
    def test_145_get_a_second_before_datetime(self):
        self.assertEqual(ex.test_145_get_a_second_before_datetime("2022-01-01 00:00:01"), datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(ex.test_145_get_a_second_before_datetime("2022-01-01 00:00:00"), datetime(2021, 12, 31, 23, 59, 59))
    def test_146_show_a_non_iso8601_date(self):
        self.assertEqual(ex.show_a_non_iso8601_date(2021, 12, 31), 'Fri Dec 31')
        self.assertEqual(ex.show_a_non_iso8601_date(2021, 1, 1), 'Sat Jan 01')
    def test_147_parse_a_non_iso8601_datetime(self):
        self.assertEqual(ex.parse_a_non_iso8601_datetime("Fri Dec 31 21 23:59:59"), '2021-12-31 23:59:59')
        self.assertEqual(ex.parse_a_non_iso8601_datetime("Sat Jan 01 22 00:00:01"), '2022-01-01 00:00:01')
    def test_148_import_covid19_time_series_confirmed(self):
        covid19_time_series_confirmed = ex.import_covid19_time_series_confirmed()
        self.assertIsInstance(covid19_time_series_confirmed, pd.core.frame.DataFrame)
        self.assertEqual(covid19_time_series_confirmed.shape, (280, 735))
    def test_149_extract_date_columns(self):
        date_columns = ex.extract_date_columns()
        self.assertIsInstance(date_columns, pd.core.indexes.base.Index)
        self.assertEqual(date_columns.size, 731)
    def test_150_parse_date_columns(self):
        date_columns = ex.parse_date_columns()
        self.assertIsInstance(date_columns, pd.core.indexes.datetimes.DatetimeIndex)
        self.assertEqual(date_columns.size, 731)

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
    
run_suite(TestWorkingWithDateTime, 16)