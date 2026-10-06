from pydantic import BaseModel
from typing import Optional, List

class CriaturaView(BaseModel):
    id: int
    nombre: str
    dados: int
    tipo: int
    vida: int
    publico: bool
    modificador: int
    owner: Optional[int] = None
    class Config:
        from_attributes = True

class AccionesView(BaseModel):
    id: int | None = None
    idcriatura: int | None = None
    nombre: str | None = None
    tipo: str | None = None
    titulo: str | None = None
    detalle: str | None = None
    class Config:
        from_attributes = True

class DetallesView(BaseModel):
    id: int | None = None
    idcriatura:int | None = None
    nombre: str | None = None
    dados: int | None = None
    tdado: int | None = None
    vida: int | None = None
    modificador: int | None = None
    exp: int | None = None
    armadura: int | None = None
    velocidad: int | None = None
    fuerza: int | None = None
    destreza: int | None = None
    constitucion: int | None = None
    inteligencia: int | None = None
    sabiduria: int | None = None
    carisma: int | None = None
    duenio: int | None = None
    publico: bool | None = None
    class Config:
        from_attributes = True

class SentidosView(BaseModel):
    id: int | None = None
    idcriatura: int | None = None
    idtiposentido: int | None = None
    tiposentido: str | None = None
    valor: int | None = None
    class Config:
        from_attributes = True

class HabilidadesView(BaseModel):
    id: int | None = None
    idcriatura: int | None = None
    idhabilidad: int | None = None
    habilidad: str | None = None
    modif: int | None = None
    class Config:
        from_attributes = True

class SalvacionesView(BaseModel):
    id: int | None = None
    idcriatura: int | None = None
    idcaracteristica: int | None = None
    carac: str | None = None
    modif: int | None = None
    class Config:
        from_attributes = True

class InmunidadesView(BaseModel):
    id: int | None = None
    idcriatura: int | None = None
    inmunidad: str | None = None
    class Config:
        from_attributes = True

class ResistenciasView(BaseModel):
    id: int | None = None
    idcriatura: int | None = None
    idtipodanio: int | None = None
    resist: str | None = None
    valor: float | None = None
    class Config:
        from_attributes = True