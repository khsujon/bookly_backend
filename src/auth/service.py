from .models import User
from sqlmodel.ext.asyncio.session import AsyncSession




class UserService:
    """Service class for user-related operations."""
    
    #check if user exists by email
    async def get_user():
        pass