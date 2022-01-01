import unittest
import json
import ipynb.fs.full.exercises as ex

class TestClasses(unittest.TestCase):
    def test_046_reverse_str(self):
        self.assertEqual(ex.reverse_str("eye"), 'eye')
        self.assertEqual(ex.reverse_str("dad"), 'dad')
        self.assertEqual(ex.reverse_str("dye"), 'eyd')
        self.assertEqual(ex.reverse_str("mad"), 'dam')
    def test_047_is_palindrome(self):
        self.assertTrue(ex.is_palindrome("eye"))
        self.assertTrue(ex.is_palindrome("dad"))
        self.assertFalse(ex.is_palindrome("dye"))
        self.assertFalse(ex.is_palindrome("mad"))
    def test_048_PalindromeMethods(self):
        palindrome_methods = ex.PalindromeMethods()
        self.assertEqual(palindrome_methods.reverse_str("eye"), 'eye')
        self.assertEqual(palindrome_methods.reverse_str("dad"), 'dad')
        self.assertEqual(palindrome_methods.reverse_str("dye"), 'eyd')
        self.assertEqual(palindrome_methods.reverse_str("mad"), 'dam')
        self.assertTrue(palindrome_methods.is_palindrome("eye"))
        self.assertTrue(palindrome_methods.is_palindrome("dad"))
        self.assertFalse(palindrome_methods.is_palindrome("dye"))
        self.assertFalse(palindrome_methods.is_palindrome("mad"))
    def test_049_Palindrome(self):
        palindrome = ex.Palindrome("eye")
        self.assertEqual(palindrome.original_str, 'eye')
        self.assertEqual(palindrome.reversed_str, 'eye')
        self.assertTrue(palindrome.is_palindrome())
        palindrome = ex.Palindrome("dye")
        self.assertEqual(palindrome.original_str, 'dye')
        self.assertEqual(palindrome.reversed_str, 'eyd')
        self.assertFalse(palindrome.is_palindrome())
    def test_050_collect_divisors_as_set(self):
        self.assertEqual(ex.collect_divisors_as_set(3), {1, 3})
        self.assertEqual(ex.collect_divisors_as_set(6), {1, 2, 3, 6})
        self.assertEqual(ex.collect_divisors_as_set(4), {1, 2, 4})
        self.assertEqual(ex.collect_divisors_as_set(8), {1, 2, 4, 8})
    def test_051_find_common_divisors(self):
        self.assertEqual(ex.find_common_divisors(3, 6), {1, 3})
        self.assertEqual(ex.find_common_divisors(4, 8), {1, 2, 4})
    def test_052_find_the_max_common_divisor(self):
        self.assertEqual(ex.find_the_max_common_divisor(3, 6), 3)
        self.assertEqual(ex.find_the_max_common_divisor(4, 8), 4)
        self.assertEqual(ex.find_the_max_common_divisor(6, 8), 2)
    def test_053_CommonDivisorMethods(self):
        common_divisor_methods = ex.CommonDivisorMethods()
        self.assertEqual(common_divisor_methods.collect_divisors_as_set(3), {1, 3})
        self.assertEqual(common_divisor_methods.collect_divisors_as_set(6), {1, 2, 3, 6})
        self.assertEqual(common_divisor_methods.find_common_divisors(3, 6), {1, 3})
        self.assertEqual(common_divisor_methods.find_the_max_common_divisor(6, 8), 2)
    def test_054_CommonDivisors(self):
        common_divisors = ex.CommonDivisors(3, 6)
        self.assertEqual(common_divisors.x_divisors, {1, 3})
        self.assertEqual(common_divisors.y_divisors, {1, 2, 3, 6})
        self.assertEqual(common_divisors.find_common_divisors(), {1, 3})
        self.assertEqual(common_divisors.find_the_max_common_divisor(), 3)
        common_divisors = ex.CommonDivisors(4, 8)
        self.assertEqual(common_divisors.x_divisors, {1, 2, 4})
        self.assertEqual(common_divisors.y_divisors, {1, 2, 4, 8})
        self.assertEqual(common_divisors.find_common_divisors(), {1, 2, 4})
        self.assertEqual(common_divisors.find_the_max_common_divisor(), 4)
    def test_055_PrimeJudger(self):
        prime_judger = ex.PrimeJudger(1)
        self.assertEqual(prime_judger.x, 1)
        self.assertEqual(prime_judger.count_number_of_divisors(), 1)
        self.assertFalse(prime_judger.is_prime())
        prime_judger = ex.PrimeJudger(2)
        self.assertEqual(prime_judger.x, 2)
        self.assertEqual(prime_judger.count_number_of_divisors(), 2)
        self.assertTrue(prime_judger.is_prime())
        prime_judger = ex.PrimeJudger(4)
        self.assertEqual(prime_judger.x, 4)
        self.assertEqual(prime_judger.count_number_of_divisors(), 3)
        self.assertFalse(prime_judger.is_prime())

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
        elif chapter_index == 13:
            print("太令人佩服，你已經完成「Python 的 50+ 練習」的第三階段：Python 資料科學的基礎，距離完課只剩下最後一哩路！")
    elif chapter_percentage == 100 and chapter_index == 19:
        print("恭喜完課，你已經完成「{}」所有習題，能夠堅持到底完成所有的教學影片與練習題真是非常了不起！後面已經沒有練習題了，你現在是一位擅長寫程式處理資料的分析師！")
    elif chapter_percentage >= 50:
        print("你已經完成「{}」章節一半以上的練習，繼續加油！".format(chapter_name))
    
run_suite(TestClasses, 5)