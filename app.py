import notes
import storage

print ("Welcome to my AI Study Assistant!")

notes_list = storage.load_notes()

while True:
    print("\n===== AI STUDY ASSISTANT =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Edit Note")
    print("6. Exit")
    
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
        notes.display_notes(notes_list)
        
        if len(notes_list) == 0:
            print("There are no notes to delete.")
            continue
        
        try:
            note_number = int(input("Enter the number of the note you want to delete: "))
            
            index = note_number - 1
            
            if 0 <= index < len(notes_list):
                confirmation = input("Are you sure you want to delete this note? (y/n): ")
                
                if confirmation.lower()  in ["y", "yes"]:
                    notes.delete_note(notes_list, index)
                    storage.save_notes(notes_list)
                    print("Note deleted successfully!")
                else:
                    print("Note was not deleted.")
            else:
                print("Invalid note number.")
                
        except ValueError:
            print("Please enter a number.")
    
    elif choice == "5":
        notes.display_notes(notes_list)
        
        if len(notes_list) == 0:
            print("There are no notes to edit.")
            continue
        
        try:
            note_number = int(input("Enter the number of the note you want to edit: "))
            
            index = note_number - 1
            
            if 0 <= index < len(notes_list):
                
                current_note = notes_list[index]
                
                print("\nPress Enter to keep the current value.")
                
                title = input(
                    f"Current title: {current_note['title']}\n"
                    "New title:"
                )
                
                content = input(
                    f"Current concent: {current_note['content']}\n"
                    "New content:"
                )
                
                subject = input(
                    f"Current subject: {current_note['subject']}\n"
                    "New subject:"
                )
                
                if notes.edit_note(
                    notes_list,
                    index,
                    title,
                    content,
                    subject
                ):
                    storage.save_notes(notes_list)
                    print("Note updated successfully!")
            else:
                print("Invalid note number.")
        except ValueError:
            print("Please enter a number.")
            
    elif choice == "6":
        break

    else:
        print("Invalid option. Please choose 1, 2, 3 or 4.")
        
print("Goodbye, have a good day!")