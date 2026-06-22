from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import status

from sqlalchemy.orm import Session
from app.auth.role_dependency import (
    require_roles
)

from app.dependencies.database_dependency import get_db

from app.schemas.user_schema import UserCreate
from app.schemas.user_schema import UserUpdate
from app.schemas.user_schema import UserPatch
from app.schemas.user_schema import UserResponse

from app.services.user_service import *

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"]
)


@router.get(
    "/",
    summary="Listar usuarios",
    response_model=list[UserResponse]
)
def get_users(
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):

    users = get_all_users(db)

    if role:
        users = [
            user for user in users
            if user.role == role
        ]

    if is_active is not None:
        users = [
            user for user in users
            if user.is_active == is_active
        ]

    return users


@router.get(
    "/{user_id}",
    summary="Obtener usuario por ID",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return user


@router.post(
    "/",
    summary="Crear nuevo usuario",
    response_model=UserResponse,
    status_code=201
)
def create_new_user(
    user: UserCreate,
    response: Response,
    db: Session = Depends(get_db)
):

    existing = get_user_by_email(
        db,
        user.email
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email duplicado"
        )

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    return create_user(
        db,
        user
    )


@router.put(
    "/{user_id}",
    summary="Actualizar usuario existente",
    response_model=UserResponse
)
def update_existing_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):

    user_db = get_user_by_id(
        db,
        user_id
    )

    if not user_db:
        raise HTTPException(
            404,
            "Usuario no encontrado"
        )

    return update_user(
        db,
        user_db,
        user
    )


@router.patch(
    "/{user_id}",
    summary="Actualizar parcialmente un usuario",
    response_model=UserResponse
)
def patch_existing_user(
    user_id: int,
    user: UserPatch,
    db: Session = Depends(get_db)
):

    user_db = get_user_by_id(
        db,
        user_id
    )

    if not user_db:
        raise HTTPException(
            404,
            "Usuario no encontrado"
        )

    data = user.model_dump(
        exclude_unset=True
    )

    if not data:
        raise HTTPException(
            400,
            "No hay datos para actualizar"
        )

    return patch_user(
        db,
        user_db,
        data
    )


@router.delete(
    "/{user_id}",
    summary="Eliminar un usuario",
    status_code=204
)
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(
        require_roles("admin")
    )
):

    user_db = get_user_by_id(
        db,
        user_id
    )

    if not user_db:
        raise HTTPException(
            404,
            "Usuario no encontrado"
        )

    delete_user(
        db,
        user_db
    )