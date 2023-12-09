from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author one", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "love"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS