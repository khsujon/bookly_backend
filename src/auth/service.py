from .models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select




class UserService:
    """Service class for user-related operations."""
    
    #check if user exists by email
    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.exec(statement)
        user = result.first()
        return user
    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)
        
        if user is None:
            return False
        return True