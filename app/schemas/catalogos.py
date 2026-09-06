from pydantic import BaseModel
from typing import Optional, List

class CatalogoBase(BaseModel):
    id: int
    descripcion: str
    class Config:
        from_attributes = True

