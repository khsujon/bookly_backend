from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request



class AccessTokenBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super(AccessTokenBearer, self).__init__(auto_error=auto_error)
        
    async def __call__(self, request: Request)->HTTPAuthorizationCredentials|None:
        credential = await super().__call__(request)
        
        