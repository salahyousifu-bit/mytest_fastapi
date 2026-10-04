from security.password import hash_password , verify_password

def test_password_verification():
    password = "123456"
    
    hashed_password = hash_password(password)
    
    assert verify_password(password , hashed_password) is True
    
    assert verify_password("wrong-password" , hashed_password) is False