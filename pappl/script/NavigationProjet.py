# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtGui, QtWidgets


class NavigationProjet(QtWidgets.QFrame):
    """
    Classe représentant la navigation dans une fenêtre projet.
    """
    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe NavigationProjet.
        """
        super(NavigationProjet, self).__init__(parent)
        self.__parent = parent
        self.initUI()
        self.retranslateUi()

    def initUI(self):
        """
        Méthode permettant d'initialiser les composants de la navigation dans une fenêtre projet.
        """
        self.navigation = QtWidgets.QFrame(self)
        self.navigation.setGeometry(QtCore.QRect(0, 40, 200, 420))
        self.navigation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.navigation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigation.setObjectName("navigation")

        self.bouton_materiaux = QtWidgets.QPushButton(self.navigation)
        self.bouton_materiaux.setGeometry(QtCore.QRect(0, 10, 200, 40))
        self.bouton_materiaux.setFlat(True)
        self.bouton_materiaux.setObjectName("bouton_materiaux")
        self.bouton_materiaux.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

        self.bouton_plaque = QtWidgets.QPushButton(self.navigation)
        self.bouton_plaque.setGeometry(QtCore.QRect(0, 50, 200, 40))
        self.bouton_plaque.setFlat(True)
        self.bouton_plaque.setObjectName("bouton_plaque")
        self.bouton_plaque.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

        self.bouton_chargement = QtWidgets.QPushButton(self.navigation)
        self.bouton_chargement.setGeometry(QtCore.QRect(0, 90, 200, 40))
        self.bouton_chargement.setFlat(True)
        self.bouton_chargement.setObjectName("bouton_chargement")
        self.bouton_chargement.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

        self.bouton_visualisation = QtWidgets.QPushButton(self.navigation)
        self.bouton_visualisation.setGeometry(QtCore.QRect(0, 130, 200, 40))
        self.bouton_visualisation.setFlat(True)
        self.bouton_visualisation.setObjectName("bouton_visualisation")
        self.bouton_visualisation.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

        self.bouton_export_visualisation = QtWidgets.QPushButton(self.navigation)
        self.bouton_export_visualisation.setGeometry(QtCore.QRect(0, 370, 200, 40))
        self.bouton_export_visualisation.setFlat(True)
        self.bouton_export_visualisation.setObjectName("bouton_export_visualisation")
        self.bouton_export_visualisation.setStyleSheet("background-color: rgb(255, 255, 255);border:none;")

    def retranslateUi(self):
        """
        Méthode permettant de mettre à jour le contenu textuel des composants.
        """
        _translate = QtCore.QCoreApplication.translate
        self.bouton_materiaux.setText(_translate("navigation", "Gestion matériaux"))
        self.bouton_plaque.setText(_translate("navigation", "Paramètrage plaque"))
        self.bouton_chargement.setText(_translate("navigation", "Chargement"))
        self.bouton_visualisation.setText(_translate("navigation", "Visualisation"))
        self.bouton_export_visualisation.setText(_translate("navigation", "EXPORT VISUALISATION"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = NavigationProjet()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
