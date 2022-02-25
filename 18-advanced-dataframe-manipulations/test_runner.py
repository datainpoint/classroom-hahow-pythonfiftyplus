import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
import pandas as pd

class TestAdvancedDataframeManipulations(unittest.TestCase):
    def test_151_import_covid19_daily_report(self):
        covid19_daily_report = ex.import_covid19_daily_report()
        self.assertIsInstance(covid19_daily_report, pd.core.frame.DataFrame)
        self.assertEqual(covid19_daily_report.shape, (4006, 14))
    def test_152_sum_confirmed_deaths_by_country_region(self):
        confirmed_deaths_by_country_region = ex.sum_confirmed_deaths_by_country_region()
        self.assertIsInstance(confirmed_deaths_by_country_region, pd.core.frame.DataFrame)
        self.assertEqual(confirmed_deaths_by_country_region.shape, (196, 3))
    def test_153_import_covid19_time_series_confirmed(self):
        covid19_time_series_confirmed = ex.import_covid19_time_series_confirmed()
        self.assertIsInstance(covid19_time_series_confirmed, pd.core.frame.DataFrame)
        self.assertEqual(covid19_time_series_confirmed.shape, (280, 735))
    def test_154_melt_covid19_time_series_confirmed(self):
        melted_covid19_time_series_confirmed = ex.melt_covid19_time_series_confirmed()
        self.assertIsInstance(melted_covid19_time_series_confirmed, pd.core.frame.DataFrame)
        self.assertEqual(melted_covid19_time_series_confirmed.shape, (204680, 6))
    def test_155_sum_confirmed_by_country_region_date(self):
        confirmed_by_country_region_date = ex.sum_confirmed_by_country_region_date()
        self.assertIsInstance(confirmed_by_country_region_date, pd.core.frame.DataFrame)
        self.assertEqual(confirmed_by_country_region_date.shape, (143276, 3))
    def test_156_import_covid19_time_series_deaths(self):
        covid19_time_series_deaths = ex.import_covid19_time_series_deaths()
        self.assertIsInstance(covid19_time_series_deaths, pd.core.frame.DataFrame)
        self.assertEqual(covid19_time_series_deaths.shape, (280, 735))
    def test_157_sum_deaths_by_country_region_date(self):
        deaths_by_country_region_date = ex.sum_deaths_by_country_region_date()
        self.assertIsInstance(deaths_by_country_region_date, pd.core.frame.DataFrame)
        self.assertEqual(deaths_by_country_region_date.shape, (143276, 3))
    def test_158_merge_confirmed_deaths_time_series(self):
        confirmed_deaths_time_series = ex.merge_confirmed_deaths_time_series()
        self.assertIsInstance(confirmed_deaths_time_series, pd.core.frame.DataFrame)
        self.assertEqual(confirmed_deaths_time_series.shape, (143276, 4))
    def test_159_import_imdb_tables(self):
        imdb_tables = ex.import_imdb_tables()
        self.assertEqual(imdb_tables["movies"].shape, (250, 6))
        self.assertEqual(imdb_tables["casting"].shape, (3584, 3))
        self.assertEqual(imdb_tables["actors"].shape, (3108, 2))
    def test_160_find_cast_of_dark_knight_trilogy(self):
        cast_of_dark_knight_trilogy = ex.find_cast_of_dark_knight_trilogy()
        self.assertIsInstance(cast_of_dark_knight_trilogy, pd.core.frame.DataFrame)
        self.assertEqual(cast_of_dark_knight_trilogy.shape, (45, 3))
    def test_161_import_spreadsheet_and_skiprows(self):
        spreadsheet_and_skiprows = ex.import_spreadsheet_and_skiprows()
        self.assertIsInstance(spreadsheet_and_skiprows, pd.core.frame.DataFrame)
        self.assertEqual(spreadsheet_and_skiprows.shape, (1741, 14))
    def test_162_select_the_first_six_columns(self):
        the_first_six_columns = ex.select_the_first_six_columns()
        self.assertIsInstance(the_first_six_columns, pd.core.frame.DataFrame)
        self.assertEqual(the_first_six_columns.shape, (1741, 6))
    def test_163_fillna_for_towns(self):
        na_filled_for_towns = ex.fillna_for_towns()
        self.assertIsInstance(na_filled_for_towns, pd.core.frame.DataFrame)
        self.assertEqual(na_filled_for_towns.shape, (1741, 6))
        self.assertEqual(na_filled_for_towns["town"].isnull().sum(), 0)
    def test_164_dropna_for_totals_and_subtotals(self):
        na_dropped_for_totals_and_subtotals = ex.dropna_for_totals_and_subtotals()
        self.assertIsInstance(na_dropped_for_totals_and_subtotals, pd.core.frame.DataFrame)
        self.assertEqual(na_dropped_for_totals_and_subtotals.shape, (1728, 6))
        self.assertEqual(na_dropped_for_totals_and_subtotals["village"].isnull().sum(), 0)
        self.assertEqual(na_dropped_for_totals_and_subtotals["office"].isnull().sum(), 0)
    def test_165_str_strip_for_towns(self):
        str_stripped_for_towns = ex.str_strip_for_towns()
        self.assertIsInstance(str_stripped_for_towns, pd.core.frame.DataFrame)
        self.assertEqual(str_stripped_for_towns.shape, (1728, 6))
        self.assertTrue('松山區' in str_stripped_for_towns["town"].unique())
        self.assertTrue('北投區' in str_stripped_for_towns["town"].unique())
        self.assertEqual(str_stripped_for_towns["town"].nunique(), 12)
    def test_166_melt_candidate_columns(self):
        melted_candidate_columns = ex.melt_candidate_columns()
        self.assertIsInstance(melted_candidate_columns, pd.core.frame.DataFrame)
        self.assertEqual(melted_candidate_columns.shape, (5184, 5))
    def test_167_split_candidate_info(self):
        candidate_info = ex.split_candidate_info()
        self.assertIsInstance(candidate_info, pd.core.frame.DataFrame)
        self.assertEqual(candidate_info.shape, (5184, 6))
        self.assertEqual(candidate_info["number"].nunique(), 3)
        self.assertEqual(candidate_info["candidates"].nunique(), 3)
    def test_168_transform_column_data_types(self):
        column_data_types_transformed = ex.transform_column_data_types()
        self.assertIsInstance(column_data_types_transformed, pd.core.frame.DataFrame)
        self.assertEqual(column_data_types_transformed.shape, (5184, 6))
    def test_169_sum_votes_by_candidates(self):
        votes_by_candidates = ex.sum_votes_by_candidates()
        self.assertIsInstance(votes_by_candidates, pd.core.series.Series)
        self.assertEqual(votes_by_candidates.size, 3)
    def test_170_sum_votes_by_town_candidates(self):
        votes_by_town_candidates = ex.sum_votes_by_town_candidates()
        self.assertIsInstance(votes_by_town_candidates, pd.core.frame.DataFrame)
        self.assertEqual(votes_by_town_candidates.shape, (36, 4))
        self.assertEqual(votes_by_town_candidates["town"].nunique(), 12)
        self.assertEqual(votes_by_town_candidates["number"].nunique(), 3)
        self.assertEqual(votes_by_town_candidates["candidates"].nunique(), 3)

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestAdvancedDataframeManipulations, 17)