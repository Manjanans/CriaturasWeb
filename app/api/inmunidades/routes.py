from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import Inmunidades, InmunidadCondicion
from app.schemas import InmunidadCreate, InmunidadResponse, InmunidadesView
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes

router = APIRouter()

@router.get("/ver_inmunidades", response_model=list[InmunidadesView])
async def visualizar_inmunidades(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    stmt = select(Inmunidades).where(Inmunidades.idcriatura == num_criat)
    inmunidades = db.execute(stmt).scalars()
    return inmunidades

@router.post("/crear_inmunidad", response_model=InmunidadResponse)
async def crear_inmunidad(
    data: InmunidadCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nuevo = await inserts(data, InmunidadCondicion, db)
    return nuevo

@router.put("/editar_inmunidad", response_model=InmunidadResponse)
async def update_inmunidad(
    data: InmunidadResponse,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    actualiza = await updates(data, InmunidadCondicion, db)
    return actualiza

@router.delete("/eliminar_inmunidad", status_code=204)
async def elim_inmunidad(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_criat, InmunidadCondicion, db)

    return flag  
