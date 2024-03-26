CREATE TABLE arrondissements (
    id_arrondissement INT PRIMARY KEY,
    numero_arrondissement INT,
    numero_arrondissement_INSEE INT,
    nom_arrondissement VARCHAR(255),
    nom_officiel_arrondissement VARCHAR(255),
    N_SQ_CO INT,
    surface FLOAT,
    perimetre FLOAT,
    geometry_X FLOAT,
    geometry_Y FLOAT,
    geometry VARIANT
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
    Annee INT,
    Secteurs_geographiques INT,
    Numero_du_quartier INT,
    Nom_du_quartier VARCHAR(255),
    Nombre_de_pieces_principales INT,
    Epoque_de_construction VARCHAR(50),
    Type_de_location VARCHAR(50),
    Loyers_de_reference FLOAT,
    Loyers_de_reference_majores FLOAT,
    Loyers_de_reference_minores FLOAT,
    Ville VARCHAR(255),
    Numero_INSEE_du_quartier INT,
    geo_shape VARIANT,
    geo_point_2d VARCHAR(255),
    N_SQ_CO INT,
    FOREIGN KEY (N_SQ_CO) REFERENCES arrondissements(N_SQ_CO)
);

CREATE TABLE plu_espaces_libres_a_vegetaliser_elv (
    N_SQ_ELV INT,
    N_SQ_CA INT,
    N_SQ_PC INT,
    SHAPE_AREA FLOAT,
    SHAPE_LEN FLOAT,
    C_SEC VARCHAR(10),
    C_ASP VARCHAR(20),
    N_PC INT,
    created_user VARCHAR(50),
    created_date VARCHAR(50),
    last_edited_user VARCHAR(50),
    last_edited_date VARCHAR(50),
    geo_shape VARIANT,
    geo_point_2d VARCHAR(255),
    FOREIGN KEY (N_SQ_CA) REFERENCES arrondissements(N_SQ_CA)
);

CREATE TABLE plu_espaces_verts_proteges_evp (
    N_SQ_CA INT,
    NUMEVP INT,
    TEXTE VARCHAR(255),
    created_user VARCHAR(50),
    created_date VARCHAR(50),
    last_edited_user VARCHAR(50),
    last_edited_date VARCHAR(50),
    st_area_shape FLOAT,
    st_perimeter_shape FLOAT,
    geo_shape VARIANT,
    geo_point_2d VARCHAR(255),
    FOREIGN KEY (N_SQ_CA) REFERENCES arrondissements(N_SQ_CA)
);

CREATE TABLE plu_secteurs_de_risques_delimites_par_le_ppri (
    ZONAGE VARCHAR(10),
    N_SQ_PPRIZONE INT,
    st_area FLOAT,
    st_perimeter FLOAT,
    geo_shape TEXT,
    geo_point_2d VARCHAR(50),
    N_SQ_CA INT,
    FOREIGN KEY (N_SQ_CA) REFERENCES arrondissements(N_SQ_CA)
);

CREATE TABLE quartiers_administratifs (
    N_SQ_QU INT PRIMARY KEY,
    C_QU INT,
    C_QUINSEE INT,
    L_QU VARCHAR(30),
    C_AR INT,
    N_SQ_AR INT,
    FOREIGN KEY (N_SQ_AR) REFERENCES arrondissements(N_SQ_CO)
);