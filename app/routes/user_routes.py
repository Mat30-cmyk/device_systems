from fastapi import APIRouter, HTTPException, Response
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

users = [
    {
        "id": 1,
        "name": "Teo",
        "email": "teo@gmail.com",
        "role": "admin",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Carlos Ramirez",
        "email": "carlos@gmail.com",
        "role": "user",
        "is_active": True
    },
    {
        "id": 3,
        "name": "Laura Martinez",
        "email": "laura@gmail.com",
        "role": "support",
        "is_active": False
    },
    {
        "id": 4,
        "name": "Andres Gomez",
        "email": "andres@gmail.com",
        "role": "user",
        "is_active": True
    },
    {
        "id": 5,
        "name": "Valentina Rios",
        "email": "valentina@gmail.com",
        "role": "admin",
        "is_active": True
    },
    {
        "id": 6,
        "name": "Mateo Diaz",
        "email": "mateo@gmail.com",
        "role": "user",
        "is_active": False
    },
    {
        "id": 7,
        "name": "Camila Torres",
        "email": "camila@gmail.com",
        "role": "support",
        "is_active": True
    },
    {
        "id": 8,
        "name": "Sebastian Lopez",
        "email": "sebastian@gmail.com",
        "role": "user",
        "is_active": True
    },
    {
        "id": 9,
        "name": "Daniela Castro",
        "email": "daniela@gmail.com",
        "role": "support",
        "is_active": False
    },
    {
        "id": 10,
        "name": "Juan Perez",
        "email": "juan@gmail.com",
        "role": "user",
        "is_active": True
    },
    {
        "id": 11,
        "name": "Sara Moreno",
        "email": "sara@gmail.com",
        "role": "admin",
        "is_active": True
    },
    {
        "id": 12,
        "name": "Felipe Vargas",
        "email": "felipe@gmail.com",
        "role": "user",
        "is_active": False
    },
    {
        "id": 13,
        "name": "Natalia Ruiz",
        "email": "natalia@gmail.com",
        "role": "support",
        "is_active": True
    },
    {
        "id": 14,
        "name": "David Herrera",
        "email": "david@gmail.com",
        "role": "user",
        "is_active": True
    },
    {
        "id": 15,
        "name": "Maria Fernandez",
        "email": "maria@gmail.com",
        "role": "admin",
        "is_active": False
    }
]


@router.get("/users", response_model=list[UserResponse])
def get_users(role: str = None, is_active: bool = None):

    filtered_users = users

    if role is not None:
        filtered_users = [
            user for user in filtered_users
            if user["role"] == role
        ]

    if is_active is not None:
        filtered_users = [
            user for user in filtered_users
            if user["is_active"] == is_active
        ]

    return filtered_users


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, response: Response):

    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400,
                detail="El correo ya existe"
            )

    new_user = {
        "id": len(users) + 1,
        **user.model_dump()
    }

    users.append(new_user)

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    return new_user