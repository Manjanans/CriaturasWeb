from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import Acciones, CriaturaDetalle
from app.schemas import AccionesView, DetalleCriatura, DetalleCreate
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes

router = APIRouter()

@router.get("/ver_acciones/{num_item}", response_model=list[AccionesView])
async def visualizar_acciones(
    num_item: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nueva = db.execute(
        select(Acciones)
        .where(Acciones.idcriatura == num_item)
        ).scalars()
    return nueva

@router.post("/agregar_accion", response_model=DetalleCreate)
async def crear_accion(
    data: DetalleCriatura,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    accion  = await inserts(data, CriaturaDetalle, db)
    return accion

@router.put("/actualizar_accion", response_model=DetalleCreate)
async def actualizacion_accion(
    data: DetalleCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    accion = await updates(data, CriaturaDetalle, db)
    return accion

@router.delete("/eliminar_accion/{num_accion}", status_code=204)
async def eliminacion_accion(
    num_accion: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_accion, CriaturaDetalle, db)

    return flag
