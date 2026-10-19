import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def make_ai_request(prompt):
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text

    except Exception as error:
        print("\nAI request could not be completed.")
        print("Please check your API connection or account credits.")
        print(f"Error: {error}")

        return None

def ask_ai(question):
    prompt = f"""
You are a helpful AI study assistant.

Answer the student's question clearly and simply.

Student question:
{question}
"""
    return make_ai_request(prompt)

def ask_ai_about_notes(question, notes_list):
    notes_text = ""
    
    for note in notes_list:
        notes_text += f"""
        
Title: {note['title']}
Content: {note['content']}
Subject {note['subject']}
"""

    prompt = f"""
You are a helpful AI study assistant.

Here are the student's study notes:

{notes_text}

Answer the student's question using these notes when relevant.

Student question:
{question}
"""

    return make_ai_request(prompt)

def summarise_notes(notes_list):
    notes_text = ""
    
    for note in notes_list:
        notes_text += f"""
Title: {note['title']}
Content: {note['content']}
Subject {note['subject']}
"""

    prompt = f"""
You are helpful study assistant.

Summarise the following study notes.

Make the summary:
- Easy to understand
- Concise
- Useful for revision
- Organised with headings or bullet points

Study notes: 

{notes_text}
"""
    return make_ai_request(prompt)

def generate_quiz(notes_list):
    notes_text = ""
    
    for note in notes_list:
        notes_text += f"""
Title: {note['title']}
Content: {note['content']}
Subject {note['subject']}
"""

    prompt = f"""
You are a helpful university study assistant.

Create 5 quiz questions based on the student's notes.

Do not give the answers immediately.

Make the questions test understanding rather than just memorisation.

Study notes:

{notes_text}
"""
    return make_ai_request(prompt)

def explain_note(note):
    prompt = f"""
You are a helpful university study assistant.

Explain the following study note to a beginner.

Use simple language and give an example where useful.

Note title:
{note['title']}

Subject:
{note['subject']}

Note content:
{note['content']}
"""

    return make_ai_request(prompt)