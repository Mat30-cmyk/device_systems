from typing import Optional

from sqlalchemy.orm import Session

from app.models.device_model import Device
from app.schemas.device_schema import (
    DeviceCreate,
    DeviceUpdate,
)


# ==================================================
# CONSULTAS GENERALES
# ==================================================

def get_all_devices(
    db: Session,
    device_type: Optional[str] = None,
    brand: Optional[str] = None,
    is_available: Optional[bool] = None,
    search: Optional[str] = None,
) -> list[Device]:
    """
    Obtiene todos los dispositivos aplicando
    filtros opcionales.
    """

    query = db.query(Device)

    if device_type:
        query = query.filter(
            Device.device_type == device_type
        )

    if brand:
        query = query.filter(
            Device.brand.ilike(f"%{brand}%")
        )

    if is_available is not None:
        query = query.filter(
            Device.is_available == is_available
        )

    if search:
        query = query.filter(
            Device.name.ilike(f"%{search}%")
        )

    return query.all()


def get_device_by_id(
    db: Session,
    device_id: int,
) -> Optional[Device]:
    """
    Busca un dispositivo por su ID.
    """

    return (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )


# ==================================================
# CREACIÓN
# ==================================================

def create_device(
    db: Session,
    device_data: DeviceCreate,
) -> Device:
    """
    Crea un nuevo dispositivo.
    """

    db_device = Device(
        **device_data.model_dump()
    )

    db.add(db_device)
    db.commit()
    db.refresh(db_device)

    return db_device


# ==================================================
# ACTUALIZACIÓN COMPLETA (PUT)
# ==================================================

def update_device(
    db: Session,
    device_id: int,
    device_data: DeviceCreate,
) -> Optional[Device]:
    """
    Actualiza completamente un dispositivo.
    """

    db_device = get_device_by_id(
        db,
        device_id,
    )

    if not db_device:
        return None

    for key, value in device_data.model_dump().items():
        setattr(db_device, key, value)

    db.commit()
    db.refresh(db_device)

    return db_device


# ==================================================
# ACTUALIZACIÓN PARCIAL (PATCH)
# ==================================================

def patch_device(
    db: Session,
    device_id: int,
    device_data: DeviceUpdate,
) -> Optional[Device]:
    """
    Actualiza únicamente los campos
    enviados por el cliente.
    """

    db_device = get_device_by_id(
        db,
        device_id,
    )

    if not db_device:
        return None

    update_data = device_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_device, key, value)

    db.commit()
    db.refresh(db_device)

    return db_device


# ==================================================
# ELIMINACIÓN
# ==================================================

def delete_device(
    db: Session,
    device_id: int,
) -> bool:
    """
    Elimina un dispositivo.

    Retorna:
        True  -> si fue eliminado
        False -> si no existe
    """

    db_device = get_device_by_id(
        db,
        device_id,
    )

    if not db_device:
        return False

    db.delete(db_device)
    db.commit()

    return True