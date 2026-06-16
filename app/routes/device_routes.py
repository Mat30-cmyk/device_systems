from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
)
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.schemas.device_schema import (
    DeviceCreate,
    DeviceResponse,
    DeviceUpdate,
)
from app.services.device_service import (
    create_device,
    delete_device,
    get_all_devices,
    get_device_by_id,
    patch_device,
    update_device,
)

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


# ==================================================
# GET /devices
# ==================================================
@router.get(
    "/",
    response_model=list[DeviceResponse],
    status_code=status.HTTP_200_OK,
)
def get_devices(
    device_type: Optional[str] = None,
    brand: Optional[str] = None,
    is_available: Optional[bool] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """
    Obtiene la lista de dispositivos.

    Filtros disponibles:
    - device_type
    - brand
    - is_available
    - search (búsqueda por nombre)
    """
    return get_all_devices(
        db=db,
        device_type=device_type,
        brand=brand,
        is_available=is_available,
        search=search,
    )


# ==================================================
# GET /devices/{device_id}
# ==================================================
@router.get(
    "/{device_id}",
    response_model=DeviceResponse,
    status_code=status.HTTP_200_OK,
)
def get_device(
    device_id: int,
    db: Session = Depends(get_db),
):
    device = get_device_by_id(db, device_id)

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device con ID {device_id} no encontrado.",
        )

    return device


# ==================================================
# POST /devices
# ==================================================
@router.post(
    "/",
    response_model=DeviceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_device(
    device_data: DeviceCreate,
    db: Session = Depends(get_db),
):
    return create_device(db, device_data)


# ==================================================
# PUT /devices/{device_id}
# ==================================================
@router.put(
    "/{device_id}",
    response_model=DeviceResponse,
    status_code=status.HTTP_200_OK,
)
def update_full_device(
    device_id: int,
    device_data: DeviceCreate,
    db: Session = Depends(get_db),
):
    device = update_device(db, device_id, device_data)

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device con ID {device_id} no encontrado para actualizar.",
        )

    return device


# ==================================================
# PATCH /devices/{device_id}
# ==================================================
@router.patch(
    "/{device_id}",
    response_model=DeviceResponse,
    status_code=status.HTTP_200_OK,
)
def patch_partial_device(
    device_id: int,
    device_data: DeviceUpdate,
    db: Session = Depends(get_db),
):
    device = patch_device(db, device_id, device_data)

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device con ID {device_id} no encontrado para modificar.",
        )

    return device


# ==================================================
# DELETE /devices/{device_id}
# ==================================================
@router.delete(
    "/{device_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_device(
    device_id: int,
    db: Session = Depends(get_db),
):
    success = delete_device(db, device_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device con ID {device_id} no encontrado para eliminar.",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)