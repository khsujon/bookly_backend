from fastapi import APIRouter



auth_router = APIRouter()


 #create a user
 
@auth_router.post("/signup")
async def signup():
    pass