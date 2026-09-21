import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question):
    response = client.responses.create(
        model="gpt-5-mini",
        input=question
    )

    return response.output_text

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

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text

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
    response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )
    
    return response.output_text

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

    response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )
    
    return response.output_text

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

    response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )
    
    return response.output_text