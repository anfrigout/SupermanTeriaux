# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets


class PopupRenommageProjet(QtWidgets.QFrame):
    """
    Classe représentant le popup permettant de renommer le projet.
    """

    def __init__(self,
                 parent=None) -> None:
        """
        Constructeur de la classe PopupRenommageProjet.
        """
        super(PopupRenommageProjet, self).__init__(parent)
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les différentes composants du popup.
        """
        self.popup = QtWidgets.QFrame(self)
        self.popup.setGeometry(QtCore.QRect(0, 0, 300, 100))
        self.popup.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.popup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popup.setObjectName("popup")

        self.label_renommer_projet = QtWidgets.QLabel(self.popup)
        self.label_renommer_projet.setGeometry(QtCore.QRect(0, 10, 300, 15))
        self.label_renommer_projet.setObjectName("label_renommer_projet")
        self.label_renommer_projet.setStyleSheet("color:white;")
        self.label_renommer_projet.setAlignment(QtCore.Qt.AlignCenter)

        self.bouton_modifier_nom_projet = QtWidgets.QPushButton(self.popup)
        self.bouton_modifier_nom_projet.setGeometry(QtCore.QRect(10, 70, 280, 21))
        self.bouton_modifier_nom_projet.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.bouton_modifier_nom_projet.setObjectName("bouton_modifier_nom_projet")

        self.champ_nouveau_nom_projet = QtWidgets.QLineEdit(self.popup)
        self.champ_nouveau_nom_projet.setGeometry(QtCore.QRect(10, 40, 280, 21))
        self.champ_nouveau_nom_projet.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.champ_nouveau_nom_projet.setObjectName("champ_nouveau_nom_projet")

    def quitte_popup(self) -> None:
        """
        Méthode permettant de quitter le popup.
        """
        self.setHidden(True)

    def quick_popup(self, *args, **kwargs) -> None:
        """
        Méthode permettant de demander la génération d'un popup dans l'application.
        Cette méthode va appeler la méthode de son parent, s'il existe, sinon l'appel va être perdu.

        :param args: Arguments à passer à la méthode parente
        :param kwargs: Arguments nominatifs à passer à la méthode parente
        """
        if not self.__parent is None:
            self.__parent.quick_popup(*args, **kwargs)

    def change_nom_projet(self) -> None:
        """
        Méthode permettant de changer le nom du projet.
        """
        nouveau_nom = self.champ_nouveau_nom_projet.text().strip()
        self.champ_nouveau_nom_projet.setStyleSheet("background-color:white;color:black;border:none;")
        if nouveau_nom == "":
            self.champ_nouveau_nom_projet.setText(QtCore.QCoreApplication.translate("popup", ""))
            self.champ_nouveau_nom_projet.setStyleSheet("background-color:darkred;color:white;border:none;")
            self.quick_popup("Nouveau nom incorrect...", type="Error", duree=3)
        elif nouveau_nom == self.__parent.projet.getNomProjet():
            self.quick_popup("Le nom du projet n'a pas changé...", type="Warning", duree=3)
            self.quitte_popup()
        else:
            self.__parent.setNomProjet(nouveau_nom)
            self.quick_popup("Nom du projet modifié!", type="Succes", duree=3)
            self.__parent.modification_effectuee()
            self.quitte_popup()

    def initActions(self) -> None:
        """
        Méthode permettant de connecter les actions de renommage aux composants.
        """
        self.bouton_modifier_nom_projet.clicked.connect(self.change_nom_projet)
        self.champ_nouveau_nom_projet.returnPressed.connect(self.change_nom_projet)

    def retranslateUi(self) -> None:
        """
        Méthode permettant d'initialiser le contenu textuel des composants du popup.
        """
        _translate = QtCore.QCoreApplication.translate
        self.bouton_modifier_nom_projet.setText(_translate("popup", "MODIFIER"))
        self.label_renommer_projet.setText(_translate("popup", "Renommer le projet :"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = PopupRenommageProjet()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()