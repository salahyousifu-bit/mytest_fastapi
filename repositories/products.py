from database.models import *
from sqlalchemy.orm import Session 
from sqlalchemy import select


products_db = []
def save_product(db:Session , name:str , price:float):
    product = Product(
        name = name ,
        price = price
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
    
def get_products(db:Session ):
    products = db.scalars(select(Product)).all()
    return products

def get_product_by_id(db:Session , product_id:int):
    return db.get(Product , product_id)

def update_product(db:Session , product_id:int , name:str , price:float):
   product = db.get(Product , product_id)
   if product is None:
       return None
   product.name = name 
   product.price = price
   
   db.commit()
   db.refresh(product)
   return product
    
def delete_product(db:Session, product_id):
    product = db.get(Product , product_id)
    if product is None:
        return None
    db.delete(product)
    db.commit()
   
    return product
    

def create_product(db:Session , name:str , price:float):
    product = Product(
        name = name ,
        price = price
    )
    db.add(product)
    

