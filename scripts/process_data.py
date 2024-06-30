import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def load_raw_data(address):
    with open(f"data/raw/{address}.json", 'r') as file:
        return json.load(file)

def process_data(raw_data):
    print("Raw Data:", json.dumps(raw_data, indent=2))  # Debug statement to print the structure of raw_data
    transactions = raw_data.get('transactions', [])
    processed_data = []
    for tx in transactions:
        for input in tx.get('inputs', []):
            processed_data.append({
                'hash': tx['hash'],
                'time': tx.get('received', 'N/A'),  # Use 'received' or a default value
                'input': input['addresses'][0] if input.get('addresses') else 'N/A',  # Check for empty addresses list
                'value_in': input.get('output_value', 0)  # Provide default value if key is missing
            })
        for output in tx.get('outputs', []):
            processed_data.append({
                'hash': tx['hash'],
                'time': tx.get('received', 'N/A'),  # Use 'received' or a default value
                'output': output['addresses'][0] if output.get('addresses') else 'N/A',  # Check for empty addresses list
                'value_out': output.get('value', 0)  # Provide default value if key is missing
            })
    return pd.DataFrame(processed_data)

def save_processed_data(df, address):
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(f"data/processed/{address}.csv", index=False)

if __name__ == "__main__":
    address = os.getenv('BITCOIN_ADDRESS')
    raw_data = load_raw_data(address)
    df = process_data(raw_data)
    save_processed_data(df, address)

