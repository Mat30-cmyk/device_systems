from sqlalchemy.orm import Session

from app.models.user_model import User

from app.auth.security import (
    get_password_hash,
    verify_password
)


def register_user(
    db: Session,
    user_data
):

    hashed_password = get_password_hash(
        user_data.password
    )

    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password,
        role=user_data.role,
        is_active=True
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(
        password,
        user.hashed_password
    ):
        return None

    return user