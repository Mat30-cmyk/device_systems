from sqlalchemy.orm import Session

from app.models.user_model import User


def get_all_users(db: Session):

    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):

    return db.query(User).filter(
        User.id == user_id
    ).first()


def get_user_by_email(db: Session, email: str):

    return db.query(User).filter(
        User.email == email
    ).first()

def update_user(db: Session, user_db, user):

    user_db.name = user.name
    user_db.email = user.email
    user_db.role = user.role
    user_db.is_active = user.is_active

    db.commit()

    db.refresh(user_db)

    return user_db


def patch_user(db: Session, user_db, data):

    for key, value in data.items():
        setattr(user_db, key, value)

    db.commit()

    db.refresh(user_db)

    return user_db


def delete_user(db: Session, user_db):

    db.delete(user_db)

    db.commit()