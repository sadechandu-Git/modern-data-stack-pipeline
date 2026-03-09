import pandas as pd
import requests

def fetch_data():
    # Example: Pulling public crypto data
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url)
    return response.json()

def load_to_bronze():
    data = fetch_data()
    df = pd.DataFrame(data)
    # In a real setup, we'd save this to our Postgres DB or a Parquet file
    print(f"Successfully ingested {len(df)} rows of raw data.")
    return df

if __name__ == "__main__":
    load_to_bronze()
