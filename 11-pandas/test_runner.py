import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
import pandas as pd
import numpy as np

class TestPandas(unittest.TestCase):
    def test_081_create_first_five_evens_index(self):
        first_five_evens_index = ex.create_first_five_evens_index()
        self.assertEqual(first_five_evens_index.size, 5)
        self.assertEqual(first_five_evens_index[0], 0)
        self.assertEqual(first_five_evens_index[-1], 8)
    def test_082_create_a_str_index(self):
        a_str_index = ex.create_a_str_index()
        self.assertEqual(a_str_index.size, 5)
        self.assertEqual(a_str_index[0], '1st')
        self.assertEqual(a_str_index[-1], '5th')
    def test_083_create_first_five_evens_series(self):
        first_five_evens_series = ex.create_first_five_evens_series()
        self.assertEqual(first_five_evens_series.size, 5)
        self.assertEqual(first_five_evens_series[0], 0)
        self.assertEqual(first_five_evens_series[4], 8)
        self.assertIsInstance(first_five_evens_series, pd.core.series.Series)
    def test_084_update_first_five_evens_series_index(self):
        updated_first_five_evens_series_index = ex.update_first_five_evens_series_index()
        self.assertIsInstance(updated_first_five_evens_series_index, pd.core.series.Series)
        pd.testing.assert_index_equal(updated_first_five_evens_series_index.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        np.testing.assert_array_equal(updated_first_five_evens_series_index.values, np.array([0, 2, 4, 6, 8]))
    def test_085_create_first_five_odds_series(self):
        first_five_odds_series = ex.create_first_five_odds_series()
        self.assertIsInstance(first_five_odds_series, pd.core.series.Series)
        pd.testing.assert_index_equal(first_five_odds_series.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        np.testing.assert_array_equal(first_five_odds_series.values, np.array([1, 3, 5, 7, 9]))
    def test_086_create_first_five_primes_series(self):
        first_five_primes_series = ex.create_first_five_primes_series()
        self.assertIsInstance(first_five_primes_series, pd.core.series.Series)
        pd.testing.assert_index_equal(first_five_primes_series.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        np.testing.assert_array_equal(first_five_primes_series.values, np.array([2, 3, 5, 7, 11]))
    def test_087_create_first_five_integer_dataframe(self):
        first_five_integer_dataframe = ex.create_first_five_integer_dataframe()
        self.assertIsInstance(first_five_integer_dataframe, pd.core.frame.DataFrame)
        pd.testing.assert_index_equal(first_five_integer_dataframe.index, pd.Index(['1st', '2nd', '3rd', '4th', '5th']))
        self.assertEqual(first_five_integer_dataframe.shape, (5, 3))
    def test_088_create_lord_of_the_rings_dataframe(self):
        lord_of_the_rings_dataframe = ex.create_lord_of_the_rings_dataframe()
        self.assertIsInstance(lord_of_the_rings_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(lord_of_the_rings_dataframe.shape, (3, 4))
    def test_089_create_dark_knight_dataframe(self):
        dark_knight_dataframe = ex.create_dark_knight_dataframe()
        self.assertIsInstance(dark_knight_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(dark_knight_dataframe.shape, (3, 4))
    def test_090_summarize_dataframe_with_dict(self):
        lord_of_the_rings_dataframe = ex.create_lord_of_the_rings_dataframe()
        dark_knight_dataframe = ex.create_dark_knight_dataframe()
        summary = ex.summarize_dataframe_with_dict(lord_of_the_rings_dataframe)
        self.assertEqual(summary["shape"], (3, 4))
        pd.testing.assert_index_equal(summary["columns"], pd.Index(['title', 'director', 'imdb_rating', 'release_year']))
        summary = ex.summarize_dataframe_with_dict(dark_knight_dataframe)
        self.assertEqual(summary["shape"], (3, 4))
        pd.testing.assert_index_equal(summary["columns"], pd.Index(['title', 'director', 'imdb_rating', 'release_year']))

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestPandas, 10)