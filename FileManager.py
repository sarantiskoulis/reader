import os
import json
from Config import Config
class FileManager:
    def __init__(self, data_dir, path_write):
        self.path_write = path_write
        self.data_dir = data_dir

        if self.path_write == 'cmd':
            self.write_to_cmd()
        else:
            self.write_to_path()


    def write_to_path(self):
        with open(os.path.join(os.getcwd(), str(self.path_write)), 'w') as f:
            data = Config(self.data_dir)
            json.dump(data.read_yaml(), f)

    def write_to_cmd(self):
        with open(self.data_dir, 'r') as f:
            for line in f:
                print(line)



