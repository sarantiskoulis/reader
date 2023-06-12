import unittest
import os
from Config import Config

class TestConfig(unittest.TestCase):
    def test_first_value(self):
        test_file = 'test.yaml'
        test_dict = Config(test_file).read_yaml()
        test_data_value = test_dict['simulation']['people']
        test_value = 1010
        self.assertEquals(test_value, test_data_value)
