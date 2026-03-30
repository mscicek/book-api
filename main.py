from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = []

class Book(BaseModel):
    title: str
    author: str
    year: int


@app.get("/")
def home():
    return {"message": "Book API çalışıyor"}


@app.get("/books")
def get_books():
    return books


@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Kitap eklendi", "book": book}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id < len(books):
        books.pop(book_id)
        return {"message": "Kitap silindi"}
    return {"error": "Kitap bulunamadı"}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    if book_id < len(books):
        books[book_id] = updated_book.dict()
        return {"message": "Kitap güncellendi", "book": updated_book}
    return {"error": "Kitap bulunamadı"}

@app.get("/books/search/{title}")
def search_book(title: str):
    results = []
    
    for book in books:
        if title.lower() in book["title"].lower():
            results.append(book)

    return results