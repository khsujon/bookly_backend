from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from .schemas import Book, BookUpdate
from src.db.main import get_session
from src.books.service import BookService

book_router = APIRouter()
book_service = BookService()
#endpoints

#get all books
@book_router.get("/", response_model= List[Book])
async def get_books(session: AsyncSession=Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

#create a book
@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: Book, session: AsyncSession=Depends(get_session))-> Book:
    new_book = book_service.create_book(book_data, session)
    return new_book

#get book by id
@book_router.get("/{book_uid}")
async def get_book(book_uid: str, session: AsyncSession=Depends(get_session))-> dict:
    book = book_service.get_book(book_uid, session)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_uid}")
    return book

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
    