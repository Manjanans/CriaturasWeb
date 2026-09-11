from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import Sentidos, SentidoCriatura
from app.schemas import SentidoResponse, SentidoCreate, SentidosView
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes

router = APIRouter()

@router.get("/ver_sentidos/{num_criat}", response_model=list[SentidosView])
async def visualizar_sentidos(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    stmt = select(Sentidos).where(Sentidos.idcriatura == num_criat)
    sentidos = db.execute(stmt).scalars()
    return sentidos

@router.post("/crear_sentido", response_model=SentidoResponse)
async def crear_sentido(
    data: SentidoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nuevo = await inserts(data, SentidoCriatura, db)
    return nuevo

@router.put("/editar_sentido", response_model=SentidoResponse)
async def update_sentido(
    data: SentidoResponse,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    actualiza = await updates(data, SentidoCriatura, db)
    return actualiza

@router.delete("/eliminar_sentido/{num_criat}", status_code=204)
async def elim_sentido(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_criat, SentidoCriatura, db)

    return None  
