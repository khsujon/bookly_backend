from sqlmodel import Field, SQLModel, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"
    id : uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        )
    )
    title : str
    author : str
    publisher : str
    publication_date : datetime
    page_count : int
    language : str
    created_at : datetime = Field(Column(pg.TIMESTAMP, nullable=False, default=datetime.now))
    updated_at : datetime = Field(Column(pg.TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now))