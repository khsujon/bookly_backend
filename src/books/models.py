#All the database models in here which act as the blueprint for the tables in the database. Each model corresponds to a table, and the attributes of the model correspond to the columns in the table. The models also include methods for representing the data and can be used to perform CRUD operations on the database through an ORM (Object-Relational Mapping) layer.

from sqlmodel import Field, SQLModel, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import date, datetime
import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid : uuid.UUID = Field(
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
    publication_date : date
    page_count : int
    language : str
    created_at : datetime = Field(sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.now))
    updated_at : datetime = Field(sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now))
    
    
    # This method is used to provide a string representation of the Book object, which is useful for debugging and logging purposes.
    def __repr__(self):
        return f'<Book(id={self.id}, title="{self.title}", author="{self.author}")>'