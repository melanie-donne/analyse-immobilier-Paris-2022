-- Modification des noms de colonnes dans la table arrondissements
ALTER TABLE arrondissements
RENAME COLUMN N_SQ_CO TO Numero_d_arrondissement;

-- Modification des noms de colonnes dans la table plu_espaces_libres_a_vegetaliser_elv
ALTER TABLE plu_espaces_libres_a_vegetaliser_elv
RENAME COLUMN N_SQ_ELV TO Identifiant_sequentiel_du_lieu,
RENAME COLUMN N_SQ_CA TO Identifiant_sequentiel_de_l_arrondissement;

-- Modification des noms de colonnes dans la table plu_espaces_verts_proteges_evp
ALTER TABLE plu_espaces_verts_proteges_evp
RENAME COLUMN N_SQ_CA TO Identifiant_sequentiel_de_l_arrondissement;

-- Modification des noms de colonnes dans la table plu_secteurs_de_risques_delimites_par_le_ppri
ALTER TABLE plu_secteurs_de_risques_delimites_par_le_ppri
RENAME COLUMN N_SQ_CA TO Identifiant_sequentiel_de_l_arrondissement;

-- Modification des noms de colonnes dans la table quartiers_administratifs
ALTER TABLE quartiers_administratifs
RENAME COLUMN N_SQ_QU TO Identifiant_sequentiel_du_quartier,
RENAME COLUMN C_QU TO Numero_de_quartier,
RENAME COLUMN C_QUINSEE TO Numero_INSEE_du_quartier,
RENAME COLUMN L_QU TO Nom_du_quartier,
RENAME COLUMN C_AR TO Numero_d_arrondissement;