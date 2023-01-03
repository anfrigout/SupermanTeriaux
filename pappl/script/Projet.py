# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from __future__ import annotations

from script import Materiau
from script import Chargement
from script import Plaque
from script import Pli


class Projet:
    """
    Classe définissant un projet.
    """

    def __init__(self,
                 nomProjet: str,
                 listeMateriaux: list[Materiau] = None,
                 chargementCourant: int = -1,
                 listeChargementsPossibles: list[Chargement] = None,
                 plaque: Plaque = None,
                 nPliAjout: int = 0,
                 pliAj: Pli = None) -> None:
        """
        Constructeur de la classe Projet.

        :param nomProjet: Le nom associé au projet.
        :type nomProjet: str
        :param listeMateriaux: La liste des matériaux qui composent le projet.
        :type listeMateriaux: list[Materiau]
        :param chargementCourant: L'indice du chargement par défaut (dans la liste des chargements possibles).
        :type chargementCourant: int
        :param listeChargementsPossibles: La liste des chargements possibles pour ce projet.
        :type listeChargementsPossibles: list[Chargement]
        """
        if listeChargementsPossibles is None:
            self.__chargementCourant = -1
            self.__listeChargementsPossibles = []
        else:
            self.__listeChargementsPossibles = [Chargement.Chargement().clone(chargement) for chargement in
                                                listeChargementsPossibles]
            if chargementCourant >= len(self.__listeChargementsPossibles):
                self.__chargementCourant = -1
            else:
                self.__chargementCourant = chargementCourant
        self.__nomProjet = nomProjet
        if listeMateriaux is None:
            self.__listeMateriaux = []
        else:
            self.__listeMateriaux = [Materiau.Materiau().clone(mat) for mat in listeMateriaux]
        if plaque is None:
            self.__plaque = Plaque.Plaque()
        else:
            self.__plaque = plaque
        self.__nPliAjout = nPliAjout  # nombre de pli à ajouter -- temporaire
        if pliAj is None:
            self.__pliAj = Pli.Pli()  # pli à ajouter -- temporaire
        else:
            self.__pliAj = pliAj

    def toJSON(self):
        if self.__pliAj is None:
            return dict(__type__="Projet",
                        nom_projet=self.__nomProjet,
                        liste_materiaux=[mat.toJSON() for mat in self.__listeMateriaux],
                        chargement_courant=self.__chargementCourant,
                        liste_chargements=[chargement.toJSON() for chargement in self.__listeChargementsPossibles],
                        plaque=self.__plaque.toJSON(),
                        n_pli_ajout=self.__nPliAjout,
                        pli_aj=None)
        else:
            return dict(__type__="Projet",
                        nom_projet=self.__nomProjet,
                        liste_materiaux=[mat.toJSON() for mat in self.__listeMateriaux],
                        chargement_courant=self.__chargementCourant,
                        liste_chargements=[chargement.toJSON() for chargement in self.__listeChargementsPossibles],
                        plaque=self.__plaque.toJSON(),
                        n_pli_ajout=self.__nPliAjout,
                        pli_aj=self.__pliAj.toJSON())

    def equals(self,
               projet: Projet) -> bool:
        try:
            return self.__nomProjet == projet.getNomProjet() and \
                   False not in [self.__listeMateriaux[i].equals(projet.getListeMateriaux()[i]) for i in range(0, len(self.__listeMateriaux))] and \
                   self.__chargementCourant == projet.getChargementCourantIndex() and \
                   False not in [self.__listeChargementsPossibles[i].equals(projet.getListeChargementsPossibles()[i]) for i in range(0, len(self.__listeChargementsPossibles))] and \
                   self.__plaque.equals(projet.getPlaque()) and \
                   self.__nPliAjout == projet.getNPliAjout() and \
                   self.__pliAj.equals(projet.getPliAj())
        except:
            return False

    def getNPliAjout(self):
        return self.__nPliAjout

    def setNPlisAjout(self, n: int):
        self.__nPliAjout = n

    def getPlaque(self):
        return self.__plaque

    def setPlaque(self, p: Plaque):
        self.__plaque = p

    def getPliAj(self):
        return (self.__pliAj)

    def setPliAj(self, p: Pli):
        self.__pliAj = p

    def setChargementCourant(self,
                             index: int) -> None:
        """
        Méthode permettant de changer le chargement courant.

        :param index: L'index du nouveau chargement courant dans la liste des chargements possibles.
        :raise IndexError: Si l'index ne correspond à aucun chargement.
        """
        if index >= 0 and index < len(self.__listeChargementsPossibles):
            self.__chargementCourant = index
        else:
            raise IndexError("L'index ne correspond à aucun chargement.")

    def getChargementCourant(self) -> Chargement:
        """
        Getter permettant d'obtenir le chargement courant.

        :return: Le chargement courant.
        """
        if len(self.__listeChargementsPossibles) != 0:
            try:
                return self.__listeChargementsPossibles[self.__chargementCourant]
            except ValueError:
                return []

    def getChargementCourantIndex(self) -> int:
        """
        Getter permettant d'obtenir l'index du chargement courant dans la liste des chargements possibles.

        :return: L'index du chargement courant dans la liste des chargements possibles.
        """
        return self.__chargementCourant

    def getListeChargementsPossibles(self) -> list[Chargement]:
        """
        Getter permettant d'obtenir la liste des chargements possibles.

        :return: La liste des chargements possibles.
        """
        return self.__listeChargementsPossibles

    def ajouteChargementPossible(self,
                                 chargement: Chargement) -> None:
        """
        Méthode pour ajouter un chargemetnt à la lisye des chatgements possibles.
        S'il s'agit du premier chargement du projet, la méthode va le définir comme chargement courant.

        :param chargement: Le chargement à ajouter.
        """
        self.__listeChargementsPossibles.append(Chargement.Chargement().clone(chargement))
        if self.__chargementCourant == -1:
            self.__chargementCourant = len(self.__listeChargementsPossibles) - 1

    def removeChargementPossibleAtIndex(self,
                                        index: int) -> bool:
        """
        Méthode pour supprimer un chargement possible de la liste des chargements possibles.
        Cette méthode mets à jour l'index du chargement par défaut de la manière suivante :
            - index(chargement à supprimer) > index(chargement défaut) => Pas de changement
            - index(chargement à supprimer) < index(chargement défaut) => index(chargement défaut) --
            - index(chargement à supprimer) == index(chargement défaut) => index(chargement défaut) prend 0 ou -1 si la liste est vide.
        :param index:
        :return:
        """
        try:
            self.__listeChargementsPossibles.pop(index)
            if len(self.__listeChargementsPossibles) == 0:
                self.__chargementCourant = -1
            else:
                if index == self.__chargementCourant:
                    self.__chargementCourant = 0
                elif index < self.__chargementCourant:
                    self.__chargementCourant = self.__chargementCourant - 1
            return True
        except IndexError:
            return False

    def getNomProjet(self) -> str:
        """
        Getter pour obtenir le nom du projet.

        :return: Le nom du projet.
        """
        return self.__nomProjet

    def setNomProjet(self,
                     nomProjet: str) -> None:
        """
        Setter permettant de mettre à jour le nom du projet.

        :param nomProjet: Le nouveau nom du projet.
        """
        self.__nomProjet = nomProjet

    def getListeMateriaux(self) -> list[Materiau]:
        """
        Méthode pour obtenir la liste des matériaux qui composent le projet.
        :return: La liste des matériaux qui composent le projet.
        """
        return self.__listeMateriaux

    def ajouteMateriauPossible(self,
                               mat: Materiau) -> None:
        """
        Méthode pour ajouter un matériau au projet.

        :param mat: Le matériau à ajouter au projet.
        """
        newMat = Materiau.Materiau()
        newMat = newMat.clone(mat)
        self.__listeMateriaux.append(newMat)

    def supprimeMateriauPossibleAtIndex(self,
                                        index: int) -> bool:
        """
        Méthode pour supprimer un matériau du projet via son index dans la liste des projets.

        :param index: L'index du matériau dans la liste des projets.
        :return: True si la suppression est OK, False sinon.
        """
        try:
            self.__listeMateriaux.pop(index)
            return True
        except IndexError:
            return False

    def supprimeMateriauPossible(self,
                                 mat: Materiau) -> bool:
        """
        Méthode pour supprimer un matériau possible du projet.

        :param mat: Le matériau à supprimer du projet.
        :return: True si le matériau était dans le projet, False sinon.
        """
        taille = len(self.__listeMateriaux)
        i = 0
        while (i < taille) and (not self.__listeMateriaux[i].equals(mat)):
            i = i + 1
        return self.supprimeMateriauPossibleAtIndex(i)

    def __str__(self) -> str:
        """
        Méthode pour afficher dans la sortie standard le contenu d'un projet.
        :return:
        """
        description = "Liste des matériaux disponibles pour le projet '" + self.__nomProjet + "':"
        for mat in self.__listeMateriaux:
            description = description + "\n" + mat.getNom()
        return description
