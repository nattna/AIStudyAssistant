import json
import os

def load_notes():
    """
    Loads existing notes from a JSON file
    """
    if os.path.exists("data/notes.json"):
        with open("data/notes.json", "r") as file:
            return json.load(file)
    
    return []

def save_notes(notes_list):
    """
    Saves notes to a JSON file.
    """
    
    with open("data/notes.json", "w") as file:
        json.dump(notes_list, file, indent =4)
