import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def load_processed_data(address):
    return pd.read_csv(f"data/processed/{address}.csv")

def analyze_data(df):
    total_in = df['value_in'].sum()
    total_out = df['value_out'].sum()
    num_transactions = df['hash'].nunique()
    return {
        'total_in': total_in,
        'total_out': total_out,
        'num_transactions': num_transactions
    }

if __name__ == "__main__":
    address = os.getenv('BITCOIN_ADDRESS')
    df = load_processed_data(address)
    analysis = analyze_data(df)
    print(analysis)

