"""
Ce module contient la classe CenterOfGravityCalculator qui permet de calculer le centre de gravité d'un avion en fonction des données fournies.
"""
class CenterOfGravityCalculator:
    def __init__(self, data):
        """
        Initialisation de la classe avec les données fournies.

        :param data: Dictionnaire contenant les propriétés des composants de l'avion (poids et position)
        """
        self.data = data

    def calculate(self):
        """
        Calcule le centre de gravité de l'avion.

        :return: Tuple contenant les coordonnées du centre de gravité (cg_x, cg_y, cg_z)
        """
        total_weight = 0  # Poids total de l'avion
        moment_x, moment_y, moment_z = 0, 0, 0  # Moments autour des axes x, y, z

        for component, properties in self.data.items():
            poids = properties['poids']  # Poids du composant
            position = properties['position']  # Position du composant
            total_weight += poids  # Ajouter le poids du composant au poids total
            moment_x += poids * position[0]  # Calcul du moment autour de l'axe x
            moment_y += poids * position[1]  # Calcul du moment autour de l'axe y
            moment_z += poids * position[2]  # Calcul du moment autour de l'axe z

        # Calcul des coordonnées du centre de gravité
        cg_x = moment_x / total_weight
        cg_y = moment_y / total_weight
        cg_z = moment_z / total_weight

        return cg_x, cg_y, cg_z  # Retourner les coordonnées du centre de gravité
