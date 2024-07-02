from typing import List
from fastapi import FastAPI
from .dto import User, ServerPage, Comment, CommentRate, ServerRate
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/home", status_code=301)

@app.get("/home", response_model=List[ServerPage])
def home():
    return []

@app.post("/login")
def post_login(user: User):
    return {"login": True}