from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    status,
)
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.schemas.loan_schema import (
    LoanCreate,
    LoanDetailResponse,
    LoanResponse,
)
from app.services import loan_service

router = APIRouter(
    prefix="/loans",
    tags=["Loans"],
)


# ==================================================
# GET /loans
# ==================================================
@router.get(
    "/",
    response_model=List[LoanDetailResponse],
    status_code=status.HTTP_200_OK,
)
def get_loans(
    status: Optional[str] = None,
    user_email: Optional[str] = None,
    device_type: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
    Obtiene préstamos aplicando filtros opcionales.

    Filtros disponibles:
    - status
    - user_email
    - device_type
    """
    return loan_service.get_filtered_loans(
        db=db,
        status=status,
        user_email=user_email,
        device_type=device_type,
    )


# ==================================================
# GET /loans/details
# ==================================================
@router.get(
    "/details",
    response_model=List[LoanDetailResponse],
    status_code=status.HTTP_200_OK,
)
def get_loans_details(
    db: Session = Depends(get_db),
):
    """
    Retorna todos los préstamos junto con la
    información relacionada de usuarios y dispositivos.
    """
    return loan_service.get_all_loans_with_details(db)


# ==================================================
# GET /loans/users/{user_id}
# ==================================================
@router.get(
    "/users/{user_id}",
    response_model=List[LoanDetailResponse],
    status_code=status.HTTP_200_OK,
)
def get_loans_by_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    """
    Obtiene todos los préstamos asociados
    a un usuario específico.
    """
    return loan_service.get_loans_by_user_id(db, user_id)


# ==================================================
# GET /loans/devices/{device_id}
# ==================================================
@router.get(
    "/devices/{device_id}",
    response_model=List[LoanDetailResponse],
    status_code=status.HTTP_200_OK,
)
def get_loans_by_device(
    device_id: int,
    db: Session = Depends(get_db),
):
    """
    Obtiene todos los préstamos asociados
    a un dispositivo específico.
    """
    return loan_service.get_loans_by_device_id(db, device_id)


# ==================================================
# POST /loans
# ==================================================
@router.post(
    "/",
    response_model=LoanResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_loan(
    loan_data: LoanCreate,
    db: Session = Depends(get_db),
):
    """
    Crea un nuevo préstamo.
    """
    return loan_service.create_loan(db, loan_data)
