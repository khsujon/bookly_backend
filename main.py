from fastapi import FastAPI


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