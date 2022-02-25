import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
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
        self.assertEqual(ex.get_a_second_before_datetime("2022-01-01 00:00:01"), datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(ex.get_a_second_before_datetime("2022-01-01 00:00:00"), datetime(2021, 12, 31, 23, 59, 59))
    def test_146_show_a_non_iso8601_date(self):
        self.assertEqual(ex.show_a_non_iso8601_date(2021, 12, 31), 'Fri Dec 31')
        self.assertEqual(ex.show_a_non_iso8601_date(2022, 1, 1), 'Sat Jan 01')
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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestWorkingWithDateTime, 16)