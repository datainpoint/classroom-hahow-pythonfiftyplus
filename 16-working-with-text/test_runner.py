import unittest
import json
import ipynb.fs.full.exercises as ex
import re
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
        combined_keys = pd.Series(["Taiwan*", "Crimea Republic*, Ukraine", "Sevastopol*, Ukrain"])
        pd.testing.assert_series_equal(ex.replace_series_asterisks(combined_keys), pd.Series(["Taiwan", "Crimea Republic, Ukraine", "Sevastopol, Ukrain"]))
    def test_140_import_lookup_table(self):
        ex.export_lookup_table()
        lookup_table = pd.read_csv("lookup_table.csv")
        self.assertIsInstance(lookup_table, pd.core.frame.DataFrame)
        self.assertEqual(lookup_table.shape, (4215, 12))
        condition = lookup_table["Combined_Key"].isin(["Taiwan", "Crimea Republic, Ukraine", "Sevastopol, Ukraine"])
        self.assertEqual(lookup_table[condition].shape, (3, 12))

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
    
run_suite(TestWorkingWithText, 15)