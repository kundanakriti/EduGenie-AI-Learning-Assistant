import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the API key
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the model
model = genai.GenerativeModel("gemini-2.5-flash")


def explain_topic(topic):
    """
    Explains a topic in simple language.
    """

    prompt = f"""
    Explain the following topic in simple language for a beginner.

    Topic:
    {topic}
    """

    response = model.generate_content(prompt)

    return response.text