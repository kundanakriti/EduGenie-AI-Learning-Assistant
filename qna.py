import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def answer_question(question):
    """
    Answers educational questions.
    """

    prompt = f"""
Answer the following question in plain text.

Do not use Markdown.
Do not use ** or ##.

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text