import unittest
import json
import ipynb.fs.full.exercises as ex
import numpy as np
import pandas as pd

class TestSupervisedLearning(unittest.TestCase):
    def test_181_import_house_prices(self):
        train, test = ex.import_house_prices()
        self.assertIsInstance(train, pd.core.frame.DataFrame)
        self.assertIsInstance(test, pd.core.frame.DataFrame)
        self.assertEqual(train.shape, (1460, 81))
        self.assertEqual(test.shape, (1459, 80))
    def test_182_find_target_array_variable_house_prices(self):
        target_array_variable_house_prices = ex.find_target_array_variable_house_prices()
        pd.testing.assert_index_equal(target_array_variable_house_prices, pd.Index(["SalePrice"]))
    def test_183_extract_target_array_feature_matrix_house_prices(self):
        y, X = ex.extract_target_array_feature_matrix_house_prices()
        self.assertEqual(y.shape, (1460,))
        self.assertEqual(X.shape, (1460, 1))
    def test_184_split_train_valid_house_prices(self):
        y, X = ex.extract_target_array_feature_matrix_house_prices()
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_house_prices(X, y)
        self.assertEqual(X_train.shape, (1022, 1))
        self.assertEqual(X_valid.shape, (438, 1))
        self.assertEqual(y_train.shape, (1022,))
        self.assertEqual(y_valid.shape, (438,))
    def test_185_DummyModelHousePrices(self):
        y, X = ex.extract_target_array_feature_matrix_house_prices()
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_house_prices(X, y)
        dummy_model_house_prices = ex.DummyModelHousePrices()
        dummy_model_house_prices.fit(y_train)
        y_hat = dummy_model_house_prices.predict(X_valid)
        self.assertEqual(y_hat.shape, (438,))
    def test_186_ExpertModelHousePrices(self):
        y, X = ex.extract_target_array_feature_matrix_house_prices()
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_house_prices(X, y)
        expert_model_house_prices = ex.ExpertModelHousePrices()
        expert_model_house_prices.fit(X_train, y_train)
        y_hat = expert_model_house_prices.predict(X_valid)
        self.assertEqual(y_hat.shape, (438,))
    def test_187_MachineLearningModelHousePrices(self):
        y, X = ex.extract_target_array_feature_matrix_house_prices()
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_house_prices(X, y)
        machine_learning_model_house_prices = ex.MachineLearningModelHousePrices()
        machine_learning_model_house_prices.fit(X_train, y_train)
        y_hat = machine_learning_model_house_prices.predict(X_valid)
        self.assertEqual(y_hat.shape, (438,))
    def test_188_validate_model_performance_house_prices(self):
        y, X = ex.extract_target_array_feature_matrix_house_prices()
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_house_prices(X, y)
        dummy_model_house_prices = ex.DummyModelHousePrices()
        dummy_model_house_prices.fit(y_train)
        dummy_y_hat = dummy_model_house_prices.predict(X_valid)
        expert_model_house_prices = ex.ExpertModelHousePrices()
        expert_model_house_prices.fit(X_train, y_train)
        expert_y_hat = expert_model_house_prices.predict(X_valid)
        machine_learning_model_house_prices = ex.MachineLearningModelHousePrices()
        machine_learning_model_house_prices.fit(X_train, y_train)
        machine_learning_y_hat = machine_learning_model_house_prices.predict(X_valid)
        model_performance_house_prices = ex.validate_model_performance_house_prices(dummy_y_hat, expert_y_hat, machine_learning_y_hat, y_valid)
        self.assertIsInstance(model_performance_house_prices, dict)
        self.assertEqual(len(model_performance_house_prices), 3)
        self.assertTrue("dummy" in model_performance_house_prices.keys())
        self.assertTrue("expert" in model_performance_house_prices.keys())
        self.assertTrue("machine_learning" in model_performance_house_prices.keys())
    def test_189_predict_sale_price(self):
        train, test = ex.import_house_prices()
        X_test = test[["Id", "OverallQual"]]
        sale_price = ex.predict_sale_price(X_test)
        self.assertIsInstance(sale_price, pd.core.frame.DataFrame)
        self.assertEqual(sale_price.shape, (1459, 2))
    def test_190_export_sale_price_as_submission(self):
        train, test = ex.import_house_prices()
        X_test = test[["Id", "OverallQual"]]
        ex.export_sale_price_as_submission(X_test)
        submission_csv = pd.read_csv("submission_house_prices.csv")
        self.assertEqual(submission_csv.shape, (1459, 2))
    def test_191_import_titanic(self):
        train, test = ex.import_titanic()
        self.assertIsInstance(train, pd.core.frame.DataFrame)
        self.assertIsInstance(test, pd.core.frame.DataFrame)
        self.assertEqual(train.shape, (891, 12))
        self.assertEqual(test.shape, (418, 11))
    def test_192_find_target_array_variable_titanic(self):
        target_array_variable_titanic = ex.find_target_array_variable_titanic()
        pd.testing.assert_index_equal(target_array_variable_titanic, pd.Index(["Survived"]))
    def test_193_extract_target_array_feature_matrix_titanic(self):
        y, X = ex.extract_target_array_feature_matrix_titanic()
        self.assertEqual(y.shape, (891,))
        self.assertEqual(X.shape, (891, 2))
    def test_194_wrangle_feature_matrix_titanic(self):
        y, X = ex.extract_target_array_feature_matrix_titanic()
        X_wrangled = ex.wrangle_feature_matrix_titanic(X)
        self.assertEqual(np.unique(X_wrangled[:, 0]).size, 2)
        self.assertEqual(np.sum(np.isnan(X_wrangled[:, 1])), 0)
    def test_195_split_train_valid_titanic(self):
        y, X = ex.extract_target_array_feature_matrix_titanic()
        X_wrangled = ex.wrangle_feature_matrix_titanic(X)
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_titanic(X_wrangled, y)
        self.assertEqual(X_train.shape, (623, 2))
        self.assertEqual(X_valid.shape, (268, 2))
        self.assertEqual(y_train.shape, (623,))
        self.assertEqual(y_valid.shape, (268,))
    def test_196_DummyModelTitanic(self):
        y, X = ex.extract_target_array_feature_matrix_titanic()
        X_wrangled = ex.wrangle_feature_matrix_titanic(X)
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_titanic(X_wrangled, y)
        dummy_model_titanic = ex.DummyModelTitanic()
        dummy_model_titanic.fit(y_train)
        y_hat = dummy_model_titanic.predict(X_valid)
        self.assertEqual(y_hat.shape, (268,))
    def test_197_ExpertModelTitanic(self):
        y, X = ex.extract_target_array_feature_matrix_titanic()
        X_wrangled = ex.wrangle_feature_matrix_titanic(X)
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_titanic(X_wrangled, y)
        expert_model_titanic = ex.ExpertModelTitanic()
        expert_model_titanic.fit(X_train)
        y_hat = expert_model_titanic.predict(X_valid)
        self.assertEqual(y_hat.shape, (268,))
    def test_198_MachineLearningModelTitanic(self):
        y, X = ex.extract_target_array_feature_matrix_titanic()
        X_wrangled = ex.wrangle_feature_matrix_titanic(X)
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_titanic(X_wrangled, y)
        machine_learning_model_titanic = ex.MachineLearningModelTitanic()
        machine_learning_model_titanic.fit(X_train, y_train)
        y_hat = machine_learning_model_titanic.predict(X_valid)
        self.assertEqual(y_hat.shape, (268,))
    def test_199_validate_model_performance_titanic(self):
        y, X = ex.extract_target_array_feature_matrix_titanic()
        X_wrangled = ex.wrangle_feature_matrix_titanic(X)
        X_train, X_valid, y_train, y_valid = ex.split_train_valid_titanic(X_wrangled, y)
        dummy_model_titanic = ex.DummyModelTitanic()
        dummy_model_titanic.fit(y_train)
        dummy_y_hat = dummy_model_titanic.predict(X_valid)
        expert_model_titanic = ex.ExpertModelTitanic()
        expert_model_titanic.fit(X_train)
        expert_y_hat = expert_model_titanic.predict(X_valid)
        machine_learning_model_titanic = ex.MachineLearningModelTitanic()
        machine_learning_model_titanic.fit(X_train, y_train)
        machine_learning_y_hat = machine_learning_model_titanic.predict(X_valid)
        model_performance_titanic = ex.validate_model_performance_titanic(dummy_y_hat, expert_y_hat, machine_learning_y_hat, y_valid)
        self.assertIsInstance(model_performance_titanic, dict)
        self.assertEqual(len(model_performance_titanic), 3)
        self.assertTrue("dummy" in model_performance_titanic.keys())
        self.assertTrue("expert" in model_performance_titanic.keys())
        self.assertTrue("machine_learning" in model_performance_titanic.keys())
    def test_200_predict_survived(self):
        train, test = ex.import_titanic()
        X_test = test[["PassengerId", "Sex", "Age"]]
        ex.predict_survived(X_test)
        submission_csv = pd.read_csv("submission_titanic.csv")
        self.assertEqual(submission_csv.shape, (418, 2))
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
    
run_suite(TestSupervisedLearning, 19)