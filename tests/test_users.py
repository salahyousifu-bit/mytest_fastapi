from fastapi.testclient import TestClient
from main import app
from datetime import timedelta
from security.jwt import create_access_token

client = TestClient(app)

def test_get_products():
    response = client.get("/")
    
    assert response.status_code == 200
    
def test_get_me_without_token():
    response = client.get("/users/me")
    
    assert response.status_code == 401
    
def test_get_me_with_token():
    token = create_access_token(data={"sub":"salah"}, expires_delta=timedelta(minutes=30))
    
    response = client.get("/users/me" , headers={ "Authorization": f"Bearer {token}"} )
    
    assert response.status_code == 200
    assert response.json()["username"]=="salah"
    
def test_get_me_with_invalled_token():
    token = create_access_token(data={"sub":"salah"}, expires_delta=timedelta(minutes=30))
    
    response = client.get("/users/me" , headers={"Authorization":"Bearer invalid-token"})
    
    assert response.status_code == 401
    
def test_admin_endpoint_forbidden_for_user():
    token = create_access_token(data={"sub":"ahmed"}, expires_delta=timedelta(minutes=30))
    
    respons = client.get("/users/admin" , headers={
            "Authorization": f"Bearer {token}"
        })
    assert respons.status_code ==403
    
def test_admin_endpoint_for_admin():
    token = create_access_token(data={"sub":"salah"}, expires_delta=timedelta(minutes=30))
    response = client.get("/users/admin" , headers={
            "Authorization": f"Bearer {token}"
        })
    assert response.status_code == 200
    assert response.json()["username"]=="salah"