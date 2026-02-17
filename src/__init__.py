from fastapi import FastAPI
from .books.routes import book_router
from .auth.routers import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any startup tasks here (e.g., connect to the database)
    print("Starting up server...")
    await init_db()
    yield   
    # Perform any shutdown tasks here (e.g., disconnect from the database)
    print("Shutting down has been stopped")


version = "v1"
app = FastAPI(
    title="Bookly",
    description="A REST API for a book review application built with FastAPI",
    version=version,
    lifespan=lifespan
)

app.include_router(book_router, prefix=f"/{version}/books", tags=["books"])
app.include_router(auth_router, prefix=f"/{version}/auth", tags=["auth"])
@app.get("/")
async def root():
    return {"message": f"Welcome to the Book API {version}!"}