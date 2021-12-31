import unittest
import json
import ipynb.fs.full.exercises as ex

class TestFunctions(unittest.TestCase):
    def test_036_calculate_circle_area(self):
        self.assertGreater(ex.calculate_circle_area(5), 78)
        self.assertGreater(ex.calculate_circle_area(6), 113)
        self.assertGreater(ex.calculate_circle_area(7), 153)
    def test_037_calculate_cylinder_volume(self):
        self.assertGreater(ex.calculate_cylinder_volume(5, 6), 470)
        self.assertGreater(ex.calculate_cylinder_volume(6, 5), 565)
        self.assertGreater(ex.calculate_cylinder_volume(7, 8), 1230)
    def test_038_count_number_of_divisors(self):
        self.assertEqual(ex.count_number_of_divisors(1), 1)
        self.assertEqual(ex.count_number_of_divisors(2), 2)
        self.assertEqual(ex.count_number_of_divisors(3), 2)
        self.assertEqual(ex.count_number_of_divisors(4), 3)
        self.assertEqual(ex.count_number_of_divisors(5), 2)
        self.assertEqual(ex.count_number_of_divisors(6), 4)
    def test_039_is_prime(self):
        self.assertFalse(ex.is_prime(1))
        self.assertTrue(ex.is_prime(2))
        self.assertTrue(ex.is_prime(3))
        self.assertFalse(ex.is_prime(4))
        self.assertTrue(ex.is_prime(5))
    def test_040_is_args_prime(self):
        self.assertEqual(ex.is_args_prime(1, 2, 3), [False, True, True])
        self.assertEqual(ex.is_args_prime(4, 5, 6), [False, True, False])
        self.assertEqual(ex.is_args_prime(7, 11, 13, 17, 19), [True, True, True, True, True])
        self.assertEqual(ex.is_args_prime(20, 21, 22, 24, 25, 26, 27), [False, False, False, False, False, False, False])
    def test_041_find_primes_in_range(self):
        self.assertEqual(ex.find_primes_in_range(1, 5), [2, 3, 5])
        self.assertEqual(ex.find_primes_in_range(6, 10), [7])
        self.assertEqual(ex.find_primes_in_range(11, 15), [11, 13])
    def test_042_find_primes_below_100(self):
        primes_below_100 = ex.find_primes_below_100()
        self.assertEqual(len(primes_below_100), 25)
        self.assertEqual(len(primes_below_100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    def test_043_find_the_first_n_primes(self):
        self.assertEqual(ex.find_the_first_n_primes(5), [2, 3, 5, 7, 11])
        self.assertEqual(ex.find_the_first_n_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(ex.find_the_first_n_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])
    def test_044_square_negatives_from_args(self):
        self.assertEqual(ex.square_negatives_from_args(-3, -2, -1, 0, 1, 2, 3), [9, 4, 1])
        self.assertEqual(ex.square_negatives_from_args(-3, 0, 1, 2, 3, -2, -1), [9, 4, 1])
        self.assertEqual(ex.square_negatives_from_args(0, 1, 2, 3, -1, -2, -3), [1, 4, 9])
    def test_045_uppercase_keys_values_from_kwargs(self):
        self.assertEqual(ex.uppercase_keys_values_from_kwargs(tw="twn"), {'TW': 'TWN'})
        self.assertEqual(ex.uppercase_keys_values_from_kwargs(tw="twn", jp="jpn"), {'TW': 'TWN', 'JP': 'JPN'})
        self.assertEqual(ex.uppercase_keys_values_from_kwargs(tw="twn", jp="jpn", lt="ltu"), {'TW': 'TWN', 'JP': 'JPN', 'LT': 'LTU'})

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
    
run_suite(TestFunctions, 4)