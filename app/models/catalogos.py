from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .user import Base

class TipoSentido(Base):
    __tablename__= "tiposentido"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(25))

class TipoDesc(Base):
    __tablename__= "tipodesc"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(10))

class Caracteristica(Base):
    __tablename__= "caracteristica"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(15))

class Habilidad(Base):
    __tablename__= "habilidad"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(20))

class TipoCondicion(Base):
    __tablename__= "tipocondicion"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(20))

class TipoDanio(Base):
    __tablename__= "tipodanio"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(25))



