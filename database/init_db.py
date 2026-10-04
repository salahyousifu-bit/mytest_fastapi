from database.base import Base
from database.connection import engine
from database.models import Product , User

Base.metadata.create_all(engine)