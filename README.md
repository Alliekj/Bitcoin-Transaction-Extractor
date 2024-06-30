# Bitcoin Transaction Extractor

## Description
This project is designed to extract Bitcoin transactions from the blockchain. The project uses Python scripts to interact with blockchain APIs, retrieve transaction data, and process it for further analysis. The aim is to provide a tool that can be used to gather detailed information about Bitcoin transactions for research, analytics, or other purposes.

## Features
- Extract transaction data for a given Bitcoin address or block.
- Retrieve detailed information about each transaction including inputs, outputs, and transaction fees.
- Store the extracted data in a structured format (CSV, JSON, SQLite).
- Provide tools for filtering and analyzing transaction data.
- Visualize transaction flows and other key metrics.

## Technologies
- Python
- Requests library for API interaction
- pandas for data manipulation
- matplotlib for data visualization
- SQLite for data storage

## Setup Instructions
import os
import subprocess

def run_command(command):
    """Run a command in the terminal."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"Error running command: {command}\n{stderr.decode('utf-8')}")
    print(stdout.decode('utf-8'))

def main():
    # Step 1: Clone the repository
    repo_url = "https://github.com/yourusername/Bitcoin-Transaction-Extractor.git"
    run_command(f"git clone {repo_url}")
    project_path = "Bitcoin-Transaction-Extractor"
    os.chdir(project_path)
    print(f"Cloned repository and changed directory to {project_path}")

    # Step 2: Create and activate a virtual environment
    run_command("python3 -m venv bitcoin-env")
    run_command("source bitcoin-env/bin/activate")
    print("Created and activated virtual environment")

    # Step 3: Install the required packages
    run_command("pip install -r requirements.txt")
    print("Installed required packages")

    # Step 4: Configure the API settings
    config_content = """api:
  base_url: "https://api.blockcypher.com/v1/btc/main/"
  endpoint: "addrs/"
  token: "YOUR_API_TOKEN"
"""
    os.makedirs("config", exist_ok=True)
    with open("config/config.yaml", "w") as file:
        file.write(config_content)
    print("Created config/config.yaml with API settings")

    # Step 5: Create a .env file
    env_content = "BITCOIN_ADDRESS=your_bitcoin_address\n"
    with open(".env", "w") as file:
        file.write(env_content)
    print("Created .env file with Bitcoin address")

    # Step 6: Run the scripts
    scripts = ["extract_transactions.py", "process_data.py", "analyze_transactions.py", "visualize_transactions.py"]
    for script in scripts:
        run_command(f"python scripts/{script}")
        print(f"Executed {script}")

if __name__ == "__main__":
    main()

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. :)
