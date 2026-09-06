from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .user import Base

class Criatura(Base):
    __tablename__ = "criatura"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    cantdados = Column(Integer)
    tipodado = Column(Integer)
    vidatotal = Column(Integer)
    modificadorvida = Column(Integer)
    cantexp = Column(Integer)
    publico = Column(Boolean, default=True)

    id_privado = Column(Integer, ForeignKey("usuarios.users.id"))

class CriaturaStats(Base):
    __tablename__ = "criaturastats"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    clasearmadura = Column(Integer)
    velocidad = Column(Integer)
    fuerza = Column(Integer)
    destreza = Column(Integer)
    constitucion = Column(Integer)
    inteligencia = Column(Integer)
    sabiduria = Column(Integer)
    carisma = Column(Integer)

class CriaturaDetalle(Base):
    __tablename__ = "criaturadetalle"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    idtipodesc = Column(Integer, ForeignKey("public.tipodesc.id", ondelete="CASCADE"))
    titulodetalle = Column(String(20))
    descripciondetalle = Column(String(500))



