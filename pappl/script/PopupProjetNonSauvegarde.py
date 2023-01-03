# coding: utf-8
# @author: Antoine FRIGOUT - <antoine.frigout@eleves.ec-nantes.fr>
# @author: Mailys LE LOCH - <mailys.le-loch@eleves.ec-nantes.fr>
# @version: 0.1

from PyQt5 import QtCore, QtWidgets


class PopupProjetNonSauvegarde(QtWidgets.QFrame):
    """
    Classe représentant le popup permettant de renommer le projet.
    """

    def __init__(self,
                 parent=None,
                 index=0) -> None:
        """
        Constructeur de la classe PopupRenommageProjet.
        """
        super(PopupProjetNonSauvegarde, self).__init__(parent)
        self.__index_tmp = index
        self.__parent = parent
        self.initUI()
        self.retranslateUi()
        self.initActions()

    def initUI(self) -> None:
        """
        Méthode permettant d'initialiser les différentes composants du popup.
        """
        self.popup = QtWidgets.QFrame(self)
        self.popup.setGeometry(QtCore.QRect(0, 0, 300, 130))
        self.popup.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.popup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popup.setObjectName("popup")

        self.label_info = QtWidgets.QLabel(self.popup)
        self.label_info.setGeometry(QtCore.QRect(0, 10, 300, 15))
        self.label_info.setObjectName("label_info")
        self.label_info.setStyleSheet("color:white;")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)

        self.bouton_save = QtWidgets.QPushButton(self.popup)
        self.bouton_save.setGeometry(QtCore.QRect(10, 40, 280, 20))
        self.bouton_save.setStyleSheet(
            "background-color: lightblue;color: black;border:none;")
        self.bouton_save.setObjectName("bouton_save")

        self.bouton_pas_save = QtWidgets.QPushButton(self.popup)
        self.bouton_pas_save.setGeometry(QtCore.QRect(10, 70, 280, 20))
        self.bouton_pas_save.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.bouton_pas_save.setObjectName("bouton_pas_save")

        self.bouton_annuler = QtWidgets.QPushButton(self.popup)
        self.bouton_annuler.setGeometry(QtCore.QRect(10, 100, 280, 20))
        self.bouton_annuler.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.bouton_annuler.setObjectName("bouton_annuler")

        """
        self.bouton_annuler = QtWidgets.QLineEdit(self.popup)
        self.bouton_annuler.setGeometry(QtCore.QRect(10, 140, 280, 20))
        self.bouton_annuler.setStyleSheet(
            "background-color: rgb(255, 255, 255);color: black;border:none;")
        self.bouton_annuler.setObjectName("bouton_annuler")
        """

    def quitte_popup_annuler(self) -> int:
        """
        Méthode permettant de quitter le popup en annulant l'action
        """
        self.setHidden(True)
        self.exit = -1

    def quitte_popup_save(self) -> int:
        """
        Méthode permettant de quitter le popup en sauvegardant
        """
        self.setHidden(True)
        self.exit = 0

    def quitte_popup_no_save(self) -> int:
        """
        Méthode permettant de quitter le popup en ne sauvegardant pas
        """
        self.setHidden(True)
        self.exit = 1

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
        Méthode permettant de connecter les actions de renommage aux composants.
        """
        self.bouton_annuler.clicked.connect(self.__parent.quitte_popup_annuler)
        self.bouton_save.clicked.connect(lambda: self.__parent.quitte_popup_save(self.__index_tmp))
        self.bouton_pas_save.clicked.connect(lambda: self.__parent.quitte_popup_no_save(self.__index_tmp))

    def retranslateUi(self) -> None:
        """
        Méthode permettant d'initialiser le contenu textuel des composants du popup.
        """
        _translate = QtCore.QCoreApplication.translate
        self.label_info.setText(_translate("popup", "Attention, le projet n'est pas sauvegardé!"))
        self.bouton_save.setText(_translate("popup", "ENREGISTRER"))
        self.bouton_pas_save.setText(_translate("popup", "IGNORER ET FERMER"))
        self.bouton_annuler.setText(_translate("popup", "ANNULER"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tmp = PopupProjetNonSauvegarde()
    tmp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()