# device_systems - FastAPI Intermedio

## Información General

**Proyecto:** device_systems
**Actividad:** GA1-220501096-01-AA1-EV08 – FastAPI Intermedio: Evolución de device_systems con CRUD Completo, Manejo de Errores, Swagger/OpenAPI y Dependency Injection.
**Versión:** 2.0.0

## Descripción

**device_systems** es una API REST desarrollada con FastAPI para la gestión de usuarios. Esta versión corresponde a la evolución del proyecto inicial, incorporando un CRUD completo, manejo profesional de errores, Dependency Injection mediante `Depends()`, documentación automática con Swagger/OpenAPI y una arquitectura organizada por capas.

La API permite:

* Crear usuarios.
* Listar usuarios.
* Consultar usuarios por ID.
* Filtrar usuarios por rol o estado.
* Actualizar usuarios completamente (PUT).
* Actualizar usuarios parcialmente (PATCH).
* Eliminar usuarios.
* Validar datos de entrada.
* Manejar errores mediante HTTPException.
* Documentar automáticamente los endpoints.

---

# Tecnologías Utilizadas

* Python 3.x
* FastAPI
* Uvicorn
* Pydantic v2
* Git
* GitHub
* Swagger UI
* ReDoc
* Thunder Client

---

# Estructura del Proyecto

```text
device_systems/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   └── user_routes.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   ├── dependencies/
│   │   └── user_dependencies.py
│   │
│   └── data/
│       └── user_db.py
│
├── image/
|
├── requirements.txt
└── README.md
```

---

# Arquitectura Utilizada

El proyecto está organizado siguiendo una arquitectura por capas, permitiendo una mejor separación de responsabilidades, mayor mantenibilidad del código y facilidad para escalar la aplicación en futuras versiones.

### routes

Contiene los endpoints de la API. Esta capa se encarga de recibir las solicitudes HTTP, procesar los parámetros enviados por el cliente y devolver las respuestas correspondientes. Además, conecta las peticiones con la lógica de negocio implementada en los servicios.

### schemas

Contiene los modelos Pydantic utilizados para validar y estructurar los datos de entrada y salida de la API. Gracias a estos modelos se garantiza que la información enviada por el cliente cumpla con las reglas definidas antes de ser procesada.

### services

Contiene la lógica de negocio de la aplicación. Aquí se implementan las operaciones principales relacionadas con la gestión de usuarios, como listar, crear, actualizar y eliminar registros. Esta separación permite reutilizar código y mantener las rutas más limpias.

### dependencies

Contiene funciones reutilizables implementadas mediante `Depends()`. Estas dependencias permiten centralizar validaciones y procesos comunes, como verificar la existencia de un usuario o validar correos electrónicos duplicados, evitando la repetición de código en múltiples endpoints.

### data

Simula una base de datos en memoria mediante una lista de usuarios almacenada en un archivo independiente. Esta capa funciona como fuente de datos temporal para realizar las operaciones CRUD sin necesidad de utilizar un sistema gestor de bases de datos real.

### Beneficios de esta arquitectura

- Separación clara de responsabilidades.
- Código más organizado y fácil de mantener.
- Mayor reutilización de funciones y validaciones.
- Facilita la implementación de nuevas funcionalidades.
- Permite migrar fácilmente a una base de datos real en futuras versiones.
- Sigue buenas prácticas utilizadas en proyectos backend profesionales con FastAPI.

---

# Instalación

## Clonar repositorio

```bash
git clone https://github.com/Mat30-cmyk/device_systems
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

# Ejecutar el Servidor

```bash
uvicorn app.main:app --reload
```

Servidor disponible en:

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

# Endpoints Disponibles

| Método | Endpoint    | Descripción                     |
| ------ | ----------- | ------------------------------- |
| GET    | /users      | Listar usuarios                 |
| GET    | /users/{id} | Obtener usuario por ID          |
| POST   | /users      | Crear usuario                   |
| PUT    | /users/{id} | Actualizar usuario completo     |
| PATCH  | /users/{id} | Actualizar usuario parcialmente |
| DELETE | /users/{id} | Eliminar usuario                |

---

# Ejemplos de Uso

## Crear Usuario

POST /users

```json
{
  "name": "Carlos",
  "email": "carlos@gmail.com",
  "role": "user",
  "is_active": true
}
```

Respuesta:

```json
{
  "id": 3,
  "name": "Carlos",
  "email": "carlos@gmail.com",
  "role": "user",
  "is_active": true
}
```

---

## Actualización Completa

PUT /users/1

```json
{
  "name": "Carlos Actualizado",
  "email": "carlos@gmail.com",
  "role": "admin",
  "is_active": true
}
```

---

## Actualización Parcial

PATCH /users/1

```json
{
  "role": "support"
}
```

---

## Eliminar Usuario

DELETE /users/1

Respuesta:

```text
204 No Content
```

---

# Códigos HTTP Utilizados

| Código | Significado          |
| ------ | -------------------- |
| 200    | OK                   |
| 201    | Created              |
| 204    | No Content           |
| 400    | Bad Request          |
| 404    | Not Found            |
| 422    | Unprocessable Entity |

---

# Manejo de Errores

La API implementa manejo de errores mediante HTTPException.

## Usuario no encontrado

```json
{
  "detail": "Usuario no encontrado"
}
```

## Correo duplicado

```json
{
  "detail": "El correo ya existe"
}
```

## PATCH vacío

```json
{
  "detail": "No se enviaron datos para actualizar"
}
```

## Datos inválidos

```json
{
  "detail": [
    {
      "type": "string_too_short"
    }
  ]
}
```

---

# Dependency Injection con Depends()

Para evitar duplicar lógica, se implementó Dependency Injection mediante Depends().

Ejemplo:

```python
def get_user_or_404(user_id: int):
    ...
```

Esta dependencia permite:

* Buscar usuarios por ID.
* Validar existencia del usuario.
* Reutilizar código en GET, PUT, PATCH y DELETE.
* Reducir duplicación de lógica.

Ejemplo de uso:

```python
user = Depends(get_user_or_404)
```

---

# Swagger y OpenAPI

FastAPI genera automáticamente la documentación interactiva de la API.

## Swagger UI

Agregar captura:

![Captura de pantalla](/image/swagger.png)

---

## ReDoc

Agregar captura:

![Captura de pantalla](/image/redoc.png)

---

# Evidencias de Pruebas

## GET /users

![Captura de pantalla](/image/FastAPI_GET_users.png)

## GET /users/{id}

![Captura de pantalla](/image/FastAPI_GET_users_ID.png)

## POST /users

![Captura de pantalla](/image/FastAPI_POST_users.png)

## PUT /users/{id}

![Captura de pantalla](/image/FastAPI_Intermedio_PUT_users.png)

## PATCH /users/{id}

![Captura de pantalla](/image/FastAPI_Intermedio_PATCH_users.png)

## DELETE /users/{id}

![Captura de pantalla](/image/FastAPI_Intermedio_DELETE_users.png)

---

# Evidencias de Manejo de Errores

## Usuario inexistente

![Captura de pantalla](/image/Usuario_No_Encontrado.png)

## Correo duplicado

![Captura de pantalla](/image/Correo_Duplicado.png)

## PATCH vacío

![Captura de pantalla](/image/PATCH_Vacio.png)

## Datos inválidos

![Captura de pantalla](/image/Datos_Invalidos.png)

---

# Conclusiones

Durante esta actividad se evolucionó la API inicial implementando operaciones CRUD completas para el recurso users.

Se aplicaron conceptos intermedios de FastAPI como:

* Dependency Injection mediante Depends().
* Manejo profesional de errores con HTTPException.
* Validaciones avanzadas con Pydantic.
* Códigos de estado HTTP adecuados.
* Documentación automática mediante Swagger/OpenAPI.
* Arquitectura organizada por capas.

Estas mejoras permiten construir APIs más mantenibles, reutilizables, escalables y alineadas con buenas prácticas de desarrollo backend.
