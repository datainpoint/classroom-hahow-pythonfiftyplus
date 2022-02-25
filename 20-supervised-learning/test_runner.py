import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestSupervisedLearning, 19)