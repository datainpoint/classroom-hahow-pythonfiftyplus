import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
import numpy as np
import pandas as pd
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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestExploration, 18)