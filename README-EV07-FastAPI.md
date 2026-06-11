# device_systems V 1.0

Device Systems es una API REST desarrollada con FastAPI para la gestión de usuarios del sistema. Este proyecto fue realizado como evidencia de aprendizaje.

La aplicación implementa operaciones CRUD básicas enfocadas en el recurso users, utilizando buenas prácticas de desarrollo backend con FastAPI, validaciones de datos mediante Pydantic v2 y documentación automática con Swagger UI.

---

## Funcionalidades principales

- Registro de usuarios mediante endpoint POST.
- Consulta de usuarios mediante endpoints GET.
- Búsqueda de usuarios por ID.
- Filtros por rol y estado activo.
- Validación de datos con Pydantic.
- Prevención de correos duplicados.
- Uso de Path Parameters y Query Parameters.
- Response Models para respuestas estructuradas.
- Cabeceras HTTP personalizadas.
- Documentación interactiva con Swagger UI.

---

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic v2
- Swagger UI
- Thunder Client / Postman
- Git y GitHub

---

## Objetivo del proyecto

Aplicar los fundamentos de FastAPI para construir una API REST funcional, comprendiendo el manejo de rutas, validaciones, modelos de datos y pruebas de endpoints en un entorno backend moderno.

---

## Estructura inicial del proyecto

```bash
device_systems/
│   │── main.py
│   │
│   │── routes/
│   │   │──__init__.py 
│   │   │──user_routes.py
│   │
│   │── schemas/
│   │   │──__init__.py
│   │   │──user_schemas.py
│
│── image/
│
│── requirements.txt
│── README.md
```

### Creación del entorno virtual

```bash
python -m venv device_systems
```

+ Captura:

![Captura de pantalla](/image/entorno_virtual.png)

### Activación del entorno virtual

```bash
device_systems\Scripts\activate
```

+ Captura:

![Captura de pantalla](/image/activacion_entorno_virtual.png)

### Instalación de dependencias

```bash
pip install fastapi uvicorn email-validator
```

+ Captura:

![Captura de pantalla](/image/instalacion_dependencias.png)

![Captura de pantalla](/image/instalacion_dependencias_2.png)

### Generación de requirements.txt

```bash
pip freeze > requirements.txt
```

+ Captura:

![Captura de pantalla](/image/generacion_requirements.txt.png)

### Ejecución del servidor

```bash
uvicorn app.main:app --reload
```

+ Captura:

![Captura de pantalla](/image/ejecucion_servidor.png)

#### Resultado esperado

+ Servidor FastAPI funcionando correctamente en:

```bash
http://127.0.0.1:8000/
```

`Captura:`

![Captura de pantalla](/image/FastAPI_funcionando.png)

+ Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

`Captura:`

![Captura de pantalla](/image/Swagger_UI.png)

+ Metodos FastAPI Funcionando correctamente en:

## Tabla de Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /users | Obtener todos los usuarios |
| GET | /users/{user_id} | Obtener usuario por ID |
| GET | /users?role=admin | Filtrar usuarios por rol |
| GET | /users?is_active=true | Filtrar usuarios activos |
| POST | /users | Registrar un nuevo usuario |

`GET`: /users

```bash
http://localhost:8000/users
```

`Captura:`

![Captura de pantalla](/image/FastAPI_GET_users.png)

`GET`: /users/:ID

```bash
http://localhost:8000/users/3
```

`Captura:`

![Captura de pantalla](/image/FastAPI_GET_users_ID.png)

`POST`: /users

```bash
http://localhost:8000/users
```

`Captura:`

![Captura de pantalla](/image/FastAPI_POST_users.png)

`BODY`

```bash
{
  "name": "Danna Sofia",
  "email": "dannasof@gmail.com",
  "role": "user",
  "is_active": true
}
```

`GET`: /users?role=admin

```bash
http://localhost:8000/users?role=admin
```

`Captura:`

![Captura de pantalla](/image/FastAPI_GET_role=admin.png)

`GET` /users?role=admin&is_active=true

```bash
http://localhost:8000/users?is_active=true
```

`Captura:`

![Captura de pantalla](/image/FastAPI_GET_is_active=true.png)


## Video Youtube Evidencia

```bash
https://youtu.be/MMLlbfQdk44
```

## Autor

Desarrollado por Mateo Betancur Escobar 💻

Proyecto académico - SENA