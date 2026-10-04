from database.models import User
from sqlalchemy.orm import Session
from sqlalchemy import select


def create_user(db:Session , username:str , hashed_password:str):
    user = User(
        username=username ,
        hashed_password=hashed_password
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def get_user_by_username(db:Session , username:str):
    stmt = select(User).filter_by(username=username)
    user = db.scalars(stmt).first()
    return user