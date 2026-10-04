from fastapi import APIRouter , Depends
from services.products import *
from schemas.products import *
from database.connection import get_db


router = APIRouter()

@router.post("/" , response_model=ProductResponse , status_code=201)
def create_product_endpoint(product:ProductCreate , db:Session = Depends(get_db)):
    return create_product(db = db , product = product)

@router.get("/" , response_model=list[ProductResponse] )
def get_products_endpoint(db:Session = Depends(get_db)):
    return get_all_products(db=db)

@router.get("/{product_id}" , response_model=ProductResponse)
def get_product_endpoint(product_id:int , db:Session = Depends(get_db)):
    return get_product(product_id , db)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(product_id:int , product:ProductUpdate , db:Session = Depends(get_db)):
    return update_product_service(product_id=product_id , name=product.name , price=product.price , db=db)

@router.delete("/{product_id}" , response_model=ProductResponse)
def delete_product_endpoint(product_id:int , db:Session = Depends(get_db)):
    return delete_product_service(product_id=product_id , db=db)