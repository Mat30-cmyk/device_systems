from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.request_middleware import (
    log_requests
)
from app.database.connection import Base, engine

from app.auth.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router
from app.routes.device_routes import router as device_router
from app.routes.loan_routes import router as loan_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Gestión de Dispositivos",
    description="""
## API REST para Administración de Recursos Tecnológicos

Esta API permite gestionar:

- Usuarios
- Dispositivos
- Préstamos

Desarrollada con FastAPI, SQLAlchemy y SQLite.
    """,
    version="4.0.0",
    contact={
        "name": "Mateo Betancur Escobar",
        "email": "betancurmateo116@gmail.com"
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

app.middleware("http")(log_requests)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get(
    "/",
    tags=["Inicio"],
    summary="Página principal"
)
def home():
    return {
        "message": "Bienvenido al Sistema de Gestión de Dispositivos"
    }

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(device_router)
app.include_router(loan_router)