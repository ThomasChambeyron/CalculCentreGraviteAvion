"""
Permet de nettoyer une base de données existante afin de pouvoir l'utiliser dans le programme.
S'applique auc données relatives aux composants de l'avion.
"""

import pandas as pd

# On définit les paramètres pour la lecture du fichier CSV
# delimiter: délimiteur utilisé dans le fichier CSV
# decimal: caractère utilisé pour représenter les décimales
delimiter = ';'
decimal = '.'

# Lecture des données depuis le fichier CSV
df = pd.read_csv('components_data.csv', delimiter=delimiter, decimal=decimal)

# Affichage des colonnes du DataFrame avant tout traitement
print('Avant traitement, liste des colonnes:\n')
print(df.columns)
print('\n')

# Affichage des premières lignes du DataFrame pour vérifier les données
print(df.head())

# Affichage des types de données de chaque colonne avant traitement
print('dtype des differentes colonnes avant traitement\n')
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
df.to_csv('components_data_cleaned.csv', index=False)

# Indication que les données nettoyées ont été sauvegardées avec succès
print("Données nettoyées sauvegardées sous components_data_cleaned.csv")
