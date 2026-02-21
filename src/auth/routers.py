from fastapi import APIRouter, Depends, HTTPException, status
from .dependencies import RefreshTokenBearer
from .schemas import UserCreateModel, UserModel, UserLoginModel
from .service import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .utils import create_access_token, decode_access_token, verify_password
from datetime import timedelta, datetime
from fastapi.responses import JSONResponse

auth_router = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXPIRY_DAYS = 2

 #create a user
@auth_router.post("/signup", response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreateModel, session : AsyncSession = Depends(get_session)):
    email = user_data.email
    
    # Check if user already exists
    user_exists = await user_service.user_exists(email, session)
    
    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this email already exists.")
    
    # Create the user
    new_user = await user_service.create_user(user_data, session)
    return new_user


#Login user
@auth_router.post("/login")
async def login_user(login_data: UserLoginModel, session : AsyncSession = Depends(get_session)):
    email = login_data.email
    password = login_data.password
    
    #check if user exists
    user = await user_service.get_user_by_email(email, session)
    
    if user is not None:
        #verify password
        password_valid = verify_password(password, user.password_hash)
        if not password_valid:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
        #create access token
        access_token = create_access_token(
            user_data={
                "email": user.email,
                "user_uid": str(user.uid)
            }
        )
        
        #create refresh token
        refresh_token = create_access_token(
            user_data={
                "email": user.email,
                "user_uid": str(user.uid)
            },
            refresh=True,
            expiry=timedelta(days=REFRESH_TOKEN_EXPIRY_DAYS)
        )
        
        return JSONResponse(content={
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "uid": str(user.uid)
            }
        })
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials, user not found with this email")


#refresh access token
@auth_router.get("/refresh")
async def get_new_access_token(token_details:dict=Depends(RefreshTokenBearer())):
    expiry_timestamp = token_details['exp']
    
    if datetime.fromtimestamp(expiry_timestamp) < datetime.now():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token has expired, please login again")
    
    
    # Generate a new access token
    new_access_token = create_access_token(user_data=token_details['user'])
    
    return JSONResponse(content={
        "message": "New access token generated successfully",
        "access_token": new_access_token
    })