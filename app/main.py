from fastapi import FastAPI

from app.database.connection import Base
from app.database.connection import engine

from app.routes.user_routes import router
from app.routes.device_routes import router as device_router
from app.routes.loan_routes import router as loan_router

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="device_systems API",
    description="API REST para gestión de usuarios",
    version="3.0.0"
)

@app.get("/")
def home():
    return {
        "message": "device_systems API"
    }

app.include_router(router)
app.include_router(device_router)
app.include_router(loan_router)
