from fastapi import FastAPI
from .books.routes import book_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any startup tasks here (e.g., connect to the database)
    print("Starting up server...")
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
@app.get("/")
async def root():
    return {"message": f"Welcome to the Book API {version}!"}