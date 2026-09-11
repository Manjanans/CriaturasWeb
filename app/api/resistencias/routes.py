from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import Resistencia, Resistencias
from app.schemas import ResistenciasView, ResistenciaCreate, ResistenciaResponse
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes

router = APIRouter()

@router.get("/ver_resistencias/{num_criat}", response_model=list[ResistenciasView])
async def visualizar_resistencias(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    stmt = select(Resistencias).where(Resistencias.idcriatura == num_criat)
    resistencias = db.execute(stmt).scalars()
    return resistencias

@router.post("/crear_resistencia", response_model=ResistenciaResponse)
async def crear_resistencia(
    data: ResistenciaCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nuevo = await inserts(data, Resistencia, db)
    return nuevo

@router.put("/editar_resistencia", response_model=ResistenciaResponse)
async def update_resistencia(
    data: ResistenciaResponse,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    actualiza = await updates(data, Resistencia, db)
    return actualiza

@router.delete("/eliminar_resistencia/{num_criat}", status_code=204)
async def elim_resistencia(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_criat, Resistencia, db)

    return flag  
