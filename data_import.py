"""
Ce module contient la classe DataImporter qui permet d'importer et de traiter les données nécessaires pour le calcul du centre de gravité et l'analyse aérodynamique d'un avion.
Il inclut des méthodes pour entrer les données manuellement, les importer depuis une base de données et utiliser des données par défaut.
"""

import pandas as pd
import ast


class DataImporter:
    def manual_input(self):
        """
        Permet à l'utilisateur d'entrer manuellement les données des composants de l'avion.

        :return: Dictionnaire contenant les positions et poids des composants de l'avion
        """
        empennage = {
            'position': [float(input("Position X de l'empennage: ")),
                         float(input("Position Y de l'empennage: ")),
                         float(input("Position Z de l'empennage: "))],
            'poids': float(input("Poids de l'empennage: "))
        }

        ailes = {
            'position': [float(input("Position X des ailes: ")),
                         float(input("Position Y des ailes: ")),
                         float(input("Position Z des ailes: "))],
            'poids': float(input("Poids des ailes: "))
        }

        moteurs = {
            'position': [float(input("Position X du moteur: ")),
                         float(input("Position Y du moteur: ")),
                         float(input("Position Z du moteur: "))],
            'poids': float(input("Poids du moteur: "))
        }

        fuselage = {
            'position': [float(input("Position X du fuselage: ")),
                         float(input("Position Y du fuselage: ")),
                         float(input("Position Z du fuselage: "))],
            'poids': float(input("Poids du fuselage: "))
        }

        train_atterrissage = {
            'position': [float(input("Position X du train d'atterrissage: ")),
                         float(input("Position Y du train d'atterrissage: ")),
                         float(input("Position Z du train d'atterrissage: "))],
            'poids': float(input("Poids du train d'atterrissage: "))
        }

        # Retourner les données saisies sous forme de dictionnaire
        return {
            'empennage': empennage,
            'ailes': ailes,
            'moteurs': moteurs,
            'fuselage': fuselage,
            'train_atterrissage': train_atterrissage
        }

    def from_database(self, filepath):
        """
        Importe les données depuis un fichier CSV.

        :param filepath: Chemin du fichier CSV
        :return: DataFrame contenant les données importées
        """
        return pd.read_csv(filepath)

    def data_component(self, filepath):
        """
        Importe les données des composants depuis un fichier CSV et les organise sous forme de dictionnaire.

        :param filepath: Chemin du fichier CSV
        :return: Dictionnaire contenant les positions et poids des composants de l'avion
        """
        df = self.from_database(filepath)

        # Créer un dictionnaire pour stocker les données de chaque composant
        data = {}
        for index, row in df.iterrows():
            component = row['component']
            position = [row['position_x'], row['position_y'], row['position_z']]
            poids = row['poids']
            data[component] = {'position': position, 'poids': poids}

        # Retourner les données sous forme de dictionnaire
        return data

    def data_profil(self, filepath):
        """
        Importe les données du profil d'aile depuis un fichier CSV et les extrait.

        :param filepath: Chemin du fichier CSV
        :return: Tuple contenant le profil d'aile, la corde, les angles d'attaque, les coefficients de portance et les coefficients de traînée
        """
        data = self.from_database(filepath)

        # Extraction des valeurs depuis le DataFrame
        profil_aile = data['profil_aile'].iloc[0]
        corde = data['corde'].iloc[0]
        alpha_data = ast.literal_eval(data['alpha_data'].iloc[0])
        cl_data = ast.literal_eval(data['cl_data'].iloc[0])
        cd_data = ast.literal_eval(data['cd_data'].iloc[0])

        # Retourner les valeurs extraites sous forme de tuple
        return profil_aile, corde, alpha_data, cl_data, cd_data

    def default_components_data(self):
        """
        Retourne des données par défaut pour les composants de l'avion.

        :return: Dictionnaire contenant les positions et poids par défaut des composants de l'avion
        """
        return {
            'empennage': {'position': [10, 0, 1], 'poids': 300},
            'ailes': {'position': [5.5, 0, 0], 'poids': 500},
            'moteurs': {'position': [5, 0, 0], 'poids': 200},
            'fuselage': {'position': [5, 0, 0.5], 'poids': 1000},
            'train_atterrissage': {'position': [4, 0, -1], 'poids': 100}
        }

    def default_profil_data(self):
        """
        Retourne des données par défaut pour le profil d'aile.

        :return: Tuple contenant le profil d'aile, la corde, les angles d'attaque, les coefficients de portance et les coefficients de traînée
        """
        profil_aile = 12
        corde = 1.5
        alpha_data = [-10, -5, 0, 5, 10, 15, 20]
        cl_data = [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]
        cd_data = [0.02, 0.025, 0.03, 0.04, 0.06, 0.1, 0.2]

        # Retourner les valeurs par défaut sous forme de tuple
        return profil_aile, corde, alpha_data, cl_data, cd_data
