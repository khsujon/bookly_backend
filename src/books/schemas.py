from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import uuid
#request model
class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime
    
    
#response model
class BookResponse(BaseModel):
    uid: uuid.UUID
    title: str 
    author: str
    publisher: str
    published_date: str
    page_count: int
    
#update model
class BookUpdate(BaseModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None