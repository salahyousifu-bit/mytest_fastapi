from fastapi import FastAPI
from routers.products import router as products
from routers.users import router as users

app = FastAPI()


app.include_router(products , prefix="/products",tags=["products"])
app.include_router(users , prefix="/users" , tags=["users"] )
@app.get("/")
def read_root():
    return {
         "message": "مرحباً بك في تطبيق FastAPI الخاص بي!",
        "status": "السيرفر يعمل بنجاح، توجه إلى /docs لرؤية المسارات"
    }
