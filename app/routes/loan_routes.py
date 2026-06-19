from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)

from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db

from app.schemas.loan_schema import (
    LoanCreate,
    LoanDetailResponse,
    LoanResponse,
)
from fastapi import status
from app.models.loan_model import Loan

from app.services import loan_service

router = APIRouter(
    prefix="/loans",
    tags=["Préstamos"],
)


# ==================================================
# GET /loans
# ==================================================
@router.get(
    "/",
    response_model=list[LoanDetailResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar préstamos"
)
def get_loans(
    status_filter: Optional[str] = None,
    user_email: Optional[str] = None,
    device_type: Optional[str] = None,
    db: Session = Depends(get_db),
):

    return loan_service.get_filtered_loans(
        db=db,
        status=status_filter,
        user_email=user_email,
        device_type=device_type
    )

# ==================================================
# GET /loans/details
# ==================================================
@router.get(
    "/details",
    response_model=list[LoanDetailResponse],
    status_code=status.HTTP_200_OK,
    summary="Obtener detalles de todos los préstamos"
)
def get_loans_details(
    db: Session = Depends(get_db),
):

    return loan_service.get_all_loans_with_details(db)


# ==================================================
# GET /loans/{loan_id}
# ==================================================
@router.get(
    "/{loan_id}",
    response_model=LoanDetailResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener préstamo por ID"
)
def get_loan_by_id(
    loan_id: int,
    db: Session = Depends(get_db)
):

    return loan_service.get_loan_by_id(
        db,
        loan_id
    )


# ==================================================
# POST /loans
# ==================================================
@router.post(
    "/",
    response_model=LoanResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear préstamo"
)
def create_loan(
    loan_data: LoanCreate,
    db: Session = Depends(get_db)
):

    return loan_service.create_loan(
        db,
        loan_data
    )

# ==================================================
# PATCH /loans/{loan_id}/return
# ==================================================
@router.patch(
    "/{loan_id}/return",
    status_code=status.HTTP_200_OK,
    summary="Devolver préstamo"
)
def return_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):

    return loan_service.return_loan(
        db,
        loan_id
    )


# ==================================================
# DELETE /loans/{loan_id}
# ==================================================
@router.delete(
    "/{loan_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar préstamo"
)
def delete_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):

    loan_service.delete_loan(
        db,
        loan_id
    )

    return None
