from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./products.db")
session_local = sessionmaker(engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally : db.close()