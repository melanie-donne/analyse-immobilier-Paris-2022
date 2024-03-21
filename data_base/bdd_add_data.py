import snowflake.connector
import json
import csv

# Fonction pour insérer des données JSON dans une table Snowflake
def inserer_donnees_json(cur, json_file, table_name):
    try:
        # Lecture du fichier JSON
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Insertion des données dans la table spécifiée
            cur.executemany(f"""
                INSERT INTO {table_name} ({', '.join(data[0].keys())})
                VALUES ({', '.join(['%s' for _ in data[0].keys()])})
            """, [tuple(item.values()) for item in data])
    except (snowflake.connector.errors.ProgrammingError, FileNotFoundError, json.JSONDecodeError) as e:
        # Gestion des erreurs
        print(f"Erreur lors de l'insertion des données JSON : {e}")

# Fonction pour insérer des données CSV dans une table Snowflake
def inserer_donnees_csv(cur, csv_file, table_name):
    try:
        # Lecture du fichier CSV
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Insertion des données dans la table spécifiée
            cur.executemany(f"""
                INSERT INTO {table_name} ({', '.join(reader.fieldnames)})
                VALUES ({', '.join(['%s' for _ in reader.fieldnames])})
            """, [tuple(row.values()) for row in reader])
    except (snowflake.connector.errors.ProgrammingError, FileNotFoundError, csv.Error) as e:
        # Gestion des erreurs
        print(f"Erreur lors de l'insertion des données CSV : {e}")

def main():
    try:
        # Connexion à la base de données Snowflake
        conn = snowflake.connector.connect(
            user='<utilisateur>',
            password='<mot_de_passe>',
            account='<nom_compte_snowflake>',
            warehouse='<entrepôt_snowflake>',
            database='<base_de_donnees_snowflake>',
            schema='<schema_snowflake>'
        )
        cur = conn.cursor()

        # Insertion des données à partir des fichiers JSON
        inserer_donnees_json(cur, 'arrondissements-formatted.json', 'Arrondissements')
        inserer_donnees_json(cur, 'espaces-verts-assimiles-formatted.json', 'EspacesVertsAssimiles')
        inserer_donnees_json(cur, 'logement-encadrement-loyers-formatted.json', 'LogementEncadrementLoyers')
        inserer_donnees_json(cur, 'plu-espaces-libres-a-vegetaliser-elv-formatted.json', 'PLUEspacesLibresVegetaliser')
        inserer_donnees_json(cur, 'plu-secteurs-de-risques-delimites-par-le-ppri-formatted.json', 'PLUSecteursRisquesPPRI')
        inserer_donnees_json(cur, 'quartiers-administratifs-formatted.json', 'QuartiersAdministratifs')

        # Insertion des données à partir du fichier CSV
        inserer_donnees_csv(cur, 'valeursfoncieres_paris_2022.csv', 'ValeursFoncieresParis2022')

        # Validation des modifications et fermeture de la connexion
        conn.commit()
    except snowflake.connector.errors.DatabaseError as e:
        # Gestion des erreurs Snowflake
        print(f"Erreur Snowflake : {e}")
    finally:
        # Fermeture de la connexion à la base de données
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
