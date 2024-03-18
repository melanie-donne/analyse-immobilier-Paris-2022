import os
import requests
import json

# Fonction pour faire une requête à une API et sauvegarder les données dans un fichier JSON
def fetch_and_save_data(api_url, output_file):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()  # Convertir la réponse en JSON
        
        # Créer le dossier raw_api_data dans le répertoire fetching_api_data s'il n'existe pas
        raw_data_dir = os.path.join(os.path.dirname(__file__), 'raw_api_data')
        if not os.path.exists(raw_data_dir):
            os.makedirs(raw_data_dir)
        
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file)  # Enregistrer les données JSON dans un fichier
        print(f"Les données ont été récupérées avec succès depuis {api_url} et enregistrées dans {output_file}.")
    else:
        print(f"Erreur lors de la récupération des données depuis {api_url}. Statut de la requête : {response.status_code}")

# Liste des API à interroger avec les URLs correspondantes et les noms des fichiers de sortie
api_urls = [
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/plu-espaces-libres-a-vegetaliser-elv/records", "fetching_api_data/raw_api_data/plu-espaces-libres-a-vegetaliser-elv.json"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/plu-secteurs-de-risques-delimites-par-le-ppri/records", "fetching_api_data/raw_api_data/plu-secteurs-de-risques-delimites-par-le-ppri.json"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/arrondissements/records", "fetching_api_data/raw_api_data/arrondissements.json"),
    ("https://parisdata.opendatasoft.com/api/explore/v2.1/catalog/datasets/quartier_paris/records", "fetching_api_data/raw_api_data/quartiers-administratifs.json"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/logement-encadrement-des-loyers/records","fetching_api_data/raw_api_data/logement-encadrement-des-loyers.json"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/espaces_verts/records","fetching_api_data/raw_api_data/espaces-verts-et-assimiles.json")
]

# Parcourir la liste des API et exécuter la fonction fetch_and_save_data pour chaque API
for api_url, output_file in api_urls:
    fetch_and_save_data(api_url, output_file)