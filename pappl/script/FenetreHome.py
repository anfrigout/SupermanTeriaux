# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

import sys

from PyQt5 import QtCore, QtWidgets

from script import OngletAccueil
from script import OngletGestionBDD
from script import NavigationHome
from script import CustomDecoder


class FenetreHome(QtWidgets.QWidget):
    """
    Classe permettant de représenter la fenêtre d'accueil de l'interface graphqiue.
    La fenêtre d'accueil offre deux possibilités :
        - Importer un projet
        - Gérer la base de données (Ajout de matériaux et recherche de matériaux)
    """

    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe FenetreHome.

        :param parent: Un objet Qt qui recevra le Widget FenetreHome.
        """
        super(FenetreHome, self).__init__()
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Classe permettant d'initialiser le contenu de la fenêtre d'accueil.
        """
        # Navigation latérale
        self.navigation = NavigationHome.NavigationHome(self)
        self.navigation.setObjectName("navigation")

        # Bandeau supérieur
        self.setObjectName("PageHome")
        self.bandeau = QtWidgets.QFrame(self)
        self.bandeau.setGeometry(QtCore.QRect(0, 0, 1080, 40))
        self.bandeau.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.bandeau.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandeau.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bandeau.setObjectName("bandeau")

        # Contenu de la page
        self.pile_onglets = QtWidgets.QStackedWidget(self)
        self.pile_onglets.setGeometry(QtCore.QRect(200, 40, 881, 421))
        self.pile_onglets.setObjectName("pile_onglets")

        # Page d'accueil
        self.widget_accueil = OngletAccueil.OngletAccueil()

        # Page gestion de la bdd
        self.widget_materiaux_bdd = OngletGestionBDD.OngletGestionBDD(self)

        # Ajout des pages à la pile
        self.pile_onglets.addWidget(self.widget_accueil)
        self.pile_onglets.addWidget(self.widget_materiaux_bdd)

    def retranslateUi(self) -> None:
        """
        Classe permettant d'initialiser les composants créer (position dans la pile d'onglet, textes...)
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        self.pile_onglets.setCurrentIndex(0)
        self.navigation.bouton_accueil.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")

    def aller_onglet_accueil(self) -> None:
        """
        Méthode permettant d'aller sur la page d'acuueil de la fenêtre d'accueil.
        Cette méthode est connectée au bouton Accueil de la navigation.
        :return:
        """
        self.pile_onglets.setCurrentIndex(0)
        self.navigation.bouton_accueil.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")
        self.navigation.bouton_gestion_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

    def aller_onglet_gestion_bdd(self) -> None:
        """
        Méthode permettant d'aller dans l'onglet gestion de la base de données de la fenêtre d'accueil.
        Cette méthode est connectée au bouton Gestion Matériaux de la navigation.
        """
        self.pile_onglets.setCurrentIndex(1)
        self.navigation.bouton_accueil.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")
        self.navigation.bouton_gestion_materiaux.setStyleSheet("background-color: rgb(221, 237, 242);border:none;")

    def import_projet(self) -> None:
        """
        Méthode permettant d'importer un projet enregistrer au format JSON par l'application.
        """
        options = QtWidgets.QFileDialog.Options()
        if sys.platform == 'darwin':
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
        chemin_fichier = QtWidgets.QFileDialog.getOpenFileName(self, caption='Ouvrir',
                                                               directory=QtCore.QDir.currentPath(),
                                                               filter='JSON (*.json*)',
                                                               options=options)[0]
        try:
            fichier = open(chemin_fichier, "r")
            json_str = fichier.read()
            fichier.close()
        except FileNotFoundError:
            self.quick_popup("Opération avortée, mauvais fichier!", type="Error", duree=3)
            return
        try:
            projet = CustomDecoder.CustomDecoder().decode(json_str)
            self.__parent.import_projet(projet, chemin_fichier)
        except KeyError:
            self.quick_popup("Le fichier de sauvegarde est corrompu!", type="Error", duree=3)
            return

    def initActions(self) -> None:
        """
        Méthode permettant de connecter les boutons de la navigation pour le fonctionnement de l'interface
        """
        self.navigation.bouton_accueil.clicked.connect(self.aller_onglet_accueil)
        self.navigation.bouton_gestion_materiaux.clicked.connect(self.aller_onglet_gestion_bdd)
        self.widget_accueil.bouton_gestion_bdd.clicked.connect(self.aller_onglet_gestion_bdd)
        self.widget_accueil.bouton_import_projet.clicked.connect(self.import_projet)

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if self.__parent is not None:
            self.__parent.quick_popup(*args, **kwargs)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = FenetreHome()
    tmp.setStyleSheet("background-color: rgb(224, 224, 224)")
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
