# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from __future__ import annotations
import numpy as np

from script import Pli
from script import Materiau


class Plaque:
    """
    Méthode représentant une plaque.
    Une plaque est définie comme une liste de pli.
    """
    def __init__(self,
                 liste_plis: list[Pli] = None,
                 z_min: float = 0) -> None:
        """
        Constructeur de la classe Plaque
        Classe représentant une Plaque
        :param liste_pLis: liste des plis contenus dans la plaque
        :param z_min: hauteur minimale de la plaque
        """

        if liste_plis is None:
            self.__listePlis = []
        else:
            self.__listePlis = liste_plis

        self.__matriceA_rigidite = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceB_rigidite = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceD_rigidite = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.__matriceA_souplesse = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceB_souplesse = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceD_souplesse = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.__z_min = z_min

    def getA_rigidite(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice A de rigidité de la plaque.

        :return: La matrice A de rigidité de la plaque.
        """
        return self.__matriceA_rigidite

    def getB_rigidite(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice D de rigidité de la plaque.

        :return: La matrice B de rigidité de la plaque.
        """
        return self.__matriceB_rigidite

    def getD_rigidite(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice D de rigidité de la plaque.

        :return: La matrice D de rigidité de la plaque.
        """
        return self.__matriceD_rigidite

    def getA_souplesse(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice A de souplesse de la plaque.

        :return: La matrice A de souplesse de la plaque.
        """
        return self.__matriceA_souplesse

    def getB_souplesse(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice B de souplesse de la plaque.

        :return: La matrice B de souplesse de la plaque.
        """
        return self.__matriceB_souplesse

    def getD_souplesse(self) -> list[list[float]]:
        """
        Getter permettant d'obtenir la matrice D de souplesse de la plaque.

        :return: La matrice D de souplesse de la plaque.
        """
        return self.__matriceD_souplesse

    def getZmin(self) -> float:
        """
        Getter permettant d'obtenir la valeur du paramètre zmin de la plaque.
        :return: La valeur du paramètre zmin de la plaque.
        """
        return self.__z_min

    def setZMin(self, zmin:float) -> None:
        """
        Setter permettant de mettre à jour la position base de la plaque
        :param zmin: La nouvelle position basse de la plaque en mm
        """
        self.__z_min = zmin

    def equals(self,
               plaque: Plaque) -> bool:
        """
        Méthode permettant de tester que deux plaques sont similaires.

        :param plaque: La plaque à comparer.
        :return: True si les deux plaques sont simillaires, False sinon.
        """
        bool_taille = (len(self.__listePlis) == len(plaque.getListePlis()))
        if bool_taille:
            return False not in [self.__listePlis[i].equals(plaque.getListePlis()[i]) for i in range(0, len(self.__listePlis))]
        else:
            return False

    def toJSON(self):
        """
        Méthode pour exporter une plaque au format JSON.
        Le dictionnaire est utilisé par le PlaqueEncoder.

        :return: Un dictionnaire permettant l'encodage au format JSON.
        """
        return dict(__type__="Plaque",
                    listePlis=[pli.toJSON() for pli in self.__listePlis],
                    zmin=self.__z_min)

    def getListePlis(self) -> list[Pli]:
        """
        Getter de l'attribut listePlis
        :return: listePlis : liste des plis de la plaque
        """
        return self.__listePlis

    def ajoutePli(self,
                  pli: Pli,
                  nbrePlis: int) -> bool:
        """
        Méthode permettant d'ajouter un pli à la liste de pli.
        :param pli: Le pli à ajouter.
        :param nbrePlis: Le nombre de copie du pli.
        :return: True si l'ajout à eu lieu, False sinon.
        """
        flag = False
        nbrePliTotal = len(self.__listePlis)
        if ((pli.getMateriau() != "") and (0 < pli.getPositionRelPlaque()) and (
                pli.getPositionRelPlaque() <= nbrePliTotal + 1) and (pli.getOrientation() != "") and (
                pli.getEpaisseur() != 0) and (nbrePlis != 0)):
            try:
                place = pli.getPositionRelPlaque()
                for k in range(0, nbrePlis):
                    pliTmp = Pli.Pli()
                    pliTmp.setMateriau(pli.getMateriau())
                    pliTmp.setOrientation(pli.getOrientation())
                    pliTmp.setPositionRelPlaque(0)
                    pliTmp.setEpaisseur(pli.getEpaisseur())
                    self.__listePlis.insert(place - 1, pliTmp)
                flag = True
            except ValueError:
                flag = False
            self.maj_pos_rel_pli()
        return flag

    def supprimePli(self,
                    nPli: int) -> bool:
        """
        Méthode permettant de supprimer un pli de la plaque par sa position dans la plaque. (Les positions commencent à 1)

        :param nPli: La position du pli dans la plaque.
        :return: True si la suppression est effective, False sinon
        """
        flag = False
        nbrePlis = len(self.getListePlis())
        if (nPli > 0) and (nPli <= nbrePlis):
            self.__listePlis.pop(nPli - 1)
            flag = True
        self.maj_pos_rel_pli()
        return flag

    def duppliquePli(self,
                     nPli: int) -> bool:
        """
        Méthode permettant de dupliquer un pli.

        :param nPli: La position du pli à dupliquer.
        :return: true si la duplication est effective, False sinon.
        """
        flag = False
        nbrePlis = len(self.getListePlis())
        if (nPli > 0) and (nPli <= nbrePlis):
            if len(self.__listePlis) > 1:
                self.__listePlis.insert(nPli, self.__listePlis[nPli - 1])
            elif len(self.__listePlis) == 1:
                self.__listePlis.append(self.__listePlis[0])
            flag = True
        self.maj_pos_rel_pli()
        return flag

    def montePli(self,
                 nPli: int) -> bool:
        """
        Méthode permettant de monter un pli dans l'arborescence de la plaque.

        :param nPli: La position du pli à monter.
        :return: True si le changement de position est effectif, False sinon.
        """
        flag = False
        nbrePlis = len(self.getListePlis())
        if (nPli > 1) and (nPli <= nbrePlis):
            tmp = self.__listePlis[nPli - 1]
            self.__listePlis[nPli - 1] = self.__listePlis[nPli - 2]
            self.__listePlis[nPli - 2] = tmp
            flag = True
        self.maj_pos_rel_pli()
        return flag

    def descendPli(self,
                   nPli: int) -> bool:
        """
        Méthode permettant de descendre un pli dans l'arborescence de la plaque.

        :param nPli: La position du pli à descendre.
        :return: True si le changement de position est effectif, False sinon.
        """
        flag = False
        nbrePlis = len(self.getListePlis())
        if (nPli > 0) and (nPli < nbrePlis):
            tmp = self.__listePlis[nPli - 1]
            self.__listePlis[nPli - 1] = self.__listePlis[nPli]
            self.__listePlis[nPli] = tmp
            flag = True
        self.maj_pos_rel_pli()
        return flag

    def maj_pos_rel_pli(self) -> None:
        """
        Méthode permettant de remettre à jour les positions relatives des plis
        """
        nbrePlis = len(self.__listePlis)
        for k in range(0, nbrePlis):
            self.__listePlis[k].setPositionRelPlaque(k + 1)

    def majMatricesPlis(self) -> None:
        """
        Méthode permettant de mettre à jour recursivement l'ensemble des matrices de l'ensemble des plis.
        """
        nbrePlis=len(self.__listePlis)
        for k in range (0,nbrePlis):
            pli=self.__listePlis[k]
            pli.majMatrices()

    def majMatrices(self) -> None:
        """
        Méthode permettant de mettre à jour les matrices de la plaque.
        """
        # Remise à zéro des matrices
        self.__matriceA_rigidite = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceB_rigidite = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceD_rigidite = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.__matriceA_souplesse = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceB_souplesse = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.__matriceD_souplesse = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # Mise à jour des matrices des plis
        self.majMatricesPlis()
        tmp_pos = self.__z_min
        for pli in self.__listePlis:
            tmp_pos2 = tmp_pos + pli.getEpaisseur()
            self.__matriceA_rigidite = self.__matriceA_rigidite + pli.getEpaisseur()*pli.getMatRigiditeBase()
            self.__matriceB_rigidite = self.__matriceB_rigidite + (tmp_pos2**2-tmp_pos**2)/2*pli.getMatRigiditeBase()
            self.__matriceD_rigidite = self.__matriceD_rigidite + (
                        tmp_pos2 ** 3 - tmp_pos ** 3) / 3 * pli.getMatRigiditeBase()
            tmp_pos = tmp_pos2


        try:
            self.__matriceA_souplesse = np.linalg.pinv(self.__matriceA_rigidite)
            self.__matriceB_souplesse = np.linalg.pinv(self.__matriceB_rigidite)
            self.__matriceD_souplesse = np.linalg.pinv(self.__matriceD_rigidite)
        except :
            pass
