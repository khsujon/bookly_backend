from sqlmodel import SQLModel
import uuid
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"
    id : uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime