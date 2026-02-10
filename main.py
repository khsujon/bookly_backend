from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


#book data
book = [
    {"id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publisher": "Scribner",
    "published_date": "1925-04-10",
    "page_count": 218,
    "language": "English",},
    {"id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publisher": "J.B. Lippincott & Co.",
    "published_date": "1960-07-11",
    "page_count": 281,
    "language": "English",},
    {"id": 3,
    "title": "1984",
    "author": "George Orwell",
    "publisher": "Secker & Warburg",
    "published_date": "1949-06-08",
    "page_count": 328,
    "language": "English",},
    {"id": 4,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "publisher": "T. Egerton",
    "published_date": "1813-01-28",
    "page_count": 432,
    "language": "English",},
    
]

#endpoints

#get all books
@app.get("/books")
async def get_books():
    pass

#get book by id
@app.get("/books/{book_id}")
async def get_book(book_id: int)-> dict:
    pass

#create a book
@app.post("/books")
async def create_book()-> dict:
    pass

#update a book
@app.patch("/books/{book_id}")
async def update_book(book_id: int)-> dict:
    pass

@app.delete("/books/{book_id}")
async def delete_book(book_id: int)-> dict:
    pass
    

# @app.get('/health')
# async def get_health():
#     return {
#     'status': 'ok'
#     }
# #Path parameter example
# @app.get("/great/{name}")
# async def great(name: str) -> dict:
#     return {"message":f"Hello {name}!"} # request send as http://127.0.0.1:8000/great/YourName

# #Query parameter example
# @app.get("/book/")
# async def get_item(name: str, price: float) -> dict:
#     return {"name": name, "price": price} # request send as http://127.0.0.1:8000/items/?name=Item1&price=10.5

# #optional query parameter example
# @app.get("/users/")
# async def get_user(name: str, age: Optional[int] = 25) -> dict:
#     if age:
#         return {"name": name, "age": age}
#     return {"name": name} # request send as http://127.0.0.1:8000/users/?name=User1

# #defining a model for request body
# class BookCreate(BaseModel):
#     title: str
#     author: str
#     price : float
# #Create a book using request body
# @app.post("/create")
# async def create_book(book:BookCreate):
#     return{
#     "title": book.title,
#     "author": book.author,
#     "price": book.price
#     }