import notes
import storage

print ("Welcome to my AI Study Assistant!")

notes_list = storage.load_notes()

while True:
    print("\n===== AI STUDY ASSISTANT =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Exit")
    
    choice = input("Choose and option: ")\

    if choice == 4:
        break
    
    print("You chose: ", choice)
    
title = input("Enter the note title: ")
content = input("Enter the note content: ")
subject = input("Enter the subject: ")

new_note = notes.create_note(
    title,
    content,
    subject
)

notes.add_note(notes_list, new_note)

storage.save_notes(notes_list)

print("Your note has been saved successfully!")

notes.display_notes(notes_list)

print("\nSearching for Python...\n")

notes.search_notes(notes_list, "Python")

