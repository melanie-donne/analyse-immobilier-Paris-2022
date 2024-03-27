import os
import pandas as pd

# Chemin du fichier CSV des arrondissements
arrondissements_csv_path = 'fetching_api_data/api_data/arrondissements.csv'

# Vérifier si le fichier des arrondissements existe
if os.path.exists(arrondissements_csv_path):
    print("Le fichier des arrondissements existe.")
else:
    print("Le fichier des arrondissements n'existe pas.")

# Vérifier si le fichier des arrondissements existe
if os.path.isfile(arrondissements_csv_path):
    # Charger le fichier CSV des arrondissements
    arrondissements_df = pd.read_csv(arrondissements_csv_path, delimiter=';')

    # Renommer les colonnes des arrondissements
    arrondissements_df.rename(columns={
        'Identifiant séquentiel de l’arrondissement': 'IDENTIFIANT_SEQUENTIEL',
        'Numéro d’arrondissement': 'NUMERO_ARRONDISSEMENT',
        'Numéro d’arrondissement INSEE': 'NUMERO_ARRONDISSEMENT_INSEE',
        'Nom de l’arrondissement': 'NOM_ARRONDISSEMENT',
        'Nom officiel de l’arrondissement': 'NOM_OFFICIEL_ARRONDISSEMENT',
        'n_sq_co': 'N_SQ_CO',
        'Surface': 'SURFACE',
        'Périmètre': 'PERIMETRE',
        'Geometry X Y': 'GEOMETRY_X_Y',
        'Geometry': 'GEOMETRY'
    }, inplace=True)

    # Enregistrer le fichier CSV des arrondissements avec les nouveaux noms d'en-têtes
    arrondissements_df.to_csv(arrondissements_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des arrondissements ont été modifiés avec succès.")
else:
    print("Le fichier 'arrondissements.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV des établissements scolaires (collèges)
etablissements_colleges_csv_path = 'fetching_api_data/api_data/etablissements-scolaires-colleges.csv'

# Vérifier si le fichier des établissements scolaires (collèges) existe
if os.path.exists(etablissements_colleges_csv_path):
    print("Le fichier des établissements scolaires (collèges) existe.")
else:
    print("Le fichier des établissements scolaires (collèges) n'existe pas.")

# Vérifier si le fichier des établissements scolaires (collèges) existe
if os.path.isfile(etablissements_colleges_csv_path):
    # Charger le fichier CSV des établissements scolaires (collèges)
    etablissements_colleges_df = pd.read_csv(etablissements_colleges_csv_path, delimiter=';')

    # Renommer les colonnes des établissements scolaires (collèges)
    etablissements_colleges_df.rename(columns={
        'Type d\'établissement - Année scolaire': 'TYPE_ETABLISSEMENT_ANNEE_SCOLAIRE',
        'Libellé établissement': 'LIBELLE_ETABLISSEMENT',
        'Adresse': 'ADRESSE',
        'Arrondissement': 'ARRONDISSEMENT',
        'Code INSEE': 'CODE_INSEE NUMBER',
        'Année scolaire': 'ANNEE_SCOLAIRE',
        'Type établissement': 'TYPE_ETABLISSEMENT',
        'created_user': 'CREATED_USER',
        'created_date': 'CREATED_DATE',
        'last_edited_user': 'LAST_EDITED_USER',
        'last_edited_date': 'LAST_EDITED_DATE',
        'geo_shape': 'GEO_SHAPE',
        'geo_point_2d': 'GEO_POINT_2D'
    }, inplace=True)

    # Enregistrer le fichier CSV des établissements scolaires (collèges) avec les nouveaux noms d'en-têtes
    etablissements_colleges_df.to_csv(etablissements_colleges_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des établissements scolaires (collèges) ont été modifiés avec succès.")
else:
    print("Le fichier 'etablissements-scolaires-colleges.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV des établissements scolaires (écoles élémentaires)
etablissements_ecoles_elementaires_csv_path = 'fetching_api_data/api_data/etablissements-scolaires-ecoles-elementaires.csv'

# Vérifier si le fichier des établissements scolaires (écoles élémentaires) existe
if os.path.exists(etablissements_ecoles_elementaires_csv_path):
    print("Le fichier des établissements scolaires (écoles élémentaires) existe.")
else:
    print("Le fichier des établissements scolaires (écoles élémentaires) n'existe pas.")

# Vérifier si le fichier des établissements scolaires (écoles élémentaires) existe
if os.path.isfile(etablissements_ecoles_elementaires_csv_path):
    # Charger le fichier CSV des établissements scolaires (écoles élémentaires)
    etablissements_ecoles_elementaires_df = pd.read_csv(etablissements_ecoles_elementaires_csv_path, delimiter=';')

    # Renommer les colonnes des établissements scolaires (écoles élémentaires)
    etablissements_ecoles_elementaires_df.rename(columns={
        'Type d\'établissement - Année scolaire': 'TYPE_ETABLISSEMENT_ANNEE_SCOLAIRE',
        'Libellé établissement': 'LIBELLE_ETABLISSEMENT',
        'Adresse': 'ADRESSE',
        'Arrondissement': 'ARRONDISSEMENT',
        'Code INSEE': 'CODE_INSEE NUMBER',
        'Année scolaire': 'ANNEE_SCOLAIRE',
        'Type établissement': 'TYPE_ETABLISSEMENT',
        'created_user': 'CREATED_USER',
        'created_date': 'CREATED_DATE',
        'last_edited_user': 'LAST_EDITED_USER',
        'last_edited_date': 'LAST_EDITED_DATE',
        'geo_shape': 'GEO_SHAPE',
        'geo_point_2d': 'GEO_POINT_2D'
    }, inplace=True)

    # Enregistrer le fichier CSV des établissements scolaires (écoles élémentaires) avec les nouveaux noms d'en-têtes
    etablissements_ecoles_elementaires_df.to_csv(etablissements_ecoles_elementaires_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des établissements scolaires (écoles élémentaires) ont été modifiés avec succès.")
else:
    print("Le fichier 'etablissements-scolaires-ecoles-elementaires.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV des établissements scolaires (maternelles)
etablissements_maternelles_csv_path = 'fetching_api_data/api_data/etablissements-scolaires-maternelles.csv'

# Vérifier si le fichier des établissements scolaires (maternelles) existe
if os.path.exists(etablissements_maternelles_csv_path):
    print("Le fichier des établissements scolaires (maternelles) existe.")
else:
    print("Le fichier des établissements scolaires (maternelles) n'existe pas.")

# Vérifier si le fichier des établissements scolaires (maternelles) existe
if os.path.isfile(etablissements_maternelles_csv_path):
    # Charger le fichier CSV des établissements scolaires (maternelles)
    etablissements_maternelles_df = pd.read_csv(etablissements_maternelles_csv_path, delimiter=';')

    # Renommer les colonnes des établissements scolaires (maternelles)
    etablissements_maternelles_df.rename(columns={
        'Type d\'établissement - Année scolaire': 'TYPE_ETABLISSEMENT_ANNEE_SCOLAIRE',
        'Libellé établissement': 'LIBELLE_ETABLISSEMENT',
        'Adresse': 'ADRESSE',
        'Arrondissement': 'ARRONDISSEMENT',
        'Code INSEE': 'CODE_INSEE NUMBER',
        'Année scolaire': 'ANNEE_SCOLAIRE',
        'Type établissement': 'TYPE_ETABLISSEMENT',
        'created_user': 'CREATED_USER',
        'created_date': 'CREATED_DATE',
        'last_edited_user': 'LAST_EDITED_USER',
        'last_edited_date': 'LAST_EDITED_DATE',
        'geo_shape': 'GEO_SHAPE',
        'geo_point_2d': 'GEO_POINT_2D'
    }, inplace=True)

    # Enregistrer le fichier CSV des établissements scolaires (maternelles) avec les nouveaux noms d'en-têtes
    etablissements_maternelles_df.to_csv(etablissements_maternelles_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des établissements scolaires (maternelles) ont été modifiés avec succès.")
else:
    print("Le fichier 'etablissements-scolaires-maternelles.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV des données sur les logements encadrés des loyers
logement_encadrement_des_loyers_csv_path = 'fetching_api_data/api_data/logement_encadrement_des_loyers.csv'

# Vérifier si le fichier des données sur les logements encadrés des loyers existe
if os.path.exists(logement_encadrement_des_loyers_csv_path):
    print("Le fichier des données sur les logements encadrés des loyers existe.")
else:
    print("Le fichier des données sur les logements encadrés des loyers n'existe pas.")

# Vérifier si le fichier des données sur les logements encadrés des loyers existe
if os.path.isfile(logement_encadrement_des_loyers_csv_path):
    # Charger le fichier CSV des données sur les logements encadrés des loyers
    logement_encadrement_des_loyers_df = pd.read_csv(logement_encadrement_des_loyers_csv_path, delimiter=';')

    # Renommer les colonnes des données sur les logements encadrés des loyers
    logement_encadrement_des_loyers_df.rename(columns={
        'Année': 'ANNEE',
        'Secteurs géographiques': 'SECTEURS_GEOGRAPHIQUES',
        'Numéro du quartier': 'NUMERO_DU_QUARTIER',
        'Nom du quartier': 'NOM_DU_QUARTIER',
        'Nombre de pièces principales': 'NOMBRE_DE_PIECES_PRINCIPALES',
        'Epoque de construction': 'EPOQUE_DE_CONSTRUCTION',
        'Type de location': 'TYPE_DE_LOCATION',
        'Loyers de référence': 'LOYERS_DE_REFERENCE',
        'Loyers de référence majorés': 'LOYERS_DE_REFERENCE_MAJORES',
        'Loyers de référence minorés': 'LOYERS_DE_REFERENCE_MINORES',
        'Ville': 'VILLE',
        'Numéro INSEE du quartier': 'NUMERO_INSEE_DU_QUARTIER',
        'geo_shape': 'GEO_SHAPE',
        'geo_point_2d': 'GEO_POINT_2D'
    }, inplace=True)

    # Enregistrer le fichier CSV des données sur les logements encadrés des loyers avec les nouveaux noms d'en-têtes
    logement_encadrement_des_loyers_df.to_csv(logement_encadrement_des_loyers_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des données sur les logements encadrés des loyers ont été modifiés avec succès.")
else:
    print("Le fichier 'logement_encadrement_des_loyers.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV des espaces libres à végétaliser
plu_espaces_libres_a_vegetaliser_elv_csv_path = 'fetching_api_data/api_data/plu_espaces_libres_a_vegetaliser_elv.csv'

# Vérifier si le fichier des espaces libres à végétaliser existe
if os.path.exists(plu_espaces_libres_a_vegetaliser_elv_csv_path):
    print("Le fichier des espaces libres à végétaliser existe.")
else:
    print("Le fichier des espaces libres à végétaliser n'existe pas.")

# Vérifier si le fichier des espaces libres à végétaliser existe
if os.path.isfile(plu_espaces_libres_a_vegetaliser_elv_csv_path):
    # Charger le fichier CSV des espaces libres à végétaliser
    plu_espaces_libres_a_vegetaliser_elv_df = pd.read_csv(plu_espaces_libres_a_vegetaliser_elv_csv_path, delimiter=';')

    # Renommer les colonnes des espaces libres à végétaliser
    plu_espaces_libres_a_vegetaliser_elv_df.rename(columns={
        'N_SQ_ELV': 'N_SQ_CA',
        'N_SQ_CA': 'NUMEVP',
        'N_SQ_PC': 'TEXTE',
        'SHAPE.AREA': 'ST_AREA_SHAPE',
        'SHAPE.LEN': 'ST_PERIMETER_SHAPE',
        'C_SEC': 'GEO_SHAPE',
        'C_ASP': 'GEO_POINT_2D',
        'N_PC': 'N_PC',
        'created_user': 'CREATED_USER',
        'created_date': 'CREATED_DATE',
        'last_edited_user': 'LAST_EDITED_USER',
        'last_edited_date': 'LAST_EDITED_DATE',
        'geo_shape': 'GEO_SHAPE_OLD',
        'geo_point_2d': 'GEO_POINT_2D_OLD'
    }, inplace=True)

    # Enregistrer le fichier CSV des espaces libres à végétaliser avec les nouveaux noms d'en-têtes
    plu_espaces_libres_a_vegetaliser_elv_df.to_csv(plu_espaces_libres_a_vegetaliser_elv_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des espaces libres à végétaliser ont été modifiés avec succès.")
else:
    print("Le fichier 'plu_espaces_libres_a_vegetaliser_elv.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV des espaces verts protégés
plu_espaces_verts_proteges_evp_csv_path = 'fetching_api_data/api_data/plu_espaces_verts_proteges_evp.csv'

# Vérifier si le fichier des espaces verts protégés existe
if os.path.exists(plu_espaces_verts_proteges_evp_csv_path):
    print("Le fichier des espaces verts protégés existe.")
else:
    print("Le fichier des espaces verts protégés n'existe pas.")

# Vérifier si le fichier des espaces verts protégés existe
if os.path.isfile(plu_espaces_verts_proteges_evp_csv_path):
    # Charger le fichier CSV des espaces verts protégés
    plu_espaces_verts_proteges_evp_df = pd.read_csv(plu_espaces_verts_proteges_evp_csv_path, delimiter=';')

    # Renommer les colonnes des espaces verts protégés
    plu_espaces_verts_proteges_evp_df.rename(columns={
        'N_SQ_CA': 'N_SQ_ELV',
        'NUMEVP': 'N_SQ_CA',
        'TEXTE': 'N_SQ_PC',
        'created_user': 'CREATED_USER',
        'created_date': 'CREATED_DATE',
        'last_edited_user': 'LAST_EDITED_USER',
        'last_edited_date': 'LAST_EDITED_DATE',
        'st_area(shape)': 'SHAPE_AREA',
        'st_perimeter(shape)': 'SHAPE_LEN',
        'geo_shape': 'GEO_SHAPE',
        'geo_point_2d': 'GEO_POINT_2D'
    }, inplace=True)

    # Enregistrer le fichier CSV des espaces verts protégés avec les nouveaux noms d'en-têtes
    plu_espaces_verts_proteges_evp_df.to_csv(plu_espaces_verts_proteges_evp_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des espaces verts protégés ont été modifiés avec succès.")
else:
    print("Le fichier 'plu_espaces_verts_proteges_evp.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV des secteurs de risques délimités par le PPRI
plu_secteurs_de_risques_delimites_par_le_ppri_csv_path = 'fetching_api_data/api_data/plu_secteurs_de_risques_delimites_par_le_ppri.csv'

# Vérifier si le fichier des secteurs de risques existe
if os.path.exists(plu_secteurs_de_risques_delimites_par_le_ppri_csv_path):
    print("Le fichier des secteurs de risques existe.")
else:
    print("Le fichier des secteurs de risques n'existe pas.")

# Vérifier si le fichier des secteurs de risques existe
if os.path.isfile(plu_secteurs_de_risques_delimites_par_le_ppri_csv_path):
    # Charger le fichier CSV des secteurs de risques
    plu_secteurs_de_risques_delimites_par_le_ppri_df = pd.read_csv(plu_secteurs_de_risques_delimites_par_le_ppri_csv_path, delimiter=';')

    # Renommer les colonnes des secteurs de risques
    plu_secteurs_de_risques_delimites_par_le_ppri_df.rename(columns={
        'ZONAGE': 'ZONAGE',
        'N_SQ_PPRIZONE': 'N_SQ_PPRIZONE',
        'st_area(shape)': 'ST_AREA_SHAPE',
        'st_perimeter(shape)': 'ST_PERIMETER_SHAPE',
        'geo_shape': 'GEO_SHAPE',
        'geo_point_2d': 'GEO_POINT_2D'
    }, inplace=True)

    # Enregistrer le fichier CSV des secteurs de risques avec les nouveaux noms d'en-têtes
    plu_secteurs_de_risques_delimites_par_le_ppri_df.to_csv(plu_secteurs_de_risques_delimites_par_le_ppri_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des secteurs de risques ont été modifiés avec succès.")
else:
    print("Le fichier 'plu_secteurs_de_risques_delimites_par_le_ppri.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")


###################################################################################################################################################################
# Chemin du fichier CSV des quartiers administratifs
quartiers_administratifs_csv_path = 'fetching_api_data/api_data/quartier_administratifs.csv'

# Vérifier si le fichier des quartiers administratifs existe
if os.path.exists(quartiers_administratifs_csv_path):
    print("Le fichier des quartiers administratifs existe.")
else:
    print("Le fichier des quartiers administratifs n'existe pas.")

# Vérifier si le fichier des quartiers administratifs existe
if os.path.isfile(quartiers_administratifs_csv_path):
    # Charger le fichier CSV des quartiers administratifs
    quartiers_administratifs_df = pd.read_csv(quartiers_administratifs_csv_path, delimiter=';')

    # Renommer les colonnes des quartiers administratifs
    quartiers_administratifs_df.rename(columns={
        'N_SQ_QU': 'N_SQ_QU',
        'C_QU': 'C_QU',
        'C_QUINSEE': 'C_QUINSEE',
        'L_QU': 'L_QU',
        'C_AR': 'C_AR',
        'N_SQ_AR': 'N_SQ_AR',
        'PERIMETRE': 'PERIMETRE',
        'SURFACE': 'SURFACE',
        'Geometry X Y': 'GEOMETRY_X_Y',
        'Geometry': 'GEOMETRY',
        'st_area(shape)': 'ST_AREA_SHAPE',
        'st_perimeter(shape)': 'ST_PERIMETER_SHAPE'
    }, inplace=True)

    # Enregistrer le fichier CSV des quartiers administratifs avec les nouveaux noms d'en-têtes
    quartiers_administratifs_df.to_csv(quartiers_administratifs_csv_path, sep=';', index=False)

    print("Les noms des en-têtes du fichier des quartiers administratifs ont été modifiés avec succès.")
else:
    print("Le fichier 'quartier_administratifs.csv' n'a pas été trouvé dans 'api_data'. Veuillez vérifier que le téléchargement a réussi.")

###################################################################################################################################################################
# Chemin du fichier CSV
valeursfoncieres_csv_path = 'data_cleaning/valeursfoncieres_paris_2022.csv'

# Vérifier si le fichier existe
if os.path.exists(valeursfoncieres_csv_path):
    print("Le fichier existe.")
else:
    print("Le fichier n'existe pas.")

# Vérifier si le fichier existe
if os.path.isfile(valeursfoncieres_csv_path):
    # Charger le fichier CSV
    valeursfoncieres_df = pd.read_csv(valeursfoncieres_csv_path)

    # Renommer les colonnes
    valeursfoncieres_df.rename(columns={
        'Date mutation': 'DATEMUTATION',
        'Nature mutation': 'NATUREMUTATION',
        'Valeur fonciere': 'VALEURFONCIERE',
        'Type de voie': 'TYPEVOIE',
        'Code voie': 'CODEVOIE',
        'Voie': 'VOIE',
        'Code postal': 'CODEPOSTAL',
        'Commune': 'COMMUNE',
        'Code departement': 'CODEDEPARTEMENT',
        'Code commune': 'CODECOMMUNE',
        'Type local': 'TYPELOCAL',
        'Surface reelle bati': 'SURFACEREELLEBATI',
        'Nombre pieces principales': 'NOMBREPIECESPRINCIPALES',
        'Surface terrain': 'SURFACETERRAIN'
    }, inplace=True)

    # Enregistrer le fichier CSV avec les nouveaux noms d'en-têtes
    valeursfoncieres_df.to_csv(valeursfoncieres_csv_path, index=False)

    print("Les noms des en-têtes ont été modifiés avec succès.")
else:
    print("Le fichier 'valeursfoncieres_paris_2022.csv' n'a pas été trouvé. Veuillez vérifier le chemin.")

# Extraire le numéro de l'arrondissement
valeursfoncieres_df['NUMERO_ARRONDISSEMENT'] = valeursfoncieres_df['COMMUNE'].str.extract(r'(\d+)')
valeursfoncieres_df['NUMERO_ARRONDISSEMENT'] = valeursfoncieres_df['NUMERO_ARRONDISSEMENT'].astype(str).str.lstrip('0')

# Chemin du nouveau fichier CSV avec les modifications
nouveau_csv_path = 'data_cleaning/valeursfoncieres_paris_2022.csv'

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
valeursfoncieres_df.to_csv(nouveau_csv_path, index=False)

print(f"Les modifications ont été enregistrées dans le fichier '{nouveau_csv_path}'.")