import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
import numpy as np
import sklearn

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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestSklearn, 12)