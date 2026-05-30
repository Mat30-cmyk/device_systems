from fastapi import HTTPException
from app.data.user_db import users


def get_user_or_404(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


def validate_email_exists(email: str):

    for user in users:
        if user["email"] == email:
            raise HTTPException(
                status_code=400,
                detail="El correo ya existe"
            )