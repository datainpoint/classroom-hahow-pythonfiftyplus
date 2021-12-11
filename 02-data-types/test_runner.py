import unittest
import json
import ipynb.fs.full.suggested_answers as ex

class TestDataTypes(unittest.TestCase):
    def test_006_convert_km_to_mile(self):
        self.assertTrue(ex.convert_km_to_mile(42.195) > 26)
        self.assertTrue(ex.convert_km_to_mile(42.195) < 27)
        self.assertTrue(ex.convert_km_to_mile(21.095) > 13)
        self.assertTrue(ex.convert_km_to_mile(21.095) < 14)
    def test_007_convert_fahrenheit_to_celsius(self):
        self.assertTrue(ex.convert_fahrenheit_to_celsius(212) >= 100.0)
        self.assertTrue(ex.convert_fahrenheit_to_celsius(32) >= 0.0)
    def test_008_calculate_bmi(self):
        self.assertTrue(ex.calculate_bmi(206, 113) >= 26)
        self.assertTrue(ex.calculate_bmi(206, 113) < 27)
        self.assertTrue(ex.calculate_bmi(211, 110) >= 24)
        self.assertTrue(ex.calculate_bmi(211, 110) < 25)
        self.assertTrue(ex.calculate_bmi(201, 104) >= 25)
        self.assertTrue(ex.calculate_bmi(201, 104) < 26)
    def test_009_show_integer_with_commas(self):
        self.assertEqual(ex.show_integer_with_commas(1000), "1,000.00")
        self.assertEqual(ex.show_integer_with_commas(10000), "10,000.00")
        self.assertEqual(ex.show_integer_with_commas(100000), "100,000.00")
        self.assertEqual(ex.show_integer_with_commas(1000000), "1,000,000.00")
        self.assertEqual(ex.show_integer_with_commas(10000000), "10,000,000.00")
    def test_010_convert_one_usd_to_another_currency(self):
        self.assertEqual(ex.convert_one_usd_to_another_currency("NTD", 28), "1.00 USD = 28.00 NTD")
        self.assertEqual(ex.convert_one_usd_to_another_currency("KRW", 1196), "1.00 USD = 1,196.00 KRW")
        self.assertEqual(ex.convert_one_usd_to_another_currency("JPY", 112), "1.00 USD = 112.00 JPY")
    def test_011_is_positive(self):
        self.assertFalse(ex.is_positive(-2))
        self.assertFalse(ex.is_positive(-1))
        self.assertTrue(ex.is_positive(0))
        self.assertTrue(ex.is_positive(1))
        self.assertTrue(ex.is_positive(2))
    def test_012_has_two_digits(self):
        self.assertFalse(ex.has_two_digits(8))
        self.assertFalse(ex.has_two_digits(9))
        self.assertFalse(ex.has_two_digits(100))
        self.assertTrue(ex.has_two_digits(10))
        self.assertTrue(ex.has_two_digits(99))
    def test_013_is_odd(self):
        self.assertFalse(ex.is_odd(0))
        self.assertFalse(ex.is_odd(2))
        self.assertFalse(ex.is_odd(4))
        self.assertTrue(ex.is_odd(1))
        self.assertTrue(ex.is_odd(3))
    def test_014_is_a_divisor(self):
        self.assertFalse(ex.is_a_divisor(2, 3))
        self.assertFalse(ex.is_a_divisor(3, 4))
        self.assertTrue(ex.is_a_divisor(1, 3))
        self.assertTrue(ex.is_a_divisor(3, 3))
        self.assertTrue(ex.is_a_divisor(1, 4))
        self.assertTrue(ex.is_a_divisor(2, 4))
        self.assertTrue(ex.is_a_divisor(4, 4))
    def test_015_contain_vowels(self):
        self.assertTrue(ex.contain_vowels("python"))
        self.assertTrue(ex.contain_vowels("anaconda"))
        self.assertTrue(ex.contain_vowels("reticulate"))
        self.assertFalse(ex.contain_vowels("pythn"))
        self.assertFalse(ex.contain_vowels("ncnd"))
        self.assertFalse(ex.contain_vowels("rtclt"))
        
def run_suite(test_class, chapter_index=1):
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
        elif chapter_index == 13:
            print("太令人佩服，你已經完成「Python 的 50+ 練習」的第三階段：Python 資料科學的基礎，距離完課只剩下最後一哩路！")
    elif chapter_percentage == 100 and chapter_index == 19:
        print("恭喜完課，你已經完成「{}」所有習題，能夠堅持到底完成所有的教學影片與練習題真是非常了不起！後面已經沒有練習題了，你現在是一位擅長寫程式處理資料的分析師！")
    elif chapter_percentage >= 50:
        print("你已經完成「{}」章節一半以上的練習，繼續加油！".format(chapter_name))
    
run_suite(TestDataTypes)