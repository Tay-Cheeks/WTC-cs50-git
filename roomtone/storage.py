"""
storage.py

Handles all saving/loading of RoomTone data.

For CS50, this uses a simple local JSON file for persistence.

Responsibilities:
- save_home(home)
- load_home(home_name)
- list_homes()
"""

class Storage:

    DATA_FILE = "roomtone_data.json"

    @staticmethod
    def save_home(home):
        # TODO: write home object to JSON file
        pass

    @staticmethod
    def load_home(home_name):
        # TODO: load a home dictionary from JSON and convert back to Home object
        pass

    @staticmethod
    def list_homes():
        # TODO: return list of home names available in local data
        pass
