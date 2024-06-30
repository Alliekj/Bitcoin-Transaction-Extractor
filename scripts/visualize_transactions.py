import pandas as pd
import matplotlib.pyplot as plt

def load_processed_data(address):
    return pd.read_csv(f"data/processed/{address}.csv")

def plot_transaction_values(df, address):
    df['time'] = pd.to_datetime(df['time'], unit='s')
    plt.figure(figsize=(10, 5))
    plt.plot(df['time'], df['value_in'], label='Value In')
    plt.plot(df['time'], df['value_out'], label='Value Out')
    plt.xlabel('Time')
    plt.ylabel('Value (Satoshis)')
    plt.title(f'Transaction Values for {address}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    address = "your_bitcoin_address"
    df = load_processed_data(address)
    plot_transaction_values(df, address)

