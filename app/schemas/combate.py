from pydantic import BaseModel
from typing import Optional, List

class IniciativaCreate(BaseModel):
    idusuario: int
    nombrecriatura: str
    valoriniciativa: int
    idcriatura: int | None = None
    vida: int | None = None

class IniciativaResponse(IniciativaCreate):
    id: int
    class Config:
        from_attributes = True

class IniciativaEdit(BaseModel):
    id: int
    idusuario: int | None = None
    nombrecriatura: str | None = None
    valoriniciativa: int | None = None
    idcriatura: int | None = None
    vida: int | None = None
    class Config:
        from_attributes = True

class TurnoCreate(BaseModel):
    idusuario: int
    numturno: int
    index_tabla: int

class TurnoResponse(TurnoCreate):
    id: int
    class Config:
        from_attributes = True

class TurnoEdit(BaseModel):
    id: int
    idusuario: int | None = None
    numturno: int | None = None
    index_tabla: int | None = None
    class Config:
        from_attributes = True