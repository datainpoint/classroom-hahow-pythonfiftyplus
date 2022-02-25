import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestBasicDataframeManipulations, 14)    