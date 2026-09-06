from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.api import api_router
from app.db import engine
from app.core.config import settings
from sqlalchemy import text
import os
import time

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# Static files and templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(BASE_DIR, "..", "templates")
static_path = os.path.join(BASE_DIR, "..", "static")

templates = Jinja2Templates(directory=templates_path)
app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/status", response_class=HTMLResponse)
def get_status(request: Request):
    """Database connection status page"""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1;"))
            message = "✅ Connection Successful"
    except Exception as e:
        message = f"❌ Connection Failed: {str(e)}"

    return templates.TemplateResponse("status.html", {
        "request": request,
        "message": message
    })

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to CriaturasWeb API",
        "docs": "/docs",
        "api_docs": f"{settings.API_V1_STR}/docs",
        "health": "/health/health"
    }

@app.get("/docs", response_class=HTMLResponse)
def custom_docs(request: Request):
    """Custom documentation page with endpoint health"""
    
    # Check database health
    db_healthy = False
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1;"))
            db_healthy = True
    except:
        pass
    
    # Check auth system health
    auth_healthy = False
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT COUNT(*) FROM usuarios.users;"))
            auth_healthy = True
    except:
        pass
    
    # Define all endpoints with their status
    endpoints = {
        "Authentication": {
            "POST /auth/register": {
                "description": "Register a new user",
                "status": "🟢 Active",
                "requires_auth": False
            },
            "POST /auth/token": {
                "description": "Login and get access token",
                "status": "🟢 Active",
                "requires_auth": False
            }
        },
        "Users": {
            "GET /auth/me": {
                "description": "Get current user information",
                "status": "🟢 Active",
                "requires_auth": True
            }
        },
        "Health Checks": {
            "GET /health/health": {
                "description": "Basic health check",
                "status": "🟢 Active",
                "requires_auth": False
            },
            "GET /health/database": {
                "description": "Database health check",
                "status": "🟢 Active" if db_healthy else "🔴 Unhealthy",
                "requires_auth": False
            },
            "GET /health/auth": {
                "description": "Authentication system health",
                "status": "🟢 Active" if auth_healthy else "🔴 Unhealthy",
                "requires_auth": False
            },
            "GET /health/endpoints": {
                "description": "All endpoints status",
                "status": "🟢 Active",
                "requires_auth": False
            },
            "GET /health/full": {
                "description": "Complete health check",
                "status": "🟢 Active" if db_healthy and auth_healthy else "🔴 Unhealthy",
                "requires_auth": False
            }
        }
    }
    
    return templates.TemplateResponse("docs.html", {
        "request": request,
        "endpoints": endpoints,
        "db_healthy": db_healthy,
        "auth_healthy": auth_healthy,
        "timestamp": time.time()
    })
