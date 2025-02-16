import json
import os
from django.conf import settings

# Define the file path for storing JSON data
DATA_FILE = os.path.join(settings.BASE_DIR, "data.json")

# Function to load existing data
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Function to save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new sustainability action
def add_action(action, date, points):
    data = load_data()
    new_entry = {
        "id": len(data) + 1,
        "action": action,
        "date": date,
        "points": points
    }
    data.append(new_entry)
    save_data(data)
    return new_entry

# Function to get all actions
def get_actions():
    return load_data()

# Function to delete an action by ID
def delete_action(action_id):
    data = load_data()
    updated_data = [entry for entry in data if entry["id"] != action_id]
    save_data(updated_data)
    return {"message": "Action deleted successfully"}
