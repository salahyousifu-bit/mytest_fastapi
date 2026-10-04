from database.base import Base
from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy import String , Float

class Product(Base):
    __tablename__="products"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    price:Mapped[float] = mapped_column(Float)
    

class User(Base):
    __tablename__="users"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(100))
    hashed_password:Mapped[str] = mapped_column(String(250))
    role:Mapped[str] = mapped_column(String(20) , default="user" , server_default="user",nullable=False)