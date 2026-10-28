import os
import pandas as pd

data_path = os.getenv("DATA_PATH", "data/dataset.csv")

print("--- Big Data Analytics Container Started ---")

if os.path.exists(data_path):
    print(f"Loading data from: {data_path} (reading first 100,000 rows)...")
    df = pd.read_csv(data_path, nrows=100000)
    print(f"Sample loaded successfully! Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
    print("--- First 5 Rows ---")
    print(df.head())
    print("\n--- Summary Statistics ---")
    print(df.describe())
else:
    print(f"Error: {data_path} not found.")