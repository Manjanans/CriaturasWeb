ALTER DATABASE criaturas SET timezone TO 'America/Santiago';
-- Crear schema usuarios
CREATE SCHEMA IF NOT EXISTS usuarios;

-- Tabla de usuarios
CREATE TABLE usuarios.users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	hashed_password VARCHAR(255) NOT NULL,
	is_active BOOLEAN DEFAULT true
);

SET search_path TO public;

CREATE TABLE criatura (
	id SERIAL PRIMARY KEY,
	cantDados	INTEGER,
	tipoDado	INTEGER,
	vidaTotal	INTEGER,
	modificadorVida	INTEGER,
	nombre	VARCHAR(50) NOT NULL,
	cantEXP	INTEGER,
	publico boolean DEFAULT true,
	id_privado INTEGER REFERENCES usuarios.users(id) ON DELETE CASCADE
);

CREATE TABLE criaturastats(
	id	SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	claseArmadura	INTEGER,
	velocidad	INTEGER,
	fuerza	INTEGER,
	destreza	INTEGER,
	constitucion	INTEGER,
	inteligencia	INTEGER,
	sabiduria	INTEGER,
	carisma	INTEGER
);

CREATE TABLE tiposentido(
	id SERIAL PRIMARY KEY,
	descripcion	VARCHAR(25) NOT NULL
);

INSERT INTO tiposentido(descripcion) VALUES
('Visión Ciega'),
('Visión en la Oscuridad'),
('Visión Verdadera'),
('Percepción Pasiva');

CREATE TABLE sentidocriatura (
	id	SERIAL PRIMARY KEY,
	idCriatura INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idTipoSentido INTEGER REFERENCES tiposentido(id) ON DELETE CASCADE,
	cantidad INTEGER
);

CREATE TABLE tipodesc(
	id SERIAL PRIMARY KEY,
	descripcion VARCHAR(10) NOT NULL
);

INSERT INTO tipodesc(descripcion) VALUES
('Habilidad'),
('Acción');

CREATE TABLE criaturadetalle(
	id SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idTipoDesc	INTEGER REFERENCES tipodesc(id) ON DELETE CASCADE,
	tituloDetalle	VARCHAR(20),
	descripcionDetalle	VARCHAR(500)
);

CREATE TABLE caracteristica(
	id SERIAL PRIMARY KEY,
	descripcion	VARCHAR(15)
);

INSERT INTO caracteristica(descripcion) VALUES
('Fuerza'),
('Destreza'),
('Constitución'),
('Inteligencia'),
('Sabiduría'),
('Carisma');

CREATE TABLE tiradasalvacion(
	id SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idCaracteristica INTEGER REFERENCES caracteristica(id) ON DELETE CASCADE,
	modificador	INTEGER
);

CREATE TABLE habilidad(
	id SERIAL PRIMARY KEY,
	descripcion VARCHAR(20)
);

INSERT INTO habilidad(descripcion) VALUES
('Acrobacias'),
('Atletismo'),
('Conocimiento Arcano'),
('Engaño'),
('Historia'),
('Interpretación'),
('Intimidación'),
('Investigación'),
('Juego de Manos'),
('Medicina'),
('Naturaleza'),
('Percepción'),
('Perspicacia'),
('Persuasión'),
('Religión'),
('Sigilo'),
('Supervivencia'),
('Trato con Animales');

CREATE TABLE habilidadcriatura(
	id	SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idHabilidad	INTEGER REFERENCES habilidad(id) ON DELETE CASCADE,
	modificador	INTEGER	
);

CREATE TABLE tipocondicion(
	id SERIAL PRIMARY KEY,
	descripcion	VARCHAR(20)
);

INSERT INTO tipocondicion(descripcion) VALUES
('Asustado'),
('Apresado'),
('Aturdido'),
('Cegado'),
('Encantado'),
('Ensordecido'),
('Envenenado'),
('Incapacitado'),
('Inconsciente'),
('Invisible'),
('Neutralizado'),
('Paralizado'),
('Petrificado'),
('Tumbado'),
('Cansancio');

CREATE TABLE inmunidadcondicion(
	id SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idTipoCondicion	INTEGER  REFERENCES tipocondicion(id) ON DELETE CASCADE
);

CREATE TABLE tipodanio (
	id	SERIAL PRIMARY KEY,
	descripcion	VARCHAR(25)
);

INSERT INTO tipodanio(descripcion) VALUES
('Ácido'),
('Contundente'),
('Hielo'),
('Fuego'),
('Force'),
('Relámpago'),
('Necrótico'),
('Perforante'),
('Veneno'),
('Psíquico'),
('Radiante'),
('Cortante'),
('Trueno'),
('Ataque No-Mágico'),
('Ataque No-Plata'),
('Ataque No-Adamantita');

CREATE TABLE resistencia(
	id	SERIAL PRIMARY KEY,
	idCriatura INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idTipoDanio INTEGER REFERENCES tipodanio(id) ON DELETE CASCADE,
	cantidad NUMERIC(2,1)
);

CREATE TABLE iniciativa(
	id SERIAL PRIMARY KEY,
	idUsuario INTEGER REFERENCES usuarios.users(id) ON DELETE CASCADE,
	nombreCriatura VARCHAR(50) NOT NULL UNIQUE,
	valorIniciativa INTEGER NOT NULL,
	idCriatura INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	vida INTEGER
);

CREATE TABLE turno(
	id SERIAL PRIMARY KEY,
	idUsuario INTEGER REFERENCES usuarios.users(id) ON DELETE CASCADE,
	numTurno INTEGER
);


CREATE VIEW criaturas AS
SELECT 
ID, 
NOMBRE, 
CANTDADOS AS DADOS, 
TIPODADO AS TIPO, 
VIDATOTAL AS VIDA,
PUBLICO AS PUBLICO,
ID_PRIVADO AS OWNER 
FROM CRIATURA;

CREATE VIEW acciones AS
SELECT 
	C.ID as IDCRIATURA, 
	C.NOMBRE as NOMBRE,
	TD.DESCRIPCION AS TIPO, 
	CD.TITULODETALLE as TITULO, 
	CD.descripcionDetalle as DETALLE,
	CD.ID AS ID
FROM CriaturaDetalle CD 
INNER JOIN Criatura C ON 
C.id  = CD.idCriatura
INNER JOIN TIPODESC TD ON TD.ID = CD.IDTIPODESC;

CREATE VIEW detalles AS
SELECT
CS.ID AS ID,
C.ID AS IDCRIATURA,
C.NOMBRE AS NOMBRE,
C.CANTDADOS AS DADOS,
C.TIPODADO AS TDADO,
C.VIDATOTAL AS VIDA,
C.MODIFICADORVIDA AS MODIFICADOR,
C.CANTEXP AS EXP,
CS.CLASEARMADURA AS ARMADURA,
CS.VELOCIDAD AS VELOCIDAD,
CS.FUERZA AS FUERZA,
CS.DESTREZA AS DESTREZA,
CS.CONSTITUCION AS CONSTITUCION,
CS.INTELIGENCIA AS INTELIGENCIA,
CS.SABIDURIA AS SABIDURIA,
CS.CARISMA AS CARISMA
FROM CRIATURA C 
INNER JOIN CRIATURASTATS CS ON 
C.ID = CS.IDCRIATURA;

CREATE VIEW sentidos AS
SELECT
SC.ID AS ID,
SC.IDCRIATURA AS IDCRIATURA,
TS.DESCRIPCION AS TIPOSENTIDO,
SC.CANTIDAD AS VALOR
FROM TIPOSENTIDO TS
INNER JOIN SENTIDOCRIATURA SC 
ON TS.ID = SC.idTipoSentido;

CREATE VIEW habilidades AS
SELECT
HC.ID AS ID,
HC.IDCRIATURA AS IDCRIATURA,
H.DESCRIPCION AS HABILIDAD,
HC.MODIFICADOR AS MODIF
FROM HABILIDADCRIATURA HC
INNER JOIN HABILIDAD H ON H.ID = HC.IDHABILIDAD;

CREATE VIEW salvaciones AS
SELECT
TS.ID AS ID,
TS.IDCRIATURA AS IDCRIATURA,
C.DESCRIPCION AS CARAC,
TS.MODIFICADOR AS MODIF
FROM TIRADASALVACION TS
INNER JOIN CARACTERISTICA C ON TS.IDCARACTERISTICA = C.ID;

CREATE VIEW inmunidades AS
SELECT
IC.ID AS ID,
IC.IDCRIATURA AS IDCRIATURA,
TC.DESCRIPCION AS INMUNIDAD
FROM INMUNIDADCONDICION IC
INNER JOIN TIPOCONDICION TC ON TC.ID = IC.IDTIPOCONDICION;

CREATE VIEW resistencias AS
SELECT
R.ID AS ID,
R.IDCRIATURA AS IDCRIATURA,
TD.DESCRIPCION AS RESIST,
R.CANTIDAD AS VALOR
FROM RESISTENCIA R
INNER JOIN TIPODANIO TD ON TD.ID = R.IDTIPODANIO;