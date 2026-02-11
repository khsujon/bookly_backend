from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

from typing import List

app = FastAPI()




#endpoints

#get all books
@app.get("/books", response_model= List[Book])
async def get_books():
    return books

#create a book
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book)-> dict:
    new_book = book.model_dump()
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return new_book

#get book by id
@app.get("/books/{book_id}")
async def get_book(book_id: int)-> dict:
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_id}")

#update a book
@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_update: BookUpdate)-> dict:
    for book in books:
        if book["id"] == book_id:
            if book_update.title is not None:
                book["title"] = book_update.title
            if book_update.publisher is not None:
                book["publisher"] = book_update.publisher
            if book_update.page_count is not None:
                book["page_count"] = book_update.page_count
            if book_update.language is not None:
                book["language"] = book_update.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_id}")


#delete a book
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book Not Found with id {book_id}")
    

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