from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config


# Create an asynchronous engine
engine = AsyncEngine(
    create_engine(Config.DATABASE_URL, echo=True)
)