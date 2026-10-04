from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from security.jwt import decode_token
from repositories.users import get_user_by_username
from database.models import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="users/login"
)

def get_current_user(token:str = Depends(oauth2_scheme) , db:Session = Depends(get_db)):
    payload = decode_token(token=token)
    
    username = payload.get("sub")
    if username is None :
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    user = get_user_by_username(db=db , username=username)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="user is not found"
        
        )
    return user  

def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user