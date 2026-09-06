from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .user import Base

class Criaturas(Base):
    __tablename__= "criaturas"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key = True)
    nombre = Column(String(50))
    dados = Column(Integer)
    tipo = Column(Integer)
    vida = Column(Integer)
    publico = Column(Boolean)
    owner = Column(Integer)

class Acciones(Base):
    __tablename__= "acciones"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key = True)
    idcriatura = Column(Integer)
    nombre = Column(String(50))
    tipo = Column(String(25))
    titulo = Column(String(20))
    detalle = Column(String(500))
    

class Detalles(Base):
    __tablename__= "detalles"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key = True)
    idcriatura = Column(Integer)
    nombre = Column(String(50))
    dados = Column(Integer)
    tdado = Column(Integer)
    vida = Column(Integer)
    modificador = Column(Integer)
    exp = Column(Integer)
    armadura = Column(Integer)
    velocidad = Column(Integer)
    fuerza = Column(Integer)
    destreza = Column(Integer)
    constitucion = Column(Integer)
    inteligencia = Column(Integer)
    sabiduria = Column(Integer)
    carisma = Column(Integer)

class Sentidos(Base):
    __tablename__= "sentidos"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key = True)
    idcriatura = Column(Integer)
    tiposentido = Column(String(25))
    valor = Column(Integer)

class Habilidades(Base):
    __tablename__= "habilidades"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key = True)
    idcriatura = Column(Integer)
    habilidad = Column(String(20))
    modif = Column(Integer)

class Salvaciones(Base):
    __tablename__= "salvaciones"
    __table_args__= {"schema": "public"}
    
    id = Column(Integer, primary_key = True)
    idcriatura = Column(Integer)
    carac = Column(String(255))
    modif = Column(Integer)

class Inmunidades(Base):
    __tablename__= "inmunidades"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key = True)
    idcriatura = Column(Integer)
    inmunidad = Column(String(20))

class Resistencias(Base):
    __tablename__= "resistencias"
    __table_args__= {"schema": "public"}

    id = Column(Integer, primary_key = True)
    idcriatura = Column(Integer)
    resist = Column(String(25))
    valor = Column(Numeric(2,1))
