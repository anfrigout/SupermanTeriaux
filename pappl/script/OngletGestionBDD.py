# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtGui, QtWidgets

from script import Materiau
from script import DatabaseTools


class OngletGestionBDD(QtWidgets.QWidget):
    """
    Classe représentant l'onglet de gestion de la base de données dans l'interface.
    """

    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe OngletGestionBDD.
        """
        super(OngletGestionBDD, self).__init__(parent)
        self.__parent = parent
        self.__bdd_recherche_index = None
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les composants de l'onglet gestion de la base de données :
            - Interface de recherche dans la base de données
                -> Champ de recherche sur les champs nom et référence.
                -> Affichage de l'ensemble des résultats correspondants
                -> Fiche du matériau selectionné lors de la selection dans la liste des résultats
            - Interface d'ajout
                -> Nom, Ref, E1, E2, G12, v12, s11c, s22c, s11t, s22t, s12 et %age de fibre
        """
        self.widget_materiaux_bdd = QtWidgets.QWidget(self)
        self.widget_materiaux_bdd.setObjectName("widget_materiaux_bdd")

        self.onglet_materiaux_bdd = QtWidgets.QFrame(self.widget_materiaux_bdd)
        self.onglet_materiaux_bdd.setGeometry(QtCore.QRect(0, 0, 881, 421))
        self.onglet_materiaux_bdd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onglet_materiaux_bdd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onglet_materiaux_bdd.setObjectName("onglet_materiaux_bdd")

        self.label = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label.setGeometry(QtCore.QRect(50, 20, 131, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : black;")

        self.champ_recherche_materiaux = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_recherche_materiaux.setGeometry(QtCore.QRect(40, 40, 331, 21))
        self.champ_recherche_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);border:none;color:black;")
        self.champ_recherche_materiaux.setText("")
        self.champ_recherche_materiaux.setObjectName("champ_recherche_materiaux")

        self.liste_materiaux_correspondant = QtWidgets.QListView(self.onglet_materiaux_bdd)
        self.liste_materiaux_correspondant.setGeometry(QtCore.QRect(40, 70, 331, 131))
        self.liste_materiaux_correspondant.setStyleSheet(
            "background-color: rgb(255, 255, 255);border:none;color:black;")
        self.liste_materiaux_correspondant.setObjectName("liste_materiaux_correspondant")

        self.label_2 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 241, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color : black;")

        self.fenetre_fiche_materiau_selectionne = QtWidgets.QFrame(self.onglet_materiaux_bdd)
        self.fenetre_fiche_materiau_selectionne.setGeometry(QtCore.QRect(40, 240, 331, 161))
        self.fenetre_fiche_materiau_selectionne.setStyleSheet("background-color:rgb(255,255,255);border:none;")
        self.fenetre_fiche_materiau_selectionne.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fenetre_fiche_materiau_selectionne.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fenetre_fiche_materiau_selectionne.setObjectName("fenetre_fiche_materiau_selectionne")

        self.label_3 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 271, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color : black;")

        self.label_4 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_4.setGeometry(QtCore.QRect(430, 50, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color : black;")

        self.champ_nom_materiau = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_nom_materiau.setGeometry(QtCore.QRect(430, 70, 411, 21))
        self.champ_nom_materiau.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_nom_materiau.setObjectName("champ_nom_materiau")

        self.label_5 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_5.setGeometry(QtCore.QRect(430, 100, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color : black;")

        self.champ_reference_materiau = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_reference_materiau.setGeometry(QtCore.QRect(430, 120, 411, 21))
        self.champ_reference_materiau.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_reference_materiau.setObjectName("champ_reference_materiau")

        self.label_6 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_6.setGeometry(QtCore.QRect(440, 150, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color : black;")

        self.champ_e1 = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_e1.setGeometry(QtCore.QRect(430, 170, 81, 21))
        self.champ_e1.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_e1.setObjectName("champ_e1")

        self.label_7 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_7.setGeometry(QtCore.QRect(550, 150, 60, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color : black;")

        self.champ_e2 = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_e2.setGeometry(QtCore.QRect(540, 170, 81, 21))
        self.champ_e2.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_e2.setObjectName("champ_e2")

        self.label_8 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_8.setGeometry(QtCore.QRect(660, 150, 81, 16))
        self.label_8.setObjectName("label_810")
        self.label_8.setStyleSheet("color : black;")

        self.champ_g12 = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_g12.setGeometry(QtCore.QRect(650, 170, 81, 21))
        self.champ_g12.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_g12.setObjectName("champ_g12")

        self.label_9 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_9.setGeometry(QtCore.QRect(770, 150, 60, 16))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("color : black;")

        self.champ_v12 = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_v12.setGeometry(QtCore.QRect(760, 170, 81, 21))
        self.champ_v12.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_v12.setObjectName("champ_v12")

        self.label_10 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_10.setGeometry(QtCore.QRect(440, 200, 171, 16))
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("color : black;")

        self.champ_s11c = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_s11c.setGeometry(QtCore.QRect(430, 250, 81, 21))
        self.champ_s11c.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_s11c.setObjectName("champ_s11c")

        self.label_11 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_11.setGeometry(QtCore.QRect(450, 230, 41, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("color : black;")

        self.champ_s22c = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_s22c.setGeometry(QtCore.QRect(540, 250, 81, 21))
        self.champ_s22c.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_s22c.setObjectName("champ_s22c")

        self.label_12 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_12.setGeometry(QtCore.QRect(560, 230, 41, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet("color : black;")

        self.champ_s11t = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_s11t.setGeometry(QtCore.QRect(650, 250, 81, 21))
        self.champ_s11t.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_s11t.setObjectName("champ_s11t")

        self.label_13 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_13.setGeometry(QtCore.QRect(670, 200, 171, 16))
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet("color : black;")

        self.champ_s22t = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_s22t.setGeometry(QtCore.QRect(760, 250, 81, 21))
        self.champ_s22t.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_s22t.setObjectName("champS22_t")

        self.label_14 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_14.setGeometry(QtCore.QRect(780, 230, 41, 16))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_146")
        self.label_14.setStyleSheet("color : black;")

        self.champ_pourcentage_fibre = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_pourcentage_fibre.setGeometry(QtCore.QRect(430, 300, 191, 21))
        self.champ_pourcentage_fibre.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_pourcentage_fibre.setObjectName("champ_pourcentage_fibre")

        self.label_15 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_15.setGeometry(QtCore.QRect(670, 230, 41, 16))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet("color : black;")

        self.champ_s12 = QtWidgets.QLineEdit(self.onglet_materiaux_bdd)
        self.champ_s12.setGeometry(QtCore.QRect(650, 300, 81, 21))
        self.champ_s12.setStyleSheet("background-color: rgb(255, 255, 255);color:black;border:none;")
        self.champ_s12.setObjectName("champ_s12")

        self.label_16 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_16.setGeometry(QtCore.QRect(430, 280, 171, 16))
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet("color : black;")

        self.label_17 = QtWidgets.QLabel(self.onglet_materiaux_bdd)
        self.label_17.setGeometry(QtCore.QRect(660, 280, 171, 16))
        self.label_17.setObjectName("label_17")
        self.label_17.setStyleSheet("color : black;")

        self.bouton_ajouter_materiau = QtWidgets.QPushButton(self.onglet_materiaux_bdd)
        self.bouton_ajouter_materiau.setGeometry(QtCore.QRect(430, 340, 411, 31))
        self.bouton_ajouter_materiau.setStyleSheet(
            "background-color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);")
        self.bouton_ajouter_materiau.setDefault(False)
        self.bouton_ajouter_materiau.setObjectName("bouton_ajouter_materiau")

        self.label_nom_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_nom_selectionne.setGeometry(QtCore.QRect(10, 5, 310, 12))
        self.label_nom_selectionne.setObjectName("label_nom_selectionne")
        self.label_nom_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_ref_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_ref_selectionne.setGeometry(QtCore.QRect(10, 17, 310, 12))
        self.label_ref_selectionne.setObjectName("label_ref_selectionne")
        self.label_ref_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_fibre_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_fibre_selectionne.setGeometry(QtCore.QRect(10, 29, 310, 12))
        self.label_fibre_selectionne.setObjectName("label_fibre_selectionne")
        self.label_fibre_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_e1_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_e1_selectionne.setGeometry(QtCore.QRect(10, 41, 310, 12))
        self.label_e1_selectionne.setObjectName("label_e1_selectionne")
        self.label_e1_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_e2_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_e2_selectionne.setGeometry(QtCore.QRect(10, 53, 310, 12))
        self.label_e2_selectionne.setObjectName("label_e2_selectionne")
        self.label_e2_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_g12_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_g12_selectionne.setGeometry(QtCore.QRect(10, 65, 310, 12))
        self.label_g12_selectionne.setObjectName("label_g12_selectionne")
        self.label_g12_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_v12_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_v12_selectionne.setGeometry(QtCore.QRect(10, 77, 310, 12))
        self.label_v12_selectionne.setObjectName("label_v12_selectionne")
        self.label_v12_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_s11c_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_s11c_selectionne.setGeometry(QtCore.QRect(10, 89, 310, 12))
        self.label_s11c_selectionne.setObjectName("label_s11c_selectionne")
        self.label_s11c_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_s22c_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_s22c_selectionne.setGeometry(QtCore.QRect(10, 101, 310, 12))
        self.label_s22c_selectionne.setObjectName("label_s22c_selectionne")
        self.label_s22c_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_s11t_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_s11t_selectionne.setGeometry(QtCore.QRect(10, 113, 310, 12))
        self.label_s11t_selectionne.setObjectName("label_s11t_selectionne")
        self.label_s11t_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_s22t_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_s22t_selectionne.setGeometry(QtCore.QRect(10, 125, 310, 12))
        self.label_s22t_selectionne.setObjectName("label_s22t_selectionne")
        self.label_s22t_selectionne.setStyleSheet("color : black;font-size:10px;")

        self.label_s12_selectionne = QtWidgets.QLabel(self.fenetre_fiche_materiau_selectionne)
        self.label_s12_selectionne.setGeometry(QtCore.QRect(10, 137, 310, 12))
        self.label_s12_selectionne.setObjectName("label_s12_selectionne")
        self.label_s12_selectionne.setStyleSheet("color : black;font-size:10px;")

    def retranslateUi(self) -> None:
        """
        Méthode permettant de mettre à jour le contenu textuel des composants
        """

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("onglet_materiaux_bdd", "Recherche matériau"))
        self.label_2.setText(_translate("onglet_materiaux_bdd", "Fiche du matériau sélectionné"))
        self.label_3.setText(_translate("onglet_materiaux_bdd", "Ajout d\'un matériau à la base de données"))
        self.label_4.setText(_translate("onglet_materiaux_bdd", "Nom du matériau"))
        self.label_5.setText(_translate("onglet_materiaux_bdd", "Référence du matériau"))
        self.label_6.setText(_translate("onglet_materiaux_bdd", "E1 (MPa)"))
        self.label_7.setText(_translate("onglet_materiaux_bdd", "E2 (MPa)"))
        self.label_8.setText(_translate("onglet_materiaux_bdd", "G12 (MPa)"))
        self.label_9.setText(_translate("onglet_materiaux_bdd", "v12 (MPa)"))
        self.label_10.setText(_translate("onglet_materiaux_bdd", "Sigma compression (MPa)"))
        self.label_11.setText(_translate("onglet_materiaux_bdd", "s11_c"))
        self.label_12.setText(_translate("onglet_materiaux_bdd", "s22_c"))
        self.label_13.setText(_translate("onglet_materiaux_bdd", "Sigma traction (MPa)"))
        self.label_14.setText(_translate("onglet_materiaux_bdd", "s22_t"))
        self.label_15.setText(_translate("onglet_materiaux_bdd", "s11_t"))
        self.label_16.setText(_translate("onglet_materiaux_bdd", "Pourcentage de fibre "))
        self.label_17.setText(_translate("onglet_materiaux_bdd", "s12 (MPa)"))
        self.label_nom_selectionne.setText(_translate("onglet_materiaux_bdd", "Nom : "))
        self.label_ref_selectionne.setText(_translate("onglet_materiaux_bdd", "Ref : "))
        self.label_fibre_selectionne.setText(_translate("onglet_materiaux_bdd", "Pourcentage fibre : "))
        self.label_e1_selectionne.setText(_translate("onglet_materiaux_bdd", "E1 (MPa) : "))
        self.label_e2_selectionne.setText(_translate("onglet_materiaux_bdd", "E2 (MPa) : "))
        self.label_g12_selectionne.setText(_translate("onglet_materiaux_bdd", "G12 (MPa) : "))
        self.label_v12_selectionne.setText(_translate("onglet_materiaux_bdd", "v12 (MPa) : "))
        self.label_s11c_selectionne.setText(_translate("onglet_materiaux_bdd", "s11c (MPa) : "))
        self.label_s22c_selectionne.setText(_translate("onglet_materiaux_bdd", "s22c (MPa) : "))
        self.label_s11t_selectionne.setText(_translate("onglet_materiaux_bdd", "s11t (MPa) : "))
        self.label_s22t_selectionne.setText(_translate("onglet_materiaux_bdd", "s22t (MPa) : "))
        self.label_s12_selectionne.setText(_translate("onglet_materiaux_bdd", "s12 (MPa) : "))
        self.bouton_ajouter_materiau.setText(_translate("onglet_materiaux_bdd", "AJOUTER"))

    def maj_label_selectionne(self,
                              carac: list[str] = None) -> None:
        """
        Méthode pour remettre par défaut l'ensemble des champs d'un matériau selectionné.

        :param mat: Le matériau d'où extraire les information. None pour reset les champs.
        """

        _translate = QtCore.QCoreApplication.translate
        if carac is None:
            self.fenetre_fiche_materiau_selectionne.setStyleSheet("background-color:lightgrey;color:black;border:none;")
            self.label_nom_selectionne.setText(_translate("onglet_materiaux_bdd", "Nom : "))
            self.label_ref_selectionne.setText(_translate("onglet_materiaux_bdd", "Ref : "))
            self.label_fibre_selectionne.setText(_translate("onglet_materiaux_bdd", "Pourcentage fibre : "))
            self.label_e1_selectionne.setText(_translate("onglet_materiaux_bdd", "E1 (MPa) : "))
            self.label_e2_selectionne.setText(_translate("onglet_materiaux_bdd", "E2 (MPa) : "))
            self.label_g12_selectionne.setText(_translate("onglet_materiaux_bdd", "G12 (MPa) : "))
            self.label_v12_selectionne.setText(_translate("onglet_materiaux_bdd", "v12 (MPa) : "))
            self.label_s11c_selectionne.setText(_translate("onglet_materiaux_bdd", "s11c (MPa) : "))
            self.label_s22c_selectionne.setText(_translate("onglet_materiaux_bdd", "s22c (MPa) : "))
            self.label_s11t_selectionne.setText(_translate("onglet_materiaux_bdd", "s11t (MPa) : "))
            self.label_s22t_selectionne.setText(_translate("onglet_materiaux_bdd", "s22t (MPa) : "))
            self.label_s12_selectionne.setText(_translate("onglet_materiaux_bdd", "s12 (MPa) : "))
        else:
            self.fenetre_fiche_materiau_selectionne.setStyleSheet("background-color:white;color:black;border:none;")
            self.label_nom_selectionne.setText(_translate("onglet_materiaux_bdd", "Nom : " + carac[0]))
            self.label_ref_selectionne.setText(_translate("onglet_materiaux_bdd", "Ref : " + carac[1]))
            self.label_fibre_selectionne.setText(
                _translate("onglet_materiaux_bdd", "Pourcentage fibre : " + carac[11]))
            self.label_e1_selectionne.setText(_translate("onglet_materiaux_bdd", "E1 (MPa) : " + carac[2]))
            self.label_e2_selectionne.setText(_translate("onglet_materiaux_bdd", "E2 (MPa) : " + carac[3]))
            self.label_g12_selectionne.setText(_translate("onglet_materiaux_bdd", "G12 (MPa) : " + carac[4]))
            self.label_v12_selectionne.setText(_translate("onglet_materiaux_bdd", "v12 (MPa) : " + carac[5]))
            self.label_s11c_selectionne.setText(_translate("onglet_materiaux_bdd", "s11c (MPa) : " + carac[6]))
            self.label_s22c_selectionne.setText(_translate("onglet_materiaux_bdd", "s22c (MPa) : " + carac[7]))
            self.label_s11t_selectionne.setText(_translate("onglet_materiaux_bdd", "s11t (MPa) : " + carac[8]))
            self.label_s22t_selectionne.setText(_translate("onglet_materiaux_bdd", "s22t (MPa) : " + carac[9]))
            self.label_s12_selectionne.setText(_translate("onglet_materiaux_bdd", "s12 (MPa) : " + carac[10]))

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def reset_background_ajout(self) -> None:
        """
        Méthode permettant de remettre le style des champs d'ajout de matériaux au style par défaut.
        """
        defaut_stylesheet = "background-color:white;border:none;color:black;"
        self.champ_nom_materiau.setStyleSheet(defaut_stylesheet)
        self.champ_reference_materiau.setStyleSheet(defaut_stylesheet)
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
        Méthode permettant de vider le contenu des champs d'ajout de matériaux.
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        self.champ_nom_materiau.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_reference_materiau.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_e1.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_e2.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_g12.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_v12.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_s11c.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_s22c.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_s11t.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_s22t.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_s12.setText(_translate("onglet_materiaux_bdd", ""))
        self.champ_pourcentage_fibre.setText(_translate("onglet_materiaux_bdd", ""))

    def verif_input_ajout(self, nom: str, ref: str,
                          e1: str, e2: str,
                          g12: str,
                          v12: str,
                          s11_c: str, s22_c: str,
                          s11_t: str, s22_t: str,
                          s12: str,
                          fibre: str) -> bool:
        """
        Méthode permettant de vérifier le contenu des champs d'ajout de matériaux et de mettre en évidence les valeurs manquantes ou éronnées.

        :param nom: Le nom du matériau à vérifier (Usage : non vide)
        :param ref: La réference du matériau à vérifier (Usage : non vide)
        :param e1: La valeur de E1 (Usage : float)
        :param e2: La valeur de E2 (Usage : float)
        :param g12: La valeur de G12 (Usage : float)
        :param v12: La valeur de v12 (Usage : float)
        :param s11_c: La valeur de s11 en compréssion (Usage : float)
        :param s22_c: La valeur de s22 en compréssion (Usage : float)
        :param s11_t: La valeur de s11 en traction (Usage : float)
        :param s22_t: La valeur de s22 en traction (Usage : float)
        :param s12: La valeur de s12 (Usage : float)
        :param fibre: La valeur du pourcentage de fibre (Usage : 100 ≥ float ≥ 0)
        :return: True si les champs sont correctes, False si un problème est detecté.
        """
        flag = True
        error_champ_stylesheet = "background-color:darkred;border:none;color:white;"
        if nom == "":
            self.champ_nom_materiau.setText("")
            self.champ_nom_materiau.setStyleSheet(error_champ_stylesheet)
            flag = False
        if ref == "":
            self.champ_reference_materiau.setText("")
            self.champ_reference_materiau.setStyleSheet(error_champ_stylesheet)
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

    def ajoute_materiau_bdd(self) -> None:
        """
        Méthode permettant d'ajouter un matériau dont les caractéristiques sont précisés dans les champs à la base de données.
        L'ajout ne s'effectue que si toutes les valeurs sont correctes.
        Sinon les champs contenant des problèmes sont mis en évidence.
        """
        self.reset_background_ajout()

        # Récupération des valeurs
        nom = self.champ_nom_materiau.text().strip()
        ref = self.champ_reference_materiau.text().strip()
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
                mat.ajouteDatabase()
                self.reset_background_ajout()
                self.reset_content_ajout()
                self.quick_popup("Matériau ajouté à la BDD!", type="Succes", duree=3)
            except ConnectionError:
                self.quick_popup("Impossible de se connecter à la BDD!", type="Error", duree=3)
        else:
            self.quick_popup("Des valeurs sont éronnées ou manquantes...", type="Error", duree=3)

    def affiche_info_materiau(self) -> None:
        """
        Méthode permettant d'afficher les informations du matériau selctionné (via la requête de recherche dans la base de données).
        """
        _translate = QtCore.QCoreApplication.translate
        index = int(self.liste_materiaux_correspondant.currentIndex().row())
        self.liste_materiaux_correspondant.blockSignals(True)
        if index >= 0 and not index == self.__bdd_recherche_index:
            self.__bdd_recherche_index = index
            reponses = self.recherche_materiaux_bdd(verbose=False)
            reponse_formatee = [str(x) if x is not None else '' for x in reponses[index]]
            self.maj_label_selectionne(reponse_formatee)

    def recherche_materiaux_bdd(self, verbose=True) -> list[tuple[str]]:
        """
        Méthode pour rechercher un matériau dans la base de données.
        La requête SQL suivante est soumise à la base de données :\n
        SELECT * FROM public.materiau WHERE materiau.nom LIKE '%recherche%' OR materiau.ref LIKE '%recherche%';\n
        Où recherche correspondant au contenu du champ de recherche.

        :param verbose: True pour afficher les quick_popup, False sinon.
        :return: La liste des matériaux correspondant sous forme d'une liste de tuples
        """
        nom = self.champ_recherche_materiaux.text().strip()
        query = """ SELECT nom, reference, e1, e2, g12, v12, s11_c, s22_c, s11_t, s22_t, s12, pourcentage_fibre FROM public.materiau 
                    WHERE materiau.nom LIKE %s 
                    OR materiau.reference LIKE %s"""
        data = [str("%" + nom + "%"), str("%" + nom + "%")]
        self.__bdd_recherche_index = None
        self.maj_label_selectionne()
        try:
            reponses = DatabaseTools.DatabaseTools().executeSelect(query, data)

            # Ajout des resultats
            modele_recherche_materiaux_bdd = QtGui.QStandardItemModel()
            self.liste_materiaux_correspondant.setModel(modele_recherche_materiaux_bdd)
            if len(reponses):
                self.liste_materiaux_correspondant.selectionModel().currentChanged.connect(
                    self.affiche_info_materiau)
                if verbose:
                    self.quick_popup(str(len(reponses)) + " résultat(s) trouvé(s)!", type="Info", duree=3)
            else:
                if verbose:
                    self.quick_popup("Aucun résultat correspondant!", type="Info", duree=3)
            for reponse in reponses:
                entree = QtGui.QStandardItem(str(reponse[0]) + " - " + str(reponse[1]))
                modele_recherche_materiaux_bdd.appendRow(entree)
            return reponses
        except ConnectionError:
            if verbose:
                self.quick_popup("Impossible de se connecter à la BDD!", type="Error", duree=3)
            pass
        return []

    def initActions(self) -> None:
        """
        Méthode pour connecter les actions (requête à la base de données) et les boutons.
        :return:
        """
        self.bouton_ajouter_materiau.clicked.connect(self.ajoute_materiau_bdd)
        self.champ_recherche_materiaux.returnPressed.connect(self.recherche_materiaux_bdd)



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = OngletGestionBDD()
    tmp.setStyleSheet("background-color: rgb(224, 224, 224)")
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
