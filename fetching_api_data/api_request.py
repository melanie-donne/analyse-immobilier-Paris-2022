import os
import requests

def download_csv_from_url(url, destination):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Obtenir le chemin complet du répertoire 'api_data' relativement au dossier du script Python
            api_data_dir = os.path.join(os.path.dirname(__file__), 'api_data')
            # Créer le répertoire 'api_data' s'il n'existe pas
            if not os.path.exists(api_data_dir):
                os.makedirs(api_data_dir)
            # Obtenir le chemin complet du fichier destination dans le dossier 'api_data'
            destination_path = os.path.join(api_data_dir, destination)
            with open(destination_path, 'wb') as f:
                f.write(response.content)
            print(f"Le fichier CSV '{destination}' a été téléchargé avec succès dans le dossier 'api_data'.")
        else:
            print(f"Erreur lors du téléchargement du fichier '{destination}': {response.status_code}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du téléchargement du fichier '{destination}': {str(e)}")

# Les URL des différents fichiers CSV avec leurs destinations dans le dossier 'api_data'
files = [
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/arrondissements/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "arrondissements.csv"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/quartier_paris/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "quartier_administratifs.csv"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/logement-encadrement-des-loyers/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "logement_encadrement_des_loyers.csv"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/plu-secteurs-de-risques-delimites-par-le-ppri/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "plu_secteurs_de_risques_delimites_par_le_ppri.csv"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/plu-espaces-verts-proteges-evp/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "plu_espaces_verts_proteges_evp.csv"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/plu-espaces-libres-a-vegetaliser-elv/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "plu_espaces_libres_a_vegetaliser_elv.csv"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/etablissements-scolaires-maternelles/exports/csv?lang=fr&refine=id_projet%3A%22MATERNELLES%20(ann%C3%A9e%20scolaire%202022%2F2023)%22&facet=facet(name%3D%22id_projet%22%2C%20disjunctive%3Dtrue)&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "etablissements-scolaires-maternelles.csv"),
    ("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/etablissements-scolaires-ecoles-elementaires/exports/csv?lang=fr&refine=id_projet%3A%22ELEMENTAIRES%20(ann%C3%A9e%20scolaire%202022%2F2023)%22&facet=facet(name%3D%22id_projet%22%2C%20disjunctive%3Dtrue)&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "etablissements-scolaires-ecoles-elementaires.csv"),
("https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/etablissements-scolaires-colleges/exports/csv?lang=fr&refine=annee_scol%3A%222022-2023%22&facet=facet(name%3D%22annee_scol%22%2C%20disjunctive%3Dtrue)&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B", "etablissements-scolaires-colleges.csv")
]

# Télécharger chaque fichier dans 'api_data'
for file in files:
    download_csv_from_url(file[0], file[1])