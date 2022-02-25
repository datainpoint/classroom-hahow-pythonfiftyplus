import unittest
import ipynb.fs.full.exercises as ex
import importlib.util
import numpy as np
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

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestMatplotlib, 11)