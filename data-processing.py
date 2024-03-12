import pandas as pd

# Charger les données de 2022
vf2022 = pd.read_csv("./valeursfoncieres-2022.txt", sep="|", low_memory=False)

# Nettoyage des colonnes avec des données manquantes
# Identifier les colonnes avec des valeurs manquantes
columns_with_nan = vf2022.columns[vf2022.isna().any()]

# Parcourir les colonnes avec des valeurs manquantes
for column in columns_with_nan:
    # Calculer le pourcentage de valeurs manquantes dans la colonne
    percentage_missing = vf2022[column].isna().sum() * 100.0 / vf2022.shape[0]
    # Supprimer la colonne si le pourcentage de valeurs manquantes est supérieur à 50%
    if percentage_missing > 50:
        vf2022.drop(column, axis=1, inplace=True)

# Supprimer les colonnes inutiles
useless_columns = ['Section', 'No plan', 'Nombre de lots', 'Code type local', 'Nature culture', 'No voie', 'No disposition']
vf2022.drop(useless_columns, axis=1, inplace=True)

# Nettoyage des lignes avec des données manquantes
# Supprimer les lignes avec au moins 14 valeurs manquantes
vf2022 = vf2022.dropna(axis=0, thresh=14)

# Remplacer les virgules par des points dans la colonne "Valeur fonciere"
vf2022["Valeur fonciere"] = vf2022["Valeur fonciere"].str.replace(',', '.')

# Afficher les cinq premières lignes après nettoyage
print(vf2022.head())

# Convertir certaines colonnes en types appropriés
vf2022["Valeur fonciere"] = pd.to_numeric(vf2022["Valeur fonciere"])
vf2022["Surface reelle bati"] = pd.to_numeric(vf2022["Surface reelle bati"])
vf2022["Code postal"] = vf2022["Code postal"].astype({'Code postal': 'int32'})
vf2022["Date mutation"] = pd.to_datetime(vf2022["Date mutation"])

# Déterminer les codes postaux de Paris
paris_postal_codes = [75001, 75002, 75003, 75004, 75005, 75006, 75007, 75008, 75009, 75010, 
                      75011, 75012, 75013, 75014, 75015, 75016, 75017, 75018, 75019, 75020]

# Filtrer les données pour n'inclure que les codes postaux de Paris
vf_paris2022 = vf2022[vf2022['Code postal'].isin(paris_postal_codes)]

# Afficher les cinq premières lignes des données de Paris
print(vf_paris2022.head())

# Enregistrer les données organisées dans un fichier CSV avec alignement
vf_paris2022.to_csv("valeursfoncieres_paris_2022.csv", index=False, float_format='%.1f', sep=',', line_terminator='\n')