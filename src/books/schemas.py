from typing import Optional
from pydantic import BaseModel

#response model
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
#update model
class BookUpdate(BaseModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None