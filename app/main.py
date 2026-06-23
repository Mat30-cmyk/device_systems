from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.request_middleware import (
    log_requests
)
from app.database.connection import Base, engine

from app.middlewares.request_middleware import log_requests
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.middlewares.rate_limit import limiter

from app.auth.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router
from app.routes.device_routes import router as device_router
from app.routes.loan_routes import router as loan_router
from app.routes.security_routes import router as security_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="device_systems API",
    description="""
API REST segura para gestión de usuarios, dispositivos y préstamos.

### Funcionalidades

- Autenticación con OAuth2 + JWT
- Gestión de usuarios
- Gestión de dispositivos
- Gestión de préstamos
- Control de acceso por roles
- Rate Limiting
- Middleware personalizado
- Configuración CORS

### Seguridad

Las rutas protegidas requieren un token JWT válido.
""",
    version="5.0.0",
    contact={
        "name": "Mateo Betancur Escobar",
        "email": "betancurmateo116@gmail.com"
    },
    docs_url=None,          # <- desactivamos el docs por defecto
    redoc_url="/redoc"
)


# --- Swagger UI personalizado con traducción al español ---

TRADUCCIONES_JS = """
<script>
const traducciones = {
    "Available authorizations": "Autorizaciones disponibles",
    "Authorize": "Autorizar",
    "Authorized": "Autorizado",
    "Close": "Cerrar",
    "Logout": "Cerrar sesión",
    "Value:": "Valor:",
    "Cancel": "Cancelar",
    "Try it out": "Probar",
    "Execute": "Ejecutar",
    "Clear": "Limpiar",
    "Responses": "Respuestas",
    "Parameters": "Parámetros",
    "Request body": "Cuerpo de la petición",
    "Schemas": "Esquemas",
    "No parameters": "Sin parámetros",
    "Send empty value": "Enviar valor vacío",
    "Loading ...": "Cargando ...",
};

function traducirNodo(nodo) {
    if (nodo.nodeType === Node.TEXT_NODE) {
        const texto = nodo.textContent.trim();
        if (traducciones[texto]) {
            nodo.textContent = nodo.textContent.replace(texto, traducciones[texto]);
        }
    } else {
        nodo.childNodes.forEach(traducirNodo);
    }
}

const observer = new MutationObserver(() => {
    traducirNodo(document.body);
});
observer.observe(document.body, { childList: true, subtree: true });
</script>
"""

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    html = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Docs"
    ).body.decode()

    html = html.replace("</body>", TRADUCCIONES_JS + "</body>")
    return HTMLResponse(html)


app.state.limiter = limiter

app.add_middleware(
    SlowAPIMiddleware
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
app.include_router(security_router)
app.include_router(user_router)
app.include_router(device_router)
app.include_router(loan_router)