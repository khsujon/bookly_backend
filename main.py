from fastapi import FastAPI


app = FastAPI()


@app.get('/health')
async def get_health():
    return {
    'status': 'ok'
    }
@app.get("/great/{name}")
async def great(name: str) -> dict:
    return {"message":f"Hello {name}!"}