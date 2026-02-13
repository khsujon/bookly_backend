from sqlmodel import Field, SQLModel
from datetime import datetime

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str