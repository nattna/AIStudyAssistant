import json

def load_notes():
    """
    Loads existing notes from a JSON file
    """
    
    with open("data/notes.json", "r") as file:
        notes_list = json.load(file)
    
    return notes_list

def save_notes(notes_list):
    """
    Saves notes to a JSON file.
    """
    
    with open("data/notes.json", "w") as file:
        json.dump(notes_list, file, indent =4)
