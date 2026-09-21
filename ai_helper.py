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
        input=question
    )

    return response.output_text