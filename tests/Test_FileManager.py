from Config import Config
from FileManager import FileManager
import unittest
import os
from click.testing import CliRunner
import main

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

        runner = CliRunner()
        result = runner.invoke(main._cli_outputs ,
                                ['--yamlfile', 'test.yaml', '--writeto', 'cmd'])

        assert result.exit_code == 0
        self.assertEqual( 'simulation:\n\n  people: 1010\n\n', result.output)


    def test_output_newfile(self):
        test_file = 'test.yaml'
        test_target = 'test.json'
        FileManager(test_file, test_target)

        test_data_dic = Config('test.yaml').read_yaml()
        true_data_dic = Config('test.json').read_yaml()

        self.assertEqual(test_data_dic,true_data_dic)
        os.remove('test.json')
