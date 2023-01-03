# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

from script import FenetreDessin
from script import Materiau
from script import Projet

class OngletProjetPlaque(QtWidgets.QWidget):
    """
    Classe représentant un onglet de paramétrage de plaque.
    """
    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe OngletProjetPlaque
        Cette classe représente l'onglet de paramétrage de la plaque

        :param parent: Xidget parent de l'onglet de paramétrage de la plaque
        """
        super(OngletProjetPlaque, self).__init__()
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()


    def initUI(self) -> None:
        """
        Méthode pour initialiser le widget représentant l'onglet du paramétrage de la plaque
        """
        self.widget_projet_plaque = QtWidgets.QWidget(self)
        self.widget_projet_plaque.setObjectName("widget_projet_plaque")

        self.frame_7 = QtWidgets.QFrame(self.widget_projet_plaque)
        self.frame_7.setGeometry(QtCore.QRect(0, -10, 871, 451))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")

        self.label_36 = QtWidgets.QLabel(self.frame_7)
        self.label_36.setGeometry(QtCore.QRect(30, 30, 111, 16))
        self.label_36.setObjectName("label_36")

        self.comboBoxProjetTypeMateriaux = QtWidgets.QComboBox(self.frame_7)
        self.comboBoxProjetTypeMateriaux.setGeometry(QtCore.QRect(30, 50, 231, 21))
        self.comboBoxProjetTypeMateriaux.setObjectName("comboBoxProjetTypeMateriaux")

        self.label_37 = QtWidgets.QLabel(self.frame_7)
        self.label_37.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label_37.setObjectName("label_37")

        self.champProjetOrientation = QtWidgets.QLineEdit(self.frame_7)
        self.champProjetOrientation.setGeometry(QtCore.QRect(30, 100, 231, 21))
        self.champProjetOrientation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.champProjetOrientation.setText("")
        self.champProjetOrientation.setObjectName("champProjetOrientation")

        self.label_38 = QtWidgets.QLabel(self.frame_7)
        self.label_38.setGeometry(QtCore.QRect(30, 130, 111, 16))
        self.label_38.setObjectName("label_38")

        self.label_39 = QtWidgets.QLabel(self.frame_7)
        self.label_39.setGeometry(QtCore.QRect(30, 180, 111, 16))
        self.label_39.setObjectName("label_39")

        self.label_40 = QtWidgets.QLabel(self.frame_7)
        self.label_40.setGeometry(QtCore.QRect(30, 230, 201, 16))
        self.label_40.setObjectName("label_40")

        self.champProjetNbrePlis = QtWidgets.QLineEdit(self.frame_7)
        self.champProjetNbrePlis.setGeometry(QtCore.QRect(30, 150, 231, 21))
        self.champProjetNbrePlis.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.champProjetNbrePlis.setText("")
        self.champProjetNbrePlis.setObjectName("champProjetNbrePlis")

        self.champProjetEpaisseurPli = QtWidgets.QLineEdit(self.frame_7)
        self.champProjetEpaisseurPli.setGeometry(QtCore.QRect(30, 200, 231, 21))
        self.champProjetEpaisseurPli.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.champProjetEpaisseurPli.setText("")
        self.champProjetEpaisseurPli.setObjectName("champProjetEpaisseurPli")

        self.champProjetPosPlaque = QtWidgets.QLineEdit(self.frame_7)
        self.champProjetPosPlaque.setGeometry(QtCore.QRect(30, 250, 231, 21))
        self.champProjetPosPlaque.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.champProjetPosPlaque.setText("")
        self.champProjetPosPlaque.setObjectName("champProjetPosPlaque")

        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setGeometry(QtCore.QRect(30, 290, 231, 131))
        self.frame_10.setStyleSheet("background-color: rgba(0, 0, 0, 25);border-color: rgba(0, 0, 0, 150);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")

        self.boutonAjoutPlaque = QtWidgets.QPushButton(self.frame_10)
        self.boutonAjoutPlaque.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.boutonAjoutPlaque.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);")
        self.boutonAjoutPlaque.setDefault(False)
        self.boutonAjoutPlaque.setFlat(False)
        self.boutonAjoutPlaque.setObjectName("boutonAjoutPlaque")

        self.boutonProjetDupliquerPlaque = QtWidgets.QPushButton(self.frame_10)
        self.boutonProjetDupliquerPlaque.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.boutonProjetDupliquerPlaque.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);")
        self.boutonProjetDupliquerPlaque.setDefault(False)
        self.boutonProjetDupliquerPlaque.setFlat(False)
        self.boutonProjetDupliquerPlaque.setObjectName("boutonProjetDupliquerPlaque")

        self.boutonProjetSupprimerPlaque = QtWidgets.QPushButton(self.frame_10)
        self.boutonProjetSupprimerPlaque.setGeometry(QtCore.QRect(10, 70, 211, 21))
        self.boutonProjetSupprimerPlaque.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);")
        self.boutonProjetSupprimerPlaque.setDefault(False)
        self.boutonProjetSupprimerPlaque.setFlat(False)
        self.boutonProjetSupprimerPlaque.setObjectName("boutonProjetSupprimerPlaque")

        self.boutonProjetFlecheHaut = QtWidgets.QPushButton(self.frame_10)
        self.boutonProjetFlecheHaut.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.boutonProjetFlecheHaut.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);")
        self.boutonProjetFlecheHaut.setDefault(False)
        self.boutonProjetFlecheHaut.setFlat(False)
        self.boutonProjetFlecheHaut.setObjectName("boutonProjetFlecheHaut")

        self.boutonProjetFlecheBas = QtWidgets.QPushButton(self.frame_10)
        self.boutonProjetFlecheBas.setGeometry(QtCore.QRect(130, 100, 91, 21))
        self.boutonProjetFlecheBas.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);")
        self.boutonProjetFlecheBas.setDefault(False)
        self.boutonProjetFlecheBas.setFlat(False)
        self.boutonProjetFlecheBas.setObjectName("boutonProjetFlecheBas")

        self.frame_11_bis = FenetreDessin.FenetreDessin(self.__parent.projet)
        self.frame_11 = QtWidgets.QScrollArea(self.frame_7)
        self.frame_11.setGeometry(QtCore.QRect(310, 70, 531, 341))
        self.frame_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.frame_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.frame_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frame_11.setWidget(self.frame_11_bis)

        # Position z_min de la plaque
        self.label_zmin = QtWidgets.QLabel(self.frame_7)
        self.label_zmin.setGeometry(QtCore.QRect(310, 40, 270, 15))
        self.label_zmin.setObjectName("label_zmin")

        self.champ_altitude_min = QtWidgets.QLineEdit(self.frame_7)
        self.champ_altitude_min.setGeometry(QtCore.QRect(590, 40, 120, 15))
        self.champ_altitude_min.setStyleSheet("background-color: rgb(255, 255, 255);border:none;color:black;")
        self.champ_altitude_min.setObjectName("champ_altitude_min")

    def retranslateUi(self) -> None:
        """
        Méthode pour mettre à jour les textes à afficher sur la page
        """
        _translate = QtCore.QCoreApplication.translate
        self.label_36.setText(_translate("Frame", "Type Matériau"))
        self.label_37.setText(_translate("Frame", "Orientation (en °)"))
        self.label_38.setText(_translate("Frame", "Nombre de plis"))
        self.label_39.setText(_translate("Frame", "Epaisseur pli"))
        self.label_40.setText(_translate("Frame", "Position relative dans la plaque"))
        self.boutonAjoutPlaque.setText(_translate("Frame", "AJOUTER"))
        self.boutonProjetDupliquerPlaque.setText(_translate("Frame", "DUPLIQUER"))
        self.boutonProjetSupprimerPlaque.setText(_translate("Frame", "SUPPRIMER"))
        self.boutonProjetFlecheHaut.setText(_translate("Frame", "^"))
        self.boutonProjetFlecheBas.setText(_translate("Frame", "v"))
        self.label_zmin.setText(_translate("Frame", "Altitude minimale z_min de la plaque (mm) :"))
        self.champ_altitude_min.setText(_translate("Frame", str(self.__parent.projet.getPlaque().getZmin())))

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def initActions(self) -> None:
        """
        Méthode permettant de connecter l'ensemble des méthodes de la page aux boutons, changement, etc..
        """
        self.champProjetOrientation.textChanged.connect(lambda: self.ajout_info_plaque())
        self.champProjetEpaisseurPli.textChanged.connect(lambda: self.ajout_info_plaque())
        self.champProjetNbrePlis.textChanged.connect(lambda: self.ajout_info_plaque())
        self.champProjetPosPlaque.textChanged.connect(lambda: self.ajout_info_plaque())
        self.boutonAjoutPlaque.clicked.connect(lambda: self.ajout_pli_app())
        self.boutonProjetDupliquerPlaque.clicked.connect(lambda: self.duplique_pli_app())
        self.boutonProjetSupprimerPlaque.clicked.connect(lambda: self.supprime_pli_app())
        self.boutonProjetFlecheHaut.clicked.connect(lambda: self.monte_pli_app())
        self.boutonProjetFlecheBas.clicked.connect(lambda: self.descend_pli_app())
        self.champ_altitude_min.textEdited.connect(self.change_altitude_min)

    def change_altitude_min(self) -> None:
        """
        Méthode permettant de mettre à jour la valeur de l'altitude minimale de la plaque pour la résoltuion. Ou de mettre en valeur pour une valeur éronnée.
        """
        # Reset
        self.champ_altitude_min.setStyleSheet("background-color:white;color:black;border:none;")
        new_z = self.champ_altitude_min.text().strip()
        if new_z == "":
            self.champ_altitude_min.setStyleSheet("background-color:darkred;color:white;border:none;")
            self.quick_popup("Nouvelle altitude incorrecte!", type="Error", duree=3)
        else:
            try:
                new_z = float(new_z)
                self.__parent.projet.getPlaque().setZMin(new_z)
                self.quick_popup("Nouvelle altitude prise en compte!", type="Succes", duree=3)
                self.__parent.modification_effectuee()
            except ValueError:
                self.champ_altitude_min.setStyleSheet("background-color:darkred;color:white;border:none;")
                self.quick_popup("Nouvelle altitude incorrecte!", type="Error", duree=3)

    def affichePlaque(self) -> None:
        """
        Permet l'affichage actualisé de la plaque
        """
        self.frame_11_bis.setPlaque(self.__parent.projet.getPlaque())
        self.frame_11_bis.update()

    def ajout_info_plaque(self) -> None:
        """
        Méthode permettant d'obtenir les informations concernant la plaque en fonction de ce qui est rempli dans les champs
        """
        self.__parent.modification_effectuee()
        orientation = self.champProjetOrientation.text().strip()
        if self.champProjetOrientation.text().strip() not in [str(-45), str(0), str(45), str(90)]:
            self.quick_popup('Choisir l orientation dans : 0° ,45° ,-45° ,90°', type="Info", duree=3)
        if orientation != "":
            try:
                self.__parent.projet.getPliAj().setOrientation(int(orientation))
                flag = True
            except ValueError:
                flag = False

        epaisseur = self.champProjetEpaisseurPli.text().strip()
        if epaisseur != "":
            try:
                self.__parent.projet.getPliAj().setEpaisseur(float(epaisseur))
                flag = True
            except ValueError:
                flag = False

        posRelPlaque = self.champProjetPosPlaque.text().strip()
        if posRelPlaque != "":
            try:
                self.__parent.projet.getPliAj().setPositionRelPlaque(int(posRelPlaque))
                flag=True
            except ValueError:
                flag=False

        mat = Materiau.Materiau()
        for k in range(0, len(self.__parent.projet.getListeMateriaux())):
            if self.__parent.projet.getListeMateriaux()[k].getNom() == self.comboBoxProjetTypeMateriaux.currentText():
                mat = self.__parent.projet.getListeMateriaux()[k]
        self.__parent.projet.getPliAj().setMateriau(mat)

        nbrePlis = self.champProjetNbrePlis.text().strip()
        if nbrePlis != "":
            try:
                self.__parent.projet.setNPlisAjout(int(nbrePlis))
                flag = True
            except ValueError:
                flag = False

    def ajout_pli_app(self) -> None:
        """
        Méthode permettant d'ajouter les plis à la plaque sur le projet l'onglet
        """
        red_background = "QLineEdit{background : darkred;border:none;color:white;}"
        white_background = "QLineEdit{background : white;border:none;color:black;}"

        # Ajout du pli dans la plaque
        flag = self.__parent.projet.getPlaque().ajoutePli(self.__parent.projet.getPliAj(), self.__parent.projet.getNPliAjout())

        # Réinitialisation des valeurs
        self.__parent.projet.getPliAj().setOrientation(0)
        self.__parent.projet.getPliAj().setEpaisseur(0)
        self.__parent.projet.getPliAj().setPositionRelPlaque(0)
        self.__parent.projet.getPliAj().setMateriau(None)
        self.__parent.projet.setNPlisAjout(0)

        # Réinitialisation de la couleur des champs
        self.champProjetOrientation.setStyleSheet(white_background)
        self.champProjetEpaisseurPli.setStyleSheet(white_background)
        self.champProjetNbrePlis.setStyleSheet(white_background)
        self.champProjetPosPlaque.setStyleSheet(white_background)

        if flag:
            self.__parent.modification_effectuee()
            # Affichage du popup de validation
            self.quick_popup('Ajout des plis !', type="Succes", duree=3)

            # Réinitialisation des champs
            self.champProjetOrientation.setText("")
            self.champProjetEpaisseurPli.setText("")
            self.champProjetNbrePlis.setText("")
            self.champProjetPosPlaque.setText("")

        else:
            # Affichage du popup d'erreur
            self.quick_popup('Erreur : informations manquantes ou éronnées..', type="Error", duree=3)

            # Mise en rouge des champs vides à compléter
            if self.champProjetOrientation.text().strip() == "":
                self.champProjetOrientation.setStyleSheet(red_background)
            if self.champProjetEpaisseurPli.text().strip() == "":
                self.champProjetEpaisseurPli.setStyleSheet(red_background)
            if self.champProjetNbrePlis.text().strip() == "":
                self.champProjetNbrePlis.setStyleSheet(red_background)
            if self.champProjetPosPlaque.text().strip() == "":
                self.champProjetPosPlaque.setStyleSheet(red_background)

        # Mise à jour de l'affichage de la plaque
        self.affichePlaque()

    def duplique_pli_app(self) -> None:
        """
        Méthode permettant la duplication du pli sélectionné
        """
        self.__parent.modification_effectuee()
        nPliSelect = self.frame_11_bis.getNPli()
        flag = self.__parent.projet.getPlaque().duppliquePli(nPliSelect)
        self.frame_11_bis.setNPli(0)
        if flag:
            self.quick_popup('Duplication du pli !', type="Succes", duree=3)
        else:
            self.quick_popup('Pas de pli sélectionné..', type="Warning", duree=3)
        self.affichePlaque()

    def supprime_pli_app(self) -> None:
        """
        Méthode permettant la suppression du pli sélectionné
        """
        self.__parent.modification_effectuee()
        nPliSelect = self.frame_11_bis.getNPli()
        flag = self.__parent.projet.getPlaque().supprimePli(nPliSelect)
        self.frame_11_bis.setNPli(0)
        if flag:
            self.quick_popup('Suppression du pli !', type="Succes", duree=3)
        else:
            self.quick_popup('Pas de pli sélectionné..', type="Warning", duree=3)
        self.affichePlaque()

    def monte_pli_app(self) -> None:
        """
        Méthode permettant de monter le pli sélectionné
        """
        self.__parent.modification_effectuee()
        nPliSelect = self.frame_11_bis.getNPli()
        flag = self.__parent.projet.getPlaque().montePli(nPliSelect)
        self.frame_11_bis.setNPli(0)
        if flag:
            self.quick_popup('Changement de position du pli !', type="Succes", duree=3)
        else:
            self.quick_popup('Impossible de déplacer le pli..', type="Warning", duree=3)
        self.affichePlaque()

    def descend_pli_app(self) -> None:
        """
        Méthode permettant de descendre le pli sélectionné
        """
        self.__parent.modification_effectuee()
        nPliSelect = self.frame_11_bis.getNPli()
        flag = self.__parent.projet.getPlaque().descendPli(nPliSelect)
        self.frame_11_bis.setNPli(0)
        if flag:
            self.quick_popup('Changement de position du pli !', type="Succes", duree=3)
        else:
            self.quick_popup('Impossible de déplacer le pli..', type="Warning", duree=3)
        self.affichePlaque()

    def comboBox_Materiaux_Plaque(self) -> None:
        """
        Méthode permettant la gestion de la comboBox proposant les différents Matériaux possibles pour les plis de la plaque du projet
        """
        #Proposition des matériaux dans la comboBox
        listeMateriaux=self.__parent.projet.getListeMateriaux()
        listeNomMateriaux=[]
        for k in range(0, len(listeMateriaux)):
            listeNomMateriaux.append(listeMateriaux[k].getNom())
        self.comboBoxProjetTypeMateriaux.clear()
        self.comboBoxProjetTypeMateriaux.addItems(listeNomMateriaux)

    def getProjet(self) -> Projet:
        """
        Getter renvoyant le projet associé à cet onglet
        """
        return self.__projet
