from fastapi import FastAPI
from app.routes.user_routes import router

app = FastAPI(
    title="device_systems API"
)

app.include_router(router)