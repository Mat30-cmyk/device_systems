from fastapi import APIRouter

router = APIRouter(
    prefix="/security",
    tags=["seguridad"]
)

@router.get(
    "/info",
    summary="Información de seguridad",
    description="Muestra las características de seguridad implementadas en la API."
)
def security_info():
    return {
        "api": "device_systems",
        "authentication": "OAuth2 + JWT",
        "password_hashing": "Passlib + Bcrypt",
        "cors": True,
        "rate_limiting": True,
        "middleware": True,
        "roles": [
            "admin",
            "support",
            "user"
        ]
    }