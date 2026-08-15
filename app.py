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
    
    choice = input("Choose an option: ")\
    
    if choice == "1":
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

    elif choice == "2":
        notes.display_notes(notes_list)

    elif choice == "3":
        keyword = input("Enter a word to search for: ")
        notes.search_notes(notes_list, keyword)
        
    elif choice == "4":
        break

    else:
        print("Invalid option. Please choose 1, 2, 3 or 4.")
        
print("Goodbye, have a good day!")