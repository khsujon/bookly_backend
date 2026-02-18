from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from src.config import Config
import uuid
import logging

password_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRY = 60

# Utility function to hash passwords
def generate_password_hash(password: str) -> str:
    hash= password_context.hash(password)
    return hash

# Utility function to verify passwords
def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)

# CREATE ACCESS TOKEN
def create_access_token(user_data:dict, expiry:timedelta=None, refresh:bool=False):
    payload = {}
    payload['user']= user_data
    payload['exp'] = int((datetime.now() + (expiry if expiry is not None else timedelta(minutes=ACCESS_TOKEN_EXPIRY))).timestamp())
    payload['jti'] = str(uuid.uuid4())
    payload['refresh'] = refresh
    
    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET_KEY,
        algorithm=Config.JWT_ALGORITHM, 
    )
    return token


def decode_access_token(token:str)-> dict:
    try:
        token_data = jwt.decode(
            token,
            key=Config.JWT_SECRET_KEY,
            algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data
    except jwt.PyJWTError as e:
        logging.exception("Error decoding JWT token: %s", e)
        return None