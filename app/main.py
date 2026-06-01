from fastapi import FastAPI
from app.routes.user_routes import router

app = FastAPI(
    title="device_systems API",
    description="API REST para la gestión de usuarios",
    version="2.0.0",
    contact={
        "name": "Mateo Betancur Escobar"
    }
)

app.include_router(router)