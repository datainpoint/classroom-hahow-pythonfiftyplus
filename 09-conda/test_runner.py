import unittest
import importlib.util
import subprocess

class TestConda(unittest.TestCase):
    def test_069_python3712(self):
        cmd = '. /srv/conda/etc/profile.d/conda.sh && conda activate python3712 && python --version'  
        result = subprocess.getoutput(cmd)
        self.assertEqual(result, "Python 3.7.12")
    def test_070_python3615(self):
        cmd = '. /srv/conda/etc/profile.d/conda.sh && conda activate python3615 && python --version'  
        result = subprocess.getoutput(cmd)
        self.assertEqual(result, "Python 3.6.15")

spec = importlib.util.spec_from_file_location("testfunction.py", "/home/jovyan/testfunction.py")
test_function = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_function)
test_function.run_suite(TestConda, 8)