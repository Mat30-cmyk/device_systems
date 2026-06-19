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
        from_attributes = True 

class DeviceInLoan(BaseModel):
    id: int
    name: str
    serial_number: str
    device_type: str

    class Config:
        from_attributes = True

class LoanDetailResponse(BaseModel):

    id: int
    status: str

    user: UserInLoan
    device: DeviceInLoan

    class Config:
        from_attributes = True