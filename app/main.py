from fastapi import FastAPI

from app.database.connection import Base
from app.database.connection import engine

from app.routes.user_routes import router

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="device_systems API",
    description="API REST para gestión de usuarios",
    version="3.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "device_systems API"
    }