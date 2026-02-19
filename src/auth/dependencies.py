from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request
from .utils import decode_access_token


class AccessTokenBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super(AccessTokenBearer, self).__init__(auto_error=auto_error)
        
    async def __call__(self, request: Request)->HTTPAuthorizationCredentials|None:
        credential = await super().__call__(request)
        
    
    def token_validation(self, token: str)->bool:
        
        token_data = decode_access_token(token)
        if token_data is None:
            return False
        return True