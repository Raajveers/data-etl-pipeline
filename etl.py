
import requests
import pandas as pd

import json

def extract():
    with open("mock_data.json", "r") as file:
        data = json.load(file)
    return data


def transform(raw_data):
    time_updated = raw_data["time"]["updated"]
    usd_rate = raw_data["bpi"]["USD"]["rate_float"]
    return {
        "time": time_updated,
        "USD_rate": usd_rate
    }

def load(data_dict):
    df = pd.DataFrame([data_dict])
    output_path = "output.csv"
    df.to_csv(output_path, index=False)
    print(f"Data written to {output_path}")

def main():
    raw = extract()
    data = transform(raw)
    load(data)

if __name__ == "__main__":
    main()
