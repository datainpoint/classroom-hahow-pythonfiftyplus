import unittest
import json
import ipynb.fs.full.exercises as ex
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image

class TestExploration(unittest.TestCase):
    def test_171_import_covid19_time_series_confirmed(self):
        covid19_time_series_confirmed = ex.import_covid19_time_series_confirmed()
        self.assertIsInstance(covid19_time_series_confirmed, pd.core.frame.DataFrame)
        self.assertEqual(covid19_time_series_confirmed.shape, (280, 735))
    def test_172_find_top_ten_confirmed_by_country_region(self):
        top_ten_confirmed_by_country_region = ex.find_top_ten_confirmed_by_country_region()
        self.assertIsInstance(top_ten_confirmed_by_country_region, pd.core.series.Series)
        self.assertEqual(top_ten_confirmed_by_country_region.size, 10)
    def test_173_export_top_ten_confirmed_by_country_region(self):
        ex.export_top_ten_confirmed_by_country_region()
        im = Image.open("confirmed_barh.png")
        self.assertEqual(im.format, 'PNG')
        im_test = Image.open("/home/jovyan/test-images/confirmed_barh.png")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)
    def test_174_import_covid19_time_series_deaths(self):
        covid19_time_series_deaths = ex.import_covid19_time_series_deaths()
        self.assertIsInstance(covid19_time_series_deaths, pd.core.frame.DataFrame)
        self.assertEqual(covid19_time_series_deaths.shape, (280, 735))
    def test_175_find_top_ten_deaths_by_country_region(self):
        top_ten_deaths_by_country_region = ex.find_top_ten_deaths_by_country_region()
        self.assertIsInstance(top_ten_deaths_by_country_region, pd.core.series.Series)
        self.assertEqual(top_ten_deaths_by_country_region.size, 10)
    def test_176_export_top_ten_deaths_by_country_region(self):
        ex.export_top_ten_deaths_by_country_region()
        im = Image.open("deaths_barh.png")
        self.assertEqual(im.format, 'PNG')
        im_test = Image.open("/home/jovyan/test-images/deaths_barh.png")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)
    def test_177_sum_confirmed_by_date(self):
        confirmed_by_date = ex.sum_confirmed_by_date()
        self.assertIsInstance(confirmed_by_date, pd.core.series.Series)
        self.assertEqual(confirmed_by_date.size, 731)
    def test_178_sum_deaths_by_date(self):
        deaths_by_date = ex.sum_deaths_by_date()
        self.assertIsInstance(deaths_by_date, pd.core.series.Series)
        self.assertEqual(deaths_by_date.size, 731)
    def test_179_merge_confirmed_deaths_series(self):
        merged_confirmed_deaths = ex.merge_confirmed_deaths_series()
        self.assertIsInstance(merged_confirmed_deaths, pd.core.frame.DataFrame)
        self.assertEqual(merged_confirmed_deaths.shape, (731, 2))
    def test_180_export_time_series_subplots(self):
        ex.export_time_series_subplots()
        im = Image.open("time_series_subplots.png")
        self.assertEqual(im.format, 'PNG')
        im_test = Image.open("/home/jovyan/test-images/time_series_subplots.png")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)

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
    
run_suite(TestExploration, 18)