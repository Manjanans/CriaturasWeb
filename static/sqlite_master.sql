CREATE TABLE CRIATURA (
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

CREATE TABLE CriaturaStats(
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

CREATE TABLE TipoSentido(
	id SERIAL PRIMARY KEY,
	descripcion	VARCHAR(25) NOT NULL
);

INSERT INTO TIPOSENTIDO(DESCRIPCION) VALUES
('Visión Ciega'),
('Visión en la Oscuridad'),
('Visión Verdadera'),
('Percepción Pasiva');

CREATE TABLE SentidoCriatura (
	id	SERIAL PRIMARY KEY,
	idCriatura INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idTipoSentido INTEGER REFERENCES TipoSentido(id) ON DELETE CASCADE,
	cantidad INTEGER
);

CREATE TABLE TIPODESC(
	idTipoDesc SERIAL PRIMARY KEY,
	tipoDesc VARCHAR(10) NOT NULL
);

INSERT INTO TIPODESC (tipoDesc) VALUES
('Habilidad'),
('Acción');

CREATE TABLE CRIATURADETALLE(
	id SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES CRIATURA(id) ON DELETE CASCADE,
	idTipoDesc	INTEGER REFERENCES TIPODESC(id) ON DELETE CASCADE,
	tituloDetalle	TEXT,
	descripcionDetalle	TEXT,
	cantDados	INTEGER,
	tipoDado	INTEGER,
	modificadorAtaque	INTEGER
);

CREATE TABLE Caracteristica(
	id SERIAL PRIMARY KEY,
	descripcion	VARCHAR(15) NOT NULL
);

INSERT INTO Caracteristica(descripcion) VALUES
('Fuerza'),
('Destreza'),
('Constitución'),
('Inteligencia'),
('Sabiduría'),
('Carisma');

CREATE TABLE TiradaSalvacion(
	id SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idCaracteristica INTEGER REFERENCES Caracteristica(id) ON DELETE CASCADE,
	modificador	INTEGER NOT NULL
);

CREATE TABLE Habilidad(
	id SERIAL PRIMARY KEY,
	descripcion VARCHAR(20) NOT NULL
);

INSERT INTO Habilidad(descripcion) VALUES
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

CREATE TABLE HabilidadCriatura(
	id	SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES CRIATURA(id) ON DELETE CASCADE,
	idHabilidad	INTEGER REFERENCES HABILIDAD(id) ON DELETE CASCADE,
	modificador	INTEGER NOT NULL	
);

CREATE TABLE TipoCondicion(
	id SERIAL PRIMARY KEY,
	descripcion	TEXT
);

INSERT INTO TipoCondicion(descripcion) VALUES
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

CREATE TABLE InmunidadCondicion(
	id SERIAL PRIMARY KEY,
	idCriatura	INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idTipoCondicion	INTEGER  REFERENCES TipoCondicion(id) ON DELETE CASCADE
);

CREATE TABLE TipoDanio (
	id	SERIAL PRIMARY KEY,
	descripcion	VARCHAR(25) NOT NULL
);

INSERT INTO TipoDanio(descripcion) VALUES
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

CREATE TABLE Resistencia(
	id	SERIAL PRIMARY KEY,
	idCriatura INTEGER REFERENCES criatura(id) ON DELETE CASCADE,
	idTipoDanio INTEGER REFERENCES TipoDanio(id) ON DELETE CASCADE,
	cantidad NUMERIC(2,1) NOT NULL
);

INICIATIVA Y TURNO