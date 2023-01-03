# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets


class OngletAccueil(QtWidgets.QWidget):
    """
    Classe représentant l'onglet d'accueil de la fenêtre d'accueil.
    """
    def __init__(self) -> None:
        """
        Constructeur de la classe OngletAccueil.
        """
        super(OngletAccueil, self).__init__()

        # Attributs
        self.widget_accueil = None
        self.onglet_accueil = None
        self.label = None
        self.bouton_import_projet = None
        self.bouton_gestion_bdd = None

        # Initialisation
        self.initUI()
        self.retranslateUi()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les composants de l'onglet d'accueil.
        On retrouve :
            - Le bouton pour importer un projet.
            - Le bouton pour se rendre sur la page de gestion de la base de données.
        """
        self.widget_accueil = QtWidgets.QWidget(self)
        self.widget_accueil.setObjectName("widget_accueil")

        self.onglet_accueil = QtWidgets.QFrame(self.widget_accueil)
        self.onglet_accueil.setGeometry(QtCore.QRect(0, 0, 881, 421))
        self.onglet_accueil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onglet_accueil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onglet_accueil.setObjectName("onglet_accueil")

        self.label = QtWidgets.QLabel(self.onglet_accueil)
        self.label.setGeometry(QtCore.QRect(350, 20, 131, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : black;")

        self.bouton_import_projet = QtWidgets.QPushButton(self.onglet_accueil)
        self.bouton_import_projet.setGeometry(QtCore.QRect(350, 160, 141, 32))
        self.bouton_import_projet.setStyleSheet("background-color: rgb(221, 237, 242);font-size:13px;")
        self.bouton_import_projet.setObjectName("bouton_import_projet")

        self.bouton_gestion_bdd = QtWidgets.QPushButton(self.onglet_accueil)
        self.bouton_gestion_bdd.setGeometry(QtCore.QRect(350, 220, 141, 32))
        self.bouton_gestion_bdd.setStyleSheet("background-color: rgb(221, 237, 242);font-size:13px;")
        self.bouton_gestion_bdd.setObjectName("bouton_gestion_bdd")

    def retranslateUi(self) -> None:
        """
        Méthode permettant de mettre à jour le contenu textuel des composants de l'onglet d'accueil.
        """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("onglet_accueil", "SUPERMAN-TERIAUX"))
        self.bouton_import_projet.setText(_translate("onglet_accueil", "Importer un projet"))
        self.bouton_gestion_bdd.setText(_translate("onglet_accueil", "Gestion de la BDD"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = OngletAccueil()
    tmp.setStyleSheet("background-color: rgb(224, 224, 224)")
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()