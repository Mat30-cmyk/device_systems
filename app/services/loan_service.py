from typing import Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models.device_model import Device
from app.models.loan_model import Loan
from app.models.user_model import User
from app.schemas.loan_schema import LoanCreate


# ==================================================
# CONSULTAS GENERALES
# ==================================================

def get_all_loans_with_details(db: Session):
    """
    Obtiene todos los préstamos incluyendo
    la información relacionada de usuarios y dispositivos.
    """
    return (
        db.query(Loan)
        .join(User)
        .join(Device)
        .all()
    )


def get_loans_by_user_id(
    db: Session,
    user_id: int,
):
    """
    Obtiene todos los préstamos
    asociados a un usuario.
    """
    return (
        db.query(Loan)
        .join(User)
        .filter(Loan.user_id == user_id)
        .all()
    )


def get_loans_by_device_id(
    db: Session,
    device_id: int,
):
    """
    Obtiene todos los préstamos
    asociados a un dispositivo.
    """
    return (
        db.query(Loan)
        .join(Device)
        .filter(Loan.device_id == device_id)
        .all()
    )


# ==================================================
# FILTROS AVANZADOS
# ==================================================

def get_filtered_loans(
    db: Session,
    status: Optional[str] = None,
    user_email: Optional[str] = None,
    device_type: Optional[str] = None,
):
    """
    Obtiene préstamos aplicando filtros dinámicos.

    Filtros disponibles:
    - status
    - user_email
    - device_type
    """

    query = (
        db.query(Loan)
        .join(User)
        .join(Device)
    )

    conditions = []

    if status:
        conditions.append(Loan.status == status)

    if user_email:
        conditions.append(
            User.email.ilike(f"%{user_email}%")
        )

    if device_type:
        conditions.append(
            Device.device_type.ilike(f"%{device_type}%")
        )

    if conditions:
        query = query.filter(
            and_(*conditions)
        )

    return query.all()


# ==================================================
# CREACIÓN DE PRÉSTAMOS
# ==================================================

def create_loan(
    db: Session,
    loan_data: LoanCreate,
):
    """
    Crea un nuevo préstamo.
    """

    db_loan = Loan(
        **loan_data.model_dump()
    )

    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)

    return db_loan