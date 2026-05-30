from fastapi import APIRouter, HTTPException, Response
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.data.user_db import users

from app.dependencies.user_dependencies import (
    get_user_or_404,
    validate_email_exists
)

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

@router.put("/{user_id}")
def update_user(
    user_data: UserCreate,
    user=Depends(get_user_or_404)
):

    validate_email_exists(user_data.email)

    user.update(user_data.model_dump())

    return user

@router.patch("/{user_id}")
def partial_update_user(
    user_data: UserUpdate,
    user=Depends(get_user_or_404)
):

    update_data = user_data.model_dump(
        exclude_unset=True
    )

    if not update_data:

        raise HTTPException(
            status_code=400,
            detail="No se enviaron datos para actualizar"
        )

    user.update(update_data)

    return user