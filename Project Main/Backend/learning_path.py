import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def recommend_learning_path(topic):
    """
    Recommends a learning roadmap.
    """

    prompt = f"""
    You are EduGenie.

    Create a beginner-friendly learning roadmap.

    Topic:
    {topic}

    Include:

    Beginner

    Intermediate

    Advanced

    Mention useful skills to learn at each level.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)