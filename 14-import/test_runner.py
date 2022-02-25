import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
import pandas as pd

class TestImport(unittest.TestCase):
    def test_111_import_txt_file(self):
        txt_file = ex.import_txt_file()
        self.assertIsInstance(txt_file, list)
        self.assertEqual(len(txt_file), 5)
    def test_112_import_json_file_as_list(self):
        json_file_as_list = ex.import_json_file_as_list()
        self.assertIsInstance(json_file_as_list, list)
        self.assertEqual(len(json_file_as_list), 34)
    def test_113_import_json_file_as_dataframe(self):
        json_file_as_dataframe = ex.import_json_file_as_dataframe()
        self.assertIsInstance(json_file_as_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(json_file_as_dataframe.shape, (34, 12))
    def test_114_import_csv_file(self):
        csv_file = ex.import_csv_file()
        self.assertIsInstance(csv_file, pd.core.frame.DataFrame)
        self.assertEqual(csv_file.shape, (250, 6))
    def test_115_import_xlsx_file_movies(self):
        xlsx_file_movies = ex.import_xlsx_file_movies()
        self.assertIsInstance(xlsx_file_movies, pd.core.frame.DataFrame)
        self.assertEqual(xlsx_file_movies.shape, (250, 6))
    def test_116_import_xlsx_file_casting(self):
        xlsx_file_casting = ex.import_xlsx_file_casting()
        self.assertIsInstance(xlsx_file_casting, pd.core.frame.DataFrame)
        self.assertEqual(xlsx_file_casting.shape, (3584, 3))
    def test_117_import_xlsx_file_actors(self):
        xlsx_file_actors = ex.import_xlsx_file_actors()
        self.assertIsInstance(xlsx_file_actors, pd.core.frame.DataFrame)
        self.assertEqual(xlsx_file_actors.shape, (3108, 2))
    def test_118_import_database_table_movies(self):
        database_table_movies = ex.import_database_table_movies()
        self.assertIsInstance(database_table_movies, pd.core.frame.DataFrame)
        self.assertEqual(database_table_movies.shape, (250, 6))
    def test_119_import_database_table_casting(self):
        database_table_casting = ex.import_database_table_casting()
        self.assertIsInstance(database_table_casting, pd.core.frame.DataFrame)
        self.assertEqual(database_table_casting.shape, (3584, 3))
    def test_120_import_database_table_actors(self):
        database_table_actors = ex.import_database_table_actors()
        self.assertIsInstance(database_table_actors, pd.core.frame.DataFrame)
        self.assertEqual(database_table_actors.shape, (3108, 2))

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestImport, 13)