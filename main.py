"""
Ce script principal permet de calculer le centre de gravité d'un avion et d'analyser les performances aérodynamiques des ailes.
Il propose à l'utilisateur de choisir entre ces deux options et de saisir les données nécessaires de différentes manières.
"""

from data_import import DataImporter
from center_of_gravity import CenterOfGravityCalculator
from visualization import Visualization3D
from aerodynamics import AerodynamicsAnalyzer

def main():
    print("Bienvenue dans le programme de calcul du centre de gravité et d'analyse aérodynamique d'un avion.")

    # Demander à l'utilisateur de choisir une action
    choice = input(
        "Que souhaitez-vous faire ?\n"
        "1. Calculer le centre de gravité de l'avion.\n"
        "2. Analyser les performances aérodynamiques.\n"
        "Votre choix (1 ou 2) : "
    )

    if choice == '1':
        print("\nCalcul du centre de gravité de l'avion.")
        # Demander à l'utilisateur comment il souhaite entrer les données pour le calcul du centre de gravité
        data_choice = input(
            "Comment souhaitez-vous entrer les données ?\n"
            "1. Entrer les données manuellement\n"
            "2. Utiliser des données depuis une base de données\n"
            "3. Utiliser des données par défaut\n"
            "Votre choix (1, 2 ou 3) : "
        )

        if data_choice == '1':
            # Saisie manuelle des données
            data = DataImporter().manual_input()
        elif data_choice == '2':
            # Utilisation de données depuis une base de données
            filepath = input("Entrez le chemin du fichier de la base de données: ")
            data = DataImporter().data_component(filepath)
        elif data_choice == '3':
            # Utilisation de données par défaut
            data = DataImporter().default_components_data()
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
            return

        # Calcul du centre de gravité
        cg_calculator = CenterOfGravityCalculator(data)
        cg = cg_calculator.calculate()
        print(f"Centre de Gravité: {cg}")

        # Visualisation en 3D de l'avion et de son centre de gravité
        visualizer = Visualization3D(data, cg)
        visualizer.plot_aircraft()

    elif choice == '2':
        print("\nAnalyse des performances aérodynamiques de l'avion.")
        # Demander à l'utilisateur comment il souhaite entrer les données pour l'analyse aérodynamique
        data_choice = input(
            "Comment souhaitez-vous entrer les données ?\n"
            "1. Entrer les données manuellement\n"
            "2. Utiliser des données depuis une base de données\n"
            "3. Utiliser des données par défaut\n"
            "Votre choix (1, 2 ou 3) : "
        )

        if data_choice == '1':
            # Saisie manuelle des données aérodynamiques
            profil_aile = input("Entrez les 2 derniers chiffres du profil d'aile (NACA 4 chiffres symétrique 00XX) : ")
            corde = float(input("Entrez la longueur de la corde en mètres : "))
            alpha_data = list(map(float, input("Entrez les valeurs des angles d'incidence, séparés par des virgules : ").split(',')))
            cl_data = list(map(float, input("Entrez les valeurs des coefficients de portance, séparés par des virgules : ").split(',')))
            cd_data = list(map(float, input("Entrez les valeurs des coefficients de traînée, séparés par des virgules : ").split(',')))
        elif data_choice == '2':
            # Utilisation de données depuis une base de données
            filepath = input("Entrez le chemin du fichier de la base de données: ")
            profil_aile, corde, alpha_data, cl_data, cd_data = DataImporter().data_profil(filepath)
        elif data_choice == '3':
            # Utilisation de données par défaut
            profil_aile, corde, alpha_data, cl_data, cd_data = DataImporter().default_profil_data()
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
            return

        # Analyse aérodynamique
        aero_analyzer = AerodynamicsAnalyzer(profil_aile, corde, alpha_data, cl_data, cd_data)
        aero_analyzer.tracer_profil()
        aero_analyzer.plot_polar_cl_alpha()
        aero_analyzer.plot_polar_cl_cd()

if __name__ == "__main__":
    main()
