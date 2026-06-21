from fastapi import FastAPI

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