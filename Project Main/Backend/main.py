from fastapi import FastAPI
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import recommend_learning_path
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(title="EduGenie AI Learning Assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class UserInput(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html"
    )


@app.post("/qa")
def qa(data: UserInput):
    return {
        "answer": answer_question(data.text)
    }


@app.post("/explain")
def explain(data: UserInput):
    return {
        "explanation": explain_topic(data.text)
    }


@app.post("/summarize")
def summarize(data: UserInput):
    return {
        "summary": summarize_text(data.text)
    }


@app.post("/quiz")
def quiz(data: UserInput):
    return {
        "quiz": generate_quiz(data.text)
    }


@app.post("/learn/recommendations")
def learning(data: UserInput):
    return {
        "learning_path": recommend_learning_path(data.text)
    }