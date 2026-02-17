from fastapi import APIRouter
from .schemas import UserCreateModel
from .service import UserService


auth_router = APIRouter()
user_service = UserService()


 #create a user
 
@auth_router.post("/signup")
async def create_user_account(user_data: UserCreateModel):
    email = user_data.email
    
    # Check if user already exists
    user_exists = await user_service.user_exists(email)
    