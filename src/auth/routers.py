from fastapi import APIRouter
from .schemas import UserCreateModel


auth_router = APIRouter()


 #create a user
 
@auth_router.post("/signup")
async def signup():
    pass