# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from __future__ import annotations
from script import DatabaseTools


class Materiau:
    """
    Classe définissant un Materiau.
    Un matériau possède les caractéristiques suivantes :
        - Nom : le nom du matériau
        - Ref : une référence permettant de l'identifier rapidement
        - Un ensemble de caractéristique numérique (E1, E2, G12, v12, s11c, s22c, s11t, s22t, s12 et pourcentage fibre)
    """

    def __init__(self,
                 nom: str = "MateriauInconnu", ref: str = "RefDefaut",
                 e1: float = 0, e2: float = 0,
                 g12: float = 0,
                 v12: float = 0,
                 s11_c: float = 0, s22_c: float = 0,
                 s11_t: float = 0, s22_t: float = 0,
                 s12: float = 0,
                 pourcentageFibre: float = 0):
        """
        Constructeur de la classe Matériau.

        :param nom: Le nom du matériau
        :param ref: La référence du matériau
        :param e1: La valeur de E1 (El selon les notations)
        :param e2: La valeur de E2 (Et selon les notations)
        :param g12: La valeur de G12 (Glt selon les notations)
        :param v12: La valeur de v12 (v12 selon les notations)
        :param s11_c: La valeur de s11 en comprésion (sll selon les notations)
        :param s22_c: La valeur de s22 en comprésion (stt selon les notations)
        :param s11_t: La valeur de s11 en traction (sll selon les notations)
        :param s22_t: La valeur de s22 en traction (stt selon les notations)
        :param s12: La valeur de s12 (tlt selon les notations)
        :param pourcentageFibre: Le pourcentage de fibre du matériau
        """
        self.__nom = nom
        self.__ref = ref
        self.__E1 = e1
        self.__E2 = e2
        self.__G12 = g12
        self.__v12 = v12
        self.__s11_c = s11_c
        self.__s22_c = s22_c
        self.__s11_t = s11_t
        self.__s22_t = s22_t
        self.__s12 = s12
        self.__pourcentageFibre = pourcentageFibre

    def equals(self,
               mat: Materiau) -> bool:
        """
        Méthode permettant de comparer deux matériaux, en comparant l'ensemble des champs qui les composent.

        :param mat: Le matériau à comparer.
        :return: True si les deux matériaux ont les mêmes caractéristiques, False sinon.
        """
        isEquals = self.__nom == mat.getNom() and \
                   self.__ref == mat.getRef() and \
                   self.__E1 == mat.getE1() and \
                   self.__E2 == mat.getE2() and \
                   self.__G12 == mat.getG12() and \
                   self.__v12 == mat.getV12() and \
                   self.__s11_c == mat.getS11_c() and \
                   self.__s22_c == mat.getS22_c() and \
                   self.__s11_t == mat.getS11_t() and \
                   self.__s22_t == mat.getS22_t() and \
                   self.__s12 == mat.getS12() and \
                   self.__pourcentageFibre == mat.getPourcentageFibre()
        return isEquals

    def clone(self,
              mat: Materiau) -> Materiau:
        """
        Méthode permettant de cloner un matériaux.
        Attention : Cette méthode ne modifie pas en place.
        Exemple :
        import Materiau
        mat1 = Materiau.Materiau()
        mat2 = Materiau.Materiau().clone(mat1)

        :param mat: Le matériaux
        :return: Le materiau clone de celui passé en argument.
        """
        self.__nom = mat.getNom()
        self.__ref = mat.getRef()
        self.__E1 = mat.getE1()
        self.__E2 = mat.getE2()
        self.__G12 = mat.getG12()
        self.__v12 = mat.getV12()
        self.__s11_c = mat.getS11_c()
        self.__s22_c = mat.getS22_c()
        self.__s11_t = mat.getS11_t()
        self.__s22_t = mat.getS22_t()
        self.__s12 = mat.getS12()
        self.__pourcentageFibre = mat.getPourcentageFibre()
        return self

    def getPourcentageFibre(self) -> float:
        """
        Getter permettant d'obtenir le pourcentage de fibre d'un matériau.

        :return: Le pourcentage de fibre du matériau.
        """
        return self.__pourcentageFibre

    def setPourcentageFibre(self,
                            pourcentageFibre: float) -> None:
        """
        Setter permettant de mettre à jour le pourcentage de fibre d'un matériau.

        :param pourcentageFibre: Le nouveau pourcentage de fibre du matériau.
        """
        self.__pourcentageFibre = pourcentageFibre

    def getNom(self) -> str:
        """
        Getter permettant d'obtenir le nom du matériau.

        :return: Le nom du matériau.
        """
        return self.__nom

    def setNom(self,
               nom: str) -> None:
        """
        Setter permettant de mettre à jour le nom du matériau.

        :param nom: Le nouveau nom du matériau.
        """
        self.__nom = nom

    def getRef(self) -> str:
        """
        Getter permettant d'obtenir la référence du matériau.

        :return: La référence du matériau.
        """
        return self.__ref

    def setRef(self,
               ref: str) -> None:
        """
        Setter permettant de mettre à jour le référence du matériau.

        :param ref: La nouvelle référence du matériau.
        """
        self.__ref = ref

    def getE1(self) -> float:
        """
        Getter permettant d'obtenir la valeur de E1 du matériau (El selon les notations)

        :return: La valeur E1 du matériau.
        """
        return self.__E1

    def setE1(self,
              E1: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre E1 (El selon les notations) du matériau.

        :param E1: La nouvelle valeur du paramètre E1 du matériau.
        """
        self.__E1 = E1

    def getE2(self) -> float:
        """
        Getter permettant d'obtenir la valeur du paramètre E2 (Et selon les notations) du matériau.

        :return: La valeur du paramètre E2 du matériau.
        """
        return self.__E2

    def setE2(self,
              E2: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre E2 (Et selon les notations) du matériau.

        :param E2: La nouvelle valeur du paramètre E2 du matériau.
        """
        self.__E2 = E2

    def getG12(self) -> float:
        """
        Getter permettant d'obtenir la valeur du paramètre G1Z (Glt selon les notations) du matériau.

        :return: La valeur du paramètre G12 du matériau.
        """
        return self.__G12

    def setG12(self,
               G12: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre G12 (Glt selon les notations) du matériau.

        :param G12: La nouvelle valeur du paramètre G12
        """
        self.__G12 = G12

    def getV12(self) -> float:
        """
        Getter permettant d'obtenir la valeur du paramètre v12 (vlt selon les notations) du matériau.

        :return: La valeur du paramètre v12 du matériau.
        """
        return self.__v12

    def setV12(self,
               v12: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre v12 (vlt selon les notations) du matériau.

        :param v12: La nouvelle valeur du paramètre v12.
        """
        self.__v12 = v12

    def getS11_c(self) -> float:
        """
        Getter permettant de mettre à jour la valeur du paramètre s11 en compression (sll en compression selon les notations) du matériau.

        :return: La valeur du paramètre s11 en compression du matériau.
        """
        return self.__s11_c

    def setS11_c(self,
                 s11_c: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre s11 en compression (sll en compression selon les notations) du matériau.

        :param s11_c: La nouvelle valeur du paramètre s11 en compression.
        """
        self.__s11_c = s11_c

    def getS22_c(self) -> float:
        """
        Getter permettant de mettre à jour la valeur du paramètre s22 en compression (stt en compression selon les notations) du matériau.

        :return: La valeur du paramètre s22 en compression du matériau.
        """
        return self.__s22_c

    def setS22_c(self,
                 s22_c: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre s22 en compression (stt en compression selon les notations) du matériau.

        :param s22_c: La nouvelle valeur du paramètre s22 en compression.
        """
        self.__s22_c = s22_c

    def getS11_t(self) -> float:
        """
        Getter permettant de mettre à jour la valeur du paramètre s11 en traction (sll en traction selon les notations) du matériau.

        :return: La valeur du paramètre s11 en traction du matériau.
        """
        return self.__s11_t

    def setS11_t(self,
                 s11_t: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre s11 en traction (sll en traction selon les notations) du matériau.

        :param s11_t: La nouvelle valeur du paramètre s11 en traction.
        """
        self.__s11_t = s11_t

    def getS22_t(self) -> float:
        """
        Getter permettant de mettre à jour la valeur du paramètre s22 en traction (stt en traction selon les notations) du matériau.

        :return: La valeur du paramètre s22 en traction du matériau.
        """
        return self.__s22_t

    def setS22_t(self,
                 s22_t: float) -> None:
        """
        Setter permettant de mettre à jour la valeur du paramètre s22 en traction (stt en traction selon les notations) du matériau.

        :param s22_t: La nouvelle valeur du paramètre s22 en traction.
        """
        self.__s22_t = s22_t

    def getS12(self) -> float:
        """
        Getter permettant d'obtenir la valeur du paramètre s12 (tau(lt) en fonction des notations) du matériau.

        :return: La valeur du paramètre s12 du matériau.
        """
        return self.__s12

    def setS12(self,
               s12: float) -> None:
        """
        Setter pour mettre à jour la valeur du paramètre s12 (tau(lt) en foncrion des notations) du matériau.

        :param s12: La nouvelle valeur du paramètre s12.
        """
        self.__s12 = s12

    def __str__(self) -> str:
        """
        Méthode pour afficher un matériau dans la sortie standard.

        :return: Une chaine de caractères décrivant le matériau.
        """
        description = ["Materiau: " + str(self.__nom),
                       "Ref : " + str(self.__ref),
                       "E1 = " + str(self.__E1),
                       "E2 = " + str(self.__E2),
                       "G12 = " + str(self.__G12),
                       "v12 = " + str(self.__v12),
                       "s11_c = " + str(self.__s11_c),
                       "s22_c = " + str(self.__s22_c),
                       "s11_t = " + str(self.__s11_t),
                       "s22_t = " + str(self.__s22_t),
                       "s12 = " + str(self.__s12)]
        return '\n'.join(description)

    def ajouteDatabase(self) -> None:
        """
        Méthode pour ajouter le matériau à la base de données.
        """
        data = (
        self.__nom, self.__ref, self.__E1, self.__E2, self.__G12, self.__v12, self.__s11_c, self.__s22_c, self.__s11_t,
        self.__s22_t, self.__s12, self.__pourcentageFibre)
        query = """ INSERT INTO public.materiau(nom, reference, e1, e2, g12, v12, s11_c, s22_c, s11_t, s22_t, s12, pourcentage_fibre)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        DatabaseTools.DatabaseTools().executeInsert(query, data)

    def toJSON(self) -> dict:
        """
        Méthode pour exporter un materiau au format JSON.
        Le dictionnaire est utilisé par le MateriauEncoder.

        :return: Un dictionnaire permettant l'encodage au format JSON.
        """
        return dict(__type__="Materiau",
                    nom=self.__nom,
                    ref=self.__ref,
                    E1=self.__E1,
                    E2=self.__E2,
                    G12=self.__G12,
                    v12=self.__v12,
                    s11c=self.__s11_c,
                    s22c=self.__s22_c,
                    s11t=self.__s11_t,
                    s22t=self.__s22_t,
                    s12=self.__s12,
                    pourcentage_fibre=self.__pourcentageFibre)


        