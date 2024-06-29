import os
import json
import random
import requests
from datetime import datetime

# List of blockchain APIs to fetch data from
blockchain_apis = [
    "https://api.blockchain.info/stats",
    # Add other API endpoints as required
]

# Function to fetch data from an API
def fetch_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return {}

# Function to generate a random JSON response
def generate_random_json():
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "random_value": random.randint(1, 1000),
        "status": random.choice(["success", "error"]),
        "message": random.choice(["Operation completed", "Operation failed"]),
    }
    return data

# Function to save JSON data to a file
def save_json_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Function to fetch and save blockchain data
def fetch_and_save_blockchain_data():
    for api_url in blockchain_apis:
        data = fetch_api_data(api_url)
        if data:
            filename = os.path.join('response', f'blockchain_data_{datetime.utcnow().strftime("%Y%m%d%H%M%S")}.json')
            save_json_to_file(data, filename)

# Function to update tags/keywords
def update_tags_keywords():
    keywords = ["USDT", "BTC", "flash loan", "flash BTC", "WBTC"]
    tags = ["#crypto", "#blockchain", "#bitcoin"]
    combined = keywords + tags
    random.shuffle(combined)
    return combined

if __name__ == "__main__":
    # Create response directory if it doesn't exist
    if not os.path.exists('response'):
        os.makedirs('response')

    # Generate and save a random JSON response
    random_json = generate_random_json()
    save_json_to_file(random_json, 'response/random_response.json')

    # Fetch and save blockchain data
    fetch_and_save_blockchain_data()

    # Update and print tags/keywords
    updated_tags_keywords = update_tags_keywords()
    with open('response/tags_keywords.txt', 'w') as f:
        for item in updated_tags_keywords:
            f.write(f"{item}\n")

    print("Tags/Keywords updated:", updated_tags_keywords)
