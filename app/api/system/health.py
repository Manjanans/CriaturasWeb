from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db, engine
from app.auth import get_current_active_user
from app.models import User
from sqlalchemy import text
import time

router = APIRouter()

@router.get("/health")
def health_check():
    """Basic health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "CriaturasWeb API"
    }

@router.get("/database")
def database_health_check():
    """Check database connection"""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1;"))
            return {
                "status": "healthy",
                "database": "connected",
                "timestamp": time.time()
            }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )

@router.get("/auth")
def auth_health_check():
    """Check authentication system"""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT COUNT(*) FROM usuarios.users;"))
            return {
                "status": "healthy",
                "auth_system": "operational",
                "users_table": "accessible",
                "timestamp": time.time()
            }
    except Exception as e:
        return {
            "status": "unhealthy",
            "auth_system": "error",
            "error": str(e),
            "timestamp": time.time()
        }

@router.get("/endpoints")
def endpoints_health_check(request: object):
    """Check all API endpoints status"""
    url_list = [
        route.path for route in request.app.routes
    ]
    return {
        "status": "healthy",
        "endpoints": url_list,
        "timestamp": time.time()
    }

@router.get("/full")
def full_health_check():
    """Complete health check including database and auth"""
    db_status = "healthy"
    auth_status = "healthy"
    
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1;"))
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT COUNT(*) FROM usuarios.users;"))
    except Exception as e:
        auth_status = f"unhealthy: {str(e)}"
    
    overall_status = "healthy" if db_status == "healthy" and auth_status == "healthy" else "unhealthy"
    
    return {
        "status": overall_status,
        "database": db_status,
        "authentication": auth_status,
        "timestamp": time.time(),
        "service": "CriaturasWeb API"
    }
