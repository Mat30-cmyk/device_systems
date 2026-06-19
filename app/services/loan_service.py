from typing import Optional

from fastapi import HTTPException, status
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
    return (
        db.query(Loan)
        .join(User)
        .join(Device)
        .all()
    )


def get_loan_by_id(
    db: Session,
    loan_id: int,
):

    loan = (
        db.query(Loan)
        .filter(Loan.id == loan_id)
        .first()
    )

    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Préstamo no encontrado"
        )

    return loan

# ==================================================
# CREAR PRÉSTAMO
# ==================================================

def create_loan(
    db: Session,
    loan_data: LoanCreate,
):

    user = (
        db.query(User)
        .filter(User.id == loan_data.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    device = (
        db.query(Device)
        .filter(Device.id == loan_data.device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dispositivo no encontrado"
        )

    if not device.is_available:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Dispositivo no disponible"
        )

    loan = Loan(
        user_id=loan_data.user_id,
        device_id=loan_data.device_id,
        status="active"
    )

    device.is_available = False

    db.add(loan)
    db.commit()
    db.refresh(loan)

    return loan


# ==================================================
# DEVOLVER PRÉSTAMO
# ==================================================

def return_loan(
    db: Session,
    loan_id: int,
):

    loan = (
        db.query(Loan)
        .filter(Loan.id == loan_id)
        .first()
    )

    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Préstamo no encontrado"
        )

    if loan.status == "returned":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El préstamo ya fue devuelto"
        )

    loan.status = "returned"

    device = (
        db.query(Device)
        .filter(Device.id == loan.device_id)
        .first()
    )

    if device:
        device.is_available = True

    db.commit()

    return {
        "message": "Préstamo devuelto correctamente"
    }


# ==================================================
# ELIMINAR PRÉSTAMO
# ==================================================

def delete_loan(
    db: Session,
    loan_id: int,
):

    loan = (
        db.query(Loan)
        .filter(Loan.id == loan_id)
        .first()
    )

    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Préstamo no encontrado"
        )

    db.delete(loan)
    db.commit()

def get_filtered_loans(
    db: Session,
    status: Optional[str] = None,
    user_email: Optional[str] = None,
    device_type: Optional[str] = None,
):

    query = (
        db.query(Loan)
        .join(User)
        .join(Device)
    )

    if status:
        query = query.filter(
            Loan.status == status
        )

    if user_email:
        query = query.filter(
            User.email.ilike(
                f"%{user_email}%"
            )
        )

    if device_type:
        query = query.filter(
            Device.device_type.ilike(
                f"%{device_type}%"
            )
        )

    return query.all()