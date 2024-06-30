import requests
import yaml
import os
import json
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def load_config():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        print("Config loaded:", config)  # Debug statement
        return config

def fetch_transactions(address, config):
    base_url = config['api']['base_url']
    endpoint = config['api']['endpoint']
    token = config['api']['token']
    address_url = f"{base_url}{endpoint}{address}?token={token}"
    
    # Fetch basic address data
    response = requests.get(address_url)
    print(f"Response status code (address): {response.status_code}")  # Debug statement
    if response.status_code == 200:
        address_data = response.json()
    else:
        response.raise_for_status()

    # Fetch transaction data using tx_url
    tx_url = address_data.get('tx_url')
    if tx_url:
        tx_url = f"{tx_url}?token={token}"
        response = requests.get(tx_url)
        print(f"Response status code (transactions): {response.status_code}")  # Debug statement
        if response.status_code == 200:
            tx_data = response.json()
            address_data['transactions'] = tx_data
        else:
            response.raise_for_status()
    
    return address_data

def save_raw_data(data, address):
    raw_data_path = f"data/raw/{address}.json"
    os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)
    with open(raw_data_path, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    config = load_config()
    address = os.getenv('BITCOIN_ADDRESS')
    data = fetch_transactions(address, config)
    save_raw_data(data, address)

