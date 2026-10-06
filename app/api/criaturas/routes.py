from fastapi import APIRouter, Depends, HTTPException
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import or_, select, delete, insert, update
from app.db import get_db
from app.models import Criatura, Criaturas, CriaturaStats, Detalles, Acciones, CriaturaDetalle
from app.schemas import ResistenciaDivision, CriaturaAll, DetalleCriatura, DetalleCreate, CriaturaBase, CriaturaUpdate, CriaturaCreate, CriaturaResponse, CriaturaView, CriaturaCompleta, StatsCriatura, StatsCreate, StatsUpdate, CompletaResponse, DetallesView
from app.auth import get_current_user
from app.shared.shared import inserts, search_by_id, updates, deletes, search_by_name
from app.api.acciones.routes import visualizar_acciones
from app.api.habilidades.routes import visualizar_habilidades
from app.api.inmunidades.routes import visualizar_inmunidades
from app.api.resistencias.routes import visualizar_resistencias
from app.api.salvaciones.routes import visualizar_salvaciones
from app.api.sentidos.routes import visualizar_sentidos
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
        ).order_by(Criaturas.nombre)
    ).scalars()
    
    return nueva

@router.get("/ver_criatura/{num_criatura}", response_model=CriaturaAll)
async def ver_criatura(
    num_criatura: int,
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):

    detalles = db.execute(select(Detalles).where(Detalles.id == num_criatura)).scalar_one()
    acciones = await visualizar_acciones(num_criatura, db, current_user)
    sentidos = await visualizar_sentidos(num_criatura, db, current_user)
    salvaciones = await visualizar_salvaciones(num_criatura, db, current_user)
    habilidades = await visualizar_habilidades(num_criatura, db, current_user)
    inmunidades = await visualizar_inmunidades(num_criatura, db, current_user)
    resistencias = await visualizar_resistencias(num_criatura, db, current_user)

    weak = [weak for weak in resistencias if weak.valor == 2]
    resist = [resist for resist in resistencias if resist.valor == 0.5]
    inmune = [inmune for inmune in resistencias if inmune.valor == 0]

    resistencia = ResistenciaDivision(weak=weak, resist=resist, inmune=inmune)

    agregar = CriaturaAll(
        base=detalles,
        accion=acciones, 
        sentido=sentidos, 
        salvacion=salvaciones, 
        habilidad=habilidades, 
        inmunidad=inmunidades, 
        resistencia=resistencia
    )

    if not detalles:
        raise HTTPException(status_code=404, detail="Not found")

    return agregar

@router.get("/edicion_criatura/{id}", response_model=DetallesView)
async def editar_criatura(
    id: int,
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    nueva = db.execute(select(Detalles).where(Detalles.id == id)).scalar_one()
    return nueva

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