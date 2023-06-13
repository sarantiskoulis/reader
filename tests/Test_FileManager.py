from FileManager import FileManager
import unittest
import os
import subprocess
from Config import Config
class TestFileManager(unittest.TestCase):
    def test_path_created(self):
        test_file = 'test.yaml'
        test_target = 'test.json'

        FileManager(test_file, test_target)
        file_exists = os.path.exists(test_target)
        self.assertTrue(file_exists)
        os.remove(test_target)

    def test_print_cmd(self):
        test_file = 'test.yaml'
        test_target = 'cmd'
        FileManager(test_file, test_target)
        output = subprocess.check_output('dir', shell=True)

        # Decode the output and print it
        decoded_output = output.decode('utf-8')
        true_data = Config(test_file).read_yaml()
        self.assertEquals(decoded_output, true_data)




