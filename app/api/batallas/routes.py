from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db import get_db
from app.models import Iniciativa, Turno
from app.schemas import IniciativaResponse, IniciativaCreate, IniciativaEdit, CriaturaAll, CriaturaBattle, TurnoCreate, TurnoResponse, TurnoEdit
from app.auth import get_current_user
from app.shared.shared import inserts, updates, deletes, updates_single, delete_by_user
from app.api.criaturas.routes import ver_criatura

router = APIRouter()

@router.get("/iniciativa", response_model=list[IniciativaResponse])
async def get_all_batallas(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    stmt = select(Iniciativa).where(Iniciativa.idusuario == current_user.id).order_by(Iniciativa.valoriniciativa)
    listado = db.execute(stmt).scalars()
    return listado

@router.post("/iniciativa/crear", response_model=IniciativaResponse)
async def create_iniciativa(
    objeto: IniciativaCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nueva = await inserts(objeto, Iniciativa, db)
    return nueva

@router.put("/iniciativa/editar_iniciativa", response_model=IniciativaResponse)
async def edit_iniciativa(
    objeto: IniciativaEdit,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    nueva = await updates(objeto, Iniciativa, db)
    return nueva

@router.delete("/iniciativa/eliminar_iniciativa/{num_criat}", status_code=204)
async def elim_iniciativa(
    num_criat: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(num_criat, Iniciativa, db)

    return flag 

@router.get("/iniciativa/ver_criaturas", response_model=list[CriaturaBattle])
async def ver_criaturas(
    listado: list[int] = Query(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    criaturas = []

    for criatura in listado:
        datos = await ver_criatura(criatura, db, current_user)
        agregar = CriaturaBattle(id=criatura, data=datos)
        criaturas.append(agregar)
    
    return criaturas

@router.put("/realizar_danio", response_model=IniciativaResponse)
async def realizar_dmg(
    data: IniciativaEdit,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    ob = await updates_single(data.id, data.vida, 'vida', Iniciativa, db)

    return ob

@router.post("/crear_turno", response_model=TurnoResponse)
async def crear_turno(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        idusuario = current_user.id
        turno = TurnoCreate(idusuario=idusuario, numturno=1, index_tabla=0)
        creacion = await inserts(turno, Turno, db)

        return creacion
    except:
        raise HTTPException(
            status_code=400,
            detail={"error": "DB constraint", "message": "El usuario ya posee una batalla activa."}
        )

@router.get('/ver_turno', response_model=TurnoResponse)
async def ver_turno(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        turno = db.execute(select(Turno).where(Turno.idusuario == current_user.id)).scalar_one()
        return turno
    except:
        raise HTTPException(
            status_code=404,
            detail={"error":'Not found', "message": "Aún no hay turno creado"}
        )

@router.put("/siguiente_turno", response_model=TurnoResponse)
async def next_turno(
    data: TurnoEdit,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if data.index_tabla == 0:
        turno = db.get(Turno, data.id)
        turno.numturno = turno.numturno + 1
        turno.index_tabla = 0
        db.commit()
        db.refresh(turno)

        return turno
    
    n_ronda = await updates_single(data.id, data.index_tabla, 'index_tabla', Turno, db)

    print(n_ronda.index_tabla)
    
    return n_ronda

@router.delete("/eliminar_turno/{idturno}", status_code=204)
async def elim_turno(
    idturno: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    flag = await deletes(idturno, Turno, db)

    return flag  

@router.delete("/finalizar_batalla", status_code=204)
async def finalizar(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user) 
):
    flag = await delete_by_user(current_user, Iniciativa.idusuario, Iniciativa, db)
    flag2 = await delete_by_user(current_user, Turno.idusuario, Turno, db)

    return flag2

"""
maqueta de criaturas en batalla



"""
