# Device Systems V 3.0 FastAPI SQLAlchemy

## Descripción

Device Systems API es una aplicación desarrollada con FastAPI que permite la gestión de usuarios mediante una API REST. El proyecto implementa operaciones CRUD completas utilizando SQLAlchemy como ORM y SQLite como base de datos relacional.

La aplicación permite:

* Crear usuarios.
* Consultar usuarios.
* Buscar usuarios por ID.
* Filtrar usuarios por rol.
* Filtrar usuarios activos o inactivos.
* Actualizar usuarios de forma completa o parcial.
* Eliminar usuarios.
* Validar datos mediante Pydantic.
* Manejar errores mediante HTTPException.
* Documentar automáticamente la API con Swagger y ReDoc.

---

# Tecnologías utilizadas

* Python 3.x
* FastAPI
* SQLAlchemy
* SQLite
* Git
* GitHub
* Pydantic v2
* Uvicorn
* Swagger UI
* ReDoc
* Thunder Client

---

# Instalación

## Clonar repositorio

```bash
git https://github.com/Mat30-cmyk/device_systems
cd device_systems
```

## En tu maquina crea el entorno virtual

```bash
python -m venv device_systems_prueba
```

+ Luego borra todo lo que el codigo anterior alla creado en la carpeta device_systems y pasa todos los archivos y carpetas que alla clonado el codigo: git clone https://github.com/Mat30-cmyk/device_systems Al entorno virtual que creaste llamado device_systems_prueba

## Activar entorno virtual

Windows

```bash
cd device_systems_prueba
```

Windows

```bash
Scripts\activate
```

Linux / Mac

```bash
source device_systems/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución del proyecto

```bash
uvicorn app.main:app --reload
```

Servidor:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Estructura del proyecto

## Captura de la estructura del proyecto

![Captura de pantalla](/image/estructura_SQLAlchemy.png)

Estructura utilizada:

```text
device_systems/
│
├── app/
│   ├── database/
│   ├── dependencies/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── device_systems.db
├── requirements.txt
└── README.md
```

---

# Base de datos SQLite

## Captura de la base de datos generada

![Captura de pantalla](/image/DB_SQLite.png)

La base de datos utilizada es SQLite, la cual almacena la información de los usuarios en la tabla users.

Campos de la tabla:

| Campo      | Tipo     |
| ---------- | -------- |
| id         | Integer  |
| name       | String   |
| email      | String   |
| role       | String   |
| is_active  | Boolean  |
| created_at | DateTime |

---

# Documentación Swagger

## Captura de Swagger UI

![Captura de pantalla](/image/Swagger_SQLAlchemy.png)

## Captura de ReDoc

![Captura de pantalla](/image/Redoc_SQLAlchemy.png)

FastAPI genera automáticamente la documentación interactiva permitiendo probar todos los endpoints disponibles.

---

# Endpoints implementados

| Método | Endpoint    | Descripción           |
| ------ | ----------- | --------------------- |
| GET    | /users      | Listar usuarios       |
| GET    | /users/{id} | Consultar usuario     |
| POST   | /users      | Crear usuario         |
| PUT    | /users/{id} | Actualizar usuario    |
| PATCH  | /users/{id} | Actualización parcial |
| DELETE | /users/{id} | Eliminar usuario      |

---

# Evidencias de pruebas

## GET /users

![Captura de pantalla](/image/GET_SQLAlchemy.png)

Resultado:
Se listan todos los usuarios registrados en la base de datos.

---

## GET /users/{id}

![Captura de pantalla](/image/GET_ID_SQLAlchemy.png)

Resultado:
Se obtiene correctamente la información de un usuario específico.

---

## POST /users

![Captura de pantalla](/image/POST_SQLAlchemy.png)

Resultado:
Se registra un nuevo usuario y se retorna el código HTTP 201 Created.

---

## PUT /users/{id}

![Captura de pantalla](/image/PUT_ID_SQLAlchemy.png)

Resultado:
Se actualiza completamente la información de un usuario existente.

---

## PATCH /users/{id}

![Captura de pantalla](/image/PATCH_ID_SQLAlchemy.png)

Resultado:
Se actualizan únicamente los campos enviados por el cliente.

---

## DELETE /users/{id}

![Captura de pantalla](/image/DELETE_SQLAlchemy.png)

Resultado:
Se elimina correctamente un usuario existente.

---

# Evidencias de errores controlados

## Usuario no encontrado (404)

![Captura de pantalla](/image/ERROR_GET_ID_SQLAlchemy.png)

Ejemplo:

```json
{
    "detail": "Usuario no encontrado"
}
```

---

## Email duplicado (400)

![Captura de pantalla](/image/ERROR_EMAIL_DUPLICATE_SQLAlchemy.png)

Ejemplo:

```json
{
    "detail": "Email duplicado"
}
```

---

## Validación de datos inválidos (422)

![Captura de pantalla](/image/ERROR_VALIDACION_DATOS_SQLAlchemy.png)

Ejemplo:

```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "email"
      ],
      "msg": "value is not a valid email address: An email address must have an @-sign.",
      "input": "correo_malo",
      "ctx": {
        "reason": "An email address must have an @-sign."
      }
    },
    {
      "type": "literal_error",
      "loc": [
        "body",
        "role"
      ],
      "msg": "Input should be 'admin', 'support' or 'user'",
      "input": "hacker",
      "ctx": {
        "expected": "'admin', 'support' or 'user'"
      }
    }
  ]
}
```

---

## PUT a usuario inexistente (404)

![Captura de pantalla](/image/ERROR_PUT_USER_NOT_EXIST_SQLAlchemy.png)

Ejemplo:

```json
{
  "detail": "Usuario no encontrado"
}
```

---

## PATCH vacío (400)

![Captura de pantalla](/image/ERROR_PATCH_VACIO_SQLAlchemy.png)

Ejemplo:

```json
{
  "detail": "No hay datos para actualizar"
}
```

---

## PATCH a usuario inexistente (404)

![Captura de pantalla](/image/ERROR_PATCH_USER_INEXISTENTE_SQLAlchemy.png)

Ejemplo:

```json
{
  "detail": "Usuario no encontrado"
}
```

---

## DELETE a usuario inexistente (404)

![Captura de pantalla](/image/ERROR_DELETE_USER_INEXISTENTE_SQLAlchemy.png)

Ejemplo:

```json
{
  "detail": "Usuario no encontrado"
}
```

---

## Endpoints Implementados

| Método | Endpoint                | Descripción                                | Código Exitoso |
| ------ | ----------------------- | ------------------------------------------ | -------------- |
| GET    | `/users`                | Obtiene todos los usuarios registrados     | 200 OK         |
| GET    | `/users?role=admin`     | Filtra usuarios por rol                    | 200 OK         |
| GET    | `/users?is_active=true` | Filtra usuarios por estado activo/inactivo | 200 OK         |
| GET    | `/users/{user_id}`      | Obtiene un usuario específico por ID       | 200 OK         |
| POST   | `/users`                | Registra un nuevo usuario                  | 201 Created    |
| PUT    | `/users/{user_id}`      | Actualiza completamente un usuario         | 200 OK         |
| PATCH  | `/users/{user_id}`      | Actualiza parcialmente un usuario          | 200 OK         |
| DELETE | `/users/{user_id}`      | Elimina un usuario existente               | 204 No Content |

---

## Manejo de Errores y Excepciones

| Situación                                 | Código HTTP              | Mensaje                        |
| ----------------------------------------- | ------------------------ | ------------------------------ |
| Usuario no encontrado                     | 404 Not Found            | `Usuario no encontrado`        |
| Usuario inexistente al actualizar (PUT)   | 404 Not Found            | `Usuario no encontrado`        |
| Usuario inexistente al actualizar (PATCH) | 404 Not Found            | `Usuario no encontrado`        |
| Usuario inexistente al eliminar           | 404 Not Found            | `Usuario no encontrado`        |
| Correo electrónico duplicado              | 400 Bad Request          | `Email duplicado`              |
| Actualización parcial sin datos           | 400 Bad Request          | `No hay datos para actualizar` |
| Formato de email inválido                 | 422 Unprocessable Entity | Error generado por Pydantic    |
| Nombre menor a 3 caracteres               | 422 Unprocessable Entity | Error generado por Pydantic    |
| Rol no permitido                          | 422 Unprocessable Entity | Error generado por Pydantic    |
| Campos obligatorios faltantes             | 422 Unprocessable Entity | Error generado por Pydantic    |

---

# Diferencia entre SQLAlchemy y Pydantic

## Modelo SQLAlchemy

Los modelos SQLAlchemy representan las tablas de la base de datos y permiten realizar operaciones CRUD mediante el ORM.

Ejemplo:

```python
class User(Base):
    __tablename__ = "users"
```

Su función principal es interactuar directamente con la base de datos.

---

## Schema Pydantic

Los schemas Pydantic se utilizan para validar los datos de entrada y salida de la API.

Ejemplo:

```python
class UserCreate(BaseModel):
```

Su función principal es validar la información recibida y estructurar las respuestas enviadas al cliente.

---

## Diferencia principal

SQLAlchemy administra el almacenamiento de datos en la base de datos.

Pydantic valida y serializa los datos que ingresan y salen de la API.

---

# Reflexión final

Durante el desarrollo de esta actividad fue posible comprender cómo evolucionar una API REST desde una implementación básica en memoria hacia una solución con persistencia real utilizando SQLite y SQLAlchemy.

El uso de SQLAlchemy permitió abstraer las consultas SQL mediante un ORM, facilitando la manipulación de datos y mejorando la organización del código. Por otra parte, Pydantic permitió validar la información recibida, reduciendo errores y garantizando la integridad de los datos.

La persistencia es fundamental en una API porque permite conservar la información incluso después de reiniciar la aplicación. Gracias a esto, los datos pueden ser consultados, modificados y eliminados de forma permanente, simulando el comportamiento de sistemas reales utilizados en entornos empresariales.

Esta actividad fortaleció conocimientos sobre FastAPI, SQLAlchemy, SQLite, validaciones, manejo de errores, documentación automática y buenas prácticas para el desarrollo de servicios backend.

## Link Video Youtube Evidencia

```bash
https://youtu.be/xlYSTcp52CM
```
