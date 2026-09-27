import json
from pathlib import Path

DATA_FILE = Path("library_data.json")

DEFAULT_DATA = {
    "books": [
        {"id": 1, "name": "Python Basics", "author": "John", "available": True},
        {"id": 2, "name": "Data Structures", "author": "James", "available": True},
        {"id": 3, "name": "Computer Networks", "author": "David", "available": True},
        {"id": 4, "name": "Database Management", "author": "Robert", "available": True},
        {"id": 5, "name": "Operating Systems", "author": "William", "available": True},
        {"id": 6, "name": "Artificial Intelligence", "author": "Andrew", "available": True},
        {"id": 7, "name": "Machine Learning", "author": "Tom", "available": True},
        {"id": 8, "name": "Web Development", "author": "Michael", "available": True},
        {"id": 9, "name": "Cyber Security", "author": "Daniel", "available": True},
        {"id": 10, "name": "Cloud Computing", "author": "Chris", "available": True}
    ],
    "members": [
        {"id": 1, "name": "Student 1"},
        {"id": 2, "name": "Student 2"}
    ],
    "transactions": []
}


def load_data():
    try:
        if not DATA_FILE.exists():
            save_data(DEFAULT_DATA)
            return DEFAULT_DATA.copy()

        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read saved data. Starting with default data.")
        return DEFAULT_DATA.copy()


def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("Error: Data could not be saved.")
