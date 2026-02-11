from fastapi import FastAPI
from .books.routes import book_router

version = "v1"
app = FastAPI(
    title="Bookly",
    description="A REST API for a book review application built with FastAPI",
    version=version,
)
app.include_router(book_router, prefix=f"/{version}/books", tags=["books"])
@app.get("/")
async def root():
    return {"message": f"Welcome to the Book API {version}!"}