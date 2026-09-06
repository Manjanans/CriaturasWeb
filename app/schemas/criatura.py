from pydantic import BaseModel
from typing import Optional, List

class CriaturaBase(BaseModel):
    nombre: str
    cantdados: Optional[int] 
    tipodado: Optional[int] 
    vidatotal: Optional[int]
    modificadorvida: Optional[int]
    cantexp: int
    publico: bool
    id_privado: Optional[int] = None

class CriaturaCreate(CriaturaBase):
    class Config:
        from_attributes = True

class CriaturaResponse(CriaturaBase):
    id: int
    class Config:
        from_attributes = True


class CriaturaUpdate(BaseModel):
    id: int
    nombre: Optional[str]
    cantdados: Optional[int]
    tipodado: Optional[int]
    vidatotal: Optional[int]
    modificadorvida: Optional[int]
    cantexp: Optional[int]
    publico: Optional[bool]
    id_privado: Optional[int] = None

    class Config:
        from_attributes = True

class StatsCriatura(BaseModel):
    idcriatura: int = 0
    clasearmadura: int
    velocidad: int
    fuerza: int
    destreza: int
    constitucion: int
    inteligencia: int
    sabiduria: int
    carisma: int

class StatsCreate(StatsCriatura):
    id: int
    class Config:
        from_attributes = True

class StatsUpdate(BaseModel):
    id: int
    idcriatura: int
    clasearmadura: Optional[int]
    velocidad: Optional[int]
    fuerza: Optional[int]
    destreza: Optional[int]
    constitucion: Optional[int]
    inteligencia: Optional[int]
    sabiduria: Optional[int]
    carisma: Optional[int]

    class Config:
        from_attributes = True

class DetalleCriatura(BaseModel):
    idcriatura: int
    idtipodesc: int
    titulodetalle: str
    descripciondetalle: str

class DetalleCreate(DetalleCriatura):
    id: int
    class Config:
        from_attributes = True

class DetalleUpdate(BaseModel):
    idcriatura: int
    idtipodesc: Optional[int]
    titulodetalle: Optional[str]
    descripciondetalle: Optional[str]

    class Config:
        from_attributes = True

class CriaturaCompleta(BaseModel):
    base: CriaturaBase
    stats: StatsCriatura

class CompletaResponse(BaseModel):
    base: CriaturaResponse
    stats: StatsCreate