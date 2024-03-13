import os
import json

def format_data(input_file, output_file, keys_mapping, output_directory="formatted_json"):
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
format_data('raw_api_data/plu-espaces-libres-a-vegetaliser-elv.json', 
            'plu-espaces-libres-a-vegetaliser-elv-formatted.json',
            {'n_sq_elv': 'Identifiant',
             'st_area_shape': 'Superficie',
             'st_perimeter_shape': 'Périmètre',
             'c_sec': 'Section',
             'c_asp': 'Aspect',
             'geo_point_2d': 'Coordonnées géographiques'})

# Formatage des données pour les secteurs de risques
format_data('raw_api_data/plu-secteurs-de-risques-delimites-par-le-ppri.json', 
            'plu-secteurs-de-risques-delimites-par-le-ppri-formatted.json',
            {'zonage': 'zonage',
             'n_sq_pprizone': 'n_sq_pprizone',
             'st_area_shape': 'st_area_shape',
             'st_perimeter_shape': 'st_perimeter_shape',
             'geo_shape': 'geo_shape',
             'geo_point_2d': 'geo_point_2d'})

# Formatage des données pour l'encadrement des loyers
format_data('raw_api_data/logement-encadrement-des-loyers.json', 
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

# Formatage des données pour les espaces verts protégés
format_data('raw_api_data/plu-espaces-verts-proteges-evp.json', 
            'plu-espaces-verts-proteges-evp-formatted.json',
            {'n_sq_ca': 'n_sq_ca',
             'numevp': 'numevp',
             'texte': 'texte',
             'st_area_shape': 'st_area_shape',
             'st_perimeter_shape': 'st_perimeter_shape',
             'geo_shape': 'geo_shape',
             'geo_point_2d': 'geo_point_2d'})

# Formatage des données pour le DPE France
format_data('raw_api_data/dpe-france.json', 
            'dpe-france-formatted.json',
            {'key': 'key',
             'type': 'type',
             'title': 'title',
             'description': 'description',
             'x-cardinality': 'x-cardinality',
             'x-capabilities': 'x-capabilities',
             'enum': 'enum',
             'format': 'format',
             'x-refersTo': 'x-refersTo',
             'x-concept': 'x-concept'})

# Formatage des données pour les arrondissements
format_data('raw_api_data/arrondissements.json', 
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
