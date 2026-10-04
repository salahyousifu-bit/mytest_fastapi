from fastapi import HTTPException
from schemas.products import ProductCreate , ProductResponse
from repositories.products import *


def create_product(db:Session , product:ProductCreate)->ProductResponse:
   data = save_product(db=db , name=product.name , price = product.price )
   return ProductResponse(
       id=data.id ,
       name = data.name ,
       price = data.price 
   )
def get_all_products(db:Session)->list[ProductResponse]:
    result = []
    products = get_products(db)
    for product in products:
        result.append(ProductResponse(
            id=product.id ,
            name=product.name,
            price=product.price
        ))
        
    return result
        

def get_product(product_id:int , db:Session)->ProductResponse:
    product = get_product_by_id(db,product_id)
    if product is None :
        raise HTTPException(
            status_code=404,
            detail="product not found"
        )
    return ProductResponse(
        id=product.id,
        name=product.name,
        price=product.price
    )

def update_product_service(db:Session , product_id:int, name:str , price:float)->ProductResponse:
    product = update_product(db , product_id , name , price)
    if product is None:
        raise HTTPException(
            status_code = 404 ,
            detail="product not found"
        )
    return ProductResponse(
        id = product.id,
        name = product.name,
        price = product.price
    )
    
def delete_product_service(db:Session , product_id:int)->ProductResponse:
    product = delete_product(db =db , product_id = product_id)
    if product is None:
        raise HTTPException(
            status_code=404 , 
            detail = "product not found"
        )
    return ProductResponse(
        id = product.id ,
        name =product.name ,
        price = product.price
    )