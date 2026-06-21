from app.auth.security import *

print("SECRET_KEY =", SECRET_KEY)
print("ALGORITHM =", ALGORITHM)

password = "Admin123"

hashed = get_password_hash(password)

print("HASH:")
print(hashed)

print("\nVERIFICACION:")
print(
    verify_password(
        password,
        hashed
    )
)

token = create_access_token(
    {
        "sub": "admin@test.com"
    }
)

print("\nTOKEN:")
print(token)

print("\nDECODE:")
print(
    decode_access_token(token)
)