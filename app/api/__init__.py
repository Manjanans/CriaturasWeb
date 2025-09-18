from fastapi import APIRouter

from app.api.auth import routes as auth_routes
from app.api.system import health as health_routes
from app.api.criaturas import routes as criaturas_routes
from app.api.batallas import routes as batallas_routes

api_router = APIRouter()

api_router.include_router(auth_routes.router, prefix="/auth", tags=["Authentication & Users"])
api_router.include_router(health_routes.router, prefix="/health", tags=["System Health"])
api_router.include_router(criaturas_routes.router, prefix="/criaturas", tags=["Criaturas"])
api_router.include_router(batallas_routes.router, prefix="/batallas", tags=["Batallas"])