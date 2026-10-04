from fastapi import APIRouter , Depends
from schemas.users import UserResponse , UserCreate , Token
from services.users import create_user_service , login_user
from sqlalchemy.orm import Session 
from database.connection import get_db
from database.models import User
from security.oauth2 import get_current_user , require_admin

router = APIRouter()

@router.post("/" ,response_model=UserResponse )
def create_user_endpoint(user:UserCreate , db:Session = Depends(get_db)):
    return create_user_service(db=db , user=user)

from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login", response_model=Token)
def login_user_endpoint(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(
        db=db,
        username=form_data.username,
        password=form_data.password
    )

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return UserResponse(
    id=current_user.id,
    username=current_user.username
)
    
@router.get("/admin")
def admin_page(
    current_user: User = Depends(require_admin)
):
    return {
        "message": "Welcome admin",
        "username": current_user.username
    }