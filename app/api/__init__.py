from fastapi import APIRouter

from app.api.auth import routes as auth_routes
from app.api.system import health as health_routes
from app.api.criaturas import routes as criaturas_routes
from app.api.batallas import routes as batallas_routes
from app.api.catalogos import routes as catalogos_route
from app.api.acciones import routes as acciones_routes
from app.api.habilidades import routes as habilidades_route
from app.api.inmunidades import routes as inmunidades_route
from app.api.resistencias import routes as resistencias_route
from app.api.salvaciones import routes as salvaciones_route
from app.api.sentidos import routes as sentidos_route


api_router = APIRouter()

api_router.include_router(auth_routes.router, prefix="/auth", tags=["Authentication & Users"])
api_router.include_router(criaturas_routes.router, prefix="/criaturas", tags=["Criaturas"])
api_router.include_router(catalogos_route.router, prefix="/catalogos", tags=["Catalogos"])
api_router.include_router(acciones_routes.router, prefix="/acciones", tags=["Acciones"])
api_router.include_router(habilidades_route.router, prefix="/habilidades", tags=["Habilidades"])
api_router.include_router(inmunidades_route.router, prefix="/inmunidades", tags=["Inmunidades"])
api_router.include_router(salvaciones_route.router, prefix="/salvaciones", tags=["Salvaciones"])
api_router.include_router(resistencias_route.router, prefix="/resistencias", tags=["Resistencias"])
api_router.include_router(sentidos_route.router, prefix="/sentidos", tags=["Sentidos"])
api_router.include_router(batallas_routes.router, prefix="/batallas", tags=["Batallas"])
api_router.include_router(health_routes.router, prefix="/health", tags=["System Health"])