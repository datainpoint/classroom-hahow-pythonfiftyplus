import unittest
import json
import os
import ipynb.fs.full.exercises as ex
import numpy as np

class TestNumpy(unittest.TestCase):
    def test_072_create_first_ten_odds_array(self):
        first_ten_odds_array = ex.create_first_ten_odds_array()
        np.testing.assert_array_equal(first_ten_odds_array,
                                     np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
        self.assertIsInstance(first_ten_odds_array, np.ndarray)
        self.assertEqual(first_ten_odds_array.shape, (10,))
    def test_073_create_a_square_matrix(self):
        a_square_matrix = ex.create_a_square_matrix(2, 5566)
        self.assertEqual(a_square_matrix.shape, (2, 2))
        self.assertEqual(a_square_matrix.sum(), 5566 * 2**2)
        a_square_matrix = ex.create_a_square_matrix(3, 55)
        self.assertEqual(a_square_matrix.shape, (3, 3))
        self.assertEqual(a_square_matrix.sum(), 55 * 3**2)
        a_square_matrix = ex.create_a_square_matrix(4, 66)
        self.assertEqual(a_square_matrix.shape, (4, 4))
        self.assertEqual(a_square_matrix.sum(), 66 * 4**2)
    def test_074_create_a_diagonal_matrix(self):
        a_diagonal_matrix = ex.create_a_diagonal_matrix(2, 5566)
        self.assertEqual(a_diagonal_matrix.shape, (2, 2))
        self.assertEqual(a_diagonal_matrix.sum(), 5566 * 2)
        a_diagonal_matrix = ex.create_a_diagonal_matrix(3, 55)
        self.assertEqual(a_diagonal_matrix.shape, (3, 3))
        self.assertEqual(a_diagonal_matrix.sum(), 55 * 3)
        a_diagonal_matrix = ex.create_a_diagonal_matrix(4, 66)
        self.assertEqual(a_diagonal_matrix.shape, (4, 4))
        self.assertEqual(a_diagonal_matrix.sum(), 66 * 4)
    def test_075_create_one_nine_array(self):
        nine_nine_array = ex.create_nine_nine_array()
        self.assertEqual(nine_nine_array.shape, (9, 9))
        self.assertEqual(nine_nine_array[7, 7], 64)
        self.assertEqual(nine_nine_array[7, 8], 72)
        self.assertEqual(nine_nine_array[8, 7], 72)
        self.assertEqual(nine_nine_array[8, 8], 81)  
    def test_076_filter_evens(self):
        np.testing.assert_equal(ex.filter_evens(np.array([5, 5, 6, 6])), np.array([6, 6]))
        np.testing.assert_equal(ex.filter_evens(np.array([1, 2, 3, 4])), np.array([2, 4]))
        np.testing.assert_equal(ex.filter_evens(np.array([0, 1, 2, 3])), np.array([0, 2]))

def run_suite(test_class, chapter_index=9):
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
    
run_suite(TestNumpy)