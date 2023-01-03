# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1
from __future__ import annotations


class Chargement:
    """Classe permettant de représenté le chargement d'une expérience.
    Un chargement est associé à :
     - Son nom    : permettant de l'identifier plus facilement.
     - Son flux   : Nx, Ny, en Txy en N/mm.
     - Son moment : Mx, My, MXY en N.
    """

    def __init__(self,
                 nom: str = "Defaut",
                 nx: float = 0,
                 ny: float = 0,
                 txy: float = 0,
                 mx: float = 0,
                 my: float = 0,
                 mxy: float = 0) -> None:
        """Constructeur de la classe Chargement.

        :param nom: Optionnel, le "nom" associé au chargemenent pour l'identifier.
        :type nom: str
        :param nx: Le flux Nx du chargement en N/mm.
        :type nx: float
        :param ny: Le flux Ny du chargement en N/mm.
        :type ny: float
        :param txy: Le flux Txy du chargement en N/mm.
        :typetxy: float
        :param mx: Le moment Mx du chargement en N.
        :type mx: float
        :param my: Le moment My du chargement en N.
        :type my: float
        :param mxy: Le moment Mxy du chargement en N.
        :type mxy: float
        :raise ValueError: Si le nom est vide ou None.
        :raise TypeError: Si le chargement n'est pas numérique..
        """
        try:
            if str(nom).strip() == "":
                raise ValueError("Nom du chargement invalide.")
            else:
                nom = str(nom).strip()
        except:
            raise ValueError("Nom du chargement invalide.")
        try:
            nx = float(nx)
            ny = float(ny)
            txy = float(txy)
            mx = float(mx)
            my = float(my)
            mxy = float(mxy)
        except:
            raise TypeError("Valeur du chargement invalide.")
        self.__nom = nom
        self.__nx = nx
        self.__ny = ny
        self.__txy = txy
        self.__mx = mx
        self.__my = my
        self.__mxy = mxy

    def toJSON(self):
        """
        Méthode pour exporter un chargement au format JSON.
        Le dictionnaire est utilisé par le ChargementEncoder.

        :return: Un dictionnaire permettant l'encodage au format JSON.
        """
        return dict(__type__="Chargement",
                    nom=self.__nom,
                    nx=self.__nx,
                    ny=self.__ny,
                    txy=self.__txy,
                    mx=self.__mx,
                    my=self.__my,
                    mxy=self.__mxy)

    ## Getters
    def getNom(self) -> str:
        """Getter pour obtenir le nom du chargement.

        :return: Le nom associé au chargement.
        :rtype: str
        """
        return self.__nom

    def getNx(self) -> float:
        """Getter pour obtenir le flux Nx (en N/mm) du chargement.

        :return: Le flux Nx (en N/mm) du chargement.
        :rtype: float
        """
        return self.__nx

    def getNy(self) -> float:
        """Getter pour obtenir le flux Ny (en N/mm) du chargement.

        :return: Le flux Ny (en N/mm) du chargement.
        :rtype: float
        """
        return self.__ny

    def getTxy(self) -> float:
        """Getter pour obtenir le flux Txy (en N/mm) du chargement.

        :return: Le flux Txy (en N/mm) du chargement.
        :rtype: float
        """
        return self.__txy

    def getMx(self) -> float:
        """Getter pour obtenir le moment Mx (en N) du chargement.

        :return: Le moment Mx (en N) du chargement.
        :rtype: float
        """
        return self.__mx

    def getMy(self) -> float:
        """Getter pour obtenir le moment My (en N) du chargement.

        :return: Le moment My (en N) du chargement.
        :rtype: float
        """
        return self.__my

    def getMxy(self) -> float:
        """Getter pour obtenir le moment Mxy (en N) du chargement.

        :return: Le moment Mxy (en N) du chargement.
        :rtype: float
        """
        return self.__mxy

    def setNom(self,
              nom: str) -> None:
        """Setter permettant de mettre à jour le nom associé au chargement.

        :param nom: Le nouveau nom associé au chargement.
        :type nom: str.
        :raise ValueError: Si le nom est vide ou None.
        """
        try:
            if str(nom).strip() == "":
                raise ValueError("Nom du chargement invalide.")
            else:
                nom = str(nom).strip()
        except:
            raise TypeError
        self.__nom = nom

    def setNx(self,
              nx: float) -> None:
        """Setter permettant de mettre à jour la valeur du flux Nx du chargement.

        :param nx: La nouvelle valeur du flux Nx en N/mm.
        :type nx: float.
        :raise TypeError: Si la nouvelle valeur de Nx n'est pas un nombre.
        """
        try:
            nx = float(nx)
        except:
            raise TypeError("Valeur du chargement invalide.")
        self.__nx = nx

    def setNy(self,
              ny: float) -> None:
        """Setter permettant de mettre à jour la valeur du flux Ny du chargement.

        :param ny: La nouvelle valeur du flux Nx en N/mm.
        :type ny: float.
        :raise TypeError: Si la nouvelle valeur de Ny n'est pas un nombre.
        """
        try:
            ny = float(ny)
        except:
            raise TypeError("Valeur du chargement invalide.")
        self.__ny = ny

    def setTxy(self,
              txy: float) -> None:
        """Setter permettant de mettre à jour la valeur du flux Txy du chargement.

        :param txy: La nouvelle valeur du flux Txy en N/mm.
        :type txy: float.
        :raise TypeError: Si la nouvelle valeur de Nx n'est pas un nombre.
        """
        try:
            txy = float(txy)
        except:
            raise TypeError("Valeur du chargement invalide.")
        self.__txy = txy

    def setMx(self,
              mx: float) -> None:
        """Setter permettant de mettre à jour la valeur du moment Mx du chargement.

        :param mx: La nouvelle valeur du moment Mx en N.
        :type mx: float.
        :raise TypeError: Si la nouvelle valeur de Mx n'est pas un nombre.
        """
        try:
            mx = float(mx)
        except:
            raise TypeError("Valeur du chargement invalide.")
        self.__mx = mx

    def setMy(self,
              my: float) -> None:
        """Setter permettant de mettre à jour la valeur du moment My du chargement.

        :param my: La nouvelle valeur du moment My en N.
        :type my: float.
        :raise TypeError: Si la nouvelle valeur de My n'est pas un nombre.
        """
        try:
            my = float(my)
        except:
            raise TypeError("Valeur du chargement invalide.")
        self.__my = my

    def setMxy(self,
              mxy: float) -> None:
        """Setter permettant de mettre à jour la valeur du moment Mxy du chargement.

        :param mxy: La nouvelle valeur du moment Mxy en N.
        :type mxy: float.
        :raise TypeError: Si la nouvelle valeur de Mxy n'est pas un nombre.
        """
        try:
            mxy = float(mxy)
        except:
            raise TypeError("Valeur du chargement invalide.")
        self.__mxy = mxy

    def clone(self,
              chargement: Chargement) -> Chargement:
        """ Méthode permettant de créer une copie profonde d'un chargement.

        :param chargement: Le chargement à copier.
        :return: Une copie profonde du chargelent passé en paramètre de la mérhode.
        :rtype: Chargement
        """
        self.__nom = chargement.getNom()
        self.__nx = chargement.getNx()
        self.__ny = chargement.getNy()
        self.__txy = chargement.getTxy()
        self.__mx = chargement.getMx()
        self.__my = chargement.getMy()
        self.__mxy = chargement.getMxy()
        return self

    def equals(self,
               chargement: Chargement) -> bool:
        """
        Méthode permettant de tester si deux chargements sont similaires.

        :param chargement: Le chargement à comparer.
        :return: True si les deux chargements sont similaires, False sinon.
        """
        return chargement.getNom() == self.__nom and \
               chargement.getNx() == self.__nx and \
               chargement.getNy() == self.__ny and \
               chargement.getTxy() == self.__txy and \
               chargement.getMx() == self.__mx and \
               chargement.getMy() == self.__my and \
               chargement.getMxy() == self.__mxy