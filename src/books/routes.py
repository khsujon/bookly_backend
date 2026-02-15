from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from .schemas import Book, BookUpdate, BookCreateModel
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
async def create_book(book_data: BookCreateModel, session: AsyncSession=Depends(get_session))-> Book:
    new_book = await book_service.create_book(book_data, session)
    return new_book

#get book by id
@book_router.get("/{book_uid}")
async def get_book(book_uid: str, session: AsyncSession=Depends(get_session))-> dict:
    book = await book_service.get_book(book_uid, session)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_uid}")
    return book

#update a book
@book_router.patch("/{book_uid}")
async def update_book(book_uid: str, book_update_data: BookUpdate, session: AsyncSession=Depends(get_session))-> dict:
    updated_book =  await book_service.update_book(book_uid, book_update_data, session)
    if updated_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_uid}")
    return updated_book


#delete a book
@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession=Depends(get_session)):
    deleted_book = await book_service.delete_book(book_uid, session)
    if deleted_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_uid}")
    return None
    