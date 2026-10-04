from database.connection import session_local
from repositories.users import get_user_by_username


db = session_local()

user = get_user_by_username(
    db=db,
    username="salah"
)

if user is None:
    print("User not found")
else:
    user.role = "admin"
    db.commit()
    print("User is now admin")

db.close()