from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
    field_validator
)
from pydantic import BaseModel, Field
import re


class UserRegister(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100,
        description="Nombre del usuario"
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        description="Contraseña segura"
    )

    role: str = Field(
        description="Rol del usuario"
    )

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):

        if " " in value:
            raise ValueError(
                "La contraseña no puede contener espacios"
            )

        if not re.search(r"[A-Z]", value):
            raise ValueError(
                "Debe contener una mayúscula"
            )

        if not re.search(r"[a-z]", value):
            raise ValueError(
                "Debe contener una minúscula"
            )

        if not re.search(r"\d", value):
            raise ValueError(
                "Debe contener un número"
            )

        return value

    @field_validator("role")
    @classmethod
    def validate_role(cls, value):

        roles = [
            "admin",
            "support",
            "user"
        ]

        if value not in roles:
            raise ValueError(
                "Rol no permitido"
            )

        return value


class UserLogin(BaseModel):
    email: str = Field(
        example="juan@gmail.com"
    )

    password: str = Field(
        example="Password123"
    )


class Token(BaseModel):

    access_token: str

    token_type: str


class TokenData(BaseModel):

    email: str | None = None


class UserResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    name: str

    email: str

    role: str

    is_active: bool