# CriaturasWeb — DND Master Battle

Versión web de la aplicación de escritorio **DND Master Battle**, diseñada para ayudar a los Dungeon Masters (DMs) a gestionar criaturas, batallas e iniciativa en Dungeons & Dragons.

---

## Tecnologías Utilizadas

### Backend

| Tecnología | Uso |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Framework principal (Python 3.11+) |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM para la base de datos |
| [PostgreSQL](https://www.postgresql.org/) | Base de datos relacional |
| [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI |
| [python-jose](https://python-jose.readthedocs.io/) | JWT (autenticación) |
| [passlib + bcrypt](https://passlib.readthedocs.io/) | Hash de contraseñas |
| [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Configuración via variables de entorno |
| [psycopg2-binary](https://www.psycopg.org/) | Driver PostgreSQL |
| [python-multipart](https://github.com/Kludex/python-multipart) | Soporte para form data |
| [jinja2](https://jinja.palletsprojects.com/) | Plantillas HTML (página `/status`) |

### Frontend

| Tecnología | Uso |
|---|---|
| [Vue.js 3](https://vuejs.org/) | Framework principal |
| [Vite 5](https://vitejs.dev/) | Herramienta de build y dev server |
| [Vue Router 4](https://router.vuejs.org/) | Navegación entre páginas |
| [Pinia 4](https://pinia.vuejs.org/) | Manejo de estado global |
| [TailwindCSS 4](https://tailwindcss.com/) | Estilos utilitarios |
| [vue-toastification](https://github.com/Maronato/vue-toastification) | Notificaciones toast |

### Infraestructura

| Tecnología | Uso |
|---|---|
| [Docker Compose](https://docs.docker.com/compose/) | Orquestación de servicios (backend, frontend, db) |
| Docker | Contenerización |

---

## Estructura del Proyecto

```
CriaturasWeb/
├── app/                    # Backend FastAPI
│   ├── api/                # Routers por módulo
│   │   ├── auth/           # Registro y login (JWT)
│   │   ├── criaturas/      # CRUD de criaturas
│   │   ├── batallas/       # Gestión de batallas
│   │   ├── catalogos/      # Catálogos de referencia
│   │   ├── acciones/       # Acciones de criaturas
│   │   ├── habilidades/    # Habilidades
│   │   ├── inmunidades/    # Inmunidades
│   │   ├── resistencias/   # Resistencias
│   │   ├── salvaciones/    # Tiradas de salvación
│   │   ├── sentidos/       # Sentidos especiales
│   │   └── system/         # Health checks
│   ├── core/               # Configuración y utilidades
│   ├── models/             # Modelos SQLAlchemy
│   ├── schemas/            # Schemas Pydantic
│   ├── auth.py             # Lógica de autenticación JWT
│   ├── db.py               # Conexión a la base de datos
│   └── main.py             # Punto de entrada de la app
├── frontend/               # Frontend Vue.js
│   ├── src/
│   │   ├── components/     # Componentes reutilizables
│   │   ├── views/          # Vistas (páginas)
│   │   ├── stores/         # Stores de Pinia
│   │   ├── router/         # Configuración de Vue Router
│   │   └── utils/          # Utilidades varias
│   ├── vite.config.js
│   └── package.json
├── docker-compose.yml
├── backend.dockerfile
├── requirements.txt
└── init.sql                # Script de inicialización de la BD
```

---

## Configuración del Entorno Local

### Prerrequisitos

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

### Pasos

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Manjanans/CriaturasWeb.git
    cd CriaturasWeb
    ```

2.  **Configurar las variables de entorno:**
    ```bash
    cp .env.example .env
    ```
    Edita el `.env` con tus credenciales:
    ```env
    DATABASE_URL=postgresql://user:password@host:port/dbname
    SECRET_KEY=tu_clave_secreta_muy_segura
    ```
    > **Nota:** Para desarrollo local con Docker Compose, el `docker-compose.yml` ya configura una base de datos PostgreSQL local automáticamente. El `DATABASE_URL` del `.env` se usaría para conectar a una base de datos externa (ej. Neon).

3.  **Iniciar los servicios:**
    ```bash
    docker-compose up --build
    ```

### Acceso

| Servicio | URL |
|---|---|
| Frontend | http://localhost:8080 |
| Backend API (Swagger) | http://localhost:8000/api/v1/openapi.json |
| Backend Docs personalizadas | http://localhost:8000/docs |
| Health Check | http://localhost:8000/health/health |

---

## Características Actuales

*   **Autenticación JWT:** Registro (`POST /auth/register`), login (`POST /auth/token`) y perfil (`GET /auth/me`).
*   **CRUD de Criaturas:** Gestión completa con sus atributos (acciones, habilidades, inmunidades, resistencias, salvaciones, sentidos).
*   **Gestión de Batallas:** Módulo de batallas disponible en la API.
*   **Catálogos:** Datos de referencia para tipificar criaturas.
*   **Health Checks:** Endpoints para verificar el estado del backend y la base de datos.
*   **Notificaciones:** Feedback visual con toasts en el frontend.
*   **Estado global:** Manejo de sesión y datos con Pinia stores.