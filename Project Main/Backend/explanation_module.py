import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_topic(topic):

    prompt = f"""
    Explain the following topic in simple language for a beginner.

    Topic:
    {topic}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)