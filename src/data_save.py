import csv
import pandas as pd
from datetime import datetime

"""Module to save data to files."""

def save_data(parsed_data: pd.DataFrame, directory="data"):
    """Save parsed data to CSV files based on datetime."""
    
    timestamp = parsed_data.index[0]

    if timestamp is None:
        print("No timestamp found in data; cannot save.")
        return
    
    # Save data to CSV files by day
    date_str = timestamp.strftime("%Y-%m-%d")
    filename = f"{directory}/data_{date_str}.csv"
    write_to_csv(filename, parsed_data)

def write_to_csv(filename, parsed_data):
    """Write parsed data to a CSV file."""
    file_exists = False
    try:
        with open(filename, 'r') as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=parsed_data.keys())
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({k: v for k, v in parsed_data.items()})
        print(f"Data saved to {filename}.")