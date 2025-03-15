import yaml

class Config:
    def __init__(self, config_path="config/config.yaml", params_path="params.yaml"):
        self.config = self.load_yaml(config_path)
        self.params = self.load_yaml(params_path)
        self.data_ingestion = self.config['data_ingestion']
    
    def load_yaml(self, file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)