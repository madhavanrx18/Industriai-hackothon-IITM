import random
from web3 import Web3
import pandas as pd

# Connect to Ganache (or any Ethereum node)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Check if connected to the Ethereum network
if w3.is_connected():
    print("Connected to Ethereum network.")
    
    # Get the latest block number
    latest_block = w3.eth.block_number
    print(f"Latest block number: {latest_block}")

    # Load the dataset (ensure the path is correct)
    dataset_path = '/home/subramanian/Downloads/Industriai-hackothon-IITM/blockchain/user_access_data.csv'
    df = pd.read_csv(dataset_path)

    # Loop through all blocks from genesis to the latest block
    for block_num in range(1, latest_block + 1):
        # Get the block details
        block = w3.eth.get_block(block_num)
        print(f"Processing block {block_num}...")

        # Randomly set trigger to True or False
        trigger = random.choice([True, False])

        # Select a random row from the dataset for each block
        row = df.sample().iloc[0]
        user_id = row['User_ID']
        role = row['Role']
        file_path = row['File_Path']
        behavior_probability = row['Behavior_Probability']
        access_granted = row['Access_Granted']

        if trigger:
            print(f"Block {block_num}: Log exists on blockchain.")
            print(f"User ID: {user_id}, Role: {role}, File Path: {file_path}, "
                  f"Behavior Probability: {behavior_probability}, Access Granted: {access_granted}")
        else:
            print(f"Block {block_num}: Log does not exist on blockchain. Processing with ML model...")
else:
    print("Failed to connect to the Ethereum network. Stopping the operation.")

