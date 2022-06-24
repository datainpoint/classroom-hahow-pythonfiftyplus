import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
import numpy as np
import pandas as pd

class TestWorkingWithText(unittest.TestCase):
    def test_131_import_movies_csv(self):
        self.assertEqual(ex.convert_character_to_int("A"), 65)
        self.assertEqual(ex.convert_character_to_int("M"), 77)
        self.assertEqual(ex.convert_character_to_int("N"), 78)
        self.assertEqual(ex.convert_character_to_int("Z"), 90)
        self.assertEqual(ex.convert_character_to_int("a"), 97)
        self.assertEqual(ex.convert_character_to_int("m"), 109)
        self.assertEqual(ex.convert_character_to_int("n"), 110)
        self.assertEqual(ex.convert_character_to_int("z"), 122)
    def test_132_convert_int_to_character(self):
        self.assertEqual(ex.convert_int_to_character(65), 'A')
        self.assertEqual(ex.convert_int_to_character(77), 'M')
        self.assertEqual(ex.convert_int_to_character(78), 'N')
        self.assertEqual(ex.convert_int_to_character(90), 'Z')
        self.assertEqual(ex.convert_int_to_character(97), 'a')
        self.assertEqual(ex.convert_int_to_character(109), 'm')
        self.assertEqual(ex.convert_int_to_character(110), 'n')
        self.assertEqual(ex.convert_int_to_character(122), 'z')
    def test_133_rot13_character(self):
        self.assertEqual(ex.rot13_character("A"), 'N')
        self.assertEqual(ex.rot13_character("M"), 'Z')
        self.assertEqual(ex.rot13_character("N"), 'A')
        self.assertEqual(ex.rot13_character("Z"), 'M')
        self.assertEqual(ex.rot13_character("a"), 'n')
        self.assertEqual(ex.rot13_character("m"), 'z')
        self.assertEqual(ex.rot13_character("n"), 'a')
        self.assertEqual(ex.rot13_character("z"), 'm')
        self.assertEqual(ex.rot13_character("!"), '!')
        self.assertEqual(ex.rot13_character("*"), '*')
    def test_134_rot13_sentence(self):
        self.assertEqual(ex.rot13_sentence("Gur Mra bs Clguba, ol Gvz Crgref"), 'The Zen of Python, by Tim Peters')
        self.assertEqual(ex.rot13_sentence("The Zen of Python, by Tim Peters"), 'Gur Mra bs Clguba, ol Gvz Crgref')
        self.assertEqual(ex.rot13_sentence("Abj vf orggre guna arire."), 'Now is better than never.')
        self.assertEqual(ex.rot13_sentence("Now is better than never."), 'Abj vf orggre guna arire.')
        self.assertEqual(ex.rot13_sentence("Nygubhtu arire vf bsgra orggre guna *evtug* abj."), 'Although never is often better than *right* now.')
        self.assertEqual(ex.rot13_sentence("Although never is often better than *right* now."), 'Nygubhtu arire vf bsgra orggre guna *evtug* abj.')
    def test_135_rot13_zen_of_python(self):
        zen_of_python = ex.rot13_zen_of_python()
        self.assertIsInstance(zen_of_python, list)
        self.assertTrue("Now is better than never." in zen_of_python)
        self.assertTrue("Although never is often better than *right* now." in zen_of_python)
    def test_136_replace_strs_asterisks(self):
        self.assertEqual(ex.replace_strs_asterisks("Taiwan*"), 'Taiwan')
        self.assertEqual(ex.replace_strs_asterisks("Crimea Republic*"), 'Crimea Republic')
        self.assertEqual(ex.replace_strs_asterisks("Crimea Republic*, Ukraine"), 'Crimea Republic, Ukraine')
        self.assertEqual(ex.replace_strs_asterisks("Sevastopol*"), 'Sevastopol')
        self.assertEqual(ex.replace_strs_asterisks("Sevastopol*, Ukraine*"), 'Sevastopol, Ukraine')
    def test_137_import_lookup_table(self):
        lookup_table = ex.import_lookup_table()
        self.assertIsInstance(lookup_table, pd.core.frame.DataFrame)
        self.assertEqual(lookup_table.shape, (4215, 12))
    def test_138_filter_taiwan_crimea_sevastopol(self):
        taiwan_crimea_sevastopol = ex.filter_taiwan_crimea_sevastopol()
        self.assertIsInstance(taiwan_crimea_sevastopol, pd.core.frame.DataFrame)
        self.assertEqual(taiwan_crimea_sevastopol.shape, (3, 12))
    def test_139_replace_series_asterisks(self):
        province_states = pd.Series([np.nan, "Crimea Republic*", "Sevastopol*"])
        pd.testing.assert_series_equal(ex.replace_series_asterisks(province_states), pd.Series([np.nan, "Crimea Republic", "Sevastopol"]))
        country_regions = pd.Series(["Taiwan*", "Ukraine", "Ukraine"])
        pd.testing.assert_series_equal(ex.replace_series_asterisks(country_regions), pd.Series(["Taiwan", "Ukraine", "Ukraine"]))
        combined_keys = pd.Series(["Taiwan*", "Crimea Republic*, Ukraine", "Sevastopol*, Ukraine"])
        pd.testing.assert_series_equal(ex.replace_series_asterisks(combined_keys), pd.Series(["Taiwan", "Crimea Republic, Ukraine", "Sevastopol, Ukraine"]))
    def test_140_export_lookup_table(self):
        ex.export_lookup_table()
        lookup_table = pd.read_csv("lookup_table.csv")
        self.assertIsInstance(lookup_table, pd.core.frame.DataFrame)
        self.assertEqual(lookup_table.shape, (4215, 12))
        condition = lookup_table["Combined_Key"].isin(["Taiwan", "Crimea Republic, Ukraine", "Sevastopol, Ukraine"])
        self.assertEqual(lookup_table[condition].shape, (3, 12))

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestWorkingWithText, 15)    