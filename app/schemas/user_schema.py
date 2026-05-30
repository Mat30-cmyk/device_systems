from pydantic import BaseModel, EmailStr, Field
from typing import Literal
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    role: Literal["admin", "support", "user"]
    is_active: bool

class UserUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=3
    )

    email: Optional[EmailStr] = None

    role: Optional[
        Literal[
            "admin",
            "support",
            "user"
        ]
    ] = None

    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool
