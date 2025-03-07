import sys
from pathlib import Path
# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))  # Path to the project root
import pandas as pd
from src.preprocessing import (
    handle_missing_values,
    clean_data,
    map_ip_to_country,
    feature_engineering,
    normalize_and_encode
)

# Load raw data
fraud_data = pd.read_csv("data/row/Fraud_Data.csv")
ip_country_data = pd.read_csv("data/row/IpAddress_to_Country.csv")

# Preprocessing pipeline
fraud_data = handle_missing_values(fraud_data)
fraud_data = clean_data(fraud_data)
fraud_data = map_ip_to_country(fraud_data, ip_country_data)
fraud_data = feature_engineering(fraud_data)
fraud_data = normalize_and_encode(fraud_data)

# Save processed data
fraud_data.to_csv("data/processed/processed_fraud_data.csv", index=False)
print("Data preprocessing completed and saved to data/processed/processed_fraud_data.csv")