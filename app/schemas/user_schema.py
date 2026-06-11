from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from typing import Literal
from typing import Optional
from datetime import datetime

RoleType = Literal["admin", "support", "user"]

class UserCreate(BaseModel):

    name: str = Field(
        min_length=3
    )

    email: EmailStr

    role: RoleType

    is_active: bool = True


class UserUpdate(BaseModel):

    name: str = Field(
        min_length=3
    )

    email: EmailStr

    role: RoleType

    is_active: bool


class UserPatch(BaseModel):

    name: Optional[str] = None

    email: Optional[EmailStr] = None

    role: Optional[RoleType] = None

    is_active: Optional[bool] = None


class UserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }