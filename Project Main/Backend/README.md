# EduGenie AI Learning Assistant

EduGenie is an AI-powered learning assistant built using FastAPI and Google's Gemini API.

## Features
- Answer educational questions
- Explain concepts
- Summarize paragraphs
- Generate quizzes
- Recommend learning paths

## Technologies Used
- Python
- FastAPI
- HTML/CSS
- Google Gemini API

## How to Run

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```
GEMINI_API_KEY=your_api_key_here
```

4. Start the server

```bash
uvicorn main:app --reload
```

5. Open:

```
http://127.0.0.1:8000
```
