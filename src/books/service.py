#All logics in here

from sqlmodel.ext.asyncio.session import AsyncSession
from . schemas import BookCreateModel, BookUpdate
from sqlmodel import select, desc
from .models import Book

# Service layer for handling book-related operations
class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()
    
    async def get_book(self, book_uid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        return result.first()
    
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        session.add(new_book)             # Add the new book to the session
        await session.commit()            # Commit the transaction to save the new book to the database
        await session.refresh(new_book)   # Refresh the instance to get the updated data (like generated ID)
        return new_book
    
    async def update_book(self, book_uid: str, updated_data: BookUpdate, session: AsyncSession):
        book_to_update = await self.get_book(book_uid, session)
        
        
        updated_data_dict = updated_data.model_dump()
        
        for key, value in updated_data_dict.items():
            if value is not None:
                setattr(book_to_update, key, value)
        await session.commit()
        await session.refresh(book_to_update)
        return book_to_update
    
    async def delete_book(self, book_uid: str, session: AsyncSession):
        pass