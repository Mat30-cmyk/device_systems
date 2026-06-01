from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserUpdate
)

from app.services.user_service import (
    get_all_users,
    create_new_user,
    delete_user
)

from app.dependencies.user_dependencies import (
    get_user_or_404,
    validate_email_exists
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "",
    response_model=list[UserResponse]
)
def get_users(
    role: str = None,
    is_active: bool = None
):

    return get_all_users(role, is_active)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user=Depends(get_user_or_404)
):

    return user


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate
):

    validate_email_exists(user.email)

    return create_new_user(
        user.model_dump()
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_data: UserCreate,
    user=Depends(get_user_or_404)
):

    user.update(
        user_data.model_dump()
    )

    return user


@router.patch(
    "/{user_id}",
    response_model=UserResponse
)
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


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_user(
    user=Depends(get_user_or_404)
):

    delete_user(user)

    return