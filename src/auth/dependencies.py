from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException,status
from .utils import decode_access_token


class TokenBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super(TokenBearer, self).__init__(auto_error=auto_error)
    
    #Override the __call__ method to validate the token and ensure it's an access token
    async def __call__(self, request: Request)->HTTPAuthorizationCredentials|None:
        credential = await super().__call__(request)
        token = credential.credentials
        token_data = decode_access_token(token)
        if not self.token_validation(token):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
        
        return token_data
    
    #Validate token 
    def token_validation(self, token: str)->bool:
        token_data = decode_access_token(token)
        if token_data is None:
            return False
        return True
    

class AccessTokenBearer(TokenBearer):
    
    def verify_token_data(self, token_data:dict)->None:
        if token_data and token_data['refresh']:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type, access token required")