# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtGui, QtWidgets

from script import Materiau
from script import PopupRechercheMateriauBDD


class OngletProjetMateriaux(QtWidgets.QWidget):
    """
    Méthode représentant l'onglet de gestion des matériaux d'une fenêtre projet.
    """
    def __init__(self,
                 parent=None) -> None:
        super(OngletProjetMateriaux, self).__init__()
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les composants de l'onglet.
            - Interface d'ajout d'un matériaux propre au projet.
            - Affichage d'un popup permettant l'ajout depuis la base de données.
        """
        self.widget_projet_materiaux = QtWidgets.QWidget(self)
        self.widget_projet_materiaux.setObjectName("widget_projet_materiaux")

        self.onglet_projet_materiaux = QtWidgets.QFrame(self.widget_projet_materiaux)
        self.onglet_projet_materiaux.setGeometry(QtCore.QRect(0, 0, 880, 430))
        self.onglet_projet_materiaux.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onglet_projet_materiaux.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onglet_projet_materiaux.setObjectName("onglet_projet_materiaux")

        self.label = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label.setGeometry(QtCore.QRect(260, 10, 291, 16))
        self.label.setObjectName("label2")
        self.label.setStyleSheet("color:black;")

        self.label_2 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:black;")

        self.champ_nom_materiau = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_nom_materiau.setGeometry(QtCore.QRect(20, 70, 231, 21))
        self.champ_nom_materiau.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_nom_materiau.setObjectName("champ_nom_materiau")

        self.label_3 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:black;")

        self.champ_ref_materiau = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_ref_materiau.setGeometry(QtCore.QRect(20, 130, 231, 21))
        self.champ_ref_materiau.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_ref_materiau.setObjectName("champ_ref_materiau")

        self.label_4 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color:black;")

        self.champ_e1 = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_e1.setGeometry(QtCore.QRect(20, 190, 81, 21))
        self.champ_e1.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_e1.setObjectName("champ_e1")

        self.label_5 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_5.setGeometry(QtCore.QRect(170, 170, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color:black;")

        self.champ_e2 = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_e2.setGeometry(QtCore.QRect(160, 190, 81, 21))
        self.champ_e2.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_e2.setObjectName("champ_e2")

        self.label_6 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color:black;")

        self.champ_g12 = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_g12.setGeometry(QtCore.QRect(20, 250, 81, 21))
        self.champ_g12.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_g12.setObjectName("champ_g12")

        self.label_7 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_7.setGeometry(QtCore.QRect(170, 230, 60, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color:black;")

        self.champ_v12 = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_v12.setGeometry(QtCore.QRect(160, 250, 81, 21))
        self.champ_v12.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_v12.setObjectName("champ_v12")

        self.label_8 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_8.setGeometry(QtCore.QRect(40, 290, 171, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("color:black;")

        self.label_9 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_9.setGeometry(QtCore.QRect(30, 320, 41, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("color:black;")

        self.label_10 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_10.setGeometry(QtCore.QRect(170, 320, 41, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("color:black;")

        self.label_11 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_11.setGeometry(QtCore.QRect(330, 50, 171, 16))
        self.label_11.setObjectName("label_30")
        self.label_11.setStyleSheet("color:black;")

        self.label_12 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_12.setGeometry(QtCore.QRect(310, 80, 41, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet("color:black;")

        self.label_13 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_13.setGeometry(QtCore.QRect(450, 80, 41, 16))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet("color:black;")

        self.label_14 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_14.setGeometry(QtCore.QRect(310, 200, 171, 16))
        self.label_14.setObjectName("label_14")
        self.label_14.setStyleSheet("color:black;")

        self.label_15 = QtWidgets.QLabel(self.onglet_projet_materiaux)
        self.label_15.setGeometry(QtCore.QRect(310, 140, 151, 16))
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet("color:black;")

        self.champ_s11c = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_s11c.setGeometry(QtCore.QRect(20, 340, 81, 21))
        self.champ_s11c.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_s11c.setObjectName("champ_s11c")

        self.champ_s22c = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_s22c.setGeometry(QtCore.QRect(160, 340, 81, 21))
        self.champ_s22c.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_s22c.setObjectName("champ_s22c")

        self.champ_s11t = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_s11t.setGeometry(QtCore.QRect(300, 100, 81, 21))
        self.champ_s11t.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_s11t.setObjectName("champ_s11t")

        self.champ_s22t = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_s22t.setGeometry(QtCore.QRect(440, 100, 81, 21))
        self.champ_s22t.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_s22t.setObjectName("champ_s22t")

        self.champ_s12 = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_s12.setGeometry(QtCore.QRect(300, 160, 81, 21))
        self.champ_s12.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_s12.setObjectName("champ_s12")

        self.champ_pourcentage_fibre = QtWidgets.QLineEdit(self.onglet_projet_materiaux)
        self.champ_pourcentage_fibre.setGeometry(QtCore.QRect(300, 220, 191, 21))
        self.champ_pourcentage_fibre.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.champ_pourcentage_fibre.setObjectName("champ_pourcentage_fibre")

        self.fenetre_boutons = QtWidgets.QFrame(self.onglet_projet_materiaux)
        self.fenetre_boutons.setGeometry(QtCore.QRect(300, 280, 231, 101))
        self.fenetre_boutons.setStyleSheet("background-color: rgba(0, 0, 0, 25);border-color: rgba(0, 0, 0, 150);")
        self.fenetre_boutons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fenetre_boutons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fenetre_boutons.setObjectName("fenetre_boutons")

        self.bouton_ajouter = QtWidgets.QPushButton(self.fenetre_boutons)
        self.bouton_ajouter.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.bouton_ajouter.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);color:black; border:none;")
        self.bouton_ajouter.setDefault(False)
        self.bouton_ajouter.setFlat(False)
        self.bouton_ajouter.setObjectName("bouton_ajouter")

        self.bouton_ajouter_depuis_bdd = QtWidgets.QPushButton(self.fenetre_boutons)
        self.bouton_ajouter_depuis_bdd.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.bouton_ajouter_depuis_bdd.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border-radius:0px")
        self.bouton_ajouter_depuis_bdd.setDefault(False)
        self.bouton_ajouter_depuis_bdd.setFlat(False)
        self.bouton_ajouter_depuis_bdd.setObjectName("bouton_ajouter_depuis_bdd")

        self.bouton_supprimer = QtWidgets.QPushButton(self.fenetre_boutons)
        self.bouton_supprimer.setGeometry(QtCore.QRect(10, 70, 211, 21))
        self.bouton_supprimer.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);color:black; border:none;")
        self.bouton_supprimer.setDefault(False)
        self.bouton_supprimer.setFlat(False)
        self.bouton_supprimer.setObjectName("bouton_supprimer")

        self.liste_materiaux = QtWidgets.QListView(self.onglet_projet_materiaux)
        self.liste_materiaux.setGeometry(QtCore.QRect(560, 80, 301, 301))
        self.liste_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);color:black; border:none;")
        self.liste_materiaux.setObjectName("liste_materiaux")

    def retranslateUi(self) -> None:
        """
        Méthode permettant d'initialiser le contenu textuel des composants de l'onglet.
        """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("onglet_projet_materiaux", "AJOUT D’UN MATÉRIAU PROPRE AU PROJET"))
        self.label_2.setText(_translate("onglet_projet_materiaux", "Nom du matériau"))
        self.label_3.setText(_translate("onglet_projet_materiaux", "Référence du matériau"))
        self.label_4.setText(_translate("onglet_projet_materiaux", "E1 (MPa)"))
        self.label_5.setText(_translate("onglet_projet_materiaux", "E2 (MPa)"))
        self.label_6.setText(_translate("onglet_projet_materiaux", "G12 (MPa)"))
        self.label_7.setText(_translate("onglet_projet_materiaux", "v12 (MPa)"))
        self.label_8.setText(_translate("onglet_projet_materiaux", "Sigma compression (MPa)"))
        self.label_9.setText(_translate("onglet_projet_materiaux", "s11_c"))
        self.label_10.setText(_translate("onglet_projet_materiaux", "s22_c"))
        self.label_11.setText(_translate("onglet_projet_materiaux", "Sigma traction (MPa)"))
        self.label_12.setText(_translate("onglet_projet_materiaux", "s11_t"))
        self.label_13.setText(_translate("onglet_projet_materiaux", "s22_t"))
        self.label_14.setText(_translate("onglet_projet_materiaux", "Pourcentage de fibre "))
        self.label_15.setText(_translate("onglet_projet_materiaux", "s12 (MPa)"))
        self.bouton_ajouter.setText(_translate("onglet_projet_materiaux", "AJOUTER AU PROJET"))
        self.bouton_ajouter_depuis_bdd.setText(_translate("onglet_projet_materiaux", "AJOUTER DEPUIS LA BDD"))
        self.bouton_supprimer.setText(_translate("onglet_projet_materiaux", "SUPPRIMER"))

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def ajoute_materiau_projet(self,
                               mat: Materiau) -> None:
        """
        Méthode permettant d'ajouter un matériau à la liste des matériaux du projet.
        Cette méthode envoie à l'instance de l'application qu'une modification a été effectuée.

        :param mat: Le matériau à ajouter au projet.
        """
        self.__parent.projet.ajouteMateriauPossible(mat)
        # La sauvegarde du projet n'est plus à jour
        self.__parent.modification_effectuee()

    def get_liste_materiaux(self) -> list[Materiau]:
        """
        Méthode peremttant d'obtenir la liste des matériaux du projet.
        :return: La liste des matériaux qui composent le projet.
        """
        return self.__parent.projet.getListeMateriaux()

    def affiche_materiaux_disponibles_projet(self) -> None:
        """
        Méthode permettant de mettre à jour la liste des matériaux disponibles pour le projet dans l'interface graphique.
        """
        modele_materiaux_disponibles = QtGui.QStandardItemModel()
        self.liste_materiaux.setModel(modele_materiaux_disponibles)
        for mat in self.__parent.projet.getListeMateriaux():
            entree = QtGui.QStandardItem(str(mat.getNom() + " - " + mat.getRef()))
            modele_materiaux_disponibles.appendRow(entree)

    def reset_background_ajout(self) -> None:
        """
        Méthode permettant de remettre par défaut le style des champs d'ajout d'un matériau.
        """
        defaut_stylesheet = "background-color:white;border:none;color:black;"
        self.champ_nom_materiau.setStyleSheet(defaut_stylesheet)
        self.champ_ref_materiau.setStyleSheet(defaut_stylesheet)
        self.champ_e1.setStyleSheet(defaut_stylesheet)
        self.champ_e2.setStyleSheet(defaut_stylesheet)
        self.champ_g12.setStyleSheet(defaut_stylesheet)
        self.champ_v12.setStyleSheet(defaut_stylesheet)
        self.champ_s11c.setStyleSheet(defaut_stylesheet)
        self.champ_s22c.setStyleSheet(defaut_stylesheet)
        self.champ_s11t.setStyleSheet(defaut_stylesheet)
        self.champ_s22t.setStyleSheet(defaut_stylesheet)
        self.champ_s12.setStyleSheet(defaut_stylesheet)
        self.champ_pourcentage_fibre.setStyleSheet(defaut_stylesheet)

    def reset_content_ajout(self) -> None:
        """
        Méthode permettant de vider le contenu des champs d'ajout d'un matériau.
        """
        _translate = QtCore.QCoreApplication.translate
        self.champ_nom_materiau.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_ref_materiau.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_e1.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_e2.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_g12.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_v12.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_s11c.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_s22c.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_s11t.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_s22t.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_s12.setText(_translate("onglet_projet_materiaux", ""))
        self.champ_pourcentage_fibre.setText(_translate("onglet_projet_materiaux", ""))

    def verif_input_ajout(self, nom:str, ref:str,
                    e1:str, e2:str,
                    g12:str,
                    v12:str,
                    s11_c:str, s22_c:str,
                    s11_t:str, s22_t:str,
                    s12:str,
                    fibre:str) -> bool:
        """
        Méthode permettant de vérifier le contenu des champs pour l'ajout d'un matériau et de mettre en évidence les champs comportant des erreurs.

        :param nom: Le nom du matériau (Usage : non vide)
        :param ref: La reférence du matériau (Usage : non vide)
        :param e1: La valeur de E1 (Usage : float)
        :param e2: La valeur de E2 (Usage : float)
        :param g12: La valeur de G12 (Usage : float)
        :param v12: La valeur de v12 (Usage : float)
        :param s11_c: La valeur de s11 en compréssion (Usage : float)
        :param s22_c: La valeur de s22 en compréssion (Usage : float)
        :param s11_t: La valeur de s11 en traction (Usage : float)
        :param s22_t: La valeur de s22 en traction (Usage : float)
        :param s12: La valeur de s12 (Usage : float)
        :param fibre: La valeur du %age de fibre (Usage : 100 ≥ float ≥ 0)
        :return: True si les caractéristiques sont correctes, False sinon.
        """
        flag = True
        error_champ_stylesheet = "background-color:darkred;border:none;color:white;"
        if nom == "":
            self.champ_nom_materiau.setText("")
            self.champ_nom_materiau.setStyleSheet(error_champ_stylesheet)
            flag = False
        if ref == "":
            self.champ_ref_materiau.setText("")
            self.champ_ref_materiau.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            e1 = float(e1)
        except ValueError:
            self.champ_e1.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            e2 = float(e2)
        except ValueError:
            self.champ_e2.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            g12 = float(g12)
        except ValueError:
            self.champ_g12.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            v12 = float(v12)
        except ValueError:
            self.champ_v12.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            s11_c = float(s11_c)
        except ValueError:
            self.champ_s11c.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            s22_c = float(s22_c)
        except ValueError:
            self.champ_s22c.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            s11_t = float(s11_t)
        except ValueError:
            self.champ_s11t.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            s22_t = float(s22_t)
        except ValueError:
            self.champ_s22t.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            s12 = float(s12)
        except ValueError:
            self.champ_s12.setStyleSheet(error_champ_stylesheet)
            flag = False
        try:
            pourcentage_fibre = float(fibre)
            if pourcentage_fibre < 0 or pourcentage_fibre > 100:
                self.champ_pourcentage_fibre.setStyleSheet(error_champ_stylesheet)
                flag = False
        except ValueError:
            self.champ_pourcentage_fibre.setStyleSheet(error_champ_stylesheet)
            flag = False
        return flag

    def ajoute_materiau(self) -> None:
        """
        Méthode permettant d'ajouter un matériau au projet.
        """
        self.reset_background_ajout()

        # Récupération des valeurs
        nom = self.champ_nom_materiau.text().strip()
        ref = self.champ_ref_materiau.text().strip()
        e1 = self.champ_e1.text().strip()
        e2 = self.champ_e2.text().strip()
        g12 = self.champ_g12.text().strip()
        v12 = self.champ_v12.text().strip()
        s11_c = self.champ_s11c.text().strip()
        s22_c = self.champ_s22c.text().strip()
        s11_t = self.champ_s11t.text().strip()
        s22_t = self.champ_s22t.text().strip()
        pourcentage_fibre = self.champ_pourcentage_fibre.text().strip()
        s12 = self.champ_s12.text().strip()

        # Vérification des données et mise en évidence des erreurs
        flag = self.verif_input_ajout(nom, ref, e1, e2, g12, v12, s11_c, s22_c, s11_t, s22_t, s12, pourcentage_fibre)

        if flag:
            mat = Materiau.Materiau(nom, ref, e1, e2, g12, v12, s11_c, s22_c, s11_t, s22_t, s12, pourcentage_fibre)
            try:
                self.__parent.projet.ajouteMateriauPossible(mat)
                self.reset_background_ajout()
                self.reset_content_ajout()
                # La sauvegarde du projet n'est plus à jour
                self.__parent.modification_effectuee()
                self.quick_popup("Matériau ajouté au projet!", type="Succes", duree=3)
            except ConnectionError:
                self.quick_popup("Impossible de se connecter à la BDD!", type="Error", duree=3)
                pass
        else:
            self.quick_popup("Des valeurs sont éronnées ou manquantes...", type="Error", duree=3)
            pass

        if len(self.__parent.projet.getListeMateriaux()):
            self.affiche_materiaux_disponibles_projet()

    def affiche_popup_ajoute_depuis_bdd(self) -> None:
        """
        Méthode permettant d'afficher le popup d'ajout du matériau depuis la bdd.
        """
        self.popup_recherche_bdd = PopupRechercheMateriauBDD.PopupRechercheMateriauBDD(self)
        self.popup_recherche_bdd.setGeometry(QtCore.QRect(110, 50, 611, 261))
        self.popup_recherche_bdd.setObjectName("popup_recherche_bdd")
        self.popup_recherche_bdd.show()

    def supprime_materiau(self) -> None:
        """
        Méthode permettant de supprimer le matériau selectionné de la liste des matériaux du projet.
        """
        index = self.liste_materiaux.currentIndex().row()
        if index >= 0:
            self.__parent.projet.supprimeMateriauPossibleAtIndex(index)
            self.affiche_materiaux_disponibles_projet()
            # La sauvegarde du projet n'est plus à jour
            self.__parent.modification_effectuee()
            self.quick_popup("Matériau supprimé du projet!", type="Succes", duree=3)
        else:
            pass
            self.quick_popup("Aucun matériau sélectionné...", type="Warning", duree=3)

    def initActions(self) -> None:
        """
        Méthode permettant de connecter les actions propres à la fenêtres au différents boutons.
        """
        self.bouton_ajouter.clicked.connect(self.ajoute_materiau)
        self.bouton_ajouter_depuis_bdd.clicked.connect(self.affiche_popup_ajoute_depuis_bdd)
        self.bouton_supprimer.clicked.connect(self.supprime_materiau)

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = OngletProjetMateriaux()
    tmp.setStyleSheet("background-color: rgb(224, 224, 224)")
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()