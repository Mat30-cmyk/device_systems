# device_systems

## Descripción
Proyecto desarrollado con FastAPI para la gestión de usuarios mediante una API REST.  
En esta primera fase se realizó la configuración inicial del entorno de trabajo y la estructura base del proyecto.

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- Pydantic v2

---

## Estructura inicial del proyecto

```bash
device_systems/
│── app/
│   │── main.py
│
│── requirements.txt
│── README.md
```

### Creación del entorno virtual

```bash
python -m venv venv
```

### Activación del entorno virtual

```bash
device_systems\Scripts\activate
```

### Instalación de dependencias

```bash
pip install fastapi uvicorn
```

### Generación de requirements.txt

```bash
pip freeze > requirements.txt
```

### Ejecución del servidor

```bash
uvicorn app.main:app --reload
```

#### Resultado esperado

+ Servidor FastAPI funcionando correctamente en:

```bash
http://127.0.0.1:8000
```

+ Swagger UI:

```bash
http://127.0.0.1:8000/docs
```