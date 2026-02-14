from sqlmodel import Field, SQLModel
from datetime import datetime
from uuid import UUID

class Book(SQLModel, table=True):
    