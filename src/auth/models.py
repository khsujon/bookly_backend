from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"
    id : uuid.UUID = Field(
        sa_column=Column(
            pg.UUID, 
            primary_key=True, 
            default=uuid.uuid4, 
            nullable=False
        )
    )
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP(timezone=True), default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP(timezone=True), default=datetime.now, onupdate=datetime.utcnow, nullable=False))