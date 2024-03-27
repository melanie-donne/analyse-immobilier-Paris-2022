CREATE TABLE arrondissements (
    Identifiant_séquentiel INT PRIMARY KEY,
    Numéro_arrondissement INT,
    Numéro_arrondissement_INSEE INT,
    Nom_arrondissement VARCHAR(255),
    Nom_officiel_arrondissement VARCHAR(255),
    N_SQ_CO INT,
    Surface DECIMAL(20, 10),
    Périmètre DECIMAL(20, 10),
    Geometry_X_Y VARCHAR(50),
    Geometry GEOMETRY
);

CREATE TABLE ValeursFoncieresParis2022 (
    DateMutation DATE,
    NatureMutation VARCHAR(255),
    ValeurFonciere FLOAT,
    TypeVoie VARCHAR(255),
    CodeVoie VARCHAR(255),
    Voie VARCHAR(255),
    CodePostal VARCHAR(10),
    Commune VARCHAR(255),
    CodeDepartement VARCHAR(10),
    CodeCommune VARCHAR(10),
    TypeLocal VARCHAR(255),
    SurfaceReelleBati FLOAT,
    NombrePiecesPrincipales FLOAT,
    SurfaceTerrain FLOAT,
    N_SQ_CO INT,
    FOREIGN KEY (N_SQ_CO) REFERENCES arrondissements(N_SQ_CO)
);

CREATE TABLE logement_encadrement_des_loyers (
    Année INT,
    Secteurs_géographiques INT,
    Numéro_du_quartier INT PRIMARY KEY,
    Nom_du_quartier VARCHAR(50),
    Nombre_de_pièces_principales INT,
    Epoque_de_construction VARCHAR(20),
    Type_de_location VARCHAR(20),
    Loyers_de_référence DECIMAL(10,2),
    Loyers_de_référence_majorés DECIMAL(10,2),
    Loyers_de_référence_minorés DECIMAL(10,2),
    Ville VARCHAR(50),
    Numéro_INSEE_du_quartier INT,
    geo_shape GEOMETRY,
    geo_point_2d VARCHAR(50),
    FOREIGN KEY (Numéro_INSEE_du_quartier) REFERENCES quartiers_administratifs(N_SQ_QU)
);

CREATE TABLE plu_espaces_libres_a_vegetaliser_elv (
    N_SQ_CA INT PRIMARY KEY,
    NUMEVP INT,
    TEXTE TEXT,
    created_user VARCHAR(50),
    created_date DATE,
    last_edited_user VARCHAR(50),
    last_edited_date DATE,
    st_area_shape DECIMAL(20,10),
    st_perimeter_shape DECIMAL(20,10),
    geo_shape GEOMETRY,
    geo_point_2d VARCHAR(50),
    FOREIGN KEY (N_SQ_CA) REFERENCES arrondissements(Identifiant_séquentiel)
);

CREATE TABLE plu_espaces_verts_proteges_evp (
    N_SQ_ELV INT PRIMARY KEY,
    N_SQ_CA INT,
    N_SQ_PC INT,
    SHAPE_AREA DECIMAL(20,10),
    SHAPE_LEN DECIMAL(20,10),
    C_SEC VARCHAR(50),
    C_ASP VARCHAR(50),
    N_PC INT,
    created_user VARCHAR(50),
    created_date DATE,
    last_edited_user VARCHAR(50),
    last_edited_date DATE,
    geo_shape GEOMETRY,
    geo_point_2d VARCHAR(50),
    FOREIGN KEY (N_SQ_CA) REFERENCES arrondissements(Identifiant_séquentiel)
);

CREATE TABLE plu_secteurs_de_risques_delimites_par_le_ppri (
    ZONAGE VARCHAR(50),
    N_SQ_PPRIZONE INT PRIMARY KEY,
    st_area_shape DECIMAL(20,10),
    st_perimeter_shape DECIMAL(20,10),
    geo_shape GEOMETRY,
    geo_point_2d VARCHAR(50)
);

CREATE TABLE quartiers_administratifs (
    N_SQ_QU INT PRIMARY KEY,
    C_QU INT,
    C_QUINSEE INT,
    L_QU VARCHAR(50),
    C_AR INT,
    N_SQ_AR INT,
    PERIMETRE DECIMAL(20,10),
    SURFACE DECIMAL(20,10),
    Geometry_X_Y VARCHAR(50),
    Geometry GEOMETRY,
    st_area_shape DECIMAL(20,10),
    st_perimeter_shape DECIMAL(20,10),
    FOREIGN KEY (N_SQ_AR) REFERENCES arrondissements(Identifiant_séquentiel)
);

CREATE TABLE etablissements_scolaires_maternelles (
    Type_etablissement_Annee_scolaire VARCHAR(255),
    Libelle_etablissement VARCHAR(255),
    Adresse VARCHAR(255),
    Arrondissement VARCHAR(255),
    Code_INSEE INT,
    Annee_scolaire VARCHAR(255),
    Type_etablissement VARCHAR(255),
    geo_shape GEOMETRY,
    geo_point_2d VARCHAR(50),
    FOREIGN KEY (Code_INSEE) REFERENCES arrondissements(Numéro_arrondissement_INSEE)
);

CREATE TABLE etablissements_scolaires_elementaires (
    Type_etablissement_Annee_scolaire VARCHAR(255),
    Libelle_etablissement VARCHAR(255 ),
    Adresse VARCHAR(255),
    Arrondissement VARCHAR(255),
    Code_INSEE INT,
    Annee_scolaire VARCHAR(255),
    Type_etablissement VARCHAR(255),
    created_user VARCHAR(50),
    created_date DATE,
    last_edited_user VARCHAR(50),
    last_edited_date DATE,
    geo_shape GEOMETRY,
    geo_point_2d VARCHAR(50),
    FOREIGN KEY (Code_INSEE) REFERENCES arrondissements(Numéro_arrondissement_INSEE)
);

CREATE TABLE etablissements_scolaires_colleges (
    Type_etablissement_Annee_scolaire VARCHAR(255),
    Libelle_etablissement VARCHAR(255),
    Adresse VARCHAR(255),
    Arrondissement VARCHAR(255),
    Code_INSEE INT,
    Annee_scolaire VARCHAR(255),
    Type_etablissement VARCHAR(255),
    created_user VARCHAR(50),
    created_date DATE,
    last_edited_user VARCHAR(50),
    last_edited_date DATE,
    geo_shape GEOMETRY,
    geo_point_2d VARCHAR(50),
    FOREIGN KEY (Code_INSEE) REFERENCES arrondissements(Numéro_arrondissement_INSEE)
);
