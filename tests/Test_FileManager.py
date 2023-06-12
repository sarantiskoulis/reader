from FileManager import FileManager
import unittest
import os

class TestFileManager(unittest.TestCase):
    def test_path_created(self):
        test_file = 'test.yaml'
        test_target = 'test.json'

        FileManager(test_file, test_target)
        file_exists = os.path.exists(test_target)
        self.assertTrue(file_exists)
        os.remove(test_target)


