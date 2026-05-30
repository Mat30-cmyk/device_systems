from fastapi import APIRouter, HTTPException, Response
from app.schemas.user_schema import UserCreate, UserResponse
from app.data.user_db import users
from app.services.user_service import (
    get_all_users,
    get_user_by_id,
    create_new_user
)

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def get_users(role: str = None, is_active: bool = None):

    return get_all_users(role, is_active)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):

    user = get_user_by_id(user_id)

    if user:
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

    new_user = create_new_user(
    user.model_dump()
    )

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    return new_user