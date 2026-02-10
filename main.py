from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/health')
async def get_health():
    return {
    'status': 'ok'
    }
#Path parameter example
@app.get("/great/{name}")
async def great(name: str) -> dict:
    return {"message":f"Hello {name}!"} # request send as http://127.0.0.1:8000/great/YourName

#Query parameter example
@app.get("/items/")
async def get_item(name: str, price: float) -> dict:
    return {"name": name, "price": price} # request send as http://127.0.0.1:8000/items/?name=Item1&price=10.5

#optional query parameter example
@app.get("/users/")
async def get_user(name: str, age: Optional[int] = 25) -> dict:
    if age:
        return {"name": name, "age": age}
    return {"name": name} # request send as http://127.0.0.1:8000/users/?name=User1