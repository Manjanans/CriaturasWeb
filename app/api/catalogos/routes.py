from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import TipoSentido, TipoDesc, Caracteristica, Habilidad, TipoCondicion, TipoDanio
from app.schemas import CatalogoBase
from app.auth import get_current_user
from app.shared.shared import search_all

router = APIRouter()

@router.get("/ver_sentidos", response_model=list[CatalogoBase])
async def visualizar_sentidos(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
        Se ven todos los sentidos.
    """
    query = await search_all(TipoSentido, db)
    return query

@router.get("/ver_descripciones", response_model=list[CatalogoBase])
async def visualizar_descripciones(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = await search_all(TipoDesc, db)
    return query

@router.get("/ver_caracteristicas", response_model=list[CatalogoBase])
async def visualizar_caracteristicas(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = await search_all(Caracteristica, db)
    return query

@router.get("/ver_habilidades", response_model=list[CatalogoBase])
async def visualizar_habilidades(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = await search_all(Habilidad, db)
    return query

@router.get("/ver_condiciones", response_model=list[CatalogoBase])
async def visualizar_condiciones(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = await search_all(TipoCondicion, db)
    return query

@router.get("/ver_danios", response_model=list[CatalogoBase])
async def visualizar_danios(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    query = await search_all(TipoDanio, db)
    return query
