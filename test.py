from datetime import timedelta

from security.jwt import create_access_token, decode_token

token = create_access_token(
    data={"sub": "ahmed"},
    expires_delta=timedelta(minutes=30)
)

print("Token:")
print(token)

payload = decode_token(token)

print("Payload:")
print(payload)

print("Subject:")
print(payload["sub"])