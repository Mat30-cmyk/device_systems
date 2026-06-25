# device_systems Security

## Información General

**Proyecto:** device_systems
**Actividad:** GA1-220501096-01-AA1-EV11 – FastAPI Seguridad: Autenticación, Middleware, CORS, Rate Limiting y Validación Avanzada.
**Versión:** 5.0.0

---

# Estructura del Proyecto

**Captura de la estructura del proyecto**

![Captura de pantalla](/image/EV11/Estructura_de_proyecto.png)

---

# Instalación de Dependencias

**Captura de las Dependencias Utilizadas**

![Captura de pantalla](/image/EV11/Instalacion_dependencias_1.png)

![Captura de pantalla](/image/EV11/Instalacion_dependencias_2.png)

# Actualización de Requirements

**Captura de Actualización de Requirements**

![Captura de pantalla](/image/generacion_requirements.txt.png)

---

# Migración Alembic Aplicada

## Generación de migración

Comando ejecutado:

```bash
alembic revision --autogenerate -m "add authentication fields to users"
```

**Captura de la generación de migración**

![Captura de pantalla](/image/EV11/Generar_la_migracion.png)

## Aplicación de migración

Comando ejecutado:

```bash
alembic upgrade head
```

**Captura de la migración aplicada**

![Captura de pantalla](/image/EV11/Luego_de_la_migracion.png)

---

# Registro de Usuario

Endpoint:

```http
POST /auth/register
```

Ejemplo de solicitud:

```json
{
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "password": "Password123",
  "role": "user"
}
```

**Captura del registro exitoso**

![Captura de pantalla](/image/EV11/Metodo_Register.png)

---

# Login y Token JWT

Endpoint:

```http
POST /auth/login
```

Ejemplo de solicitud:

```json
{
  "email": "juan@example.com",
  "password": "Password123"
}
```

Respuesta:

```json
{
  "access_token": "TOKEN_GENERADO",
  "token_type": "bearer"
}
```

**Captura del login exitoso y token generado**

![Captura de pantalla](/image/EV11/Metodo_Login_y_Token_con_JWT.png)

---

# Consulta del Usuario Autenticado

Endpoint:

```http
GET /auth/me
```

Header:

```http
Authorization: Bearer TOKEN_GENERADO
```

**Captura de la respuesta de /auth/me**

![Captura de pantalla](/image/EV11/Metodo_Login_Con_Token.png)

---

# Acceso Sin Token

Prueba realizada accediendo a una ruta protegida sin enviar token JWT.

Resultado esperado:

```http
401 Unauthorized
```

**Captura de acceso sin token**

![Captura de pantalla](/image/EV11/Metodo_Login_Sin_Token.png)

---

# Acceso con Rol No Permitido

Prueba realizada utilizando un usuario sin permisos suficientes.

Resultado esperado:

```http
403 Forbidden
```

**Captura de acceso con rol no permitido**

![Captura de pantalla](/image/EV11/Permiso_para_Eliminar_por_Rol.png)

---

# Swagger/OpenAPI con OAuth2

Documentación disponible en:

```http
/docs
```

y

```http
/redoc
```

**Captura de Swagger/OpenAPI mostrando autenticación OAuth2**

**Swagger**

![Captura de pantalla](/image/EV11/Swagger_1.png)

![Captura de pantalla](/image/EV11/Swagger_2.png)

**Redoc**

![Captura de pantalla](/image/EV11/Redocs.png)

---

# Middleware Personalizado

Middleware implementado para:

* Medición de tiempo de respuesta.
* Generación de Request ID.
* Cabeceras personalizadas.

Cabeceras generadas:

```http
X-App-Name: device_systems
X-Process-Time: 0.0042
X-Request-ID: 8f42e9c1
```

**Captura de las cabeceras generadas**

![Captura de pantalla](/image/EV11/Middleware_Personalizado.png)

---

# Rate Limiting

Rate limiting implementado mediante SlowAPI.

Ejemplo:

```http
POST /auth/login
```

Límite configurado:

```text
5 solicitudes por minuto
```

Resultado al superar el límite:

```http
429 Too Many Requests
```

**Captura de la activación del rate limiting**

![Captura de pantalla](/image/EV11/Rate_Limit.png)

---

# Configuración CORS

Configuración aplicada:

```python
allow_origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

allow_credentials = True
allow_methods = ["*"]
allow_headers = ["*"]
```

## Explicación

Durante el desarrollo se permitieron orígenes específicos para facilitar la comunicación con aplicaciones frontend locales.

No se recomienda utilizar `"*"` en producción cuando se manejan credenciales porque permitiría solicitudes desde cualquier origen, aumentando los riesgos de seguridad y exposición de información sensible.

---

# Reflexión Final

La implementación de seguridad en APIs REST es fundamental para proteger la información y controlar el acceso a los recursos del sistema.

Durante esta actividad se aplicaron mecanismos de autenticación mediante JWT, almacenamiento seguro de contraseñas usando hash con Passlib, autorización basada en roles, validaciones avanzadas con Pydantic v2, middleware para trazabilidad de peticiones, configuración CORS y rate limiting para prevenir abusos.

Estas prácticas permiten construir APIs más seguras, escalables y alineadas con estándares utilizados en entornos reales de desarrollo backend.

# Video De Socialización EV11

```text
https://youtu.be/9v-cZZh1Aws
```