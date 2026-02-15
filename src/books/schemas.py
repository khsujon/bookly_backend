from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date
import uuid

# Database model (what gets stored)
class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime

# Create book model (request body - no uid, timestamps)
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    
# Response model (what API returns)
class BookResponse(BaseModel):
    uid: uuid.UUID
    title: str 
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime
    
# Update model
class BookUpdate(BaseModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None