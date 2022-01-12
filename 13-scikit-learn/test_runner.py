import unittest
import json
import ipynb.fs.full.exercises as ex
import numpy as np
import sklearn
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

class TestSklearn(unittest.TestCase):
    def test_101_create_a_polynomial_feature(self):
        a_polynomial_feature = ex.create_a_polynomial_feature()
        self.assertIsInstance(a_polynomial_feature, sklearn.preprocessing._polynomial.PolynomialFeatures)
    def test_102_create_polynomial_features_for_ndarray(self):
        input_ndarray = np.arange(10).reshape(-1, 1)
        self.assertEqual(ex.create_polynomial_features_for_ndarray(input_ndarray).shape, (10, 3))
    def test_103_add_intercepts_for_ndarray(self):
        input_ndarray = np.arange(10).reshape(-1, 1)
        self.assertEqual(ex.add_intercepts_for_ndarray(input_ndarray).shape, (10, 2))
    def test_104_create_a_standard_scaler(self):
        a_standard_scaler = ex.create_a_standard_scaler()
        self.assertIsInstance(a_standard_scaler, sklearn.preprocessing._data.StandardScaler)
    def test_105_standardize_a_ndarray(self):
        input_ndarray = np.arange(10).reshape(-1, 1)
        self.assertEqual(ex.standardize_a_ndarray(input_ndarray).shape, (10, 1))
    def test_106_get_standard_scalers_attributes(self):
        input_ndarray = np.arange(10).reshape(-1, 1)
        mu, sigma = ex.get_standard_scalers_attributes(input_ndarray)
        self.assertTrue(mu >= 4.5)
        self.assertTrue(sigma >= 2.8)
    def test_107_create_a_minmax_scaler(self):
        a_minmax_scaler = ex.create_a_minmax_scaler()
        self.assertIsInstance(a_minmax_scaler, sklearn.preprocessing._data.MinMaxScaler)
    def test_108_min_max_a_ndarray(self):
        input_ndarray = np.arange(10).reshape(-1, 1)
        self.assertEqual(ex.min_max_a_ndarray(input_ndarray).shape, (10, 1))
    def test_109_get_minmax_scalers_attributes(self):
        input_ndarray = np.arange(10).reshape(-1, 1)
        Xmin, Xmax = ex.get_minmax_scalers_attributes(input_ndarray)
        self.assertAlmostEqual(Xmin, 0.0)
        self.assertAlmostEqual(Xmax, 9.0)
    def test_110_create_linear_logistic_regression(self):
        linear_regression, logistic_regression = ex.create_linear_logistic_regression()
        self.assertIsInstance(linear_regression, sklearn.linear_model._base.LinearRegression)
        self.assertIsInstance(logistic_regression, sklearn.linear_model._logistic.LogisticRegression)

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
    
run_suite(TestSklearn, 12)