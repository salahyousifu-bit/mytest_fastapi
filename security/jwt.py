from datetime import datetime , timedelta , timezone
from fastapi import HTTPException
from config import settings

import jwt 

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

def create_access_token(data:dict , expires_delta:timedelta):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc)+expires_delta
    
    to_encode.update({"exp":expire})
    
    encoded_jwt = jwt.encode(
        to_encode ,
        SECRET_KEY ,
        algorithm=ALGORITHM
    )
    return encoded_jwt

def decode_token(token:str ):
    try:
        payload = jwt.decode(
                token ,
                SECRET_KEY,
                algorithms=[ALGORITHM] ,
                
            )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
        )    
    
    return payload