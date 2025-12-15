"""
Handles all saving/loading of RoomTone data.

Responsibilities:
- save_home(home)
- load_home(home_name)
- list_homes()
"""

import json
import os
from models import User, MoodEntry, Home
from datetime import date

class Storage:

    DATA_FILE = "roomtone_data.json"  # universal file

    @staticmethod
    def load_all_data():
        """Load data collected daily from JSON file."""
        if not os.path.exists(Storage.DATA_FILE):
            return {}
        with open(Storage.DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}

    @staticmethod
    def save_all_data(data):
        with open(Storage.DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_home(home: Home):
        """Save a Home object to JSON file."""
        data = Storage.load_all_data()

        # Convert Home object to dict
        home_dict = {
            "name": home.name,
            "users": [{"username": existing_u.username} for existing_u in home.users],
            "mood_entries": [
                {
                    "username": entry.user.username,
                    "mood": entry.mood,
                    "note": entry.note,
                    "date": entry.date.isoformat()
                }
                for entry in home.mood_entries
            ]
        }

        data[home.name] = home_dict
        Storage.save_all_data(data)

    @staticmethod
    def load_home(home_name: str) -> Home:
        """Load a Home object from JSON file."""
        data = Storage.load_all_data()

        if home_name not in data:
            raise ValueError(f"No home found with name '{home_name}'")

        home_data = data[home_name]
        home = Home(home_data["name"])

        # Load users
        home.users = [User(existing_u["username"]) for existing_u in home_data.get("users", [])]

        # Load mood entries
        for entry_data in home_data.get("mood_entries", []):
            user = next((existing_u for existing_u in home.users if existing_u.username == entry_data["username"]), None)
            if user:
                mood_entry = MoodEntry(user, entry_data["mood"], entry_data.get("note"))
                mood_entry.date = date.fromisoformat(entry_data["date"])
                home.mood_entries.append(mood_entry)

        return home

    @staticmethod
    def list_homes():
        """Return a list of home names available in local data."""
        data = Storage.load_all_data()
        return list(data.keys())
