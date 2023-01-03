import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canva(FigureCanvas):
    def __init__(self, parent, liste_x, liste_y, titre):
        """
        Constructeur de la classe Canva
        Classe permettant de construire les graphiques
        :param parent: widget parent accueillant le graphique
        :param liste_x: liste des abscisses à tracer
        :param liste_y: liste des ordonnées à tracer
        """
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=90)
        self.__x = liste_x
        self.__y = liste_y
        self.__titre = str(titre)
        self.ax.plot(self.__x, self.__y)
        self.ax.set(title=str(self.__titre))
        self.ax.set_ylim(-30, 30)
        super().__init__(fig)
        self.setParent(parent)

    def getFig(self):
        """
        Méthode permettant d'obtenir la figure associé au canva

        :return: La figure associé au canva
        """
        return self

    def maj_graphique(self,
                      liste_x=[],
                      liste_y=[],
                      titre="") -> None:
        """
        Mise à jour du graphique.

        :param liste_x: Liste des valeurs en x.
        :param liste_y: Liste des valeurs en y
        :param titre: Le titre du graphique.
        """

        self.__x = liste_x
        self.__y = liste_y
        self.__titre = str(titre)
        self.ax.plot(self.__x, self.__y)
        self.ax.set(title=str(self.__titre))
        minX = min(self.__x) - 1
        maxX = max(self.__x) + 1
        minY = min(self.__y) - 1
        maxY = max(self.__y) + 1
        self.ax.set_xlim(minX, maxX)
        self.ax.set_ylim(minY, maxY)
        self.ax.grid()
        self.draw()
        self.ax.cla()
