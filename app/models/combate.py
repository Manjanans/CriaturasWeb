from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .user import Base

class Iniciativa(Base):
    __tablename__ = "iniciativa"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey("usuarios.users.id", ondelete="CASCADE"))
    nombrecriatura = Column(String(50), unique=True)
    valoriniciativa = Column(Integer)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    vida = Column(Integer)

class Turno(Base):
    __tablename__ = "turno"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey("usuarios.users.id", ondelete="CASCADE"))
    numturno = Column(Integer)
    index_tabla = Column(Integer)