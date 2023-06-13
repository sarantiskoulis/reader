import os
import json
from Config import Config
import yaml
class FileManager:
    def __init__(self, data_dir, path_write):
        self.path_write = path_write
        self.data_dir = data_dir
        self.data_list = self._write_to_list(self.data_dir)

        if self.path_write == 'cmd':
            self.write_to_cmd()
        else:
            self.write_to_path()

    def write_to_path(self):
        with open(os.path.join(os.getcwd(),str(self.path_write)), 'w') as f:
            data = Config(self.data_dir)
            json.dump(data.read_yaml(), f)
    @staticmethod
    def _write_to_list(data_dir: str):
        data_list = []
        with open(os.path.join(os.getcwd(),data_dir), 'r') as f:
            for line in f:
                data_list.append(line)

        return data_list

    def write_to_cmd(self):
        for line in self.data_list:
            print(line)

#FileManager('input.yaml','cmd')
