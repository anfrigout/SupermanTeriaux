# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from __future__ import annotations
import math
import numpy as np

from script import Materiau


class Pli:
    """
    Classe représentant un pli.
    Un pli est défini par :
        - Son orientation
        - Le matériau qui le compose
        - Son épaisseur
        - Sa position dans la plaque
        - Des matrices de changement de bases (contraintes et déformations)
        - Des matrices de souplesses et de rigidité selon les bases.
    """

    def __init__(self,
                 orientation: float = 0,
                 mat: Materiau = None,
                 epaisseur: float = 0,
                 positionRelPlaque: int = 0,
                 matChangementBaseDeformation: list[list[float]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                 matChangementBaseContrainte: list[list[float]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                 matSouplesse: list[list[float]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                 matRigidite: list[list[float]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                 matSouplesseBase: list[list[float]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                 matRigiditeBase: list[list[float]] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) -> None:
        """
        Constructeur de la classe pli.
        """
        self.__orientation = orientation
        self.__materiau = mat
        self.__epaisseur = epaisseur
        self.__positionRelPlaque = positionRelPlaque
        self.__matChangeBaseDeformation = matChangementBaseDeformation
        self.__matChangeBaseContrainte = matChangementBaseContrainte
        self.__matSouplesse = matSouplesse
        self.__matRigidite = matRigidite
        self.__matSouplesseBase = matSouplesseBase
        self.__matRigiditeBase = matRigiditeBase

    def equals(self,
               pli: Pli) -> bool:
        """
        Méthode permettant de tester que deux plis sont similaires.

        :param pli: Le plis à comparer.
        :return: True si les deux plis sont similaires, False sinon.
        """
        return pli.getOrientation() == self.__orientation and \
               pli.getMateriau().equals(self.__materiau) and \
               pli.getEpaisseur() == self.__epaisseur and \
               pli.getPositionRelPlaque() == self.__positionRelPlaque and \
               pli.__matChangeBaseContrainte == self.__matChangeBaseContrainte and \
               pli.__matChangeBaseDeformation == self.__matChangeBaseDeformation and \
               pli.__matSouplesse == self.__matSouplesse and \
               pli.__matRigidite == self.__matRigidite and \
               pli.__matRigiditeBase == self.__matRigiditeBase and \
               pli.__matSouplesseBase == self.__matSouplesseBase

    def toJSON(self):
        """
        Méthode pour exporter un pli au format JSON.
        Le dictionnaire est utilisé par le PliEncoder.

        :return: Un dictionnaire permettant l'encodage au format JSON.
        """
        if self.__materiau is None:
            return dict(__type__="Pli",
                        orientation=self.__orientation,
                        materiau=None,
                        epaisseur=self.__epaisseur,
                        positionRelPlaque=self.__positionRelPlaque)
        else:
            return dict(__type__="Pli",
                        orientation=self.__orientation,
                        materiau=self.__materiau.toJSON(),
                        epaisseur=self.__epaisseur,
                        positionRelPlaque=self.__positionRelPlaque)

    def getOrientation(self) -> float:
        """
        Getter permettant d'obtenir le paramètre orientation du pli.

        :return: La valeur du paramètre orientation du pli.
        """
        return self.__orientation

    def setOrientation(self,
                       orientation: float) -> None:
        """
        Setter permettant de mettre à jour la valeur de l'orientation du pli.

        :param orientation: La nouvelle orientation du pli.
        """
        self.__orientation = orientation

    def getMateriau(self) -> Materiau:
        """
        Getter permettant d'obtenir le matériau qui compose le pli.

        :return: Le matériau qui compose le pli.
        """
        return self.__materiau

    def setMateriau(self,
                    mat: Materiau) -> None:
        """
        Méthode permettant de mettre à jour le matériau qui compose le pli.

        :param mat: Le nouveau matériau qui compose le pli.
        """
        if mat is None:
            self.__materiau = None
        else:
            self.__materiau = Materiau.Materiau().clone(mat)

    def getEpaisseur(self) -> float:
        """
        Méthode permettant d'obtenir la valeur de l'épaisseur du pli.

        :return: L'épaisseur du pli.
        """
        return self.__epaisseur

    def setEpaisseur(self,
                     e: float) -> None:
        """
        Setter permettant de mettre à jour l'épaisseur du pli.

        :param e: La nouvelle épaisseur du pli.
        """
        self.__epaisseur = e

    def getPositionRelPlaque(self) -> int:
        """
        Getter permettant d'obtenir la position du pli dans la plaque.

        :return: La position du pli dans la pli
        """
        return self.__positionRelPlaque

    def setPositionRelPlaque(self,
                             posPlaque: int) -> None:
        """
        Seter permettant de modifier la position du pli dans la plaque.

        :param posPlaque: La nouvelle position du pli dans la plaque.
        """
        self.__positionRelPlaque = posPlaque

    def getMatSouplesse(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice de souplesse.

        :return: La matrice de souplesse.
        """
        return self.__matSouplesse

    def getMatSouplesseBase(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice de souplesse dans la base de la plaque.

        :return: La matrice de souplesse dans la base de la plaque.
        """
        return self.__matSouplesseBase

    def getMatRigidite(self):
        """
        Getter permettant d'obtenir la matrice de rigidité dans la base canonique.

        :return: La matrice de rigidité dans la base canonique.
        """
        return self.__matRigidite

    def getMatRigiditeBase(self):
        """
        Getter permettant d'obtenir la matrice de rigidité dans la base du stratifié.

        :return: La matrice de rigidité dans la base du stratifié.
        """
        return self.__matRigiditeBase

    def majMatChangeBaseDeformation(self) -> None:
        """
        Méthode permettant de recalculer la matrice de changement de base en déformation lors d'un changement d'orientation.
        """
        rad = self.__orientation * math.pi / 180
        cos = math.cos(rad)
        sin = math.sin(rad)

        self.__matChangeBaseDeformation[0][0] = cos * cos
        self.__matChangeBaseDeformation[0][1] = sin * sin
        self.__matChangeBaseDeformation[0][2] = -1 * cos * sin
        self.__matChangeBaseDeformation[1][0] = sin * sin
        self.__matChangeBaseDeformation[1][1] = cos * cos
        self.__matChangeBaseDeformation[1][2] = cos * sin
        self.__matChangeBaseDeformation[2][0] = 2 * cos * sin
        self.__matChangeBaseDeformation[2][1] = -2 * cos * sin
        self.__matChangeBaseDeformation[2][2] = cos * cos - sin * sin

    def majMatChangeBaseContrainte(self) -> None:
        """
        Méthode permettant de recalculer la matrice de changement de base en contrainte lors d'un changement d'orientation.
        """
        rad = self.__orientation * math.pi / 180
        cos = math.cos(rad)
        sin = math.sin(rad)

        self.__matChangeBaseContrainte[0][0] = cos * cos
        self.__matChangeBaseContrainte[0][1] = sin * sin
        self.__matChangeBaseContrainte[0][2] = -2 * cos * sin
        self.__matChangeBaseContrainte[1][0] = sin * sin
        self.__matChangeBaseContrainte[1][1] = cos * cos
        self.__matChangeBaseContrainte[1][2] = 2 * cos * sin
        self.__matChangeBaseContrainte[2][0] = cos * sin
        self.__matChangeBaseContrainte[2][1] = -1 * cos * sin
        self.__matChangeBaseContrainte[2][2] = cos * cos - sin * sin

    def majMatSouplesse(self) -> None:
        """
        Méthode permettant de recalculer la matrice de souplesse.
        Indice de la matrice
        (0,0) (0,1) (0,2)
        (1,0) (1,1) (1,2)
        (2,0) (2,1) (2,2)
        """
        self.__matSouplesse[0][0] = 1 / float(self.__materiau.getE1())
        self.__matSouplesse[0][1] = -1 * float(self.__materiau.getV12()) / float(self.__materiau.getE1())
        self.__matSouplesse[0][2] = 0
        self.__matSouplesse[1][0] = -1 * float(self.__materiau.getV12()) / float(self.__materiau.getE1())
        self.__matSouplesse[1][1] = 1 / float(self.__materiau.getE2())
        self.__matSouplesse[1][2] = 0
        self.__matSouplesse[2][0] = 0
        self.__matSouplesse[2][1] = 0
        self.__matSouplesse[2][2] = 1 / float(self.__materiau.getG12())

    def majMatSouplesseBase(self) -> None:
        """
        Mise a jour de la matrice de souplesse dans le repere du stratifie
        """
        self.majMatChangeBaseDeformation()
        self.majMatChangeBaseContrainte()
        self.majMatSouplesse()
        Teps = np.array(self.__matChangeBaseDeformation)
        try:
            Tsig = np.linalg.inv(np.array(self.__matChangeBaseContrainte))
        except:
            pass
        S = np.array(self.__matSouplesse)
        self.__matSouplesseBase = np.dot(np.dot(Teps, S), Tsig)

    def majMatRigidite(self) -> None:
        """
        Mise a jour de la matrice de rigidite dans le repere du pli
        """
        self.majMatSouplesse()
        soup = self.__matSouplesse
        self.__matRigidite[0][0] = (soup[1][1]*soup[2][2]-soup[2][1]*soup[1][2])/(soup[0][0]*soup[1][1]*soup[2][2]+soup[0][1]*soup[1][2]*soup[2][0]+soup[0][2]*soup[1][0]*soup[2][1]-soup[2][0]*soup[1][1]*soup[0][2]-soup[2][1]*soup[1][2]*soup[0][0]-soup[2][2]*soup[1][0]*soup[0][1])
        self.__matRigidite[0][1] = -(soup[0][1]*soup[2][2]-soup[2][1]*soup[0][2])/(soup[0][0]*soup[1][1]*soup[2][2]+soup[0][1]*soup[1][2]*soup[2][0]+soup[0][2]*soup[1][0]*soup[2][1]-soup[2][0]*soup[1][1]*soup[0][2]-soup[2][1]*soup[1][2]*soup[0][0]-soup[2][2]*soup[1][0]*soup[0][1])
        self.__matRigidite[0][2] = 0
        self.__matRigidite[1][0] = -(soup[0][1]*soup[2][2]-soup[2][1]*soup[0][2])/(soup[0][0]*soup[1][1]*soup[2][2]+soup[0][1]*soup[1][2]*soup[2][0]+soup[0][2]*soup[1][0]*soup[2][1]-soup[2][0]*soup[1][1]*soup[0][2]-soup[2][1]*soup[1][2]*soup[0][0]-soup[2][2]*soup[1][0]*soup[0][1])
        self.__matRigidite[1][1] = (soup[0][0]*soup[2][2]-soup[2][0]*soup[0][2])/(soup[0][0]*soup[1][1]*soup[2][2]+soup[0][1]*soup[1][2]*soup[2][0]+soup[0][2]*soup[1][0]*soup[2][1]-soup[2][0]*soup[1][1]*soup[0][2]-soup[2][1]*soup[1][2]*soup[0][0]-soup[2][2]*soup[1][0]*soup[0][1])
        self.__matRigidite[1][2] = 0
        self.__matRigidite[2][0] = 0
        self.__matRigidite[2][1] = 0
        self.__matRigidite[2][2] = (soup[0][0]*soup[1][1]-soup[1][0]*soup[0][1])/(soup[0][0]*soup[1][1]*soup[2][2]+soup[0][1]*soup[1][2]*soup[2][0]+soup[0][2]*soup[1][0]*soup[2][1]-soup[2][0]*soup[1][1]*soup[0][2]-soup[2][1]*soup[1][2]*soup[0][0]-soup[2][2]*soup[1][0]*soup[0][1])

    def majMatRigiditeBase(self) -> None:
        """
        Mise a jour de la matrice de rigidite dans le repere du stratifie
        """
        self.majMatChangeBaseDeformation()
        self.majMatChangeBaseContrainte()
        self.majMatRigidite()
        Tsig = np.array(self.__matChangeBaseContrainte)
        try:
            Teps = np.linalg.inv(np.array(self.__matChangeBaseDeformation))
        except:
            pass
        E = np.array(self.__matRigidite)
        self.__matRigiditeBase = np.dot(np.dot(Tsig, E), Teps)

    def majMatrices(self) -> None:
        """
        Méthode permettant de mettre à jour l'ensemble des matrices.
        """
        self.majMatSouplesseBase()
        self.majMatRigiditeBase()


