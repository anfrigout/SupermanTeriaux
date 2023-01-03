# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1
from PyQt5 import QtCore, QtGui, QtWidgets


class BandeauProjet(QtWidgets.QWidget):
    """
    Classe représentant le bandeau d'action possible pour un projet.
    Pour le moment, les actions suivantes sont disponibles :
        - Renommer : pour changer le nom d'un projet
        - Save : pour enregistrer le projet au format JSON
        - Résoudre : pour demander la résolution du problème
    """
    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe BandeauProjet.
        :param parent: Un objet Qt qui recevra le Widget BandeauProjet.
        """
        super(BandeauProjet, self).__init__(parent)
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Méthode permettant d'ajouter le contenu du bandeau.
        """
        self.widget_projet_bandeau = QtWidgets.QWidget(self)
        self.widget_projet_bandeau.setObjectName("widget_projet_bandeau")

        self.bandeau = QtWidgets.QFrame(self)
        self.bandeau.setGeometry(QtCore.QRect(0, 0, 1080, 40))
        self.bandeau.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.bandeau.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandeau.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bandeau.setObjectName("bandeau")

        # Bouton RENOMMER
        self.bouton_renommer = QtWidgets.QPushButton(self.bandeau)
        self.bouton_renommer.setGeometry(QtCore.QRect(20, 10, 90, 20))
        self.bouton_renommer.setStyleSheet("background-color: rgb(6, 176, 229);color: rgb(255, 255, 255);")
        self.bouton_renommer.setObjectName("bouton_renommer")

        # Bouton SAVE
        self.bouton_save = QtWidgets.QPushButton(self.bandeau)
        self.bouton_save.setGeometry(QtCore.QRect(120, 10, 90, 20))
        self.bouton_save.setStyleSheet("background-color: rgb(6, 176, 229);color: rgb(255, 255, 255);")
        self.bouton_save.setObjectName("bouton_save")

        # Bouton SAVE AS
        self.bouton_save_as = QtWidgets.QPushButton(self.bandeau)
        self.bouton_save_as.setGeometry(QtCore.QRect(220, 10, 90, 20))
        self.bouton_save_as.setStyleSheet("background-color: rgb(6, 176, 229);color: rgb(255, 255, 255);")
        self.bouton_save_as.setObjectName("bouton_save_as")

        # Bouton RÉSOUDRE
        self.bouton_resoudre = QtWidgets.QPushButton(self.bandeau)
        self.bouton_resoudre.setGeometry(QtCore.QRect(320, 10, 90, 20))
        self.bouton_resoudre.setStyleSheet("background-color: rgb(6, 176, 229);color: rgb(255, 255, 255);")
        self.bouton_resoudre.setObjectName("bouton_resoudre")

    def retranslateUi(self) -> None:
        """
        Méthode permettant de mettre à jour le contenu textuel des éléments générés.
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        self.bouton_renommer.setText(_translate("bandeau", "RENOMMER"))
        self.bouton_save.setText(_translate("bandeau", "SAVE"))
        self.bouton_save_as.setText(_translate("bandeau", "SAVE AS"))
        self.bouton_resoudre.setText(_translate("bandeau", "RÉSOUDRE"))

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
        Méthode permettant d'initialiser les actions pour rendre l'application fonctionnelle.
        """
        pass


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = BandeauProjet()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
