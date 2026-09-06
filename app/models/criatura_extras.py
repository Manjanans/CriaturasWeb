from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .user import Base

class SentidoCriatura(Base):
    __tablename__ = "sentidocriatura"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    idtiposentido = Column(Integer, ForeignKey("public.tiposentido.id", ondelete="CASCADE"))
    cantidad = Column(Integer)

class TiradaSalvacion(Base):
    __tablename__ = "tiradasalvacion"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    idcaracteristica = Column(Integer, ForeignKey("public.caracteristica.id", ondelete="CASCADE"))
    modificador = Column(Integer)

class HabilidadCriatura(Base):
    __tablename__ = "habilidadcriatura"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    idhabilidad = Column(Integer, ForeignKey("public.habilidad.id", ondelete="CASCADE"))
    modificador = Column(Integer)

class InmunidadCondicion(Base):
    __tablename__ = "inmunidadcondicion"
    __table_args__ = {"schema": "public"}
    
    id = Column(Integer, primary_key=True)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    idtipocondicion = Column(Integer, ForeignKey("public.tipocondicion.id", ondelete="CASCADE"))
    
class Resistencia(Base):
    __tablename__ = "resistencia"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    idcriatura = Column(Integer, ForeignKey("public.criatura.id", ondelete="CASCADE"))
    idtipodanio = Column(Integer, ForeignKey("public.habilidad.id", ondelete="CASCADE"))
    cantidad = Column(Numeric(precision=2, scale=1))