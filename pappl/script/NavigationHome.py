# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets


class NavigationHome(QtWidgets.QFrame):
    """
    Classe représentant la navigation de la fenêtre principale.
    """
    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe NavigationHome.
        """
        super(NavigationHome, self).__init__(parent)
        self.__parent = parent
        self.initUI()
        self.retranslateUi()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les composants de l'instance de navigation.
        """
        self.navigation = QtWidgets.QFrame(self)
        self.navigation.setGeometry(QtCore.QRect(0, 40, 200, 420))
        self.navigation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.navigation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigation.setObjectName("navigation")

        self.bouton_gestion_materiaux = QtWidgets.QPushButton(self.navigation)
        self.bouton_gestion_materiaux.setGeometry(QtCore.QRect(0, 50, 200, 40))
        self.bouton_gestion_materiaux.setFlat(True)
        self.bouton_gestion_materiaux.setObjectName("bouton_gestion_materiaux")
        self.bouton_gestion_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

        self.bouton_accueil = QtWidgets.QPushButton(self.navigation)
        self.bouton_accueil.setGeometry(QtCore.QRect(0, 10, 200, 40))
        self.bouton_accueil.setFlat(True)
        self.bouton_accueil.setObjectName("bouton_accueil")
        self.bouton_accueil.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

    def retranslateUi(self):
        """
        Méthode permettant de mettre à jour le contenu textuel des composants.
        """
        _translate = QtCore.QCoreApplication.translate
        self.bouton_gestion_materiaux.setText(_translate("navigation", "Gestion Matériaux"))
        self.bouton_accueil.setText(_translate("navigation", "Accueil"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = NavigationHome()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
