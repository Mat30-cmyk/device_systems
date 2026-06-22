from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db

from app.schemas.auth_schema import (
    UserRegister,
    UserLogin,
    Token,
    UserResponse
)

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.models.user_model import User

from app.services.user_service import (
    get_user_by_email
)

from app.auth.auth_service import (
    register_user,
    authenticate_user
)

from app.auth.security import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["autenticación"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing = get_user_by_email(
        db,
        user.email
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email ya registrado"
        )

    return register_user(
        db,
        user
    )


@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    authenticated_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    token = create_access_token(
        {
            "sub": authenticated_user.email,
            "role": authenticated_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get(
    "/me",
    response_model=UserResponse
)
def me(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user