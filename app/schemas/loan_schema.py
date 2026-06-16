from pydantic import BaseModel
from typing import Optional

class LoanCreate(BaseModel):
    user_id: int
    device_id: int
    status: str = "active"

class LoanResponse(BaseModel):

    id: int
    user_id: int
    device_id: int
    status: str

    model_config = {
        "from_attributes": True
    }


# Esquemas anidados mínimos para la respuesta del detalle
class UserInLoan(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True # En Pydantic v1 era orm_mode = True

class LoanDetailResponse(BaseModel):

    id: int
    user_id: int
    device_id: int
    status: str
    user_name: str
    device_name: str

    model_config = {
        "from_attributes": True
    }

class DeviceInLoan(BaseModel):
    id: int
    name: str
    serial_number: str
    device_type: str

    class Config:
        from_attributes = True

# El esquema principal solicitado por la guía del SENA
class LoanDetailResponse(BaseModel):
    loan_id: int  # Asegúrate de que coincida con el nombre del atributo en tu modelo (ej. 'id' o 'loan_id')
    status: str
    user: UserInLoan
    device: DeviceInLoan

    class Config:
        from_attributes = True