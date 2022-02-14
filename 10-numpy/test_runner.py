import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestNumpy, 9)