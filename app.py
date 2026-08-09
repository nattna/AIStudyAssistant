import notes

print ("Welcome to my AI Study Assistant!")

notes_list = []

my_note = notes.create_note(
    "Python Variables",
    "Variables store information.",
    "Programming"
)

my_note2 = notes.create_note(
    "Generative AI", 
    "Relies on deep learning algorithms.",
    "AI"
)

my_note3 = notes.create_note(
    "Functions",
    "A function is a relation from one set to another.",
    "Mathematics"
)

notes.add_note(notes_list, my_note)
notes.add_note(notes_list, my_note2)
notes.add_note(notes_list, my_note3)

notes.display_notes(notes_list)

print("\nSearching for Python...\n")

notes.search_notes(notes_list, "Python")

