from schemas.users import UserResponse , UserCreate , Token
from sqlalchemy.orm import Session
from repositories.users import create_user , get_user_by_username
from security.password import hash_password , verify_password
from fastapi import HTTPException
from security.jwt import create_access_token
from datetime import timedelta

def create_user_service(db:Session , user:UserCreate)-> UserResponse:
    hashed_password =hash_password(user.password)
    saved_user = create_user(db = db , username = user.username , hashed_password=hashed_password)
    return UserResponse(id=saved_user.id , username=saved_user.username)

def authenticate_user(db:Session , username:str , password:str):
    user= get_user_by_username(db=db , username=username)
    if user is None or not verify_password(password=password , hashed_password=user.hashed_password):
        raise HTTPException(
            status_code=401 ,
            detail="username or password not correct"
        )
    return user

def login_user(db:Session ,username:str , password:str)->Token:
    user= authenticate_user(db=db , username=username , password=password)
    token =  create_access_token(data={"sub":user.username}, expires_delta=timedelta(minutes=30))
    return Token(
        access_token=token,
        token_type="bearer"
    )