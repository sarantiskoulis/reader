import os
import json
from Config import Config
class FileManager:
    def __init__(self, data_dir, path_write):
        self.path_write = path_write
        self.data_dir = data_dir
        self.write_to_path()

    def write_to_path(self):
        # if os.path.exists(self.path_write):
        #     with open(str(self.path_write), 'w') as f:
        #         data = Config(self.data_dir)
        #         json.dump(data.read_yaml(), f)
        # else:
        with open(os.path.join(os.getcwd(),str(self.path_write)), 'w') as f:
            data = Config(self.data_dir)
            json.dump(data.read_yaml(), f)
#
# FileManager('input.yaml','ouput.json')
# os.remove('ouput.json')