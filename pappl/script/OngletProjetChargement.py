# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtGui, QtWidgets

from script import Chargement


class OngletprojetChargement(QtWidgets.QWidget):
    """
    Classe représentant l'onglet de gestion du chargement dans un projet.
    Plusieurs chargement peuvent être définis dans un même projet.
    Un chargement courant est utilisé pour la résolution numérique.
    """

    def __init__(self, parent=None) -> None:
        """
        Constructeur de la classe OngletprojetChargement.
        """
        super(OngletprojetChargement, self).__init__()
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()
        self.maj_page_chargement()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les composants de l'onglet de gestion des chargemnts :
            - Interface d'ajout d'un chargement
                -> Nom, Nx, Ny, Txy, Mx, My et Mxy
            - Visualisation de l'ensemble des chargements disponibles
            - Modification d'un chargement pré-défini
            - Visualisation des caractéristiques du chargement courant
        """
        self.widget_projet_chargement = QtWidgets.QWidget(self)
        self.widget_projet_chargement.setObjectName("widget_projet_chargement")

        self.onglet_projet_chargement = QtWidgets.QFrame(self.widget_projet_chargement)
        self.onglet_projet_chargement.setGeometry(QtCore.QRect(0, 0, 880, 430))
        self.onglet_projet_chargement.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onglet_projet_chargement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onglet_projet_chargement.setObjectName("onglet_projet_chargement")

        ## Partie ajouter une configuration
        ### Ajout des labels statics
        self.label = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label.setGeometry(QtCore.QRect(40, 10, 211, 10))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label_2 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.label_3 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 181, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.label_4 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)

        self.label_5 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_5.setGeometry(QtCore.QRect(50, 160, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)

        self.label_6 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_6.setGeometry(QtCore.QRect(50, 190, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)

        self.label_7 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_7.setGeometry(QtCore.QRect(50, 230, 181, 20))
        self.label_7.setObjectName("label_7")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)

        self.label_8 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_8.setGeometry(QtCore.QRect(50, 260, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)

        self.label_9 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_9.setGeometry(QtCore.QRect(50, 290, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)

        self.label_10 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_10.setGeometry(QtCore.QRect(50, 320, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)

        ### Champs de texte
        self.champ_nom_nouveau_chargement = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_nom_nouveau_chargement.setGeometry(QtCore.QRect(50, 70, 181, 21))
        self.champ_nom_nouveau_chargement.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_nom_nouveau_chargement.setObjectName("champ_nom_nouveau_chargement")

        self.champ_nx_nouveau_chargement = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_nx_nouveau_chargement.setGeometry(QtCore.QRect(140, 130, 91, 21))
        self.champ_nx_nouveau_chargement.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_nx_nouveau_chargement.setObjectName("champ_nx_nouveau_chargement")

        self.champ_ny_nouveau_chargement = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_ny_nouveau_chargement.setGeometry(QtCore.QRect(140, 160, 91, 21))
        self.champ_ny_nouveau_chargement.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_ny_nouveau_chargement.setObjectName("champ_ny_nouveau_chargement")

        self.champ_txy_nouveau_chargement = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_txy_nouveau_chargement.setGeometry(QtCore.QRect(140, 190, 91, 21))
        self.champ_txy_nouveau_chargement.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_txy_nouveau_chargement.setObjectName("champ_txy_nouveau_chargement")

        self.champ_mx_nouveau_chargement = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_mx_nouveau_chargement.setGeometry(QtCore.QRect(140, 260, 91, 21))
        self.champ_mx_nouveau_chargement.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_mx_nouveau_chargement.setObjectName("champ_mx_nouveau_chargement")

        self.champ_my_nouveau_chargement = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_my_nouveau_chargement.setGeometry(QtCore.QRect(140, 290, 91, 21))
        self.champ_my_nouveau_chargement.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_my_nouveau_chargement.setObjectName("champ_my_nouveau_chargement")

        self.champ_mxy_nouveau_chargement = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_mxy_nouveau_chargement.setGeometry(QtCore.QRect(140, 320, 91, 21))
        self.champ_mxy_nouveau_chargement.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_mxy_nouveau_chargement.setObjectName("champ_mxy_nouveau_chargement")

        ### Bouton d'ajout de la nouvelle config
        self.bouton_enregistrer_nouveau_chargement = QtWidgets.QPushButton(self.onglet_projet_chargement)
        self.bouton_enregistrer_nouveau_chargement.setGeometry(QtCore.QRect(40, 360, 191, 32))
        self.bouton_enregistrer_nouveau_chargement.setStyleSheet(
            "background-color: white;border: none;color: black;")
        self.bouton_enregistrer_nouveau_chargement.setObjectName("bouton_enregistrer_nouveau_chargement")

        ## Liste des configurations existentes
        ### Labels statiques
        self.label_11 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_11.setGeometry(QtCore.QRect(290, 10, 251, 20))
        self.label_11.setObjectName("label_11")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)

        ### Boutons de gestion
        self.bouton_supprimer_chargement_selectionne = QtWidgets.QPushButton(self.onglet_projet_chargement)
        self.bouton_supprimer_chargement_selectionne.setGeometry(QtCore.QRect(290, 330, 260, 30))
        self.bouton_supprimer_chargement_selectionne.setStyleSheet(
            "background-color: white;border: none;color: black;")
        self.bouton_supprimer_chargement_selectionne.setObjectName("bouton_supprimer_chargement_selectionne")

        self.bouton_definir_chargement_courant = QtWidgets.QPushButton(self.onglet_projet_chargement)
        self.bouton_definir_chargement_courant.setGeometry(QtCore.QRect(290, 370, 260, 30))
        self.bouton_definir_chargement_courant.setStyleSheet(
            "background-color: white;border: none;color: black;")
        self.bouton_definir_chargement_courant.setObjectName("bouton_definir_chargement_courant")

        ### Liste de toutes les config disponibles
        self.liste_chargement_dispo = QtWidgets.QListView(self.onglet_projet_chargement)
        self.liste_chargement_dispo.setGeometry(QtCore.QRect(290, 40, 260, 280))
        self.liste_chargement_dispo.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.liste_chargement_dispo.setObjectName("liste_chargement_dispo")

        ## Partie modification des config enregistrées
        ### Labels statiques
        self.label_12 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_12.setGeometry(QtCore.QRect(620, 10, 210, 20))
        self.label_12.setObjectName("label_12")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)

        self.label_13 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_13.setGeometry(QtCore.QRect(590, 62, 130, 15))
        self.label_13.setObjectName("label_13")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)

        self.label_14 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_14.setGeometry(QtCore.QRect(590, 112, 130, 15))
        self.label_14.setObjectName("label_73")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)

        self.label_15 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_15.setGeometry(QtCore.QRect(590, 162, 130, 15))
        self.label_15.setObjectName("label_74")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)

        self.label_16 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_16.setGeometry(QtCore.QRect(730, 62, 130, 15))
        self.label_16.setObjectName("label_16")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)

        self.label_17 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_17.setGeometry(QtCore.QRect(730, 112, 130, 15))
        self.label_17.setObjectName("label_17")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)

        self.label_18 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_18.setGeometry(QtCore.QRect(730, 162, 130, 15))
        self.label_18.setObjectName("label_18")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)

        ## Champs de textes
        self.champ_nom_chargement_selectionne = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_nom_chargement_selectionne.setGeometry(QtCore.QRect(590, 40, 270, 20))
        self.champ_nom_chargement_selectionne.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_nom_chargement_selectionne.setObjectName("champ_nom_chargement_selectionne")

        self.champ_nx_chargement_selectionne = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_nx_chargement_selectionne.setGeometry(QtCore.QRect(590, 80, 130, 20))
        self.champ_nx_chargement_selectionne.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_nx_chargement_selectionne.setObjectName("champ_nx_chargement_selectionne")

        self.champ_ny_chargement_selectionne = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_ny_chargement_selectionne.setGeometry(QtCore.QRect(590, 130, 130, 20))
        self.champ_ny_chargement_selectionne.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_ny_chargement_selectionne.setObjectName("champ_ny_chargement_selectionne")

        self.champ_txy_chargement_selectionne = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_txy_chargement_selectionne.setGeometry(QtCore.QRect(590, 180, 130, 20))
        self.champ_txy_chargement_selectionne.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_txy_chargement_selectionne.setObjectName("champ_txy_chargement_selectionne")

        self.champ_mx_chargement_selectionne = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_mx_chargement_selectionne.setGeometry(QtCore.QRect(730, 80, 130, 20))
        self.champ_mx_chargement_selectionne.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_mx_chargement_selectionne.setObjectName("champ_mx_chargement_selectionne")

        self.champ_my_chargement_selectionne = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_my_chargement_selectionne.setGeometry(QtCore.QRect(730, 130, 130, 20))
        self.champ_my_chargement_selectionne.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_my_chargement_selectionne.setObjectName("champ_my_chargement_selectionne")

        self.champ_mxy_chargement_selectionne = QtWidgets.QLineEdit(self.onglet_projet_chargement)
        self.champ_mxy_chargement_selectionne.setGeometry(QtCore.QRect(730, 180, 130, 20))
        self.champ_mxy_chargement_selectionne.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_mxy_chargement_selectionne.setObjectName("champ_mxy_chargement_selectionne")

        # Bouton de gestion
        self.bouton_modifier_chargement_selectionne = QtWidgets.QPushButton(self.onglet_projet_chargement)
        self.bouton_modifier_chargement_selectionne.setGeometry(QtCore.QRect(590, 210, 270, 20))
        self.bouton_modifier_chargement_selectionne.setStyleSheet(
            "background-color: white;border: none;color: black;")
        self.bouton_modifier_chargement_selectionne.setObjectName("bouton_modifier_chargement_selectionne")

        ## Partie visualisation de la config courante
        ### Labels statiques
        self.label_19 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_19.setGeometry(QtCore.QRect(620, 240, 210, 20))
        self.label_19.setObjectName("label_19")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)

        self.label_20 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_20.setGeometry(QtCore.QRect(590, 290, 130, 15))
        self.label_20.setObjectName("label_20")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)

        self.label_21 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_21.setGeometry(QtCore.QRect(590, 330, 130, 15))
        self.label_21.setObjectName("label_21")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)

        self.label_22 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_22.setGeometry(QtCore.QRect(590, 370, 130, 15))
        self.label_22.setObjectName("label_22")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)

        self.label_23 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_23.setGeometry(QtCore.QRect(730, 290, 130, 15))
        self.label_23.setObjectName("label_23")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)

        self.label_24 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_24.setGeometry(QtCore.QRect(730, 330, 130, 15))
        self.label_24.setObjectName("label_24")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)

        self.label_25 = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_25.setGeometry(QtCore.QRect(730, 370, 130, 15))
        self.label_25.setObjectName("label_25")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)

        ### Labels dynamiques
        self.label_nom_chargement_courant = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_nom_chargement_courant.setGeometry(QtCore.QRect(590, 270, 270, 20))
        self.label_nom_chargement_courant.setObjectName("label_nom_chargement_courant")
        self.label_nom_chargement_courant.setAlignment(QtCore.Qt.AlignCenter)

        self.label_nx_chargement_courant = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_nx_chargement_courant.setGeometry(QtCore.QRect(590, 310, 130, 15))
        self.label_nx_chargement_courant.setObjectName("label_nx_chargement_courant")
        self.label_nx_chargement_courant.setAlignment(QtCore.Qt.AlignCenter)

        self.label_ny_chargement_courant = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_ny_chargement_courant.setGeometry(QtCore.QRect(590, 350, 130, 15))
        self.label_ny_chargement_courant.setObjectName("label_ny_chargement_courant")
        self.label_ny_chargement_courant.setAlignment(QtCore.Qt.AlignCenter)

        self.label_txy_chargement_courant = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_txy_chargement_courant.setGeometry(QtCore.QRect(590, 390, 130, 15))
        self.label_txy_chargement_courant.setObjectName("label_txy_chargement_courant")
        self.label_txy_chargement_courant.setAlignment(QtCore.Qt.AlignCenter)

        self.label_mx_chargement_courant = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_mx_chargement_courant.setGeometry(QtCore.QRect(730, 310, 130, 15))
        self.label_mx_chargement_courant.setObjectName("label_mx_chargement_courant")
        self.label_mx_chargement_courant.setAlignment(QtCore.Qt.AlignCenter)

        self.label_my_chargement_courant = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_my_chargement_courant.setGeometry(QtCore.QRect(730, 350, 130, 15))
        self.label_my_chargement_courant.setObjectName("label_my_chargement_courant")
        self.label_my_chargement_courant.setAlignment(QtCore.Qt.AlignCenter)

        self.label_mxy_chargement_courant = QtWidgets.QLabel(self.onglet_projet_chargement)
        self.label_mxy_chargement_courant.setGeometry(QtCore.QRect(730, 390, 130, 15))
        self.label_mxy_chargement_courant.setObjectName("label_mxy_chargement_courant")
        self.label_mxy_chargement_courant.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self) -> None:
        """
        Méthode permettant de mettre à jour le contenu textuel des composants.
        """
        _translate = QtCore.QCoreApplication.translate
        self.label_10.setText(_translate("onglet_projet_chargement", "Mxy (N)"))
        self.label_9.setText(_translate("onglet_projet_chargement", "My (N)"))
        self.label_8.setText(_translate("onglet_projet_chargement", "Mx (N)"))
        self.label_7.setText(_translate("onglet_projet_chargement", "MOMENT"))
        self.label_6.setText(_translate("onglet_projet_chargement", "Txy (N/mm)"))
        self.label_5.setText(_translate("onglet_projet_chargement", "Ny (N/mm)"))
        self.label_4.setText(_translate("onglet_projet_chargement", "Nx (N/mm)"))
        self.label_3.setText(_translate("onglet_projet_chargement", "FLUX D'EFFORT"))
        self.label_2.setText(_translate("onglet_projet_chargement", "Nom de la configuration"))
        self.label.setText(_translate("onglet_projet_chargement", "AJOUTER UNE CONFIGURATION"))
        self.label_18.setText(_translate("onglet_projet_chargement", "Mxy (N)"))
        self.label_17.setText(_translate("onglet_projet_chargement", "My (N)"))
        self.label_16.setText(_translate("onglet_projet_chargement", "Mx (N)"))
        self.label_15.setText(_translate("onglet_projet_chargement", "Txy (N/mm)"))
        self.label_14.setText(_translate("onglet_projet_chargement", "Ny (N/mm)"))
        self.label_13.setText(_translate("onglet_projet_chargement", "Nx (N/mm)"))
        self.label_12.setText(_translate("onglet_projet_chargement", "CONFIGURATION SELECTIONNÉE"))
        self.bouton_definir_chargement_courant.setText(
            _translate("onglet_projet_chargement", "DÉFINIR COMME CONFIG COURANTE"))
        self.bouton_supprimer_chargement_selectionne.setText(
            _translate("onglet_projet_chargement", "SUPPRIMER LA CONFIG"))
        self.label_11.setText(_translate("onglet_projet_chargement", "CONFIGURATIONS ENREGISTRÉES"))
        self.bouton_enregistrer_nouveau_chargement.setText(
            _translate("onglet_projet_chargement", "ENREGISTRER LA CONFIG"))
        self.label_25.setText(_translate("onglet_projet_chargement", "Mxy (N)"))
        self.label_24.setText(_translate("onglet_projet_chargement", "My (N)"))
        self.label_23.setText(_translate("onglet_projet_chargement", "Mx (N)"))
        self.label_22.setText(_translate("onglet_projet_chargement", "Txy (N/mm)"))
        self.label_21.setText(_translate("onglet_projet_chargement", "Ny (N/mm)"))
        self.label_20.setText(_translate("onglet_projet_chargement", "Nx (N/mm)"))
        self.label_19.setText(_translate("onglet_projet_chargement", "CONFIGURATION COURANTE"))
        self.bouton_modifier_chargement_selectionne.setText(
            _translate("onglet_projet_chargement", "MODIFIER LA CONFIG SELECTIONNÉE"))

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def reset_style_ajout_chargement(self) -> None:
        """
        Méthode pour remettre le style par défaut des champs d'ajout d'un chargement.
        """
        default_stylesheet = "background-color:white; color:black; border:none;"
        self.champ_nom_nouveau_chargement.setStyleSheet(default_stylesheet)
        self.champ_nx_nouveau_chargement.setStyleSheet(default_stylesheet)
        self.champ_ny_nouveau_chargement.setStyleSheet(default_stylesheet)
        self.champ_txy_nouveau_chargement.setStyleSheet(default_stylesheet)
        self.champ_mx_nouveau_chargement.setStyleSheet(default_stylesheet)
        self.champ_my_nouveau_chargement.setStyleSheet(default_stylesheet)
        self.champ_mxy_nouveau_chargement.setStyleSheet(default_stylesheet)

    def reset_style_modif_chargement(self) -> None:
        """
        Méthode pour vider les contenues des champs de modification d'un chargement.
        """
        default_stylesheet = "background-color:white; color:black; border:none;"
        self.champ_nom_chargement_selectionne.setStyleSheet(default_stylesheet)
        self.champ_nx_chargement_selectionne.setStyleSheet(default_stylesheet)
        self.champ_ny_chargement_selectionne.setStyleSheet(default_stylesheet)
        self.champ_txy_chargement_selectionne.setStyleSheet(default_stylesheet)
        self.champ_mx_chargement_selectionne.setStyleSheet(default_stylesheet)
        self.champ_my_chargement_selectionne.setStyleSheet(default_stylesheet)
        self.champ_mxy_chargement_selectionne.setStyleSheet(default_stylesheet)

    def reset_content_ajout_chargement(self):
        """
        Méthode pour vider le contenu des champs d'ajout d'un nouveau chargement.
        """
        _translate = QtCore.QCoreApplication.translate
        self.champ_nom_nouveau_chargement.setText(_translate("onglet_projet_chargement", ""))
        self.champ_nx_nouveau_chargement.setText(_translate("onglet_projet_chargement", ""))
        self.champ_ny_nouveau_chargement.setText(_translate("onglet_projet_chargement", ""))
        self.champ_txy_nouveau_chargement.setText(_translate("onglet_projet_chargement", ""))
        self.champ_mx_nouveau_chargement.setText(_translate("onglet_projet_chargement", ""))
        self.champ_my_nouveau_chargement.setText(_translate("onglet_projet_chargement", ""))
        self.champ_mxy_nouveau_chargement.setText(_translate("onglet_projet_chargement", ""))

    def verif_input_nouveau_chargement(self,
                                       nom: str,
                                       nx: str, ny: str, txy: str,
                                       mx: str, my: str, mxy: str) -> bool:
        """
        Méthode pour vérifier le contenu des champs d'ajout d'un nouveau chargement et mettre en valeur les champs contenant des erreurs.

        :param nom: Le nom du nouveau chargement (Usage : non vide)
        :param nx: La valeur de Nx (Usage : nombre float)
        :param ny: La valeur de Ny (Usage : nombre float)
        :param txy: La valeur de Txy (Usage : nombre float)
        :param mx: La valeur de Mx (Usage : nombre float)
        :param my: La valeur de My (Usage : nombre float)
        :param mxy: La valeur de Mxy (Usage : nombre float)
        :return: True si le chargements est conforme, False sinon.
        """
        flag = True
        error_stylesheet = "background-color:darkred; color:white; border:none;"
        if str(nom).strip() == "":
            self.champ_nom_nouveau_chargement.setText(QtCore.QCoreApplication.translate("onglet_projet_chargement", ""))
            self.champ_nom_nouveau_chargement.setStyleSheet(error_stylesheet)
            flag = False
        try:
            nx = float(nx)
        except:
            self.champ_nx_nouveau_chargement.setStyleSheet(error_stylesheet)
            flag = False
        try:
            ny = float(ny)
        except:
            self.champ_ny_nouveau_chargement.setStyleSheet(error_stylesheet)
            flag = False
        try:
            txy = float(txy)
        except:
            self.champ_txy_nouveau_chargement.setStyleSheet(error_stylesheet)
            flag = False
        try:
            mx = float(mx)
        except:
            self.champ_mx_nouveau_chargement.setStyleSheet(error_stylesheet)
            flag = False
        try:
            my = float(my)
        except:
            self.champ_my_nouveau_chargement.setStyleSheet(error_stylesheet)
            flag = False
        try:
            mxy = float(mxy)
        except:
            self.champ_mxy_nouveau_chargement.setStyleSheet(error_stylesheet)
            flag = False
        return flag

    def verif_input_modif_chargement(self,
                                     nom: str,
                                     nx: str, ny: str, txy: str,
                                     mx: str, my: str, mxy: str) -> bool:
        """
        Méthode pour vérifier le contenu des champs de modification d'un chargement et mettre en valeur les champs contenant des erreurs.

        :param nom: Le nom du nouveau chargement (Usage : non vide)
        :param nx: La valeur de Nx (Usage : nombre float)
        :param ny: La valeur de Ny (Usage : nombre float)
        :param txy: La valeur de Txy (Usage : nombre float)
        :param mx: La valeur de Mx (Usage : nombre float)
        :param my: La valeur de My (Usage : nombre float)
        :param mxy: La valeur de Mxy (Usage : nombre float)
        :return: True si le chargements est conforme, False sinon.
        """
        flag = True
        error_stylesheet = "background-color:darkred; color:white; border:none;"
        if str(nom).strip() == "":
            self.champ_nom_chargement_selectionne.setText(
                QtCore.QCoreApplication.translate("onglet_projet_chargement", ""))
            self.champ_nom_chargement_selectionne.setStyleSheet(error_stylesheet)
            flag = False
        try:
            nx = float(nx)
        except:
            self.champ_nx_chargement_selectionne.setStyleSheet(error_stylesheet)
            flag = False
        try:
            ny = float(ny)
        except:
            self.champ_ny_chargement_selectionne.setStyleSheet(error_stylesheet)
            flag = False
        try:
            txy = float(txy)
        except:
            self.champ_txy_chargement_selectionne.setStyleSheet(error_stylesheet)
            flag = False
        try:
            mx = float(mx)
        except:
            self.champ_mx_chargement_selectionne.setStyleSheet(error_stylesheet)
            flag = False
        try:
            my = float(my)
        except:
            self.champ_my_chargement_selectionne.setStyleSheet(error_stylesheet)
            flag = False
        try:
            mxy = float(mxy)
        except:
            self.champ_mxy_chargement_selectionne.setStyleSheet(error_stylesheet)
            flag = False
        return flag

    def reset_content_chargement_selectionne(self,
                                             chargement: Chargement = None) -> None:
        """
        Méthode pour mettre à jour le contenu des champs de modification du chargement en fonction du chargmeent selectionné.
        Si aucun chargement n'est selectionné, cette méthode peut être utilisée avec None, pour vider les champs.

        :param chargement: Le chargement à mettre en valeur dans les champs.
        """
        _translate = QtCore.QCoreApplication.translate
        if chargement is None:
            self.champ_nom_chargement_selectionne.setText(_translate("onglet_projet_chargement", ""))
            self.champ_nx_chargement_selectionne.setText(_translate("onglet_projet_chargement", ""))
            self.champ_ny_chargement_selectionne.setText(_translate("onglet_projet_chargement", ""))
            self.champ_txy_chargement_selectionne.setText(_translate("onglet_projet_chargement", ""))
            self.champ_mx_chargement_selectionne.setText(_translate("onglet_projet_chargement", ""))
            self.champ_my_chargement_selectionne.setText(_translate("onglet_projet_chargement", ""))
            self.champ_mxy_chargement_selectionne.setText(_translate("onglet_projet_chargement", ""))
        else:
            self.champ_nom_chargement_selectionne.setText(_translate("onglet_projet_chargement", chargement.getNom()))
            self.champ_nx_chargement_selectionne.setText(
                _translate("onglet_projet_chargement", str(chargement.getNx())))
            self.champ_ny_chargement_selectionne.setText(
                _translate("onglet_projet_chargement", str(chargement.getNy())))
            self.champ_txy_chargement_selectionne.setText(
                _translate("onglet_projet_chargement", str(chargement.getTxy())))
            self.champ_mx_chargement_selectionne.setText(
                _translate("onglet_projet_chargement", str(chargement.getMx())))
            self.champ_my_chargement_selectionne.setText(
                _translate("onglet_projet_chargement", str(chargement.getMy())))
            self.champ_mxy_chargement_selectionne.setText(
                _translate("onglet_projet_chargement", str(chargement.getMxy())))

    def maj_page_chargement(self) -> None:
        """
        Méthode permettant de mettre à jour le contenu textuel et la liste des chargements disponibles dans le projet sur la page.
        """
        self.reset_content_chargement_selectionne()
        _translate = QtCore.QCoreApplication.translate
        if self.__parent.projet.getChargementCourantIndex() == -1:
            self.label_nom_chargement_courant.setText(_translate("onglet_projet_chargement", "AUCUN CHARGEMENT"))
            self.label_nx_chargement_courant.setText(_translate("onglet_projet_chargement", "NA"))
            self.label_ny_chargement_courant.setText(_translate("onglet_projet_chargement", "NA"))
            self.label_txy_chargement_courant.setText(_translate("onglet_projet_chargement", "NA"))
            self.label_mx_chargement_courant.setText(_translate("onglet_projet_chargement", "NA"))
            self.label_my_chargement_courant.setText(_translate("onglet_projet_chargement", "NA"))
            self.label_mxy_chargement_courant.setText(_translate("onglet_projet_chargement", "NA"))
        else:
            chargement_courant = self.__parent.projet.getChargementCourant()
            self.label_nom_chargement_courant.setText(
                _translate("onglet_projet_chargement", str(chargement_courant.getNom())))
            self.label_nx_chargement_courant.setText(
                _translate("onglet_projet_chargement", str(chargement_courant.getNx())))
            self.label_ny_chargement_courant.setText(
                _translate("onglet_projet_chargement", str(chargement_courant.getNy())))
            self.label_txy_chargement_courant.setText(
                _translate("onglet_projet_chargement", str(chargement_courant.getTxy())))
            self.label_mx_chargement_courant.setText(
                _translate("onglet_projet_chargement", str(chargement_courant.getMx())))
            self.label_my_chargement_courant.setText(
                _translate("onglet_projet_chargement", str(chargement_courant.getMy())))
            self.label_mxy_chargement_courant.setText(
                _translate("onglet_projet_chargement", str(chargement_courant.getMxy())))

        # Mise à jour de la liste de toutes les configurations possibles
        modele_chargements_possibles = QtGui.QStandardItemModel()
        self.liste_chargement_dispo.setModel(modele_chargements_possibles)
        for chargement in self.__parent.projet.getListeChargementsPossibles():
            entree = QtGui.QStandardItem(str(chargement.getNom()))
            modele_chargements_possibles.appendRow(entree)

    def affiche_info_chargement_selectionne(self) -> None:
        """
        Méthode pour afficher les informations du chargement selectionné dans la liste des chargements disponibles.
        """
        index = self.liste_chargement_dispo.currentIndex().row()
        if index >= 0:
            chargement_sel = self.__parent.projet.getListeChargementsPossibles()[index]
            self.reset_content_chargement_selectionne(chargement=chargement_sel)
        else:
            self.reset_content_chargement_selectionne()

    def enregistre_chargement(self) -> None:
        """
        Méthode pour enregistrer un chargement dans le projet.
        """
        self.reset_style_ajout_chargement()
        nom_chargement = self.champ_nom_nouveau_chargement.text()
        nx_chargement = self.champ_nx_nouveau_chargement.text()
        ny_chargement = self.champ_ny_nouveau_chargement.text()
        txy_chargement = self.champ_txy_nouveau_chargement.text()
        mx_chargement = self.champ_mx_nouveau_chargement.text()
        my_chargement = self.champ_my_nouveau_chargement.text()
        mxy_chargement = self.champ_mxy_nouveau_chargement.text()

        flag = self.verif_input_nouveau_chargement(nom_chargement,
                                                   ny_chargement, ny_chargement, txy_chargement,
                                                   mx_chargement, my_chargement, mxy_chargement)

        if flag:
            nouveau_chargement = Chargement.Chargement(nom=nom_chargement,
                                                       nx=nx_chargement,
                                                       ny=ny_chargement,
                                                       txy=txy_chargement,
                                                       mx=mx_chargement,
                                                       my=my_chargement,
                                                       mxy=mxy_chargement)
            self.__parent.projet.ajouteChargementPossible(nouveau_chargement)
            self.quick_popup("Chargement ajouté!", type="Succes", duree=3)
            self.reset_content_ajout_chargement()
            self.maj_page_chargement()
            self.liste_chargement_dispo.selectionModel().currentChanged.connect(
                self.affiche_info_chargement_selectionne)

            # La sauvegarde du projet n'est plus à jour
            self.__parent.modification_effectuee()
        else:
            self.quick_popup("Des valeurs sont manquantes ou éronnées...", type="Error", duree=3)

    def supprime_chargement(self) -> None:
        """
        Méthode pour supprimer un chargement du projet.
        """
        index = self.liste_chargement_dispo.currentIndex().row()
        if index >= 0:
            self.__parent.projet.removeChargementPossibleAtIndex(index)
            self.maj_page_chargement()
            # La sauvegarde du projet n'est plus à jour
            self.__parent.modification_effectuee()
            self.quick_popup("Chargement supprimé!", type="Succes", duree=3)
        else:
            self.quick_popup("Aucun chargement sélectionné!", type="Warning", duree=3)

    def modif_chargement(self) -> None:
        """
        Méthode pour modifier un chargement du projet.
        :return:
        """
        index = self.liste_chargement_dispo.currentIndex().row()
        if index >= 0:
            self.reset_style_modif_chargement()

            nom_chargement = self.champ_nom_chargement_selectionne.text()
            nx_chargement = self.champ_nx_chargement_selectionne.text()
            ny_chargement = self.champ_ny_chargement_selectionne.text()
            txy_chargement = self.champ_txy_chargement_selectionne.text()
            mx_chargement = self.champ_mx_chargement_selectionne.text()
            my_chargement = self.champ_my_chargement_selectionne.text()
            mxy_chargement = self.champ_mxy_chargement_selectionne.text()

            flag = self.verif_input_modif_chargement(nom_chargement,
                                                     nx_chargement, ny_chargement, txy_chargement,
                                                     mx_chargement, my_chargement, mxy_chargement)

            if flag:
                self.__parent.projet.getListeChargementsPossibles()[index] = Chargement.Chargement(nom=nom_chargement,
                                                                                                   nx=nx_chargement,
                                                                                                   ny=ny_chargement,
                                                                                                   txy=txy_chargement,
                                                                                                   mx=mx_chargement,
                                                                                                   my=my_chargement,
                                                                                                   mxy=mxy_chargement)
                self.quick_popup("Chargement modifié!", type="Succes", duree=3)
                self.maj_page_chargement()
                # La sauvegarde du projet n'est plus à jour
                self.__parent.modification_effectuee()
                self.liste_chargement_dispo.selectionModel().currentChanged.connect(
                    self.affiche_info_chargement_selectionne)
        else:
            self.quick_popup("Aucun chargement selectionné!", type="Warning", duree=3)

    def change_chargement_courant(self) -> None:
        """
        Méthode permettant de changer le chargement courant utiliser pour la résolution du problème.
        """
        index = self.liste_chargement_dispo.currentIndex().row()
        if index >= 0:
            try:
                self.__parent.projet.setChargementCourant(index)
                self.maj_page_chargement()
                self.quick_popup("Chargement courant modifié!", type="Succes", duree=3)
                self.liste_chargement_dispo.selectionModel().currentChanged.connect(
                    self.affiche_info_chargement_selectionne)
                # La sauvegarde du projet n'est plus à jour
                self.__parent.modification_effectuee()
            except IndexError:
                self.quick_popup("Une erreur est survenue.", type="Error", duree=3)
        else:
            self.quick_popup("Aucun chargement sélectionné!", type="Warning", duree=3)

    def initActions(self) -> None:
        """
        Méthode permettant de connecter les actions aux différents bouton de l'interface.
        """
        self.bouton_enregistrer_nouveau_chargement.clicked.connect(self.enregistre_chargement)
        self.bouton_supprimer_chargement_selectionne.clicked.connect(self.supprime_chargement)
        self.bouton_modifier_chargement_selectionne.clicked.connect(self.modif_chargement)
        self.bouton_definir_chargement_courant.clicked.connect(self.change_chargement_courant)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = OngletprojetChargement()
    tmp.setStyleSheet("background-color: rgb(224, 224, 224)")
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
