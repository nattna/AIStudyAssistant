def create_note(title, content, subject):
    """
    Creates a note using the information provided.
    """
    note = {
        "title": title,
        "content": content,
        "subject": subject
    }
    
    return note
    
def add_note(notes_list, note):
    """
    Adds a note to the list of notes.
    """
    
    notes_list.append(note)
    
def display_notes(notes_list):
    """
    Displays all notes in a readable format.
    """
    
    for note in notes_list:
        print("---------------------------")
        print("Title:", note["title"])
        print("Content:", note["content"])
        print("Subject:", note["subject"])
        print("---------------------------")
        
def search_notes(notes_list, keyword):
    """
    Searches for a keyword in the note titles.
    """
    found = False
    
    for note in notes_list:
        if (keyword.lower() in note ["title"].lower()
        or keyword.lower() in note["content"].lower()
        or keyword.lower() in note["subject"].lower()):
            
            print("---------------------------")
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("Subject:", note["subject"])
            print("---------------------------")
            
            found = True
            
    if not found:
        print("No notes found.")