from transaction_monitoring.components.data_ingestion import DataIngestion
from transaction_monitoring.config.configuration import Configuration
import os

# Load Configuration
config = Configuration()

# Initialize Data Ingestion
data_ingestion = DataIngestion(config)

try:
    # Load Data
    df = data_ingestion.load_data()
    print(f"✅ Data loaded successfully from {config.data_ingestion.data_path}")

    # Save Raw Data
    saved_path = data_ingestion.save_raw_data(df)

    # Verify if the file was created
    if os.path.exists(saved_path):
        print(f"✅ Data ingestion successful! File saved at: {saved_path}")
    else:
        print("❌ Data ingestion failed!")

except FileNotFoundError as e:
    print(e)
