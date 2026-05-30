from fastapi import APIRouter, HTTPException, Response
from app.schemas.user_schema import UserCreate, UserResponse
from app.data.user_service import users

router = APIRouter()

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