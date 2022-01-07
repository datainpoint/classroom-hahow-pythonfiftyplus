import unittest
import json
import ipynb.fs.full.exercises as ex
import numpy as np

class TestNumpy(unittest.TestCase):
    def test_071_create_first_ten_primes_array(self):
        first_ten_primes_array = ex.create_first_ten_primes_array()
        np.testing.assert_equal(first_ten_primes_array, np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29]))
        self.assertIsInstance(first_ten_primes_array, np.ndarray)
        self.assertEqual(first_ten_primes_array.shape, (10,))
    def test_072_create_first_ten_evens_array(self):
        first_ten_evens_array = ex.create_first_ten_evens_array()
        np.testing.assert_array_equal(first_ten_evens_array,
                                     np.array([0,  2,  4,  6,  8, 10, 12, 14, 16, 18]))
        self.assertIsInstance(first_ten_evens_array, np.ndarray)
        self.assertEqual(first_ten_evens_array.shape, (10,))
    def test_073_SummarizeNdarray(self):
        ndarray_summary = ex.SummarizeNdarray(np.arange(10))
        self.assertEqual(ndarray_summary.get_ndim(), 1)
        self.assertEqual(ndarray_summary.get_shape(), (10,))
        self.assertEqual(ndarray_summary.get_size(), 10)
        ndarray_summary = ex.SummarizeNdarray(np.array([[5, 5], [6, 6], [55, 66]]))
        self.assertEqual(ndarray_summary.get_ndim(), 2)
        self.assertEqual(ndarray_summary.get_shape(), (3, 2))
        self.assertEqual(ndarray_summary.get_size(), 6)
    def test_074_create_a_square_matrix(self):
        a_square_matrix = ex.create_a_square_matrix(2, 5566)
        self.assertEqual(a_square_matrix.shape, (2, 2))
        self.assertEqual(a_square_matrix.sum(), 5566 * 2**2)
        a_square_matrix = ex.create_a_square_matrix(3, 55)
        self.assertEqual(a_square_matrix.shape, (3, 3))
        self.assertEqual(a_square_matrix.sum(), 55 * 3**2)
        a_square_matrix = ex.create_a_square_matrix(4, 66)
        self.assertEqual(a_square_matrix.shape, (4, 4))
        self.assertEqual(a_square_matrix.sum(), 66 * 4**2)
    def test_075_convert_kilometers_to_miles(self):
        result_array = ex.convert_kilometers_to_miles(np.array([1.6, 3, 5, 10, 21.095, 42.195]))
        self.assertTrue(result_array[0] >= 0.9)
        self.assertTrue(result_array[1] >= 1.8)
        self.assertTrue(result_array[2] >= 3)
        self.assertTrue(result_array[3] >= 6)
        self.assertTrue(result_array[4] >= 13)
        self.assertTrue(result_array[5] >= 26)
    def test_076_create_a_diagonal_matrix(self):
        a_diagonal_matrix = ex.create_a_diagonal_matrix(2, 5566)
        self.assertEqual(a_diagonal_matrix.shape, (2, 2))
        self.assertEqual(a_diagonal_matrix.sum(), 5566 * 2)
        a_diagonal_matrix = ex.create_a_diagonal_matrix(3, 55)
        self.assertEqual(a_diagonal_matrix.shape, (3, 3))
        self.assertEqual(a_diagonal_matrix.sum(), 55 * 3)
        a_diagonal_matrix = ex.create_a_diagonal_matrix(4, 66)
        self.assertEqual(a_diagonal_matrix.shape, (4, 4))
        self.assertEqual(a_diagonal_matrix.sum(), 66 * 4)
    def test_077_vectorized_is_prime(self):
        np.testing.assert_equal(ex.vectorized_is_prime(np.arange(10)),
         np.array([False, False,  True,  True, False,  True, False,  True, False, False]))
        np.testing.assert_equal(ex.vectorized_is_prime(np.arange(11, 20)),
         np.array([ True, False,  True, False, False, False,  True, False,  True]))
        np.testing.assert_equal(ex.vectorized_is_prime(np.arange(21, 30)),
         np.array([False, False,  True, False, False, False, False, False,  True]))
    def test_078_filter_primes(self):
        np.testing.assert_equal(ex.filter_primes(np.arange(10)), np.array([2, 3, 5, 7]))
        np.testing.assert_equal(ex.filter_primes(np.arange(11, 20)), np.array([11, 13, 17, 19]))
        np.testing.assert_equal(ex.filter_primes(np.arange(21, 30)), np.array([23, 29]))
    def test_079_add_intercept(self):
        A = np.array([5, 5, 6, 6]).reshape(-1, 1)
        np.testing.assert_equal(ex.add_intercepts(A),
        np.array([[1, 5],
                  [1, 5],
                  [1, 6],
                  [1, 6]]))
        B = np.zeros((5, 2), dtype=int)
        np.testing.assert_equal(ex.add_intercepts(B),
        np.array([[1, 0, 0],
                  [1, 0, 0],
                  [1, 0, 0],
                  [1, 0, 0],
                  [1, 0, 0]]))
    def test_080_split_train_test(self):
        A = np.ones((10, 2))
        A_train, A_test = ex.split_train_test(A, test_size=0.3)
        self.assertEqual(A_train.shape, (7, 2))
        self.assertEqual(A_test.shape, (3, 2))
        B = np.ones((10, 3))
        B_train, B_test = ex.split_train_test(B, test_size=0.4)
        self.assertEqual(B_train.shape, (6, 3))
        self.assertEqual(B_test.shape, (4, 3))

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
    
run_suite(TestNumpy, 9)