import json
import os

FILE = "parsed_data.json"

def load_all_results():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_result(data):
    all_data = load_all_results()
    all_data.append(data)
    with open(FILE, "w") as f:
        json.dump(all_data, f, indent=4)
