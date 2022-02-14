import unittest
import ipynb.fs.full.exercises as ex
import importlib.util

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
        index_min_max = ex.IndexMinMax([5, 5, 6, 6])
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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestTips, 7)