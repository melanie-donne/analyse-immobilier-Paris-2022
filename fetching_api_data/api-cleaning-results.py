import os
import json

def format_data(input_file, output_file, keys_mapping, output_directory="fetching_api_data/formatted_json"):
    # Charger les données depuis le fichier d'entrée au format JSON
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Initialiser une liste pour stocker les données formatées
    formatted_data = []
    
    # Parcourir chaque entrée dans les données
    for entry in data.get('results', []):
        # Créer une entrée formatée en utilisant le mapping des clés
        formatted_entry = {keys_mapping[key]: entry[key] for key in keys_mapping if key in entry}
        formatted_data.append(formatted_entry)

    # Créer le répertoire de sortie s'il n'existe pas déjà
    os.makedirs(output_directory, exist_ok=True)

    # Écrire les données formatées dans un nouveau fichier JSON
    with open(os.path.join(output_directory, output_file), 'w', encoding='utf-8') as outfile:
        json.dump(formatted_data, outfile, indent=2)

# Formatage des données pour les espaces libres à végétaliser
format_data('fetching_api_data/raw_api_data/plu-espaces-libres-a-vegetaliser-elv.json', 
            'plu-espaces-libres-a-vegetaliser-elv-formatted.json',
            {'n_sq_elv': 'Identifiant',
             'st_area_shape': 'Superficie',
             'st_perimeter_shape': 'Périmètre',
             'c_sec': 'Section',
             'c_asp': 'Aspect',
             'geo_point_2d': 'Coordonnées géographiques'})

# Formatage des données pour les secteurs de risques
format_data('fetching_api_data/raw_api_data/plu-secteurs-de-risques-delimites-par-le-ppri.json', 
            'plu-secteurs-de-risques-delimites-par-le-ppri-formatted.json',
            {'zonage': 'zonage',
             'n_sq_pprizone': 'n_sq_pprizone',
             'st_area_shape': 'st_area_shape',
             'st_perimeter_shape': 'st_perimeter_shape',
             'geo_shape': 'geo_shape',
             'geo_point_2d': 'geo_point_2d'})

# Formatage des données pour l'encadrement des loyers
format_data('fetching_api_data/raw_api_data/logement-encadrement-des-loyers.json', 
            'logement-encadrement-des-loyers-formatted.json',
            {'annee': 'annee',
             'id_zone': 'id_zone',
             'id_quartier': 'id_quartier',
             'nom_quartier': 'nom_quartier',
             'piece': 'piece',
             'epoque': 'epoque',
             'meuble_txt': 'meuble_txt',
             'ref': 'ref',
             'max': 'max',
             'min': 'min',
             'ville': 'ville',
             'code_grand_quartier': 'code_grand_quartier',
             'geo_shape': 'geo_shape',
             'geo_point_2d': 'geo_point_2d'})

# Formatage des données pour les arrondissements
format_data('fetching_api_data/raw_api_data/arrondissements.json', 
            'arrondissements-formatted.json',
            {'n_sq_ar': 'n_sq_ar',
             'c_ar': 'c_ar',
             'c_arinsee': 'c_arinsee',
             'l_ar': 'l_ar',
             'l_aroff': 'l_aroff',
             'surface': 'surface',
             'perimetre': 'perimetre',
             'geom_x_y': 'geom_x_y',
             'coordinates': 'coordinates'})

# Formatage des données pour les quartiers administratifs
format_data('fetching_api_data/raw_api_data/quartiers-administratifs.json', 
            'quartiers-administratifs-formatted.json',
            {'n_sq_qu': 'n_sq_qu',
             'c_qu': 'c_qu',
             'c_quinsee': 'c_quinsee',
             'l_qu': 'l_qu',
             'c_ar': 'c_ar',
             'n_sq_ar': 'n_sq_ar',
             'perimetre': 'perimetre',
             'surface': 'surface',
             'geom_x_y': 'geom_x_y',
             'geom': 'geom',
             'st_area_shape': 'st_area_shape',
             'st_perimeter_shape': 'st_perimeter_shape'})

# Formatage des données pour les espaces verts et assimilés
format_data('fetching_api_data/raw_api_data/espaces-verts-et-assimiles.json', 
            'espaces-verts-et-assimiles.json',
            {'nsq_espace_vert': 'Identifiant',
             'nom_ev': 'Nom',
             'type_ev': 'Type',
             'categorie': 'Catégorie',
             'adresse_numero': 'Numéro',
             'adresse_complement': 'Complément',
             'adresse_typevoie': 'Type de voie',
             'adresse_libellevoie': 'Libellé de voie',
             'adresse_codepostal': 'Code postal',
             'poly_area': 'Superficie',
             'surface_totale_reelle': 'Surface totale réelle',
             'surface_horticole': 'Surface horticole',
             'presence_cloture': 'Présence de clôture',
             'perimeter': 'Périmètre',
             'annee_ouverture': 'Année d\'ouverture',
             'annee_renovation': 'Année de rénovation',
             'ancien_nom_ev': 'Ancien nom',
             'annee_changement_nom': 'Année de changement de nom',
             'nb_entites': 'Nombre d\'entités',
             'ouvert_ferme': 'Ouvert/Fermé',
             'id_division': 'ID de division',
             'id_atelier_horticole': 'ID d\'atelier horticole',
             'ida3d_enb': 'ID 3D ENB',
             'site_villes': 'Site Villes',
             'id_eqpt': 'ID Équipement',
             'competence': 'Compétence',
             'geom': 'Géométrie'})
