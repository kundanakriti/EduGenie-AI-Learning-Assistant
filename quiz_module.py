import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_quiz(topic):
    """
    Generates 5 MCQs from a topic.
    """

    prompt = f"""
    You are EduGenie, an AI learning assistant.

    Generate 5 multiple-choice questions on the topic below.

    Topic:
    {topic}

    Rules:
    1. Each question must have four options:
       A, B, C, D
    2. Mention the correct answer.
    3. Keep questions suitable for students.
    """

    response = model.generate_content(prompt)

    return response.text