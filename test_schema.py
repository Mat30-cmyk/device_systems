from app.schemas.auth_schema import UserRegister

user = UserRegister(
    name="Mateo",
    email="mateo@test.com",
    password="123",
    role="admin"
)

print(user)