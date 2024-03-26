CREATE TABLE ValeursFoncieresParis2022 (
	id_valeurFonciere INT PRIMARY KEY,
	Adresse VARCHAR(255),
	CodePostal VARCHAR(10),
	Surface FLOAT,
	ValeurFonciere FLOAT,
	DateMutation DATE,
	CodeArrondissement INT,
	FOREIGN KEY (CodeArrondissement) REFERENCES Arrondissements(CodeArrondissement)
);

CREATE TABLE Arrondissements (
	id_arrondissement INT PRIMARY KEY,
	NomArrondissement VARCHAR(255)
);

CREATE TABLE EspacesVertsAssimiles (
	id_espaceVertAssimile INT PRIMARY KEY,
	Nom VARCHAR(255),
	Superficie FLOAT,
	Perimetre FLOAT,
	Longitude FLOAT,
	Latitude FLOAT
);

CREATE TABLE LogementEncadrementLoyers (
	id_logementEncadrementLoyers INT PRIMARY KEY,
	CodePostal VARCHAR(10),
	Surface FLOAT,
	LoyerMensuel FLOAT
);

CREATE TABLE PLUEspacesLibresVegetaliser (
	id_PLUEspaceLibreVegetaliser INT PRIMARY KEY,
	Superficie FLOAT,
	Perimetre FLOAT,
	Longitude FLOAT,
	Latitude FLOAT
);

CREATE TABLE PLUSecteursRisquesPPRI (
	id_PLUSecteurRisquePPRI INT PRIMARY KEY,
	Zonage VARCHAR(10),
	N_sq_PPRIzone INT,
	Surface FLOAT,
	Perimetre FLOAT,
	PointsDeGeometrie GEOMETRY,
	Longitude FLOAT,
	Latitude FLOAT
);

CREATE TABLE QuartiersAdministratifs (
	id_quartierAdministratif INT PRIMARY KEY,
	CodeQuartier VARCHAR(10),
	CodeQuartierINSEE VARCHAR(10),
	NomQuartier VARCHAR(255),
	CodeArrondissement INT,
	CodeArrondissementINSEE VARCHAR(10),
	Perimetre FLOAT,
	Surface FLOAT,
	PointsDeGeometrie GEOMETRY,
	Longitude FLOAT,
	Latitude FLOAT,
	FOREIGN KEY (CodeArrondissement) REFERENCES Arrondissements(CodeArrondissement)
);

