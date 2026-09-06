from pydantic import BaseModel
from typing import Optional, List

class SentidoCreate(BaseModel):
    idcriatura: int
    idtiposentido: int
    cantidad: int
    class Config:
        from_attributes = True

class SentidoResponse(SentidoCreate):
    id: int
    class Config:
        from_attributes = True

class SalvacionCreate(BaseModel):
    idcriatura: int
    idcaracteristica: int
    modificador: int
    class Config:
        from_attributes = True

class SalvacionResponse(SalvacionCreate):
    id: int
    class Config:
        from_attributes = True

class HabilidadCreate(BaseModel):
    idcriatura: int
    idhabilidad: int
    modificador: int
    class Config:
        from_attributes = True

class HabilidadResponse(HabilidadCreate):
    id: int
    class Config:
        from_attributes = True

class InmunidadCreate(BaseModel):
    idcriatura: int
    idtipocondicion: int
    class Config:
        from_attributes = True

class InmunidadResponse(InmunidadCreate):
    id: int
    class Config:
        from_attributes = True

class ResistenciaCreate(BaseModel):
    idcriatura: int
    idtipodanio: int
    cantidad: float
    class Config:
        from_attributes = True

class ResistenciaResponse(ResistenciaCreate):
    id: int
    class Config:
        from_attributes = True

