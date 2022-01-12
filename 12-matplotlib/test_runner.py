import unittest
import json
import ipynb.fs.full.exercises as ex
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image

class TestMatplotlib(unittest.TestCase):
    def test_091_create_x_cosx_ndarray(self):
        x, cosx = ex.create_x_cosx_ndarray()
        self.assertIsInstance(x, np.ndarray)
        self.assertIsInstance(cosx, np.ndarray)
        self.assertEqual(x.size, 100)
        self.assertEqual(cosx.size, 100)
    def test_092_create_figure_and_axes_subplot(self):
        fig, ax = ex.create_figure_and_axes_subplot()
        self.assertIsInstance(fig, mpl.figure.Figure)
    def test_093_export_x_cosx_png(self):
        ex.export_x_cosx_png()
        im = Image.open("xcosx.png")
        self.assertEqual(im.format, 'PNG')
        im_test = Image.open("/home/jovyan/test-images/xcosx.png")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)
    def test_094_export_x_cosx_jpg(self):
        ex.export_x_cosx_jpg()
        im = Image.open("xcosx.jpg")
        self.assertEqual(im.format, 'JPEG')
        im_test = Image.open("/home/jovyan/test-images/xcosx.jpg")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)
    def test_095_create_x_tanx_ndarray(self):
        x, tanx = ex.create_x_tanx_ndarray()
        self.assertIsInstance(x, np.ndarray)
        self.assertIsInstance(tanx, np.ndarray)
        self.assertEqual(x.size, 10000)
        self.assertEqual(tanx.size, 10000)
    def test_096_create_adjusted_x_tanx_ndarray(self):
        adjusted_x, adjusted_tanx = ex.create_adjusted_x_tanx_ndarray()
        self.assertIsInstance(adjusted_x, np.ndarray)
        self.assertIsInstance(adjusted_tanx, np.ndarray)
        self.assertEqual(adjusted_x.size, 10000)
        self.assertEqual(adjusted_tanx.size, 10000)
        self.assertTrue(adjusted_x[0] > 0.5 * np.pi)
        self.assertTrue(adjusted_x[-1] < 1.5 * np.pi)
    def test_097_export_x_tanx_png(self):
        ex.export_x_tanx_png()
        im = Image.open("xtanx.png")
        self.assertEqual(im.format, 'PNG')
        im_test = Image.open("/home/jovyan/test-images/xtanx.png")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)
    def test_098_export_x_tanx_jpg(self):
        ex.export_x_tanx_jpg()
        im = Image.open("xtanx.jpg")
        self.assertEqual(im.format, 'JPEG')
        im_test = Image.open("/home/jovyan/test-images/xtanx.jpg")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)
    def test_099_export_x_tanx_png_with_title(self):
        ex.export_x_tanx_png_with_title()
        im = Image.open("xtanx_with_title.png")
        self.assertEqual(im.format, 'PNG')
        im_test = Image.open("/home/jovyan/test-images/xtanx_with_title.png")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)
    def test_100_export_x_tanx_png_final(self):
        ex.export_x_tanx_png_final()
        im = Image.open("xtanx_final.png")
        self.assertEqual(im.format, 'PNG')
        im_test = Image.open("/home/jovyan/test-images/xtanx_final.png")
        diff_sum = (np.array(im) - np.array(im_test)).sum()
        self.assertEqual(diff_sum, 0)

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
        elif chapter_index == 12:
            print("太令人佩服，你已經完成「Python 的 50+ 練習」的第三階段：Python 資料科學的基礎，距離完課只剩下最後一哩路！")
    elif chapter_percentage == 100 and chapter_index == 19:
        print("恭喜完課，你已經完成「{}」所有習題，能夠堅持到底完成所有的教學影片與練習題真是非常了不起！後面已經沒有練習題了，你現在是一位擅長寫程式處理資料的分析師！")
    elif chapter_percentage >= 50:
        print("你已經完成「{}」章節一半以上的練習，繼續加油！".format(chapter_name))
    
run_suite(TestMatplotlib, 11)