from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import Criatura, Criaturas, CriaturaStats, Detalles, Acciones, CriaturaDetalle
from app.schemas import AccionesView, DetalleCriatura, DetalleCreate, CriaturaBase, CriaturaUpdate, CriaturaCreate, CriaturaResponse, CriaturaView, CriaturaCompleta, StatsCriatura, StatsCreate, StatsUpdate, CompletaResponse, DetallesView
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes, search_by_name

router = APIRouter()

@router.get("/", response_model=list[CriaturaView])
async def get_all_criaturas(
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    nueva = db.execute(
        select(Criaturas)
        .where(
            or_(
                Criaturas.publico == True,
                Criaturas.owner == current_user.id
            )
        )
    ).scalars()
    return nueva

@router.get("/ver_criatura/{num_criatura}", response_model=DetallesView)
async def ver_criatura(
    num_criatura: int,
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    criatura = db.execute(select(Detalles).filter_by(idcriatura=num_criatura)).scalar_one()
    if not criatura:
        raise HTTPException(status_code=404, detail="Not found")
    return criatura

@router.post("/crear", response_model=CompletaResponse)
async def creacion_criatura(
    data: CriaturaCompleta,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    criat = data.base
    det = data.stats

    ncriatura = await inserts(criat, Criatura, db)
    det.idcriatura = ncriatura.id
    ndetalle = await inserts(det, CriaturaStats, db)

    return CompletaResponse(base=ncriatura, stats=ndetalle)

@router.put("/actualizar_criatura", response_model=CriaturaUpdate)
async def actualizacion_criatura(
    data: CriaturaUpdate,
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    criatura = await updates(data, Criatura, db)
    return criatura
    
@router.put("/actualizar_detalle", response_model=StatsUpdate)
async def actualizacion_detalle(
    data: StatsUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    stats = await updates(data, CriaturaStats, db)
    return stats

@router.delete("/eliminar_criatura/{num_criat}", status_code=204)
async def eliminacion_criatura(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_criat, Criatura, db)

    return None

@router.get("/buscar_criatura/{search_query}", response_model=list[CriaturaView])
async def busca_por_nombre(
    search_query: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    criatura = await search_by_name(search_query, Criaturas.nombre, Criaturas, db)
    
    return criatura