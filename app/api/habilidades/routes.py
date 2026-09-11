from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import HabilidadCriatura, Habilidades
from app.schemas import HabilidadesView, HabilidadCreate, HabilidadResponse
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes

router = APIRouter()

@router.get("/ver_habilidades/{num_criat}", response_model=list[HabilidadesView])
async def visualizar_habilidades(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    stmt = select(Habilidades).where(Habilidades.idcriatura == num_criat)
    habilidades = db.execute(stmt).scalars()
    return habilidades

@router.post("/crear_habilidad", response_model=HabilidadResponse)
async def crear_habilidad(
    data: HabilidadCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nuevo = await inserts(data, HabilidadCriatura, db)
    return nuevo

@router.put("/editar_habilidad", response_model=HabilidadResponse)
async def update_habilidad(
    data: HabilidadResponse,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    actualiza = await updates(data, HabilidadCriatura, db)
    return actualiza

@router.delete("/eliminar_habilidad/{num_criat}", status_code=204)
async def elim_habilidad(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_criat, HabilidadCriatura, db)

    return flag  
