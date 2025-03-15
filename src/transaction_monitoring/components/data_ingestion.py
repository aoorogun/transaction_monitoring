import os
import pandas as pd
from src.transaction_monitoring.config.configuration import Config
from transaction_monitoring import logger

class DataIngestion:
    def __init__(self, config: Config):
        self.config = config
        os.makedirs(self.config.data_ingestion.raw_data_dir, exist_ok=True)

    try:

        def load_data(self):
            df = pd.read_csv(self.config.data_ingestion.data_path)
            return df
        logger.info(f"dataset ingested")

        def save_raw_data(self, df):
            raw_data_path = os.path.join(self.config.data_ingestion.raw_data_dir, "raw_data.csv")
            df.to_csv(raw_data_path, index=False)
            return raw_data_path
        logger.info(f"dataset saved")
    except Exception as e:
        logger.error(f"Error in Data Ingestion: {e}")
        raise e