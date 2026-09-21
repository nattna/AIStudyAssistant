from openai import OpenAI

client = OpenAI()

def ask_ai(question):
    """
    Sends a question to the AI and returns a response.
    """
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=question
    )
    return response.output_text