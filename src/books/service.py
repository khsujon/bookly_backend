#All logics in here

from sqlmodel.ext.asyncio.session import AsyncSession
from . schemas import BookCreateModel

class BookService:
    async def get_all_books(self, session: AsyncSession):
        pass
    
    async def get_book(self, book_uid: str, session: AsyncSession):
        pass
    
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        pass