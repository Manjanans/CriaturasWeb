# DND Master Battle Web

## Descripción del Proyecto

Este proyecto es una versión web de la aplicación de escritorio "DND Master Battle", diseñada para ayudar a los Dungeon Masters (DMs) a gestionar encuentros de combate en Dungeons & Dragons. El objetivo es proporcionar una herramienta moderna y accesible para la gestión de criaturas, la iniciativa y el seguimiento de batallas, con una interfaz de usuario inmersiva y temática de fantasía.

## Tecnologías Utilizadas

El proyecto está construido con un stack moderno y modular:

### Backend
*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
*   **Lenguaje:** Python 3.11+
*   **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
*   **Base de Datos:** PostgreSQL (utilizando [Neon](https://neon.tech/) para la base de datos en la nube)
*   **Autenticación:** JWT (JSON Web Tokens)
*   **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)

### Frontend
*   **Framework:** [Vue.js 3](https://vuejs.org/)
*   **Herramienta de Build:** [Vite](https://vitejs.dev/)
*   **Lenguaje:** JavaScript, HTML, CSS
*   **Estilos:** CSS personalizado con fuentes temáticas (Cinzel, Merriweather)

### Contenedores
*   **Orquestación:** [Docker Compose](https://docs.docker.com/compose/)
*   **Contenedores:** Docker

### Control de Versiones
*   **Sistema:** Git

## Características Principales (Actuales)

*   **Autenticación de Usuarios:** Registro y inicio de sesión seguro mediante JWT.
*   **Interfaz de Usuario Temática:** Diseño inmersivo con estética de fantasía, colores oscuros y texturas de pergamino.
*   **Manejo de Errores Robusto:** Modales de error amigables para el usuario en el frontend.
*   **Navegación Básica:** Barra de navegación con enlaces a "Criaturas", "Batalla" y "Perfil" (funcionalidad pendiente).
*   **Estructura de API Modular:** Backend organizado en módulos lógicos (auth, criaturas, batallas, system) para facilitar la escalabilidad.

## Estructura del Proyecto

El proyecto se divide en dos directorios principales:

*   `app/`: Contiene todo el código del backend de FastAPI.
*   `frontend/`: Contiene todo el código de la aplicación frontend de Vue.js.

## Configuración del Entorno de Desarrollo Local

Para poner en marcha el proyecto en tu máquina local, sigue estos pasos:

### Prerrequisitos
Asegúrate de tener [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

### Pasos para Iniciar la Aplicación

1.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/Manjanans/CriaturasWeb.git
    cd CriaturasWeb
    ```

2.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la raíz del proyecto (al mismo nivel que `docker-compose.yml`). Puedes usar `.env.example` como plantilla.
    ```bash
    cp .env.example .env
    ```
    Edita el archivo `.env` y reemplaza los valores con tus credenciales de base de datos de PostgreSQL (por ejemplo, de Neon) y una clave secreta segura:
    ```
    DATABASE_URL="postgresql://user:password@host:port/dbname?sslmode=require"
    SECRET_KEY="tu_clave_secreta_muy_segura"
    ```

3.  **Iniciar los Contenedores de Docker:**
    Desde la raíz del proyecto, ejecuta:
    ```bash
    docker-compose up --build
    ```
    Esto construirá las imágenes de Docker e iniciará los servicios de backend y frontend.

### Acceso a la Aplicación

Una vez que los contenedores estén en funcionamiento:

*   **Frontend (Aplicación Web):** Abre tu navegador y ve a `http://localhost:8080`
*   **Backend (Documentación de la API):** Abre tu navegador y ve a `http://localhost:8000/docs`

## Despliegue (Consideraciones)

Para el despliegue en producción en plataformas como [Render](https://render.com/), se recomienda configurar el frontend y el backend como servicios separados:

*   **Backend:** Como un "Web Service" utilizando `backend.dockerfile`.
*   **Frontend:** Como un "Static Site" construyendo la aplicación Vue.js desde el directorio `frontend/`.

## Próximos Pasos

*   Implementar la gestión completa de criaturas (CRUD).
*   Desarrollar la funcionalidad de gestión de batallas.
*   Expandir la interfaz de usuario para las secciones de "Criaturas", "Batalla" y "Perfil".