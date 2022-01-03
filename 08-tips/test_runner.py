import unittest
import json
import ipynb.fs.full.exercises as ex

class TestTips(unittest.TestCase):
    def test_059_double_args(self):
        self.assertEqual(ex.double_args(55), [110])
        self.assertEqual(ex.double_args(55, 66), [110, 132])
        self.assertEqual(ex.double_args(55, 66, "5566"), [110, 132, '55665566'])
    def test_060_double_odd_args(self):
        self.assertEqual(ex.double_odd_args(55), [110])
        self.assertEqual(ex.double_odd_args(55, 66), [110])
        self.assertEqual(ex.double_odd_args(55, 66, 77, 88), [110, 154])
    def test_061_is_double_digit_args(self):
        self.assertEqual(ex.is_double_digit_args(5), ['No'])
        self.assertEqual(ex.is_double_digit_args(5, 55), ['No', 'Yes'])
        self.assertEqual(ex.is_double_digit_args(5, 55, 5566), ['No', 'Yes', 'No'])
    def test_062_reverse_str_as_list(self):
        self.assertEqual(ex.reverse_str_as_list("Python"), ['n', 'o', 'h', 't', 'y', 'P'])
        self.assertEqual(ex.reverse_str_as_list("Anaconda"), ['a', 'd', 'n', 'o', 'c', 'a', 'n', 'A'])
    def test_063_reverse_str_swapcase_as_list(self):
        self.assertEqual(ex.reverse_str_swapcase_as_list("Python"), ['N', 'O', 'H', 'T', 'Y', 'p'])
        self.assertEqual(ex.reverse_str_swapcase_as_list("Anaconda"), ['A', 'D', 'N', 'O', 'C', 'A', 'N', 'a'])
    def test_064_idxmax(self):
        self.assertEqual(ex.idxmax([55, 66, 5566]), [2])
        self.assertEqual(ex.idxmax([5, 6, 5, 6]), [1, 3])
        self.assertEqual(ex.idxmax([5, 5, 6, 6]), [2, 3])
    def test_065_IndexMinMax(self):
        index_min_max = ex.IndexMinMax([55, 66, 5566])
        self.assertEqual(index_min_max.input_list, [55, 66, 5566])
        self.assertEqual(index_min_max.idxmax(), [2])
        self.assertEqual(index_min_max.idxmin(), [0])
        index_min_max = ex.IndexMinMax([5, 6, 5, 6])
        self.assertEqual(index_min_max.input_list, [5, 6, 5, 6])
        self.assertEqual(index_min_max.idxmax(), [1, 3])
        self.assertEqual(index_min_max.idxmin(), [0, 2])
        index_min_max = ex.IndexMinMax([55, 66, 5566])
        self.assertEqual(index_min_max.input_list, [5, 5, 6, 6])
        self.assertEqual(index_min_max.idxmax(), [2, 3])
        self.assertEqual(index_min_max.idxmin(), [0, 1])
    def test_066_calculate_bmis(self):
        bmis = ex.calculate_bmis([206, 211, 201], [113, 110, 104]) # LeBron James, Giannis Antetokounmpo, Luka Doncic
        self.assertGreater(bmis[0], 26)
        self.assertGreater(bmis[1], 24)
        self.assertGreater(bmis[2], 25)
        self.assertLess(bmis[0], 27)
        self.assertLess(bmis[1], 25)
        self.assertLess(bmis[2], 26)
    def test_067_double_args_with_map(self):
        self.assertIsInstance(ex.double_args_with_map(55), map)
        self.assertIsInstance(ex.double_args_with_map(55, 66), map)
        self.assertIsInstance(ex.double_args_with_map(55, 66, "5566"), map)
        self.assertEqual(list(ex.double_args_with_map(55)), [110])
        self.assertEqual(list(ex.double_args_with_map(55, 66)), [110, 132])
        self.assertEqual(tuple(ex.double_args_with_map(55, 66, "5566")), (110, 132, '55665566'))
    def test_068_filter_str_args_with_filter(self):
        self.assertIsInstance(ex.filter_str_args_with_filter("5566"), filter)
        self.assertIsInstance(ex.filter_str_args_with_filter("5566", 5566, False, True, "Luke Skywalker"), filter)
        self.assertEqual(list(ex.filter_str_args_with_filter("5566")), ['5566'])
        self.assertEqual(tuple(ex.filter_str_args_with_filter("5566", 5566, False, True, "Luke Skywalker")), ('5566', 'Luke Skywalker'))

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
    
run_suite(TestTips, 7)