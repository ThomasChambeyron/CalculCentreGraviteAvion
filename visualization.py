"""
Ce module contient la classe Visualization3D qui permet de visualiser en 3D les composants de l'avion
ainsi que le centre de gravité calculé.
"""

import matplotlib.pyplot as plt


class Visualization3D:
    def __init__(self, data, cg):
        """
        Initialise la classe Visualization3D avec les données des composants de l'avion et le centre de gravité calculé.

        :param data: Dictionnaire contenant les positions et poids des composants de l'avion
        :param cg: Tuple contenant les coordonnées du centre de gravité (X, Y, Z)
        """
        self.data = data
        self.cg = cg

    def plot_aircraft(self):
        """
        Affiche une visualisation 3D des composants de l'avion et du centre de gravité.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Tracer chaque composant de l'avion
        for component, properties in self.data.items():
            ax.scatter(*properties['position'], label=component.capitalize())

        # Tracer le centre de gravité global en vert avec une taille de 100
        ax.scatter(*self.cg, color='green', s=100, label='Centre de Gravité')

        # Fixer les limites des axes
        x_max = max(abs(self.data[comp]['position'][0]) for comp in
                    self.data)  # Trouver la valeur maximale de X parmi tous les composants
        x_limits = [0, x_max]  # Limites pour X basées sur la valeur maximale de X des composants

        # Appliquer les limites à l'axe X
        ax.set_xlim3d(x_limits)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.show()
