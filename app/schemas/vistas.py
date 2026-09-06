from pydantic import BaseModel
from typing import Optional, List

class CriaturaView(BaseModel):
    id: int
    nombre: str
    dados: int
    tipo: int
    vida: int
    publico: bool
    owner: Optional[int] = None
    class Config:
        from_attributes = True

class AccionesView(BaseModel):
    id: int
    idcriatura: int
    nombre: str
    tipo: str
    titulo: str
    detalle: str
    class Config:
        from_attributes = True

class DetallesView(BaseModel):
    id: int
    idcriatura:int
    nombre: str
    dados: int
    tdado: int
    vida: int
    modificador: int
    exp: int
    armadura: int
    velocidad: int
    fuerza: int
    destreza: int
    constitucion: int
    inteligencia: int
    sabiduria: int
    carisma: int
    class Config:
        from_attributes = True

class SentidosView(BaseModel):
    id: int
    idcriatura: int
    tiposentido: str
    valor: int
    class Config:
        from_attributes = True

class HabilidadesView(BaseModel):
    id: int
    idcriatura: int
    habilidad: str
    modif: int
    class Config:
        from_attributes = True

class SalvacionesView(BaseModel):
    id: int
    idcriatura: int
    carac: str
    modif: int
    class Config:
        from_attributes = True

class InmunidadesView(BaseModel):
    id: int
    idcriatura: int
    inmunidad: str
    class Config:
        from_attributes = True

class ResistenciasView(BaseModel):
    id: int
    idcriatura: int
    resist: str
    valor: float
    class Config:
        from_attributes = True