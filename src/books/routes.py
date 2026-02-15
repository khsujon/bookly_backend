from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from .books_data import books
from .schemas import Book, BookUpdate
from src.db.main import get_session
from src.books.service import BookService

book_router = APIRouter()
#endpoints

#get all books
@book_router.get("/", response_model= List[Book])
async def get_books():
    return books

#create a book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book)-> dict:
    new_book = book.model_dump()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return new_book

#get book by id
@book_router.get("/{book_id}")
async def get_book(book_id: int)-> dict:
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_id}")

#update a book
@book_router.patch("/{book_id}")
async def update_book(book_id: int, book_update: BookUpdate)-> dict:
    for book in books:
        if book["id"] == book_id:
            if book_update.title is not None:
                book["title"] = book_update.title
            if book_update.publisher is not None:
                book["publisher"] = book_update.publisher
            if book_update.page_count is not None:
                book["page_count"] = book_update.page_count
            if book_update.language is not None:
                book["language"] = book_update.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_id}")


#delete a book
@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_id}")
    