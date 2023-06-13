import yaml

class Config:
    def __init__(self,file_dir):
        self.file_dir = file_dir

    def read_yaml(self):
        with open(self.file_dir, 'r') as f:
            self.yaml_data = yaml.safe_load(f)


        return self.yaml_data
