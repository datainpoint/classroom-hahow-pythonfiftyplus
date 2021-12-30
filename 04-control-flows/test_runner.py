import unittest
import json
import ipynb.fs.full.exercises as ex

class TestControlFlows(unittest.TestCase):
    def test_026_find_bmi_category(self):
        self.assertEqual(ex.find_bmi_category(32.90), 'Obese')
        self.assertEqual(ex.find_bmi_category(26.63), 'Overweight')
        self.assertEqual(ex.find_bmi_category(24.83), 'Normal weight')
        self.assertEqual(ex.find_bmi_category(17.58), 'Underweight')
    def test_027_check_data_type(self):
        self.assertEqual(ex.check_data_type(0), 'int')
        self.assertEqual(ex.check_data_type(1.0), 'float')
        self.assertEqual(ex.check_data_type(False), 'bool')
        self.assertEqual(ex.check_data_type(True), 'bool')
        self.assertEqual(ex.check_data_type('5566'), 'str')
        self.assertEqual(ex.check_data_type(None), 'NoneType')
    def test_028_check_data_structure_type(self):
        self.assertEqual(ex.check_data_structure_type([5, 5, 6, 6]), 'list')
        self.assertEqual(ex.check_data_structure_type((5, 5, 6, 6)), 'tuple')
        self.assertEqual(ex.check_data_structure_type({5, 6}), 'set')
        self.assertEqual(ex.check_data_structure_type({'title': 'The Shawshank Redemption', 'year': 1994}), 'dict')
    def test_029_retrieve_middle_elements(self):
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5]), 3)
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7]), (3, 5))
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7, 11, 13]), (5, 7))
        self.assertEqual(ex.retrieve_middle_elements([2, 3, 5, 7, 11, 13, 17]), 7)
    def test_030_calculate_median(self):
        self.assertEqual(ex.calculate_median([9, 8, 3, 6, 7, 3, 1]), 6)
        self.assertAlmostEqual(ex.calculate_median([1, 3, 2, 5, 4, 9, 8, 6]), 4.5)
        self.assertEqual(ex.calculate_median([5, 6, 7]), 6)
        self.assertAlmostEqual(ex.calculate_median([3, 4, 5, 6]), 4.5)
    def test_031_calculate_mean(self):
        self.assertAlmostEqual(ex.calculate_mean([5, 5, 6, 6]), 5.5)
        self.assertAlmostEqual(ex.calculate_mean([5, 3, 4]), 4.0)
        self.assertAlmostEqual(ex.calculate_mean([4, 3]), 3.5)
        self.assertAlmostEqual(ex.calculate_mean([4]), 4.0)
    def test_032_create_first_100_fizz_buzz(self):
        first_100_fizz_buzz = ex.create_first_100_fizz_buzz()
        self.assertEqual(len(first_100_fizz_buzz), 100)
        self.assertEqual(first_100_fizz_buzz[0], 1)
        self.assertEqual(first_100_fizz_buzz[1], 2)
        self.assertEqual(first_100_fizz_buzz[2], 'Fizz')
        self.assertEqual(first_100_fizz_buzz[3], 4)
        self.assertEqual(first_100_fizz_buzz[4], 'Buzz')
        self.assertEqual(first_100_fizz_buzz[13], 14)
        self.assertEqual(first_100_fizz_buzz[14], 'Fizz Buzz')
        self.assertEqual(first_100_fizz_buzz[-1], 'Buzz')
        self.assertEqual(first_100_fizz_buzz[-2], 'Fizz')
        self.assertEqual(first_100_fizz_buzz[-11], 'Fizz Buzz')
    def test_033_create_fizz_buzz_slice(self):
        self.assertEqual(ex.create_fizz_buzz_slice(1, 5), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(ex.create_fizz_buzz_slice(11, 15), [11, 'Fizz', 13, 14, 'Fizz Buzz'])
        self.assertEqual(ex.create_fizz_buzz_slice(25, 30), ['Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz'])
    def test_034_collect_divisors(self):
        self.assertEqual(ex.collect_divisors(2), [1, 2])
        self.assertEqual(ex.collect_divisors(3), [1, 3])
        self.assertEqual(ex.collect_divisors(4), [1, 2, 4])
        self.assertEqual(ex.collect_divisors(8), [1, 2, 4, 8])
        self.assertEqual(ex.collect_divisors(9), [1, 3, 9])
    def test_035_safe_divide(self):
        self.assertAlmostEqual(ex.safe_divide(10, 2), 5.0)
        self.assertAlmostEqual(ex.safe_divide(0, 2), 0.0)
        self.assertAlmostEqual(ex.safe_divide(10, 0), 'division by zero')

def run_suite(test_class, chapter_index=3):
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
    
run_suite(TestControlFlows)