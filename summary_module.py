import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_text(text):
    """
    Summarizes long text into a short and simple summary.
    """

    prompt = f"""
    Summarize the following text in simple language.

    Text:
    {text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)