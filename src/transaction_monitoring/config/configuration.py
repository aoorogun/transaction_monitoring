import yaml
import os
from transaction_monitoring.utils.logger import logger  # Import centralized logger

class Configuration:
    def __init__(self, config_path="config/config.yaml"):
        self.config_path = config_path
        logger.info(f"🔍 Attempting to load configuration from: {config_path}")

        self.config = self._read_config()

        if self.config is None:
            raise ValueError(f"❌ Failed to load configuration from {config_path}. Check the file format and content.")

        # Initialize configuration sections
        self.data_ingestion = self.DataIngestionConfig(self.config.get("data_ingestion", {}))

    def _read_config(self):
        """Reads the config.yaml file and returns the configuration dictionary."""
        if not os.path.exists(self.config_path):
            logger.warning(f"⚠️ Configuration file not found at {self.config_path}.")
            return None

        try:
            with open(self.config_path, "r") as file:
                config_data = yaml.safe_load(file)
                logger.info("✅ Configuration loaded successfully.")
                return config_data
        except yaml.YAMLError as e:
            logger.error(f"❌ Error reading YAML file: {e}")
            return None

    class DataIngestionConfig:
        """Handles configuration for data ingestion."""
        def __init__(self, config):
            self.data_path = config.get("data_path", "data/input.csv")  # Default path
            self.raw_data_dir = config.get("raw_data_dir", "data/raw")  # Default directory
            logger.info(f"📂 Data Ingestion Config - Data Path: {self.data_path}, Raw Data Dir: {self.raw_data_dir}")
