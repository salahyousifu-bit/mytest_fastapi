from database.connection import session_local
from database.models import Product

db = session_local()

product = Product(
    name="Mousa",
    price=250
)

db.add(product)

print(product.id)

db.commit()

print(product.id)

db.refresh(product)

print(product.id)

db.close()