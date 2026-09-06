from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import Salvaciones, TiradaSalvacion
from app.schemas import SalvacionesView, SalvacionCreate, SalvacionResponse
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes

router = APIRouter()

@router.get("/ver_salvaciones", response_model=list[SalvacionesView])
async def visualizar_salvaciones(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    stmt = select(Salvaciones).where(Salvaciones.idcriatura == num_criat)
    salvaciones = db.execute(stmt).scalars()
    return salvaciones

@router.post("/crear_salvacion", response_model=SalvacionResponse)
async def crear_salvacion(
    data: SalvacionCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nuevo = await inserts(data, TiradaSalvacion, db)
    return nuevo

@router.put("/editar_salvacion", response_model=SalvacionResponse)
async def update_salvacion(
    data: SalvacionResponse,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    actualiza = await updates(data, TiradaSalvacion, db)
    return actualiza

@router.delete("/eliminar_salvacion", status_code=204)
async def elim_salvacion(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_criat, TiradaSalvacion, db)

    return flag  
