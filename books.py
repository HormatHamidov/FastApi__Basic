from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {
        "title": "Title One",
        "author": "Author one",
        "category": "science",
    },
    {
        "title": "Title Two",
        "author": "Author Two",
        "category": "love",
    },
    {
        "title": "Title Three",
        "author": "Author Three",
        "category": "history",
    },
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    return [
        book
        for book in BOOKS
        if book.get("category").casefold() == category.casefold()
    ]
