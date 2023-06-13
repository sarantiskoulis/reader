
from FileManager import FileManager
import unittest
import os
import subprocess

from unittest.mock import patch, call
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
        #parent_dir = os.path.dirname(os.getcwd())

        result = subprocess.run(['python',
                                 '../main.py',
                                 '--yaml' ,'test.yaml',
                                 '--writeto', 'cmd'],
                                stdout=subprocess.PIPE)

        self.assertEqual(result.stdout.decode('utf-8'),'simulation:\n  people: 1010\n')




