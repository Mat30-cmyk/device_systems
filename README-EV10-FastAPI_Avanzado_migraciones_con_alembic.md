# EV10 - V 4.0 - Persistencia Avanzada y Relaciones con SQLAlchemy

---

# Descripción del Proyecto

Device Systems es una API REST desarrollada con FastAPI y SQLAlchemy para gestionar usuarios, dispositivos y préstamos tecnológicos dentro de una organización.

El sistema permite:

* Registrar usuarios.
* Registrar dispositivos.
* Gestionar préstamos de dispositivos.
* Realizar devoluciones.
* Consultar información mediante relaciones entre tablas.
* Aplicar filtros avanzados.
* Gestionar la base de datos mediante migraciones con Alembic.

---

# Tecnologías Utilizadas

* Python 3.x
* FastAPI
* SQLAlchemy
* SQLite
* Alembic
* Pydantic
* Swagger UI
* Uvicorn

---

# Configuración de Alembic

## Inicialización de Alembic

Comando ejecutado:

```bash
alembic init alembic
```

### Evidencia

![Captura de pantalla](/image/EV10/inicializacion_de_alembic.png)

---

## Generación de Migración

Comando ejecutado:

```bash
alembic revision --autogenerate -m "create users devices loans"
```

### Evidencia

![Captura de pantalla](/image/EV10/CREAR_MIGRACIÓN.png)

---

## Aplicación de Migraciones

Comando ejecutado:

```bash
alembic upgrade head
```

### Evidencia

![Captura de pantalla](/image/EV10/APLICACION_MIGRACION.png)

---

## Historial de Migraciones

Comando ejecutado:

```bash
alembic history
```

### Evidencia

![Captura de pantalla](/image/EV10/HISTORIAL.png)

---

# Estructura de Base de Datos

El sistema utiliza tres entidades principales:

## Tabla Users

| Campo      | Tipo     |
| ---------- | -------- |
| id         | Integer  |
| name       | String   |
| email      | String   |
| role       | String   |
| is_active  | Boolean  |
| created_at | DateTime |

---

## Tabla Devices

| Campo         | Tipo     |
| ------------- | -------- |
| id            | Integer  |
| name          | String   |
| serial_number | String   |
| device_type   | String   |
| brand         | String   |
| is_available  | Boolean  |
| created_at    | DateTime |

---

## Tabla Loans

| Campo       | Tipo     |
| ----------- | -------- |
| id          | Integer  |
| user_id     | Integer  |
| device_id   | Integer  |
| loan_date   | DateTime |
| return_date | DateTime |
| status      | String   |

---

## Relación Entre Tablas

* Un usuario puede tener múltiples préstamos.
* Un dispositivo puede tener múltiples préstamos.
* Un préstamo pertenece a un usuario.
* Un préstamo pertenece a un dispositivo.

### Evidencia de la Base de Datos

![Captura de pantalla](/image/EV10/DB_SQLite.png)

---

# Documentación Swagger

La documentación interactiva fue generada automáticamente mediante Swagger UI.

### Evidencia

![Captura de pantalla](/image/EV10/Swagger_UI_General.png)

![Captura de pantalla](/image/EV10/Swagger_UI_Device.png)

![Captura de pantalla](/image/EV10/Swagger_UI_loan.png)

---

# Creación de Usuarios

Endpoint:

```http
POST /users
```

### Evidencia

![Captura de pantalla](/image/EV10/Creacion_de_usuarios.png)

---

# Creación de Dispositivos

Endpoint:

```http
POST /devices
```

### Evidencia

![Captura de pantalla](/image/EV10/Creacion_de_dispositivos.png)

---

# Creación de Préstamos

Endpoint:

```http
POST /loans
```

### Evidencia

![Captura de pantalla](/image/EV10/Creacion_de_prestamo.png)

---

# Consultas con Relaciones (JOIN)

## Consulta de Detalles de Préstamos

Endpoint:

```http
GET /loans/details
```

Esta consulta permite obtener información relacionada entre usuarios, dispositivos y préstamos mediante relaciones configuradas en SQLAlchemy.

### Evidencia

![Captura de pantalla](/image/EV10/Consulta_de_Detalles_de_Préstamos.png)

---

# Filtros Implementados

## Filtrar por Estado

Endpoint:

```http
GET /loans?status=active
```

### Evidencia

![Captura de pantalla](/image/EV10/Filtrar_por_Estado.png)

---

## Filtrar por Correo del Usuario

Endpoint:

```http
GET /loans?user_email=aprendiz@sena.edu.co
```

### Evidencia

![Captura de pantalla](/image/EV10/Filtrar_por_Correo_del_Usuario.png)

---

## Filtrar por Tipo de Dispositivo

Endpoint:

```http
GET /loans?device_type=laptop
```

### Evidencia

![Captura de pantalla](/image/EV10/Filtrar_por_Tipo_de_Dispositivo.png)

---

# Devolución de Dispositivos

Endpoint:

```http
PATCH /loans/{loan_id}/return
```

Este endpoint permite registrar la devolución de un dispositivo prestado y actualizar automáticamente su disponibilidad.

### Evidencia

![Captura de pantalla](/image/EV10/Devolución_de_Dispositivos.png)

---

# Manejo de Errores

Durante el desarrollo se implementaron validaciones para garantizar la integridad de los datos.

## Usuario inexistente

```http
POST /loans
```

Respuesta:

```json
{
  "detail": "Usuario no encontrado"
}
```

### Evidencia

![Captura de pantalla](/image/EV10/Usuario_inexistente.png)

---

## Dispositivo inexistente

Respuesta:

```json
{
  "detail": "Dispositivo no encontrado"
}
```

### Evidencia

![Captura de pantalla](/image/EV10/Dispositivo_inexistente.png)

---

## Dispositivo no disponible

Respuesta:

```json
{
  "detail": "Dispositivo no disponible"
}
```

### Evidencia

![Captura de pantalla](/image/EV10/Dispositivo_no_disponible.png)

---

## Préstamo inexistente

Respuesta:

```json
{
  "detail": "Préstamo no encontrado"
}
```

### Evidencia

![Captura de pantalla](/image/EV10/prestamo_inexistente.png)

---

## Préstamo ya devuelto

Respuesta:

```json
{
  "detail": "El préstamo ya fue devuelto"
}
```

### Evidencia

![Captura de pantalla](/image/EV10/Préstamo_ya_devuelto.png)

---

# Conclusiones y Reflexión

La implementación de migraciones mediante Alembic permitió gestionar de manera organizada la evolución de la base de datos, facilitando la creación y modificación de estructuras sin afectar la integridad de la información.

Las relaciones establecidas con SQLAlchemy simplificaron la conexión entre usuarios, dispositivos y préstamos, permitiendo representar escenarios reales mediante claves foráneas y relaciones ORM.

Las consultas avanzadas y los filtros implementados mejoraron significativamente la capacidad de búsqueda y recuperación de información, permitiendo obtener datos relacionados de forma eficiente.

Finalmente, esta actividad permitió comprender la importancia de la persistencia avanzada, las migraciones controladas y el uso de relaciones entre entidades para construir aplicaciones backend escalables, mantenibles y alineadas con las buenas prácticas del desarrollo profesional de software.

## Video Youtube Evidencia

```bash
https://youtu.be/VG3-A9xxWks
```