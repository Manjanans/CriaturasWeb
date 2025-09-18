# CriaturasWeb API

A FastAPI application with PostgreSQL authentication system featuring schema separation and organized router structure.

## Features

- **User Authentication**: JWT-based authentication with password hashing
- **Schema Separation**: Users stored in 'usuarios' schema, other data in 'public' schema
- **Secure Password Hashing**: Using bcrypt for password security
- **Token-based Authentication**: OAuth2 password bearer tokens
- **Organized Structure**: Router-based architecture for better maintainability
- **Health Monitoring**: Comprehensive health check endpoints

## Project Structure

```
app/
├── api/                    # API routers
│   ├── __init__.py        # Main API router
│   ├── auth.py            # Authentication endpoints
│   ├── users.py           # User endpoints
│   ├── examples.py        # Example endpoints
│   └── health.py          # Health check endpoints
├── core/                  # Core configuration
│   ├── __init__.py
│   ├── config.py          # Settings and configuration
│   └── security.py        # Security utilities
├── models/                # Database models
│   ├── __init__.py
│   └── user.py            # User model
├── schemas/               # Pydantic schemas
│   ├── __init__.py
│   └── user.py            # User schemas
├── auth.py                # Authentication utilities
├── db.py                  # Database configuration
└── main.py                # Main application
```

## Setup

### 1. Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=your-secret-key-change-in-production
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

The application will automatically:
- Create the 'usuarios' schema if it doesn't exist
- Create all necessary tables in their respective schemas

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- **Custom Docs**: `http://localhost:8000/docs` - Health status and endpoint overview
- **Swagger UI**: `http://localhost:8000/docs` (FastAPI default) - Interactive testing
- **ReDoc**: `http://localhost:8000/redoc` - Alternative documentation view
- **API-specific docs**: `http://localhost:8000/api/v1/docs`

## API Endpoints

### Authentication (`/api/v1/auth/`)

- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/token` - Login and get access token

### Users (`/api/v1/users/`)

- `GET /api/v1/users/me` - Get current user information (requires authentication)

### Examples (`/api/v1/examples/`)

- `POST /api/v1/examples/create` - Create an example item (requires authentication)
- `GET /api/v1/examples/items` - Get all example items (requires authentication)

### Health Checks (`/api/v1/health/`)

- `GET /api/v1/health/health` - Basic health check
- `GET /api/v1/health/database` - Database connection health
- `GET /api/v1/health/auth` - Authentication system health
- `GET /api/v1/health/endpoints` - All endpoints status
- `GET /api/v1/health/full` - Complete health check

### Other

- `GET /` - Root endpoint
- `GET /status` - Database connection status
- `GET /docs` - Custom documentation with health status

## Quick Start Guide

### 1. Start the Application

```bash
uvicorn app.main:app --reload
```

### 2. Check System Health

Visit `http://localhost:8000/docs` to see the custom documentation page with:
- Database connection status
- Authentication system status
- All endpoint statuses
- Quick links to test endpoints

### 3. Create a User

1. In the Swagger UI, find the `POST /api/v1/auth/register` endpoint
2. Click "Try it out"
3. Enter the following JSON:
```json
{
  "username": "testuser",
  "password": "securepassword123"
}
```
4. Click "Execute"

### 4. Get an Access Token

1. Find the `POST /api/v1/auth/token` endpoint
2. Click "Try it out"
3. Enter:
   - `username`: `testuser`
   - `password`: `securepassword123`
4. Click "Execute"
5. Copy the `access_token` from the response

### 5. Use the Token

1. Click the "Authorize" button at the top of the Swagger UI
2. Enter your token in the format: `Bearer YOUR_ACCESS_TOKEN`
3. Click "Authorize"
4. Now you can test authenticated endpoints like `GET /api/v1/users/me`

## Health Monitoring

The application includes comprehensive health monitoring:

### Health Check Endpoints

- **`/api/v1/health/health`** - Basic service health
- **`/api/v1/health/database`** - Database connection status
- **`/api/v1/health/auth`** - Authentication system status
- **`/api/v1/health/endpoints`** - All endpoint statuses
- **`/api/v1/health/full`** - Complete system health

### Custom Documentation

Visit `http://localhost:8000/docs` for a custom documentation page that shows:
- Real-time system status
- Database connection health
- Authentication system health
- All endpoint descriptions and statuses
- Quick links to test endpoints

## Usage Examples

### 1. Register a User

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "password": "securepassword123"
     }'
```

### 2. Login and Get Token

```bash
curl -X POST "http://localhost:8000/api/v1/auth/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=testuser&password=securepassword123"
```

### 3. Use Token for Authenticated Requests

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 4. Check System Health

```bash
curl -X GET "http://localhost:8000/api/v1/health/full"
```

### 5. Create Example Item

```bash
curl -X POST "http://localhost:8000/api/v1/examples/create?name=TestItem&description=TestDescription" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Database Schema

### Usuarios Schema (`usuarios.users`)
- `id` - Primary key
- `username` - Unique username
- `hashed_password` - Bcrypt hashed password
- `is_active` - User status (boolean)

### Public Schema (`public.example_table`)
- `id` - Primary key
- `name` - Item name
- `description` - Item description
- `created_at` - Creation timestamp

## Security Features

- **Password Hashing**: All passwords are hashed using bcrypt
- **JWT Tokens**: Secure token-based authentication
- **Schema Isolation**: User data separated from application data
- **Input Validation**: Pydantic models for request validation
- **Centralized Configuration**: Settings management with pydantic-settings
- **Health Monitoring**: Comprehensive system health checks

## Development

The application uses:
- **FastAPI** for the web framework
- **SQLAlchemy** for database ORM
- **PostgreSQL** for the database
- **JWT** for token authentication
- **Pydantic** for data validation
- **Passlib** for password hashing
- **Router-based architecture** for better organization

## Adding New Features

To add new features:

1. **Create a new router** in `app/api/` (e.g., `app/api/products.py`)
2. **Add models** in `app/models/` if needed
3. **Add schemas** in `app/schemas/` if needed
4. **Include the router** in `app/api/__init__.py`
5. **Update this README** with new endpoints 