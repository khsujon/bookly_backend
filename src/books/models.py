from sqlmodel import Field, SQLModel
from datetime import datetime
from uuid import UUID

class Book(SQLModel, table=True):
    id : UUID
    title : str
    author : str
    publisher : str
    publication_date : datetime
    page_count : int
    language : str
    created_at : datetime
    updated_at : datetime