import os
import pandas as pd

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def load_data(self):
        """Loads data from the configured file path."""
        if not os.path.exists(self.config.data_ingestion.data_path):
            raise FileNotFoundError(f"❌ Data file not found at {self.config.data_ingestion.data_path}")

        return pd.read_csv(self.config.data_ingestion.data_path)

    def save_raw_data(self, df):
        """Ensures directory exists and saves raw data as CSV."""
        raw_data_dir = self.config.data_ingestion.raw_data_dir
        os.makedirs(raw_data_dir, exist_ok=True)

        raw_data_path = os.path.join(raw_data_dir, "raw_data.csv")
        df.to_csv(raw_data_path, index=False)
        
        return raw_data_path
