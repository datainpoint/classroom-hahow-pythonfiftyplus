import unittest
import json
import ipynb.fs.full.suggested_answers as ex

class TestClasses(unittest.TestCase):
    def test_046_palindrome(self):
        eye = ex.Palindrome('eye')
        dye = ex.Palindrome('dye')
        anna = ex.Palindrome('anna')
        emma = ex.Palindrome('emma')
        self.assertEqual(eye.original_text, 'eye')
        self.assertEqual(eye.reversed_text, 'eye')
        self.assertTrue(eye.is_palindrome())
        self.assertEqual(dye.original_text, 'dye')
        self.assertEqual(dye.reversed_text, 'eyd')
        self.assertFalse(dye.is_palindrome())
        self.assertTrue(anna.is_palindrome())
        self.assertFalse(emma.is_palindrome())
    def test_047_common_divisors(self):
        cd = ex.CommonDivisors(3, 6)
        self.assertEqual(cd.x_divisors, {1, 3})
        self.assertEqual(cd.y_divisors, {1, 2, 3, 6})
        self.assertEqual(cd.get_common_divisors(), {1, 3})
        cd = ex.CommonDivisors(4, 8)
        self.assertEqual(cd.x_divisors, {1, 2, 4})
        self.assertEqual(cd.y_divisors, {1, 2, 4, 8})
        self.assertEqual(cd.get_common_divisors(), {1, 2, 4})
        cd = ex.CommonDivisors(4, 10)
        self.assertEqual(cd.x_divisors, {1, 2, 4})
        self.assertEqual(cd.y_divisors, {1, 2, 5, 10})
        self.assertEqual(cd.get_common_divisors(), {1, 2})
    def test_048_prime_judger(self):
        one = ex.PrimeJudger(1)
        two = ex.PrimeJudger(2)
        three = ex.PrimeJudger(3)
        four = ex.PrimeJudger(4)
        five = ex.PrimeJudger(5)
        self.assertEqual(one.get_divisors(), {1})
        self.assertFalse(one.is_prime())
        self.assertEqual(two.get_divisors(), {1, 2})
        self.assertTrue(two.is_prime())
        self.assertEqual(four.get_divisors(), {1, 2, 4})
        self.assertFalse(one.is_prime())
        self.assertTrue(three.is_prime())
        self.assertTrue(five.is_prime())
    def test_049_RangePrime(self):
        range_prime = ex.RangePrime(1, 5)   
        self.assertEqual(range_prime.range_list, [1, 2, 3, 4, 5])
        self.assertEqual(range_prime.filter_primes(), [2, 3, 5])
        range_prime = ex.RangePrime(6, 15)
        self.assertEqual(range_prime.range_list, [6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(range_prime.filter_primes(), [7, 11, 13])
        range_prime = ex.RangePrime(16, 20)
        self.assertEqual(range_prime.range_list, [16, 17, 18, 19, 20])
        self.assertEqual(range_prime.filter_primes(), [17, 19])
    def test_050_MinMaxFinder(self):
        min_max_finder = ex.MinMaxFinder([2, 3, 5, 7, 11])
        self.assertEqual(min_max_finder.get_min(), 2)
        self.assertEqual(min_max_finder.get_max(), 11)
        self.assertEqual(min_max_finder.get_idxmin(), [0])
        self.assertEqual(min_max_finder.get_idxmax(), [4])
        min_max_finder = ex.MinMaxFinder([2, 2, 3, 5, 7, 11, 11])
        self.assertEqual(min_max_finder.get_min(), 2)
        self.assertEqual(min_max_finder.get_max(), 11)
        self.assertEqual(min_max_finder.get_idxmin(), [0, 1])
        self.assertEqual(min_max_finder.get_idxmax(), [5, 6])
        min_max_finder = ex.MinMaxFinder([13, 13, 5, 5, 5])
        self.assertEqual(min_max_finder.get_min(), 5)
        self.assertEqual(min_max_finder.get_max(), 13)
        self.assertEqual(min_max_finder.get_idxmin(), [2, 3, 4])
        self.assertEqual(min_max_finder.get_idxmax(), [0, 1])

def run_suite(test_class, chapter_index=5):
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
    print("整體課程的累計完成率為 ... {:.2f}% ({}/{})".format(overall_percentage, number_of_completed_questions, number_of_total_questions))
    if chapter_percentage < 100 and chapter_percentage >= 50:
        print("你已經完成了一半以上的練習，繼續加油！")
    elif chapter_percentage == 100:
        print("表現得很好，你已經完成「{}」所有習題，我們繼續往下個章節：「{}」前進！".format(exercise_index[chapter_index]["chapter_name"], exercise_index[chapter_index + 1]["chapter_name"]))
    
run_suite(TestClasses)