"""
Permet de nettoyer une base de données existante afin de pouvoir l'utiliser dans le programme.
S'applique pour les données relatives aux caractéristiques des ailes.
"""

import pandas as pd
import ast

# On définit les paramètres pour la lecture du fichier CSV
# delimiter: délimiteur utilisé dans le fichier CSV
# decimal: caractère utilisé pour représenter les décimales
delimiter = ','
decimal = '.'

# Lecture des données depuis le fichier CSV avec les paramètres définis
df = pd.read_csv('aerodynamics_data.csv', delimiter=delimiter, decimal=decimal)

# Affichage des colonnes du DataFrame avant tout traitement
print('Avant traitement, liste des colonnes:\n')
print(df.columns)
print('\n')

# Affichage des premières lignes du DataFrame pour vérifier les données
print(df.head())

# Affichage des types de données de chaque colonne avant traitement
print('dtype des différentes colonnes avant traitement\n')
for col in df.columns:
    print(col, df[col].dtype)
print('\n')

# Conversion des colonnes de type liste (alpha_data, cl_data, cd_data) de string à liste
# ast.literal_eval permet de convertir une chaîne de caractères en liste Python
print('Conversion des colonnes de type liste\n')
for col in ['alpha_data', 'cl_data', 'cd_data']:
    df[col] = df[col].apply(lambda x: ast.literal_eval(x))

# Affichage des types de données de chaque colonne après la conversion
print('dtype des différentes colonnes après traitement\n')
for col in df.columns:
    print(col, df[col].dtype)
print('\n')

# Affichage des premières lignes du DataFrame pour une seconde vérification
print(df.head())
print('\n')

# Affichage de la description statistique des données du DataFrame
print(df.describe())
print('\n')

# Sauvegarde des données nettoyées dans un nouveau fichier CSV
df.to_csv('aero_data_cleaned.csv', index=False)

# Indication que les données nettoyées ont été sauvegardées avec succès
print("Données nettoyées sauvegardées sous aero_data_cleaned.csv")
