from fastapi import FastAPI, Body

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
        book for book in BOOKS if book.get("category").casefold() == category.casefold()
    ]


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    return [
        book
        for book in BOOKS
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        )
    ]


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/book_update")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title") == update_book.get("title").casefold():
            BOOKS[i] = update_book
            return {"message": "Book updated successfully"}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
