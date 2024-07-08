"""
Ce module contient la classe AerodynamicsAnalyzer qui permet d'analyser les performances aérodynamiques des ailes d'un avion.
Il comprend des méthodes pour générer et tracer les coordonnées du profil d'aile ainsi que pour tracer les polaires aérodynamiques.
"""

import numpy as np
import matplotlib.pyplot as plt


class AerodynamicsAnalyzer:
    def __init__(self, profil_aile, corde, alpha_data=None, cl_data=None, cd_data=None):
        """
        Initialisation de la classe avec les données fournies.

        :param profil_aile: Derniers chiffres du profil NACA de l'aile
        :param corde: Longueur de la corde de l'aile
        :param alpha_data: Liste des angles d'attaque
        :param cl_data: Liste des coefficients de portance correspondants à alpha_data
        :param cd_data: Liste des coefficients de traînée correspondants à cl_data
        """
        self.profil_aile = profil_aile
        self.corde = corde
        self.alpha_data = alpha_data
        self.cl_data = cl_data
        self.cd_data = cd_data

    def generer_xc(self):
        """
        Génère une répartition uniforme des points le long de la corde.

        :return: Tableau numpy de valeurs réparties uniformément de 0 à 1
        """
        return np.linspace(0, 1, 100)  # Répartition uniforme avec 100 points le long de la corde

    def calculer_coordonnees(self, t):
        """
        Calcule les coordonnées du profil d'aile basé sur les équations NACA.

        :param t: Épaisseur relative de l'aile (en pourcentage)
        :return: Coordonnées x et y pour l'extrados et l'intrados
        """
        xc = self.generer_xc()
        # Calcul des coordonnées y basées sur la formule NACA pour une épaisseur relative donnée
        yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
        xup = xc * self.corde
        yup = yt * self.corde
        xdown = xc * self.corde
        ydown = -yt * self.corde
        return xup, yup, xdown, ydown

    def tracer_profil(self):
        """
        Trace le profil de l'aile NACA basé sur les chiffres fournis.
        """
        t = int(self.profil_aile) / 100  # Convertir le profil d'aile en épaisseur relative
        xup, yup, xdown, ydown = self.calculer_coordonnees(t)
        plt.figure(figsize=(10, 5))
        plt.plot(xup, yup, label='Extrados')  # Tracé de l'extrados
        plt.plot(xdown, ydown, label='Intrados')  # Tracé de l'intrados
        plt.title(f'Profil NACA00{self.profil_aile}')
        plt.xlabel('x (mètres)')
        plt.ylabel('y (mètres)')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()

    def plot_polar_cl_alpha(self):
        """
        Trace la polaire aérodynamique C_L vs α.
        """
        if len(self.alpha_data) != len(self.cl_data):
            raise ValueError("alpha_data and cl_data must have the same length.")
        plt.figure(figsize=(8, 6))
        plt.plot(self.alpha_data, self.cl_data, label='Polaire C_L vs α')
        plt.xlabel('Angle d\'attaque (deg)')
        plt.ylabel('Coefficient de portance C_L')
        plt.grid(True)
        plt.legend()
        plt.title(f'Polaire C_L vs α pour le profil d\'aile NACA00{self.profil_aile}')
        plt.show()

    def plot_polar_cl_cd(self):
        """
        Trace la polaire aérodynamique C_L vs C_D.
        """
        if len(self.cl_data) != len(self.cd_data):
            raise ValueError("cl_data and cd_data must have the same length.")
        plt.figure(figsize=(8, 6))
        plt.plot(self.cd_data, self.cl_data, label='Polaire C_D vs C_L')
        plt.xlabel('Coefficient de trainée C_D')
        plt.ylabel('Coefficient de portance C_L')
        plt.grid(True)
        plt.legend()
        plt.title(f'Polaire C_D vs C_L pour le profil d\'aile NACA00{self.profil_aile}')
        plt.show()
